# Zapp2md 1.0 - (c) 2026 Andrea Moretto - CC BY-NC-SA 4.0
#
# Prepara tutto il necessario nella cartella del programma:
#   uv (gestore pacchetti) -> Python 3.12 portatile -> librerie -> modello di trascrizione.
# Viene eseguito dall'installatore e dalle voci "Ripara Zapp2md" del menu Start.
#
# Modalità normale: scarica SOLO ciò che manca. Ogni componente già presente viene prima verificato
# e riutilizzato solo se funziona; in caso di dubbio viene scaricato di nuovo:
#   - componenti già installati nella cartella del programma (aggiornamento / riparazione);
#   - uv già presente sul PC;
#   - Python 3.12 già scaricato da uv;
#   - pacchetti già presenti nella cache di uv;
#   - modello di trascrizione già presente nella cache standard di Hugging Face.
# Modalità -Full: elimina i componenti del programma e riscarica tutto, senza riutilizzare nulla.

param(
    [string]$AppDir = $PSScriptRoot,
    [ValidateSet("it", "pt", "en")][string]$Lang = "it",
    [switch]$Full,
    [switch]$NoPause
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"   # rende Invoke-WebRequest molto più veloce
$UvVersion = "0.12.18"
$PythonVersion = "3.12"
$Model = "large-v3-turbo"

$Host.UI.RawUI.WindowTitle = "Zapp2md 1.0 - setup"
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

function Msg([string]$it, [string]$pt, [string]$en) {
    switch ($Lang) { "it" { $it } "pt" { $pt } default { $en } }
}
function Step([string]$it, [string]$pt, [string]$en) {
    Write-Host ""
    Write-Host ("==> " + (Msg $it $pt $en)) -ForegroundColor Cyan
}
function Info([string]$it, [string]$pt, [string]$en) {
    Write-Host ("    " + (Msg $it $pt $en)) -ForegroundColor Gray
}
function Check([string]$what) {
    if ($LASTEXITCODE -ne 0) { throw "$what (exit code $LASTEXITCODE)" }
}
function Get-File([string[]]$Urls, [string]$Out) {
    foreach ($u in $Urls) {
        for ($try = 1; $try -le 3; $try++) {
            try {
                Invoke-WebRequest -Uri $u -OutFile $Out -UseBasicParsing -TimeoutSec 600
                return $true
            } catch {
                Write-Host "    $($_.Exception.Message) - retry $try/3" -ForegroundColor Yellow
                Start-Sleep -Seconds (3 * $try)
            }
        }
    }
    return $false
}
function Remove-Dir([string]$Path) {
    if (Test-Path $Path) { Remove-Item -Recurse -Force $Path -ErrorAction SilentlyContinue }
    if (Test-Path $Path) { cmd /c "rmdir /s /q `"$Path`"" | Out-Null }
}
function Test-Uv([string]$Exe) {
    if (-not (Test-Path $Exe)) { return $false }
    try { & $Exe --version *> $null; return ($LASTEXITCODE -eq 0) } catch { return $false }
}
function Test-Python([string]$Exe) {
    if (-not (Test-Path $Exe)) { return $false }
    try {
        & $Exe -c "import sys, tkinter, sqlite3, ssl, ctypes; sys.exit(0 if sys.version_info[:2] == (3, 12) else 1)" *> $null
        return ($LASTEXITCODE -eq 0)
    } catch { return $false }
}

$uvDir = Join-Path $AppDir "uv"
$uv = Join-Path $uvDir "uv.exe"
$pyDir = Join-Path $AppDir "python"
$py = Join-Path $pyDir "python.exe"
$modelsDir = Join-Path $AppDir "models"
$ownCache = Join-Path $AppDir "uvcache"

$log = Join-Path $AppDir "install.log"
try { Start-Transcript -Path $log -Force | Out-Null } catch {}

try {
    Write-Host "Zapp2md 1.0  -  (c) 2026 Andrea Moretto  -  CC BY-NC-SA 4.0" -ForegroundColor Green
    Write-Host (Msg "Cartella: $AppDir" "Pasta: $AppDir" "Folder: $AppDir")
    Write-Host (Msg "Non chiudere questa finestra: si chiuderà da sola al termine." `
                    "Não feche esta janela: fecha-se sozinha no fim." `
                    "Do not close this window: it closes by itself when finished.")

    if ($AppDir.Length -gt 100) {
        throw (Msg "Percorso di installazione troppo lungo (max 100 caratteri): $AppDir" `
                   "Caminho de instalação demasiado longo (máx. 100 caracteres): $AppDir" `
                   "Installation path too long (max 100 characters): $AppDir")
    }

    if ($Full) {
        Step "Installazione completa: rimuovo i componenti esistenti e riscarico tutto..." `
             "Instalação completa: a remover os componentes existentes e a descarregar tudo de novo..." `
             "Full installation: removing existing components and downloading everything again..."
        foreach ($d in "venv", "python", "python_tmp", "uv", "models", "uvcache") { Remove-Dir (Join-Path $AppDir $d) }
    }
    Remove-Dir (Join-Path $AppDir "venv")        # resti di versioni di prova precedenti
    Remove-Dir (Join-Path $AppDir "python_tmp")

    # ---- 1. uv ---------------------------------------------------------------------------
    Step "1/4  Strumento di installazione (uv)" "1/4  Ferramenta de instalação (uv)" "1/4  Installation tool (uv)"
    if (Test-Uv $uv) {
        Info "già presente" "já presente" "already present"
    } else {
        Remove-Dir $uvDir
        if (-not $Full) {
            $sys = Get-Command uv.exe -ErrorAction SilentlyContinue | Select-Object -First 1
            if ($sys) {
                New-Item -ItemType Directory -Force $uvDir | Out-Null
                Copy-Item $sys.Source $uv -Force
                if (Test-Uv $uv) {
                    Info "riutilizzato quello già presente sul PC" "reutilizado o que já existe no PC" "reused the one already on this PC"
                } else { Remove-Dir $uvDir }
            }
        }
        if (-not (Test-Uv $uv)) {
            Info "download (~20 MB)..." "a descarregar (~20 MB)..." "downloading (~20 MB)..."
            $zip = Join-Path $env:TEMP "zapp2md-uv.zip"
            $urls = @("https://github.com/astral-sh/uv/releases/download/$UvVersion/uv-x86_64-pc-windows-msvc.zip",
                      "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip")
            if (-not (Get-File $urls $zip)) { throw (Msg "Download di uv non riuscito." "Falha ao descarregar o uv." "Could not download uv.") }
            New-Item -ItemType Directory -Force $uvDir | Out-Null
            Expand-Archive -Path $zip -DestinationPath $uvDir -Force
            Remove-Item $zip -Force -ErrorAction SilentlyContinue
            if (-not (Test-Path $uv)) {
                $found = Get-ChildItem $uvDir -Recurse -Filter uv.exe | Select-Object -First 1
                if (-not $found) { throw "uv.exe not found" }
                Move-Item $found.FullName $uv -Force
            }
            if (-not (Test-Uv $uv)) { throw "uv.exe does not run" }
        }
    }
    $env:UV_LINK_MODE = "copy"
    $env:UV_NO_CONFIG = "1"

    # ---- 2. Python ------------------------------------------------------------------------
    # Python "portatile" (python-build-standalone) copiato direttamente nella cartella "python":
    # niente ambiente virtuale e niente collegamenti di cartella (junction), che l'installatore
    # potrebbe bloccare per motivi di sicurezza.
    Step "2/4  Python $PythonVersion" "2/4  Python $PythonVersion" "2/4  Python $PythonVersion"
    if (Test-Python $py) {
        Info "già presente" "já presente" "already present"
    } else {
        Remove-Dir $pyDir
        if (-not $Full) {
            # Python 3.12 già scaricato in precedenza da uv (stesso pacchetto che scaricheremmo)
            $roots = @("$env:APPDATA\uv\python", "$env:LOCALAPPDATA\uv\python")
            if ($env:UV_PYTHON_INSTALL_DIR) { $roots = @($env:UV_PYTHON_INSTALL_DIR) + $roots }
            $cands = foreach ($root in $roots) {
                if (Test-Path $root) {
                    Get-ChildItem $root -Directory -ErrorAction SilentlyContinue |
                        Where-Object { $_.Name -match '^cpython-3\.12\.(\d+)-windows-x86_64-none$' -and
                                       -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -and
                                       (Test-Path (Join-Path $_.FullName "python.exe")) }
                }
            }
            $cands = $cands | Sort-Object { [int]($_.Name -replace '^cpython-3\.12\.(\d+)-.*$', '$1') } -Descending
            foreach ($c in $cands) {
                Copy-Item $c.FullName $pyDir -Recurse -Force
                if (Test-Python $py) {
                    Info "riutilizzato $($c.Name) già presente sul PC" "reutilizado $($c.Name) já presente no PC" "reused $($c.Name) already on this PC"
                    break
                }
                Remove-Dir $pyDir
            }
        }
        if (-not (Test-Python $py)) {
            Info "download (~30 MB)..." "a descarregar (~30 MB)..." "downloading (~30 MB)..."
            $list = (& $uv python list $PythonVersion --only-downloads --output-format json | Out-String) | ConvertFrom-Json
            Check "uv python list"
            $entry = $list | Where-Object { $_.implementation -eq "cpython" -and $_.os -eq "windows" -and
                                            $_.arch -eq "x86_64" -and $_.variant -eq "default" -and $_.url } |
                             Select-Object -First 1
            if (-not $entry) { throw "Python $PythonVersion download not found" }
            Info $entry.key $entry.key $entry.key
            $tgz = Join-Path $env:TEMP "zapp2md-python.tar.gz"
            if (-not (Get-File @($entry.url) $tgz)) {
                throw (Msg "Download di Python non riuscito." "Falha ao descarregar o Python." "Could not download Python.")
            }
            $tmp = Join-Path $AppDir "python_tmp"
            New-Item -ItemType Directory -Force $tmp | Out-Null
            & "$env:SystemRoot\System32\tar.exe" -xzf $tgz -C $tmp
            Check "tar"
            Remove-Item $tgz -Force -ErrorAction SilentlyContinue
            $inner = Get-ChildItem $tmp -Recurse -Filter python.exe | Select-Object -First 1
            if (-not $inner) { throw "python.exe not found in archive" }
            Move-Item $inner.Directory.FullName $pyDir
            Remove-Dir $tmp
            if (-not (Test-Python $py)) { throw "Python does not run" }
        }
    }

    # ---- 3. Librerie ----------------------------------------------------------------------
    Step "3/4  Librerie (si scarica solo ciò che manca, max ~300 MB)" `
         "3/4  Bibliotecas (descarrega-se só o que falta, máx. ~300 MB)" `
         "3/4  Libraries (only what is missing is downloaded, max ~300 MB)"
    $sharedCache = Join-Path $env:LOCALAPPDATA "uv\cache"
    $useShared = (-not $Full) -and (Test-Path $sharedCache) -and (-not $env:UV_CACHE_DIR)
    $env:UV_CACHE_DIR = if ($useShared) { $sharedCache } else { $ownCache }
    if ($useShared) {
        Info "uso i pacchetti già presenti nella cache di uv del PC" "uso os pacotes já presentes na cache do uv do PC" "using packages already in this PC's uv cache"
    }
    $req = Join-Path $AppDir "requirements.txt"
    $extra = @()
    if ($Full) { $extra = @("--reinstall", "--refresh") }
    & $uv pip install --python $py --break-system-packages @extra -r $req
    if ($LASTEXITCODE -ne 0 -and $useShared) {
        # cache condivisa inutilizzabile (bloccata o danneggiata): riprovo con una cache privata
        Write-Host "    retry with a private cache..." -ForegroundColor Yellow
        $useShared = $false
        $env:UV_CACHE_DIR = $ownCache
        & $uv pip install --python $py --break-system-packages --refresh -r $req
    }
    Check "uv pip install"

    # ---- 4. Modello di trascrizione + verifica --------------------------------------------
    Step "4/4  Modello di trascrizione ($Model, ~1,6 GB se da scaricare)" `
         "4/4  Modelo de transcrição ($Model, ~1,6 GB se for preciso descarregar)" `
         "4/4  Transcription model ($Model, ~1.6 GB if it must be downloaded)"
    $env:PYTHONIOENCODING = "utf-8"
    $engine = Join-Path $AppDir "zapp2md.py"
    if (-not $Full -and -not (Test-Path $modelsDir)) {
        # Modello già presente nella cache standard di Hugging Face (es. usato da altri programmi
        # basati su Whisper): se si carica correttamente lo si usa da lì, senza copie.
        $reuse = $false
        try {
            $ErrorActionPreference = "Continue"
            & $py $engine --check-model --model $Model *> $null
            $reuse = ($LASTEXITCODE -eq 0)
        } catch { $reuse = $false } finally { $ErrorActionPreference = "Stop" }
        if ($reuse) {
            Info "già presente sul PC (cache di Hugging Face): riutilizzato" `
                 "já presente no PC (cache do Hugging Face): reutilizado" `
                 "already on this PC (Hugging Face cache): reused"
        } else {
            New-Item -ItemType Directory -Force $modelsDir | Out-Null
        }
    }
    if ($Full) { New-Item -ItemType Directory -Force $modelsDir | Out-Null }
    & $py $engine --setup --ui $Lang --model $Model
    Check "zapp2md --setup"

    if (-not $useShared) { Remove-Dir $ownCache }
    Write-Host ""
    Write-Host (Msg "Installazione completata." "Instalação concluída." "Installation completed.") -ForegroundColor Green
    try { Stop-Transcript | Out-Null } catch {}
    if (-not $NoPause) { Start-Sleep -Seconds 3 }
    exit 0
}
catch {
    Write-Host ""
    Write-Host ("ERROR: " + $_.Exception.Message) -ForegroundColor Red
    Write-Host ""
    Write-Host (Msg "Installazione non completata. Controlla la connessione a internet e usa 'Ripara Zapp2md' dal menu Start. Dettagli: $log" `
                    "Instalação não concluída. Verifique a ligação à internet e use 'Reparar Zapp2md' no menu Iniciar. Detalhes: $log" `
                    "Installation not completed. Check the internet connection and use 'Repair Zapp2md' from the Start menu. Details: $log") -ForegroundColor Yellow
    try { Stop-Transcript | Out-Null } catch {}
    if (-not $NoPause) { Read-Host (Msg "Premi Invio per chiudere" "Prima Enter para fechar" "Press Enter to close") | Out-Null }
    exit 1
}
