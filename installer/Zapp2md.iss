; Zapp2md 1.0 - installatore
; Copyright (c) 2026 Andrea Moretto - CC BY-NC-SA 4.0 (uso non commerciale)
; Compilazione: build.bat (richiede Inno Setup 6, gratuito: https://jrsoftware.org/isinfo.php)

#define MyAppName "Zapp2md"
#define MyAppVersion "1.0"
#define MyAppPublisher "Andrea Moretto"
#define MyAppURL "https://www.linkedin.com/in/andrea-moretto-mba/"
#define SrcDir "..\app"

[Setup]
AppId={{4C6A83DE-CCB5-4888-B247-D6BE22191E88}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
AppContact={#MyAppURL}
AppCopyright=Copyright (c) 2026 {#MyAppPublisher}
VersionInfoVersion=1.0.0.0
VersionInfoCompany={#MyAppPublisher}
VersionInfoCopyright=Copyright (c) 2026 {#MyAppPublisher} - CC BY-NC-SA 4.0
VersionInfoDescription={#MyAppName} {#MyAppVersion} Setup
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion=1.0.0.0
DefaultDirName={localappdata}\Programs\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
LicenseFile={#SrcDir}\LICENSE.txt
SetupIconFile={#SrcDir}\app.ico
UninstallDisplayIcon={app}\Zapp2md.exe
UninstallDisplayName={#MyAppName} {#MyAppVersion}
OutputDir=..\dist
OutputBaseFilename={#MyAppName}-{#MyAppVersion}-Setup
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
MinVersion=10.0.17763
ShowLanguageDialog=yes
DisableWelcomePage=no
WizardSizePercent=120
; spazio occupato dai componenti scaricati (Python, librerie, modello)
ExtraDiskSpaceRequired=2700000000
CloseApplications=yes

[Languages]
Name: "it"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "pt"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "en"; MessagesFile: "compiler:Default.isl"

[CustomMessages]
it.AuthorLine=Zapp2md {#MyAppVersion}  ·  Autore: {#MyAppPublisher}
pt.AuthorLine=Zapp2md {#MyAppVersion}  ·  Autor: {#MyAppPublisher}
en.AuthorLine=Zapp2md {#MyAppVersion}  ·  Author: {#MyAppPublisher}
it.LicenseLine=Licenza CC BY-NC-SA 4.0: copia e distribuzione libere e gratuite, vendita vietata.
pt.LicenseLine=Licença CC BY-NC-SA 4.0: cópia e distribuição livres e gratuitas, venda proibida.
en.LicenseLine=CC BY-NC-SA 4.0 licence: free copying and distribution, sale prohibited.
it.WelcomeExtra=Trasforma le chat WhatsApp esportate (vocali, foto, video, documenti) in un documento da analizzare con un LLM come Claude o ChatGPT, o con altri strumenti di AI. Tutto resta sul tuo computer. Durante l'installazione si scarica solo ciò che manca (fino a circa 2 GB).
pt.WelcomeExtra=Transforma as conversas do WhatsApp exportadas (voz, fotos, vídeos, documentos) num documento para analisar com um LLM como o Claude ou o ChatGPT, ou com outras ferramentas de IA. Tudo fica no seu computador. Na instalação só se descarrega o que falta (até cerca de 2 GB).
en.WelcomeExtra=Turns exported WhatsApp chats (voice messages, photos, videos, documents) into a document to analyse with an LLM such as Claude or ChatGPT, or other AI tools. Everything stays on your computer. Installation downloads only what is missing (up to about 2 GB).
it.DownloadingDeps=Preparazione dei componenti: viene scaricato solo ciò che manca (al massimo circa 2 GB). L'avanzamento è mostrato nella finestra nera: non chiuderla...
pt.DownloadingDeps=A preparar os componentes: só é descarregado o que falta (no máximo cerca de 2 GB). O progresso é mostrado na janela preta: não a feche...
en.DownloadingDeps=Preparing the components: only what is missing is downloaded (about 2 GB at most). Progress is shown in the black window: do not close it...
it.DepsFailed=Il download dei componenti non è stato completato (codice %1).%n%nControlla la connessione a internet, poi apri "Ripara Zapp2md" dal menu Start per completare l'installazione.
pt.DepsFailed=A transferência dos componentes não foi concluída (código %1).%n%nVerifique a ligação à internet e depois abra "Reparar Zapp2md" no menu Iniciar para concluir a instalação.
en.DepsFailed=The download of the components did not complete (code %1).%n%nCheck the internet connection, then open "Repair Zapp2md" from the Start menu to complete the installation.
it.PathTooLong=Il percorso scelto è troppo lungo (massimo 90 caratteri). Scegli una cartella con un percorso più corto.
pt.PathTooLong=O caminho escolhido é demasiado longo (máximo 90 caracteres). Escolha uma pasta com um caminho mais curto.
en.PathTooLong=The chosen path is too long (maximum 90 characters). Choose a folder with a shorter path.
it.RepairName=Ripara Zapp2md
it.RepairFullName=Ripara Zapp2md (reinstallazione completa)
it.FullTask=Installazione completa: riscarica tutti i componenti, senza riutilizzare quelli già presenti sul PC
it.ExtraGroup=Opzioni di installazione:
pt.RepairFullName=Reparar Zapp2md (reinstalação completa)
pt.FullTask=Instalação completa: descarregar todos os componentes de novo, sem reutilizar os que já existem no PC
pt.ExtraGroup=Opções de instalação:
en.RepairFullName=Repair Zapp2md (full reinstall)
en.FullTask=Full installation: download all components again, without reusing those already on this PC
en.ExtraGroup=Installation options:
pt.RepairName=Reparar Zapp2md
en.RepairName=Repair Zapp2md
it.GuideName=Guida Zapp2md
pt.GuideName=Guia Zapp2md
en.GuideName=Zapp2md guide
it.LicenseName=Licenza Zapp2md
pt.LicenseName=Licença Zapp2md
en.LicenseName=Zapp2md licence

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "fullinstall"; Description: "{cm:FullTask}"; GroupDescription: "{cm:ExtraGroup}"; Flags: unchecked

[Files]
Source: "{#SrcDir}\Zapp2md.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\zapp2md.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\i18n.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\gui.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\setup.ps1"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\app.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\LICENSE.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\THIRD-PARTY-NOTICES.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SrcDir}\README.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\Zapp2md.exe"; WorkingDir: "{app}"; AppUserModelID: "AndreaMoretto.Zapp2md"; Comment: "{#MyAppName} {#MyAppVersion} - {#MyAppPublisher}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\Zapp2md.exe"; WorkingDir: "{app}"; AppUserModelID: "AndreaMoretto.Zapp2md"; Tasks: desktopicon
Name: "{group}\{cm:RepairName}"; Filename: "{sys}\WindowsPowerShell\v1.0\powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\setup.ps1"" -AppDir ""{app}"" -Lang {language}"; WorkingDir: "{app}"; IconFilename: "{app}\app.ico"
Name: "{group}\{cm:RepairFullName}"; Filename: "{sys}\WindowsPowerShell\v1.0\powershell.exe"; Parameters: "-NoProfile -ExecutionPolicy Bypass -File ""{app}\setup.ps1"" -AppDir ""{app}"" -Lang {language} -Full"; WorkingDir: "{app}"; IconFilename: "{app}\app.ico"
Name: "{group}\{cm:LicenseName}"; Filename: "{app}\LICENSE.txt"
Name: "{group}\{cm:GuideName}"; Filename: "{app}\README.txt"

[Run]
Filename: "{app}\Zapp2md.exe"; WorkingDir: "{app}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent; Check: DepsOk

[UninstallDelete]
Type: filesandordirs; Name: "{app}\venv"
Type: filesandordirs; Name: "{app}\python"
Type: filesandordirs; Name: "{app}\models"
Type: filesandordirs; Name: "{app}\uv"
Type: filesandordirs; Name: "{app}\uvcache"
Type: filesandordirs; Name: "{app}\python_tmp"
Type: filesandordirs; Name: "{app}\__pycache__"
Type: files; Name: "{app}\install.log"
Type: dirifempty; Name: "{app}"

[Code]
var
  DepsResult: Integer;

procedure LinkClick(Sender: TObject);
var
  ErrorCode: Integer;
begin
  ShellExec('open', '{#MyAppURL}', '', '', SW_SHOWNORMAL, ewNoWait, ErrorCode);
end;

procedure InitializeWizard;
var
  Extra, Author, Lic, Link: TNewStaticText;
begin
  DepsResult := -1;
  WizardForm.WelcomeLabel2.AdjustHeight;

  Extra := TNewStaticText.Create(WizardForm);
  Extra.Parent := WizardForm.WelcomePage;
  Extra.Left := WizardForm.WelcomeLabel2.Left;
  Extra.Width := WizardForm.WelcomeLabel2.Width;
  Extra.Top := WizardForm.WelcomeLabel2.Top + WizardForm.WelcomeLabel2.Height + ScaleY(12);
  Extra.WordWrap := True;
  Extra.Caption := CustomMessage('WelcomeExtra');
  Extra.AdjustHeight;

  Author := TNewStaticText.Create(WizardForm);
  Author.Parent := WizardForm.WelcomePage;
  Author.Left := Extra.Left;
  Author.Top := Extra.Top + Extra.Height + ScaleY(16);
  Author.Caption := CustomMessage('AuthorLine');
  Author.Font.Style := [fsBold];

  Lic := TNewStaticText.Create(WizardForm);
  Lic.Parent := WizardForm.WelcomePage;
  Lic.Left := Author.Left;
  Lic.Width := Extra.Width;
  Lic.Top := Author.Top + Author.Height + ScaleY(4);
  Lic.WordWrap := True;
  Lic.Caption := CustomMessage('LicenseLine');
  Lic.AdjustHeight;

  Link := TNewStaticText.Create(WizardForm);
  Link.Parent := WizardForm.WelcomePage;
  Link.Left := Author.Left;
  Link.Top := Lic.Top + Lic.Height + ScaleY(6);
  Link.Caption := '{#MyAppURL}';
  Link.Cursor := crHand;
  Link.Font.Color := clHotLight;
  Link.Font.Style := [fsUnderline];
  Link.OnClick := @LinkClick;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if (CurPageID = wpSelectDir) and (Length(WizardDirValue) > 90) then
  begin
    MsgBox(CustomMessage('PathTooLong'), mbError, MB_OK);
    Result := False;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  Params: String;
begin
  if CurStep = ssPostInstall then
  begin
    WizardForm.StatusLabel.Caption := CustomMessage('DownloadingDeps');
    WizardForm.FilenameLabel.Caption := '';
    WizardForm.ProgressGauge.Style := npbstMarquee;
    Params := '-NoProfile -ExecutionPolicy Bypass -File "' + ExpandConstant('{app}\setup.ps1') +
              '" -AppDir "' + ExpandConstant('{app}') + '" -Lang ' + ActiveLanguage;
    if WizardIsTaskSelected('fullinstall') then
      Params := Params + ' -Full';
    if WizardSilent then
      Params := Params + ' -NoPause';
    if not Exec(ExpandConstant('{sys}\WindowsPowerShell\v1.0\powershell.exe'), Params, ExpandConstant('{app}'),
                SW_SHOW, ewWaitUntilTerminated, DepsResult) then
      DepsResult := -1;
    WizardForm.ProgressGauge.Style := npbstNormal;
    if DepsResult <> 0 then
      SuppressibleMsgBox(FmtMessage(CustomMessage('DepsFailed'), [IntToStr(DepsResult)]), mbError, MB_OK, IDOK);
  end;
end;

function DepsOk: Boolean;
begin
  Result := (DepsResult = 0);
end;
