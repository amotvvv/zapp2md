"""
Zapp2md - interfaccia grafica (Windows).

La finestra non elabora nulla da sola: avvia zapp2md.py in un processo separato e ne legge
gli eventi di avanzamento (JSON, una riga per evento). Così un eventuale crash delle librerie
native non chiude la finestra, e "Interrompi" termina il lavoro in modo pulito: grazie alla cache,
premendo di nuovo "Avvia" si riprende da dove si era arrivati.
"""

from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
import threading
import time
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))
from i18n import LANGS, set_lang, t  # noqa: E402

VERSION = "1.0"
AUTHOR = "Andrea Moretto"
AUTHOR_URL = "https://www.linkedin.com/in/andrea-moretto-mba/"
ENGINE = APP_DIR / "zapp2md.py"
ICON = APP_DIR / "app.ico"
LICENSE = APP_DIR / "LICENSE.txt"
SETTINGS = Path(os.environ.get("APPDATA", str(Path.home()))) / "Zapp2md" / "settings.json"

MODELS = [("large-v3-turbo", "g_q_turbo"), ("large-v3", "g_q_best"), ("small", "g_q_fast")]
SPEECH = [("auto", None), ("it", "Italiano"), ("pt", "Português"), ("en", "English"),
          ("es", "Español"), ("fr", "Français"), ("de", "Deutsch")]
GROUPS = ["audio", "video", "image", "document"]


def fmt_dur(sec: float) -> str:
    sec = int(max(0, round(sec)))
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def engine_python() -> str:
    """python.exe accanto a pythonw.exe: serve una console 'virtuale' per leggere l'output."""
    exe = Path(sys.executable)
    cand = exe.with_name("python.exe")
    return str(cand if cand.exists() else exe)


def system_ui_language() -> str:
    try:
        import ctypes

        primary = ctypes.windll.kernel32.GetUserDefaultUILanguage() & 0x3FF
        return {0x10: "it", 0x16: "pt", 0x09: "en"}.get(primary, "en")
    except Exception:
        return "en"


def load_settings() -> dict:
    try:
        data = json.loads(SETTINGS.read_text(encoding="utf-8-sig"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_settings(data: dict) -> None:
    try:
        SETTINGS.parent.mkdir(parents=True, exist_ok=True)
        SETTINGS.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass


class App:
    def __init__(self, root: tk.Tk, initial_input: str | None):
        self.root = root
        s = load_settings()
        self.lang = tk.StringVar(value=s.get("lang") or system_ui_language())
        set_lang(self.lang.get())
        self.input = tk.StringVar(value=initial_input or "")
        self.outdir = tk.StringVar(value="")
        self.opt_video = tk.BooleanVar(value=s.get("video", True))
        self.opt_ocr = tk.BooleanVar(value=s.get("ocr", True))
        self.opt_split = tk.BooleanVar(value=s.get("split", False))
        self.model = s.get("model", "large-v3-turbo")
        self.speech = s.get("speech", self.lang.get())
        self.last_dir = s.get("last_dir", str(Path.home() / "Downloads"))

        self.proc: subprocess.Popen | None = None
        self.q: queue.Queue = queue.Queue()
        self.running = False
        self.stopping = False
        self.result: dict | None = None
        self.fatal: str | None = None
        self.outputs: list[str] = []
        self._reset_counters()

        root.title(f"Zapp2md {VERSION}")
        try:
            root.iconbitmap(str(ICON))
        except Exception:
            pass
        root.minsize(760, 640)
        root.protocol("WM_DELETE_WINDOW", self.on_close)
        self._build()
        self.retranslate()
        self.root.after(200, self.poll)
        self.root.after(1000, self.tick)

    # ------------------------------------------------------------------ layout
    def _build(self):
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 16))
        style.configure("Sub.TLabel", foreground="#5b6470")
        style.configure("Big.TLabel", font=("Segoe UI Semibold", 11))
        style.configure("Count.TLabel", font=("Segoe UI", 10))
        style.configure("Accent.TButton", font=("Segoe UI Semibold", 10))
        style.configure("Link.TLabel", foreground="#0a66c2")

        main = ttk.Frame(self.root, padding=(16, 12, 16, 8))
        main.pack(fill="both", expand=True)
        main.columnconfigure(0, weight=1)

        # intestazione + lingua
        head = ttk.Frame(main)
        head.grid(row=0, column=0, sticky="ew")
        head.columnconfigure(0, weight=1)
        ttk.Label(head, text="Zapp2md", style="Title.TLabel").grid(row=0, column=0, sticky="w")
        self.w_sub = ttk.Label(head, style="Sub.TLabel")
        self.w_sub.grid(row=1, column=0, columnspan=2, sticky="w")
        lf = ttk.Frame(head)
        lf.grid(row=0, column=1, sticky="ne")
        self.w_lang = ttk.Label(lf)
        self.w_lang.pack(side="left", padx=(0, 6))
        for code in ("it", "pt", "en"):
            ttk.Radiobutton(lf, text=LANGS[code], value=code, variable=self.lang, style="Toolbutton",
                            command=self.on_lang).pack(side="left", padx=1)

        # file di ingresso e cartella di destinazione
        self.w_files = ttk.LabelFrame(main, padding=10)
        self.w_files.grid(row=1, column=0, sticky="ew", pady=(12, 6))
        self.w_files.columnconfigure(1, weight=1)
        self.w_in_lbl = ttk.Label(self.w_files)
        self.w_in_lbl.grid(row=0, column=0, sticky="w", padx=(0, 8))
        ttk.Entry(self.w_files, textvariable=self.input).grid(row=0, column=1, sticky="ew")
        self.w_browse = ttk.Button(self.w_files, command=self.pick_zip)
        self.w_browse.grid(row=0, column=2, padx=(6, 0))
        self.w_folder = ttk.Button(self.w_files, command=self.pick_folder)
        self.w_folder.grid(row=0, column=3, padx=(4, 0))
        self.w_out_lbl = ttk.Label(self.w_files)
        self.w_out_lbl.grid(row=1, column=0, sticky="w", padx=(0, 8), pady=(8, 0))
        self.w_out = ttk.Label(self.w_files, foreground="#5b6470")
        self.w_out.grid(row=1, column=1, sticky="w", pady=(8, 0))
        self.w_out_btn = ttk.Button(self.w_files, command=self.pick_outdir)
        self.w_out_btn.grid(row=1, column=2, columnspan=2, sticky="ew", padx=(6, 0), pady=(8, 0))

        # opzioni
        self.w_opts = ttk.LabelFrame(main, padding=10)
        self.w_opts.grid(row=2, column=0, sticky="ew", pady=6)
        self.w_opts.columnconfigure(1, weight=1)
        self.w_cb_video = ttk.Checkbutton(self.w_opts, variable=self.opt_video)
        self.w_cb_video.grid(row=0, column=0, sticky="w")
        self.w_cb_ocr = ttk.Checkbutton(self.w_opts, variable=self.opt_ocr)
        self.w_cb_ocr.grid(row=1, column=0, sticky="w", pady=2)
        self.w_cb_split = ttk.Checkbutton(self.w_opts, variable=self.opt_split)
        self.w_cb_split.grid(row=2, column=0, sticky="w")
        right = ttk.Frame(self.w_opts)
        right.grid(row=0, column=1, rowspan=3, sticky="e")
        self.w_q_lbl = ttk.Label(right)
        self.w_q_lbl.grid(row=0, column=0, sticky="e", padx=(0, 6))
        self.w_quality = ttk.Combobox(right, state="readonly", width=32)
        self.w_quality.grid(row=0, column=1, sticky="w")
        self.w_s_lbl = ttk.Label(right)
        self.w_s_lbl.grid(row=1, column=0, sticky="e", padx=(0, 6), pady=(6, 0))
        self.w_speech = ttk.Combobox(right, state="readonly", width=32)
        self.w_speech.grid(row=1, column=1, sticky="w", pady=(6, 0))
        self.w_quality.bind("<<ComboboxSelected>>", lambda e: self._read_combos())
        self.w_speech.bind("<<ComboboxSelected>>", lambda e: self._read_combos())

        # pulsanti
        bar = ttk.Frame(main)
        bar.grid(row=3, column=0, sticky="ew", pady=(6, 6))
        self.w_start = ttk.Button(bar, style="Accent.TButton", command=self.start, width=14)
        self.w_start.pack(side="left")
        self.w_stop = ttk.Button(bar, command=self.stop, state="disabled", width=14)
        self.w_stop.pack(side="left", padx=6)
        self.w_open_folder = ttk.Button(bar, command=self.open_folder, state="disabled")
        self.w_open_folder.pack(side="right")
        self.w_open_md = ttk.Button(bar, command=self.open_md, state="disabled")
        self.w_open_md.pack(side="right", padx=6)

        # avanzamento
        self.w_prog = ttk.LabelFrame(main, padding=10)
        self.w_prog.grid(row=4, column=0, sticky="ew", pady=6)
        self.w_prog.columnconfigure(0, weight=1)
        self.pbar = ttk.Progressbar(self.w_prog, maximum=1000)
        self.pbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.w_pct = ttk.Label(self.w_prog, style="Big.TLabel")
        self.w_pct.grid(row=1, column=0, sticky="w", pady=(6, 0))
        self.w_eta = ttk.Label(self.w_prog, style="Big.TLabel")
        self.w_eta.grid(row=1, column=1, sticky="e", pady=(6, 0))
        self.w_status = ttk.Label(self.w_prog, foreground="#5b6470")
        self.w_status.grid(row=2, column=0, columnspan=2, sticky="w", pady=(2, 6))
        grid = ttk.Frame(self.w_prog)
        grid.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.w_counts: dict[str, tuple[ttk.Label, ttk.Label]] = {}
        for i, g in enumerate(GROUPS + ["errors"]):
            grid.columnconfigure(i, weight=1)
            name = ttk.Label(grid, style="Sub.TLabel")
            name.grid(row=0, column=i, sticky="w")
            val = ttk.Label(grid, style="Big.TLabel", text="–")
            val.grid(row=1, column=i, sticky="w")
            self.w_counts[g] = (name, val)

        # errori / registro
        self.nb = ttk.Notebook(main)
        self.nb.grid(row=5, column=0, sticky="nsew", pady=(6, 0))
        main.rowconfigure(5, weight=1)
        self.err_list = self._text_tab()
        self.log_text = self._text_tab()
        self.err_list.tag_configure("warn", foreground="#b45309")
        self.err_list.tag_configure("err", foreground="#b91c1c")

        # piè di pagina: autore, LinkedIn, informazioni
        foot = ttk.Frame(main)
        foot.grid(row=6, column=0, sticky="ew", pady=(8, 0))
        ttk.Label(foot, text=f"v{VERSION}  ·  © 2026 {AUTHOR}  ·", style="Sub.TLabel").pack(side="left")
        link = ttk.Label(foot, text="LinkedIn", style="Link.TLabel", cursor="hand2")
        link.pack(side="left", padx=4)
        link.bind("<Button-1>", lambda e: webbrowser.open(AUTHOR_URL))
        self.w_about = ttk.Button(foot, command=self.about)
        self.w_about.pack(side="right")

    def _text_tab(self) -> tk.Text:
        frame = ttk.Frame(self.nb)
        txt = tk.Text(frame, height=8, wrap="word", font=("Consolas", 9), relief="flat", borderwidth=0,
                      state="disabled", padx=6, pady=4)
        sb = ttk.Scrollbar(frame, command=txt.yview)
        txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        txt.pack(side="left", fill="both", expand=True)
        self.nb.add(frame)
        return txt

    # ------------------------------------------------------------------ lingua
    def retranslate(self):
        set_lang(self.lang.get())
        self.w_sub.configure(text=t("g_subtitle"))
        self.w_lang.configure(text=t("g_lang") + ":")
        self.w_files.configure(text=t("g_input"))
        self.w_in_lbl.configure(text=".zip")
        self.w_browse.configure(text=t("g_browse"))
        self.w_folder.configure(text=t("g_folder"))
        self.w_out_lbl.configure(text=t("g_output"))
        self.w_out.configure(text=self.outdir.get() or t("g_output_default"))
        self.w_out_btn.configure(text=t("g_change"))
        self.w_opts.configure(text=t("g_options"))
        self.w_cb_video.configure(text=t("g_opt_video"))
        self.w_cb_ocr.configure(text=t("g_opt_ocr"))
        self.w_cb_split.configure(text=t("g_opt_split"))
        self.w_q_lbl.configure(text=t("g_quality"))
        self.w_quality.configure(values=[t(k) for _, k in MODELS])
        self.w_quality.current(next((i for i, (m, _) in enumerate(MODELS) if m == self.model), 0))
        self.w_s_lbl.configure(text=t("g_speech"))
        self.w_speech.configure(values=[lbl or t("g_speech_auto") for _, lbl in SPEECH])
        self.w_speech.current(next((i for i, (c, _) in enumerate(SPEECH) if c == self.speech), 0))
        self.w_start.configure(text=t("g_start"))
        self.w_stop.configure(text=t("g_stop"))
        self.w_open_md.configure(text=t("g_open_md"))
        self.w_open_folder.configure(text=t("g_open_folder"))
        self.w_prog.configure(text=t("g_progress"))
        for g in GROUPS + ["errors"]:
            self.w_counts[g][0].configure(text=t("g_k_" + g))
        self.nb.tab(0, text=t("g_tab_errors"))
        self.nb.tab(1, text=t("g_tab_log"))
        self.w_about.configure(text=t("g_about"))
        if not self.running and self.result is None:
            self.w_status.configure(text=t("g_ready"))
        self._refresh_progress()

    def on_lang(self):
        self._read_combos()
        self.retranslate()
        self._save()

    def _read_combos(self):
        qi = self.w_quality.current()
        si = self.w_speech.current()
        if qi >= 0:
            self.model = MODELS[qi][0]
        if si >= 0:
            self.speech = SPEECH[si][0]
        self._save()

    def _save(self):
        save_settings({"lang": self.lang.get(), "video": self.opt_video.get(), "ocr": self.opt_ocr.get(),
                       "split": self.opt_split.get(), "model": self.model, "speech": self.speech,
                       "last_dir": self.last_dir})

    # ------------------------------------------------------------------ scelte file
    def pick_zip(self):
        p = filedialog.askopenfilename(title=t("g_select_zip"), initialdir=self.last_dir,
                                       filetypes=[("WhatsApp .zip", "*.zip"), ("WhatsApp .txt", "*.txt"), ("*", "*.*")])
        if p:
            self.input.set(os.path.normpath(p))
            self.last_dir = str(Path(p).parent)
            self._save()

    def pick_folder(self):
        p = filedialog.askdirectory(title=t("g_select_zip"), initialdir=self.last_dir)
        if p:
            self.input.set(os.path.normpath(p))
            self.last_dir = str(Path(p).parent)
            self._save()

    def pick_outdir(self):
        p = filedialog.askdirectory(title=t("g_select_out"), initialdir=self.outdir.get() or self.last_dir)
        if p:
            self.outdir.set(os.path.normpath(p))
            self.w_out.configure(text=self.outdir.get())

    # ------------------------------------------------------------------ esecuzione
    def _reset_counters(self):
        self.totals = {g: 0 for g in GROUPS}
        self.done = {g: 0 for g in GROUPS}
        self.n_errors = 0
        self.n_todo = 0
        self.i_done = 0
        self.eta: float | None = None
        self.eta_at = 0.0
        self.t_start = 0.0
        self.first_eta: float | None = None
        self.phase = "idle"
        self.current = ""

    def _append(self, widget: tk.Text, line: str, tag: str | None = None):
        widget.configure(state="normal")
        widget.insert("end", line + "\n", tag or ())
        if int(widget.index("end-1c").split(".")[0]) > 5000:
            widget.delete("1.0", "1000.0")
        widget.see("end")
        widget.configure(state="disabled")

    def _clear(self, widget: tk.Text):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.configure(state="disabled")

    def start(self):
        if self.running:
            return
        src = self.input.get().strip().strip('"')
        if not src or not Path(src).exists():
            messagebox.showwarning("Zapp2md", t("g_no_input"), parent=self.root)
            return
        py = engine_python()
        if not ENGINE.exists() or not Path(py).exists():
            messagebox.showerror("Zapp2md", t("g_not_installed", p=ENGINE), parent=self.root)
            return
        self._read_combos()
        self._save()
        cmd = [py, "-u", str(ENGINE), src, "--progress-json", "--ui", self.lang.get(), "--model", self.model,
               "--speech-lang", self.speech, "--video" if self.opt_video.get() else "--no-video"]
        if not self.opt_ocr.get():
            cmd.append("--no-ocr")
        if self.opt_split.get():
            cmd.append("--split-by-year")
        if self.outdir.get():
            stem = Path(src).stem if Path(src).is_file() else Path(src).name
            cmd += ["-o", str(Path(self.outdir.get()) / (stem + ".md"))]
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")
        try:
            self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         stdin=subprocess.DEVNULL, env=env, cwd=str(APP_DIR),
                                         creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
                                         text=True, encoding="utf-8", errors="replace", bufsize=1)
        except Exception as e:
            messagebox.showerror("Zapp2md", f"{t('g_failed')}:\n{e}", parent=self.root)
            return
        self._reset_counters()
        self.result, self.fatal, self.outputs = None, None, []
        self.running, self.stopping = True, False
        self.t_start = time.time()
        self.phase = "prepare"
        self._clear(self.err_list)
        self._clear(self.log_text)
        self._set_running_ui(True)
        self.w_status.configure(text=t("g_preparing"))
        threading.Thread(target=self._reader, args=(self.proc,), daemon=True).start()

    def _reader(self, proc: subprocess.Popen):
        try:
            for line in proc.stdout:  # type: ignore[union-attr]
                self.q.put(("line", line.rstrip("\r\n")))
        except Exception as e:
            self.q.put(("line", f"[reader] {e}"))
        self.q.put(("exit", proc.wait()))

    def stop(self):
        if not self.running or not self.proc:
            return
        if not messagebox.askyesno("Zapp2md", t("g_confirm_stop"), parent=self.root):
            return
        self.stopping = True
        try:
            self.proc.kill()
        except Exception:
            pass

    def _set_running_ui(self, running: bool):
        st = "disabled" if running else "normal"
        for w in (self.w_start, self.w_browse, self.w_folder, self.w_out_btn, self.w_cb_video, self.w_cb_ocr,
                  self.w_cb_split):
            w.configure(state=st)
        self.w_quality.configure(state="disabled" if running else "readonly")
        self.w_speech.configure(state="disabled" if running else "readonly")
        self.w_stop.configure(state="normal" if running else "disabled")
        if running:
            self.w_open_md.configure(state="disabled")
            self.w_open_folder.configure(state="disabled")
            self.pbar.configure(mode="indeterminate")
            self.pbar.start(15)

    # ------------------------------------------------------------------ eventi
    def poll(self):
        try:
            while True:
                kind, payload = self.q.get_nowait()
                if kind == "line":
                    self._on_line(payload)
                else:
                    self._on_exit(payload)
        except queue.Empty:
            pass
        self.root.after(150, self.poll)

    def _on_line(self, line: str):
        try:
            ev = json.loads(line)
            if not isinstance(ev, dict) or "ev" not in ev:
                raise ValueError
        except ValueError:
            if line.strip():
                self._append(self.log_text, line)
            return
        e = ev["ev"]
        if e == "log":
            self._append(self.log_text, ev.get("msg", ""))
            if ev.get("level") == "WARNING":
                self._append(self.err_list, "⚠ " + ev.get("msg", ""), "warn")
            elif self.phase == "prepare":
                self.w_status.configure(text=ev.get("msg", "")[:160])
        elif e == "plan":
            for g in GROUPS:
                self.totals[g] = ev["totals"].get(g, 0)
                self.done[g] = ev["ready"].get(g, 0)
            self.n_todo = ev.get("todo", 0)
            self.phase = "media"
            self.pbar.stop()
            self.pbar.configure(mode="determinate", value=0)
        elif e == "file_start":
            self.current = ev["name"]
            self._set_eta(ev.get("eta"))
            dur = ev.get("duration") or 0
            extra = f"  ({fmt_dur(dur)})" if dur else ""
            self.w_status.configure(text=t("g_current", v=self.current + extra))
        elif e == "file_done":
            g = ev["kind"]
            if g in self.done:
                self.done[g] += 1
            self.i_done = ev["i"]
            if not ev.get("ok"):
                self.n_errors += 1
                self._append(self.err_list, f"✖ {ev['name']}: {ev.get('error')}", "err")
            self._set_eta(ev.get("eta"))
            if ev["i"] >= ev["n"]:
                self.phase = "write"
                self.w_status.configure(text=t("g_writing"))
        elif e == "result":
            self.result = ev
            self.outputs = ev.get("outputs", [])
        elif e == "fatal":
            self.fatal = ev.get("msg", "")
            self._append(self.err_list, "✖ " + self.fatal, "err")
            if ev.get("trace"):
                self._append(self.log_text, ev["trace"])
        self._refresh_progress()

    def _set_eta(self, eta):
        if eta is None:
            return
        self.eta, self.eta_at = float(eta), time.time()
        if self.first_eta is None:
            self.first_eta = self.eta

    def _current_eta(self) -> float | None:
        if self.eta is None:
            return None
        return max(0.0, self.eta - (time.time() - self.eta_at))

    def _refresh_progress(self):
        for g in GROUPS:
            tot = self.totals[g]
            self.w_counts[g][1].configure(text=f"{self.done[g]} / {tot}" if tot else "–")
        self.w_counts["errors"][1].configure(text=str(self.n_errors),
                                             foreground="#b91c1c" if self.n_errors else "")
        if not self.running:
            return
        elapsed = time.time() - self.t_start
        eta = self._current_eta()
        if self.phase in ("media", "write") and self.n_todo:
            # frazione basata sul tempo: elaborato / (elaborato + stima del rimanente)
            spent_media = elapsed
            frac = spent_media / (spent_media + eta) if eta is not None and (spent_media + eta) > 0 else 0
            frac = max(frac, self.i_done / max(1, self.n_todo) * 0.05)
            self.pbar.configure(value=min(1000, int(frac * 1000)))
            self.w_pct.configure(text=f"{int(frac * 100)}%   ·   " + t("g_files", a=self.i_done, b=self.n_todo))
        elif self.phase in ("media", "write"):
            self.pbar.configure(value=1000)
            self.w_pct.configure(text="100%")
        else:
            self.w_pct.configure(text="")
        if eta is None or self.phase not in ("media", "write"):
            rem = t("g_estimating")
        elif eta < 15:
            rem = t("g_few_seconds")
        else:
            rem = fmt_dur(eta)
        self.w_eta.configure(text=t("g_remaining", v=rem) + "     " + t("g_elapsed", v=fmt_dur(elapsed)))

    def tick(self):
        if self.running:
            self._refresh_progress()
        self.root.after(1000, self.tick)

    def _on_exit(self, code: int):
        was_stopping = self.stopping
        self.running = False
        self.proc = None
        self.pbar.stop()
        self._set_running_ui(False)
        self.phase = "idle"
        if self.result is not None:
            self.pbar.configure(mode="determinate", value=1000)
            self.w_pct.configure(text="100%")
            self.w_eta.configure(text=t("g_elapsed", v=fmt_dur(time.time() - self.t_start)))
            self.w_status.configure(text=self.outputs[0] if self.outputs else "")
            self.w_open_md.configure(state="normal")
            self.w_open_folder.configure(state="normal")
            r = self.result
            msg = t("g_done_msg", p=self.outputs[0] if self.outputs else "?", m=r.get("messages", "?"),
                    tok=f"{r.get('tokens', 0):,}".replace(",", "."))
            if r.get("errors"):
                msg += "\n\n" + t("g_done_errors", n=len(r["errors"]))
            if r.get("tokens", 0) > 400_000:
                msg += "\n\n" + t("hint_split")
            if r.get("no_media"):
                msg += "\n\n" + t("warn_omitted", n=r["omitted"], v=r.get("omitted_voice", 0))
                messagebox.showwarning(t("g_done_title"), msg, parent=self.root)
            else:
                if r.get("omitted"):
                    v = r.get("omitted_voice", 0)
                    msg += "\n\n" + t("warn_omitted_partial", n=r["omitted"], v=t("voice_part", v=v) if v else "")
                messagebox.showinfo(t("g_done_title"), msg, parent=self.root)
        elif was_stopping:
            self.pbar.configure(mode="determinate", value=0)
            self.w_status.configure(text=t("g_stopped"))
            self._append(self.err_list, "⚠ " + t("g_stopped"), "warn")
        else:
            self.pbar.configure(mode="determinate", value=0)
            msg = self.fatal or t("g_crash", c=code)
            self.w_status.configure(text=t("g_failed"))
            self.nb.select(0 if self.fatal else 1)
            messagebox.showerror(t("g_failed"), msg, parent=self.root)

    # ------------------------------------------------------------------ varie
    def open_md(self):
        if self.outputs and Path(self.outputs[0]).exists():
            try:
                os.startfile(self.outputs[0])  # type: ignore[attr-defined]
            except OSError:
                subprocess.Popen(["notepad.exe", self.outputs[0]])

    def open_folder(self):
        if self.outputs:
            subprocess.Popen(["explorer.exe", "/select,", os.path.normpath(self.outputs[0])])

    def about(self):
        win = tk.Toplevel(self.root)
        win.title(t("g_about"))
        win.transient(self.root)
        win.resizable(False, False)
        try:
            win.iconbitmap(str(ICON))
        except Exception:
            pass
        f = ttk.Frame(win, padding=16)
        f.pack(fill="both", expand=True)
        ttk.Label(f, text=t("g_about_text", v=VERSION, a=AUTHOR), wraplength=420, justify="left").pack(anchor="w")
        link = ttk.Label(f, text=AUTHOR_URL, style="Link.TLabel", cursor="hand2")
        link.pack(anchor="w", pady=(10, 0))
        link.bind("<Button-1>", lambda e: webbrowser.open(AUTHOR_URL))
        btns = ttk.Frame(f)
        btns.pack(fill="x", pady=(14, 0))
        if LICENSE.exists():
            ttk.Button(btns, text=t("g_license"), command=lambda: os.startfile(str(LICENSE))).pack(side="left")  # type: ignore[attr-defined]
        ttk.Button(btns, text="OK", command=win.destroy).pack(side="right")
        win.grab_set()

    def on_close(self):
        if self.running:
            if not messagebox.askyesno("Zapp2md", t("g_confirm_close"), parent=self.root):
                return
            try:
                if self.proc:
                    self.proc.kill()
            except Exception:
                pass
        self._save()
        self.root.destroy()


def main():
    try:
        import ctypes

        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # testo nitido sugli schermi ad alta risoluzione
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("AndreaMoretto.Zapp2md")
    except Exception:
        pass
    root = tk.Tk()
    try:
        root.tk.call("tk", "scaling", root.winfo_fpixels("1i") / 72.0)
    except Exception:
        pass
    default_font = ("Segoe UI", 10)
    root.option_add("*Font", default_font)
    for name in ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont"):
        try:
            tk.font.nametofont(name).configure(family="Segoe UI", size=10)  # type: ignore[attr-defined]
        except Exception:
            pass
    initial = sys.argv[1] if len(sys.argv) > 1 else None
    app = App(root, initial)
    if initial and os.environ.get("W2MD_AUTOSTART") == "1":  # solo per i test automatici
        root.after(800, app.start)
    root.mainloop()


if __name__ == "__main__":
    import tkinter.font  # noqa: F401  (usato in main)

    main()
