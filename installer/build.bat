@echo off
rem Zapp2md 1.0 - crea dist\Zapp2md-1.0-Setup.exe e dist\SHA256SUMS.txt
rem Requisiti: Windows 10/11 (compilatore C# incluso) e Inno Setup 6 (winget install JRSoftware.InnoSetup)
setlocal
cd /d "%~dp0"

rem ---- 1. lanciatore Zapp2md.exe ------------------------------------------------
set "CSC=%WINDIR%\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
if not exist "%CSC%" (
  echo Compilatore C# non trovato: %CSC%
  exit /b 1
)
"%CSC%" /nologo /target:winexe /optimize+ /win32icon:..\app\app.ico /out:..\app\Zapp2md.exe /reference:System.Windows.Forms.dll ..\launcher\Zapp2md.cs || (echo ERRORE lanciatore & exit /b 1)

rem ---- 2. installatore ------------------------------------------------------------
set "ISCC=%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" (
  echo Inno Setup 6 non trovato. Installalo con: winget install JRSoftware.InnoSetup
  exit /b 1
)
"%ISCC%" /Qp Zapp2md.iss || (echo ERRORE installatore & exit /b 1)

rem ---- 3. codice di controllo SHA256 ----------------------------------------------
powershell -NoProfile -Command "$h = (Get-FileHash ..\dist\Zapp2md-1.0-Setup.exe -Algorithm SHA256).Hash.ToLower(); Set-Content -Encoding ascii ..\dist\SHA256SUMS.txt ($h + '  Zapp2md-1.0-Setup.exe'); Write-Host ('SHA256: ' + $h)"
echo.
echo OK: ..\dist\Zapp2md-1.0-Setup.exe
