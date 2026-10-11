// Zapp2md 1.0 - lanciatore
// Copyright (c) 2026 Andrea Moretto - CC BY-NC-SA 4.0
//
// Piccolo eseguibile che avvia l'interfaccia grafica (python\pythonw.exe gui.py) dalla cartella del
// programma. Gli argomenti vengono passati così come sono: trascinando uno .zip sull'icona di
// Zapp2md.exe il file viene già selezionato nella finestra.

using System;
using System.Diagnostics;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Text;
using System.Windows.Forms;

[assembly: AssemblyTitle("Zapp2md")]
[assembly: AssemblyDescription("Zapp2md - WhatsApp chat exports to Markdown for LLMs")]
[assembly: AssemblyCompany("Andrea Moretto")]
[assembly: AssemblyProduct("Zapp2md")]
[assembly: AssemblyCopyright("Copyright (c) 2026 Andrea Moretto - CC BY-NC-SA 4.0")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

static class Zapp2mdLauncher
{
    [STAThread]
    static int Main(string[] args)
    {
        string dir = AppDomain.CurrentDomain.BaseDirectory;
        string pythonw = Path.Combine(dir, "python", "pythonw.exe");
        string gui = Path.Combine(dir, "gui.py");

        if (!File.Exists(pythonw) || !File.Exists(gui))
        {
            string lang = CultureInfo.CurrentUICulture.TwoLetterISOLanguageName;
            string msg;
            if (lang == "it")
                msg = "Installazione incompleta: manca\n" + (File.Exists(pythonw) ? gui : pythonw) +
                      "\n\nApri \"Ripara Zapp2md\" dal menu Start.";
            else if (lang == "pt")
                msg = "Instalação incompleta: falta\n" + (File.Exists(pythonw) ? gui : pythonw) +
                      "\n\nAbra \"Reparar Zapp2md\" no menu Iniciar.";
            else
                msg = "Incomplete installation: missing\n" + (File.Exists(pythonw) ? gui : pythonw) +
                      "\n\nOpen \"Repair Zapp2md\" from the Start menu.";
            MessageBox.Show(msg, "Zapp2md", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return 1;
        }

        var cmd = new StringBuilder(Quote(gui));
        foreach (string a in args)
            cmd.Append(' ').Append(Quote(a));

        try
        {
            var psi = new ProcessStartInfo(pythonw, cmd.ToString());
            psi.WorkingDirectory = dir;
            psi.UseShellExecute = false;
            Process.Start(psi);
            return 0;
        }
        catch (Exception e)
        {
            MessageBox.Show(e.Message, "Zapp2md", MessageBoxButtons.OK, MessageBoxIcon.Error);
            return 2;
        }
    }

    // Quoting secondo le regole di CommandLineToArgvW (gestisce spazi, virgolette e backslash finali).
    static string Quote(string s)
    {
        if (s.Length > 0 && s.IndexOfAny(new[] { ' ', '\t', '"' }) < 0)
            return s;
        var sb = new StringBuilder("\"");
        int backslashes = 0;
        foreach (char c in s)
        {
            if (c == '\\') { backslashes++; continue; }
            if (c == '"') sb.Append('\\', backslashes * 2 + 1);
            else sb.Append('\\', backslashes);
            backslashes = 0;
            sb.Append(c);
        }
        sb.Append('\\', backslashes * 2);
        sb.Append('"');
        return sb.ToString();
    }
}
