"""Testi dell'interfaccia e del documento prodotto: Italiano, Português, English."""

LANGS = {"it": "Italiano", "pt": "Português", "en": "English"}

T = {
    # ------------------------------------------------------------------ console
    "ask_file": {
        "it": "Scegli il file .zip esportato da WhatsApp nella finestra che si apre...",
        "pt": "Escolha o ficheiro .zip exportado do WhatsApp na janela que se abre...",
        "en": "Choose the .zip file exported from WhatsApp in the window that opens...",
    },
    "ask_path": {
        "it": "Trascina qui il file .zip (o la cartella della chat) e premi Invio: ",
        "pt": "Arraste para aqui o ficheiro .zip (ou a pasta da conversa) e prima Enter: ",
        "en": "Drag the .zip file (or the chat folder) here and press Enter: ",
    },
    "ask_video": {
        "it": "Trascrivere anche l'audio dei video? (più lento) [S/n]: ",
        "pt": "Transcrever também o áudio dos vídeos? (mais lento) [S/n]: ",
        "en": "Also transcribe the audio of videos? (slower) [Y/n]: ",
    },
    "yes_letters": {"it": "sy", "pt": "sy", "en": "y"},
    "press_enter": {
        "it": "Premi Invio per chiudere.",
        "pt": "Prima Enter para fechar.",
        "en": "Press Enter to close.",
    },
    "start": {"it": "Zapp2md {v} — input: {p}", "pt": "Zapp2md {v} — entrada: {p}", "en": "Zapp2md {v} — input: {p}"},
    "extracting": {
        "it": "Estraggo {z} in {d} ...",
        "pt": "A extrair {z} para {d} ...",
        "en": "Extracting {z} to {d} ...",
    },
    "reuse_extracted": {
        "it": "Uso i file già estratti in: {d}",
        "pt": "A usar os ficheiros já extraídos em: {d}",
        "en": "Using files already extracted in: {d}",
    },
    "chat_found": {
        "it": "Chat: '{t}' (file {f}), {n} file allegati nell'esportazione.",
        "pt": "Conversa: '{t}' (ficheiro {f}), {n} ficheiros anexos na exportação.",
        "en": "Chat: '{t}' (file {f}), {n} attached files in the export.",
    },
    "messages_found": {
        "it": "Messaggi: {n} (formato data '{o}', dal {a} al {b}){x}",
        "pt": "Mensagens: {n} (formato de data '{o}', de {a} a {b}){x}",
        "en": "Messages: {n} (date format '{o}', from {a} to {b}){x}",
    },
    "reordered": {
        "it": "; {n} fuori ordine, riordinati",
        "pt": "; {n} fora de ordem, reordenadas",
        "en": "; {n} out of order, re-sorted",
    },
    "no_messages": {
        "it": "Nessun messaggio riconosciuto nel file della chat.",
        "pt": "Nenhuma mensagem reconhecida no ficheiro da conversa.",
        "en": "No messages recognised in the chat file.",
    },
    "media_summary": {
        "it": "Media: {tot} totali, {cached} già in cache, {todo} da elaborare.",
        "pt": "Multimédia: {tot} no total, {cached} já em cache, {todo} por processar.",
        "en": "Media: {tot} total, {cached} already cached, {todo} to process.",
    },
    "audio_total": {
        "it": "Audio da trascrivere: {d} (h:mm:ss) in {n} file.",
        "pt": "Áudio por transcrever: {d} (h:mm:ss) em {n} ficheiros.",
        "en": "Audio to transcribe: {d} (h:mm:ss) in {n} files.",
    },
    "eta": {
        "it": " | trascritto {a}/{b}, tempo residuo stimato ~{c}",
        "pt": " | transcrito {a}/{b}, tempo restante estimado ~{c}",
        "en": " | transcribed {a}/{b}, estimated time left ~{c}",
    },
    "media_done": {
        "it": "Elaborazione media completata in {d}.",
        "pt": "Processamento multimédia concluído em {d}.",
        "en": "Media processing completed in {d}.",
    },
    "ocr_on": {
        "it": "OCR di Windows attivo (lingua: {l}; disponibili: {a})",
        "pt": "OCR do Windows ativo (idioma: {l}; disponíveis: {a})",
        "en": "Windows OCR active (language: {l}; available: {a})",
    },
    "ocr_off": {
        "it": "OCR non disponibile ({e}): il testo delle immagini non verrà letto.",
        "pt": "OCR indisponível ({e}): o texto das imagens não será lido.",
        "en": "OCR not available ({e}): text in images will not be read.",
    },
    "loading_model": {
        "it": "Carico il modello di trascrizione '{m}' (la prima volta viene scaricato: 1,5-3 GB)...",
        "pt": "A carregar o modelo de transcrição '{m}' (na primeira vez é descarregado: 1,5-3 GB)...",
        "en": "Loading transcription model '{m}' (downloaded the first time: 1.5-3 GB)...",
    },
    "interrupted": {
        "it": "Interrotto. Il lavoro fatto è salvato: rilanciando si riprende da qui.",
        "pt": "Interrompido. O trabalho feito está guardado: ao voltar a executar, retoma daqui.",
        "en": "Interrupted. Work done so far is saved: running again resumes from here.",
    },
    "created": {
        "it": "Creato: {p}  ({s}, ~{tok} token stimati)",
        "pt": "Criado: {p}  ({s}, ~{tok} tokens estimados)",
        "en": "Created: {p}  ({s}, ~{tok} estimated tokens)",
    },
    "n_errors": {
        "it": "Attenzione: {n} file non leggibili (dettagli in {f}).",
        "pt": "Atenção: {n} ficheiros ilegíveis (detalhes em {f}).",
        "en": "Warning: {n} unreadable files (details in {f}).",
    },
    "done": {"it": "Fatto.", "pt": "Concluído.", "en": "Done."},
    "warn_omitted_partial": {
        "it": "Nota: allegati citati nella chat ma non inclusi nell'esportazione: {n}{v}. Non sono stati elaborati.",
        "pt": "Nota: anexos citados na conversa mas não incluídos na exportação: {n}{v}. Não foram processados.",
        "en": "Note: attachments mentioned in the chat but not included in the export: {n}{v}. They were not processed.",
    },
    "voice_part": {"it": " (di cui {v} vocali)", "pt": " (dos quais {v} de voz)", "en": " ({v} of them voice messages)"},
    "warn_omitted": {
        "it": "ATTENZIONE: questa esportazione è stata fatta SENZA MEDIA: {n} allegati omessi ({v} messaggi vocali). "
              "Non sono nel file, quindi non possono essere trascritti. Riesporta la chat da WhatsApp scegliendo "
              "\"Allega media\" / \"Includi media\".",
        "pt": "ATENÇÃO: esta exportação foi feita SEM MULTIMÉDIA: {n} anexos omitidos ({v} mensagens de voz). "
              "Não estão no ficheiro, por isso não podem ser transcritos. Exporte de novo a conversa no WhatsApp "
              "escolhendo \"Anexar multimédia\" / \"Incluir multimédia\".",
        "en": "WARNING: this export was made WITHOUT MEDIA: {n} attachments omitted ({v} voice messages). "
              "They are not in the file, so they cannot be transcribed. Export the chat again from WhatsApp "
              "choosing \"Attach media\" / \"Include media\".",
    },
    "md_omitted": {
        "it": "**Media omessi nell'esportazione:** {n} (di cui {v} messaggi vocali): non disponibili, quindi non trascritti",
        "pt": "**Multimédia omitida na exportação:** {n} (dos quais {v} mensagens de voz): indisponível, por isso não transcrita",
        "en": "**Media omitted from the export:** {n} (of which {v} voice messages): not available, so not transcribed",
    },
    "hint_split": {
        "it": "Nota: il file è molto grande per una singola conversazione con un LLM. Caricalo come documento di un "
              "progetto o base di conoscenza (es. Progetti di Claude) oppure crea un file per anno (--split-by-year).",
        "pt": "Nota: o ficheiro é muito grande para uma única conversa com um LLM. Carregue-o como documento de um "
              "projeto ou base de conhecimento (ex. Projetos do Claude) ou crie um ficheiro por ano (--split-by-year).",
        "en": "Note: the file is very large for a single LLM conversation. Upload it as a document of a project or "
              "knowledge base (e.g. Claude Projects) or create one file per year (--split-by-year).",
    },
    "status_ok": {"it": "ok", "pt": "ok", "en": "ok"},
    "status_err": {"it": "ERRORE", "pt": "ERRO", "en": "ERROR"},
    "err_notfound": {"it": "ERRORE: non trovo {p}", "pt": "ERRO: não encontro {p}", "en": "ERROR: cannot find {p}"},
    "err_input": {
        "it": "ERRORE: input non riconosciuto: {p} (serve uno .zip, una cartella o il .txt della chat)",
        "pt": "ERRO: entrada não reconhecida: {p} (é preciso um .zip, uma pasta ou o .txt da conversa)",
        "en": "ERROR: unrecognised input: {p} (a .zip, a folder or the chat .txt is required)",
    },
    "err_no_txt": {
        "it": "ERRORE: nessun file .txt della chat trovato nell'esportazione.",
        "pt": "ERRO: nenhum ficheiro .txt da conversa encontrado na exportação.",
        "en": "ERROR: no chat .txt file found in the export.",
    },
    "err_format": {
        "it": "ERRORE: formato del file della chat non riconosciuto ({f}).",
        "pt": "ERRO: formato do ficheiro da conversa não reconhecido ({f}).",
        "en": "ERROR: chat file format not recognised ({f}).",
    },
    "err_zip": {
        "it": "ERRORE: il file zip è danneggiato o incompleto ({e}).",
        "pt": "ERRO: o ficheiro zip está danificado ou incompleto ({e}).",
        "en": "ERROR: the zip file is damaged or incomplete ({e}).",
    },
    "setup_ok": {
        "it": "Verifica completata: tutto pronto.",
        "pt": "Verificação concluída: tudo pronto.",
        "en": "Check completed: everything is ready.",
    },
    "setup_fail": {
        "it": "PROBLEMA con {c}: {e}",
        "pt": "PROBLEMA com {c}: {e}",
        "en": "PROBLEM with {c}: {e}",
    },
    "setup_longpath": {
        "it": "Suggerimento: sposta la cartella del programma in un percorso corto, es. C:\\zapp2md, e rilancia install.bat.",
        "pt": "Sugestão: mova a pasta do programa para um caminho curto, p. ex. C:\\zapp2md, e execute de novo install.bat.",
        "en": "Tip: move the program folder to a short path, e.g. C:\\zapp2md, and run install.bat again.",
    },
    # ------------------------------------------------------------------ interfaccia grafica
    "g_subtitle": {
        "it": "Chat WhatsApp → documento per Claude, ChatGPT, Gemini e altri LLM",
        "pt": "Conversa do WhatsApp → documento para Claude, ChatGPT, Gemini e outros LLM",
        "en": "WhatsApp chat → document for Claude, ChatGPT, Gemini and other LLMs",
    },
    "g_lang": {"it": "Lingua", "pt": "Idioma", "en": "Language"},
    "g_input": {"it": "Esportazione WhatsApp", "pt": "Exportação do WhatsApp", "en": "WhatsApp export"},
    "g_browse": {"it": "File .zip…", "pt": "Ficheiro .zip…", "en": ".zip file…"},
    "g_folder": {"it": "Cartella…", "pt": "Pasta…", "en": "Folder…"},
    "g_output": {"it": "Salva in", "pt": "Guardar em", "en": "Save to"},
    "g_output_default": {
        "it": "(stessa cartella del file .zip)",
        "pt": "(mesma pasta do ficheiro .zip)",
        "en": "(same folder as the .zip file)",
    },
    "g_change": {"it": "Cambia…", "pt": "Alterar…", "en": "Change…"},
    "g_options": {"it": "Opzioni", "pt": "Opções", "en": "Options"},
    "g_opt_video": {"it": "Trascrivi l'audio dei video", "pt": "Transcrever o áudio dos vídeos", "en": "Transcribe video audio"},
    "g_opt_ocr": {
        "it": "Leggi il testo nelle immagini e nei PDF scansionati",
        "pt": "Ler o texto nas imagens e nos PDFs digitalizados",
        "en": "Read text in images and scanned PDFs",
    },
    "g_opt_split": {"it": "Crea anche un file per ogni anno", "pt": "Criar também um ficheiro por ano", "en": "Also create one file per year"},
    "g_quality": {"it": "Qualità trascrizione", "pt": "Qualidade da transcrição", "en": "Transcription quality"},
    "g_q_turbo": {"it": "Ottima e veloce (consigliata)", "pt": "Ótima e rápida (recomendada)", "en": "Very good and fast (recommended)"},
    "g_q_best": {"it": "Massima (circa 3 volte più lenta)", "pt": "Máxima (cerca de 3 vezes mais lenta)", "en": "Best (about 3 times slower)"},
    "g_q_fast": {"it": "Rapida (meno precisa)", "pt": "Rápida (menos precisa)", "en": "Fast (less accurate)"},
    "g_speech": {"it": "Lingua parlata", "pt": "Idioma falado", "en": "Spoken language"},
    "g_speech_auto": {"it": "Automatica", "pt": "Automático", "en": "Automatic"},
    "g_start": {"it": "Avvia", "pt": "Iniciar", "en": "Start"},
    "g_stop": {"it": "Interrompi", "pt": "Interromper", "en": "Stop"},
    "g_open_md": {"it": "Apri il risultato", "pt": "Abrir o resultado", "en": "Open result"},
    "g_open_folder": {"it": "Apri la cartella", "pt": "Abrir a pasta", "en": "Open folder"},
    "g_progress": {"it": "Avanzamento", "pt": "Progresso", "en": "Progress"},
    "g_ready": {
        "it": "Pronto. Scegli il file .zip esportato da WhatsApp e premi Avvia.",
        "pt": "Pronto. Escolha o ficheiro .zip exportado do WhatsApp e prima Iniciar.",
        "en": "Ready. Choose the .zip file exported from WhatsApp and press Start.",
    },
    "g_preparing": {"it": "Preparazione…", "pt": "A preparar…", "en": "Preparing…"},
    "g_writing": {"it": "Scrittura del documento…", "pt": "A escrever o documento…", "en": "Writing the document…"},
    "g_remaining": {"it": "Tempo rimanente: {v}", "pt": "Tempo restante: {v}", "en": "Time remaining: {v}"},
    "g_elapsed": {"it": "Trascorso: {v}", "pt": "Decorrido: {v}", "en": "Elapsed: {v}"},
    "g_estimating": {"it": "in calcolo…", "pt": "a calcular…", "en": "estimating…"},
    "g_few_seconds": {"it": "pochi secondi", "pt": "poucos segundos", "en": "a few seconds"},
    "g_current": {"it": "In lavorazione: {v}", "pt": "Em processamento: {v}", "en": "Processing: {v}"},
    "g_files": {"it": "File: {a} di {b}", "pt": "Ficheiros: {a} de {b}", "en": "Files: {a} of {b}"},
    "g_k_audio": {"it": "Audio", "pt": "Áudio", "en": "Audio"},
    "g_k_video": {"it": "Video", "pt": "Vídeo", "en": "Video"},
    "g_k_image": {"it": "Immagini", "pt": "Imagens", "en": "Images"},
    "g_k_document": {"it": "Documenti", "pt": "Documentos", "en": "Documents"},
    "g_k_errors": {"it": "Errori", "pt": "Erros", "en": "Errors"},
    "g_tab_errors": {"it": "Errori e avvisi", "pt": "Erros e avisos", "en": "Errors and warnings"},
    "g_tab_log": {"it": "Registro", "pt": "Registo", "en": "Log"},
    "g_done_title": {"it": "Completato", "pt": "Concluído", "en": "Completed"},
    "g_done_msg": {
        "it": "Documento creato:\n{p}\n\nMessaggi: {m}   ·   token stimati: {tok}",
        "pt": "Documento criado:\n{p}\n\nMensagens: {m}   ·   tokens estimados: {tok}",
        "en": "Document created:\n{p}\n\nMessages: {m}   ·   estimated tokens: {tok}",
    },
    "g_done_errors": {
        "it": "{n} file non leggibili: vedi la scheda \"Errori e avvisi\".",
        "pt": "{n} ficheiros ilegíveis: ver o separador \"Erros e avisos\".",
        "en": "{n} unreadable files: see the \"Errors and warnings\" tab.",
    },
    "g_stopped": {
        "it": "Interrotto. Il lavoro già fatto è salvato: premendo Avvia si riprende da qui.",
        "pt": "Interrompido. O trabalho já feito está guardado: ao premir Iniciar, retoma daqui.",
        "en": "Stopped. Work done so far is saved: pressing Start resumes from here.",
    },
    "g_failed": {"it": "Elaborazione non riuscita", "pt": "O processamento falhou", "en": "Processing failed"},
    "g_crash": {
        "it": "Il motore di elaborazione si è chiuso in modo inatteso (codice {c}).\nI dettagli sono nella scheda \"Registro\".",
        "pt": "O motor de processamento fechou-se inesperadamente (código {c}).\nOs detalhes estão no separador \"Registo\".",
        "en": "The processing engine closed unexpectedly (code {c}).\nDetails are in the \"Log\" tab.",
    },
    "g_confirm_stop": {
        "it": "Interrompere l'elaborazione?\nIl lavoro fatto finora resta salvato.",
        "pt": "Interromper o processamento?\nO trabalho feito até agora fica guardado.",
        "en": "Stop processing?\nWork done so far stays saved.",
    },
    "g_confirm_close": {
        "it": "Elaborazione in corso. Chiudere e interromperla?\nIl lavoro fatto finora resta salvato.",
        "pt": "Processamento em curso. Fechar e interrompê-lo?\nO trabalho feito até agora fica guardado.",
        "en": "Processing is running. Close and stop it?\nWork done so far stays saved.",
    },
    "g_no_input": {
        "it": "Scegli prima il file .zip esportato da WhatsApp.",
        "pt": "Escolha primeiro o ficheiro .zip exportado do WhatsApp.",
        "en": "First choose the .zip file exported from WhatsApp.",
    },
    "g_about": {"it": "Informazioni", "pt": "Sobre", "en": "About"},
    "g_about_text": {
        "it": "Zapp2md {v}\n\nAutore: {a}\n\nLicenza Creative Commons BY-NC-SA 4.0: puoi usarlo, copiarlo e distribuirlo "
              "gratuitamente, mantenendo il nome dell'autore. È vietata la vendita e ogni uso commerciale.\n\n"
              "Tutto viene elaborato sul tuo computer: nessun dato viene inviato a servizi esterni.\n\n"
              "WhatsApp è un marchio di WhatsApp LLC. Questo programma non è affiliato a WhatsApp.",
        "pt": "Zapp2md {v}\n\nAutor: {a}\n\nLicença Creative Commons BY-NC-SA 4.0: pode usá-lo, copiá-lo e distribuí-lo "
              "gratuitamente, mantendo o nome do autor. É proibida a venda e qualquer uso comercial.\n\n"
              "Tudo é processado no seu computador: nenhum dado é enviado para serviços externos.\n\n"
              "WhatsApp é uma marca da WhatsApp LLC. Este programa não está afiliado ao WhatsApp.",
        "en": "Zapp2md {v}\n\nAuthor: {a}\n\nCreative Commons BY-NC-SA 4.0 licence: you may use, copy and distribute it "
              "free of charge, keeping the author's name. Selling it or any commercial use is prohibited.\n\n"
              "Everything is processed on your computer: no data is sent to external services.\n\n"
              "WhatsApp is a trademark of WhatsApp LLC. This program is not affiliated with WhatsApp.",
    },
    "g_license": {"it": "Licenza", "pt": "Licença", "en": "Licence"},
    "g_select_zip": {"it": "Scegli l'esportazione WhatsApp", "pt": "Escolha a exportação do WhatsApp", "en": "Choose the WhatsApp export"},
    "g_select_out": {"it": "Scegli dove salvare il risultato", "pt": "Escolha onde guardar o resultado", "en": "Choose where to save the result"},
    "g_not_installed": {
        "it": "Installazione incompleta: manca {p}.\nUsa \"Ripara Zapp2md\" dal menu Start.",
        "pt": "Instalação incompleta: falta {p}.\nUse \"Reparar Zapp2md\" no menu Iniciar.",
        "en": "Incomplete installation: {p} is missing.\nUse \"Repair Zapp2md\" from the Start menu.",
    },
    # ------------------------------------------------------------------ documento
    "md_title": {"it": "Chat WhatsApp: {t}", "pt": "Conversa WhatsApp: {t}", "en": "WhatsApp chat: {t}"},
    "md_generated": {
        "it": "*Generato da Zapp2md {v} il {d} a partire da `{s}`.*",
        "pt": "*Gerado por Zapp2md {v} em {d} a partir de `{s}`.*",
        "en": "*Generated by Zapp2md {v} on {d} from `{s}`.*",
    },
    "md_summary": {"it": "Riepilogo", "pt": "Resumo", "en": "Summary"},
    "md_period": {
        "it": "**Periodo:** dal {a} al {b} ({days} giorni, {active} con messaggi)",
        "pt": "**Período:** de {a} a {b} ({days} dias, {active} com mensagens)",
        "en": "**Period:** from {a} to {b} ({days} days, {active} with messages)",
    },
    "md_messages": {
        "it": "**Messaggi:** {n} ({s} di sistema)",
        "pt": "**Mensagens:** {n} ({s} de sistema)",
        "en": "**Messages:** {n} ({s} system)",
    },
    "md_participants": {"it": "**Partecipanti:**", "pt": "**Participantes:**", "en": "**Participants:**"},
    "md_participant": {
        "it": "{s}: {n} messaggi, ~{w} parole di testo, {a} allegati (primo {f}, ultimo {l})",
        "pt": "{s}: {n} mensagens, ~{w} palavras de texto, {a} anexos (primeira {f}, última {l})",
        "en": "{s}: {n} messages, ~{w} words of text, {a} attachments (first {f}, last {l})",
    },
    "md_attachments": {"it": "**Allegati:** {n} ({p})", "pt": "**Anexos:** {n} ({p})", "en": "**Attachments:** {n} ({p})"},
    "md_not_included": {"it": "{n} non inclusi", "pt": "{n} não incluídos", "en": "{n} not included"},
    "md_audio_total": {"it": "; audio totale {d}", "pt": "; áudio total {d}", "en": "; total audio {d}"},
    "md_unreadable": {
        "it": "**File non leggibili:** {n} (vedi le note \"errore di estrazione\")",
        "pt": "**Ficheiros ilegíveis:** {n} (ver as notas \"erro de extração\")",
        "en": "**Unreadable files:** {n} (see the \"extraction error\" notes)",
    },
    "md_per_year": {"it": "**Messaggi per anno:** ", "pt": "**Mensagens por ano:** ", "en": "**Messages per year:** "},
    "md_howto": {"it": "Come leggere questo documento", "pt": "Como ler este documento", "en": "How to read this document"},
    "md_howto_lines": {
        "it": [
            "La conversazione è in ordine cronologico, divisa per giorno (`### AAAA-MM-GG, giorno`).",
            "Ogni messaggio: `**[HH:MM] Mittente:** testo`. I messaggi di sistema sono in corsivo.",
            "Gli allegati sono indicati da un'etichetta tra parentesi quadre ([MESSAGGIO VOCALE], [AUDIO], [IMMAGINE], "
            "[STICKER], [VIDEO], [DOCUMENTO], [FILE]) seguita da nome file e metadati; il contenuto estratto è nelle righe citate con `>`.",
            "Trascrizioni (riconoscimento vocale automatico) e testo delle immagini (OCR) sono generati automaticamente e "
            "possono contenere errori, soprattutto su nomi propri e audio rumorosi. Delle immagini è disponibile solo il "
            "testo visibile, non una descrizione del contenuto visivo.",
            "Nelle trascrizioni lunghe `[m:ss]` indica il punto del messaggio vocale.",
            "I documenti lunghi hanno un estratto nel punto in cui sono stati inviati e il testo completo in **Appendice**.",
        ],
        "pt": [
            "A conversa está em ordem cronológica, dividida por dia (`### AAAA-MM-DD, dia`).",
            "Cada mensagem: `**[HH:MM] Remetente:** texto`. As mensagens de sistema estão em itálico.",
            "Os anexos são indicados por uma etiqueta entre parênteses retos ([MENSAGEM DE VOZ], [ÁUDIO], [IMAGEM], "
            "[STICKER], [VÍDEO], [DOCUMENTO], [FICHEIRO]) seguida do nome do ficheiro e metadados; o conteúdo extraído está nas linhas citadas com `>`.",
            "As transcrições (reconhecimento de voz automático) e o texto das imagens (OCR) são gerados automaticamente e "
            "podem conter erros, sobretudo em nomes próprios e áudios com ruído. Das imagens só está disponível o texto "
            "visível, não uma descrição do conteúdo visual.",
            "Nas transcrições longas `[m:ss]` indica o ponto da mensagem de voz.",
            "Os documentos longos têm um excerto no ponto em que foram enviados e o texto completo no **Apêndice**.",
        ],
        "en": [
            "The conversation is in chronological order, divided by day (`### YYYY-MM-DD, weekday`).",
            "Each message: `**[HH:MM] Sender:** text`. System messages are in italics.",
            "Attachments are marked by a tag in square brackets ([VOICE MESSAGE], [AUDIO], [IMAGE], [STICKER], [VIDEO], "
            "[DOCUMENT], [FILE]) followed by file name and metadata; the extracted content is in the lines quoted with `>`.",
            "Transcripts (automatic speech recognition) and text in images (OCR) are machine-generated and may contain "
            "errors, especially in proper names and noisy audio. For images only the visible text is available, not a "
            "description of the visual content.",
            "In long transcripts `[m:ss]` marks the position within the voice message.",
            "Long documents have an excerpt where they were sent and the full text in the **Appendix**.",
        ],
    },
    "md_conversation": {"it": "Conversazione", "pt": "Conversa", "en": "Conversation"},
    "md_unref": {
        "it": "Media presenti nell'esportazione ma non collegati a un messaggio",
        "pt": "Multimédia presente na exportação mas não ligada a uma mensagem",
        "en": "Media in the export not linked to any message",
    },
    "md_unref_note": {
        "it": "*Ordinati per nome; la data, se deducibile dal nome del file, è indicata tra parentesi.*",
        "pt": "*Ordenados por nome; a data, quando dedutível do nome do ficheiro, está indicada entre parênteses.*",
        "en": "*Sorted by name; the date, when it can be inferred from the file name, is shown in brackets.*",
    },
    "md_missing": {
        "it": "Allegati citati nella chat ma assenti dall'esportazione",
        "pt": "Anexos citados na conversa mas ausentes da exportação",
        "en": "Attachments mentioned in the chat but missing from the export",
    },
    "md_appendix": {
        "it": "Appendice: testo completo dei documenti",
        "pt": "Apêndice: texto completo dos documentos",
        "en": "Appendix: full text of documents",
    },
    "md_appendix_item": {"it": "Appendice {id}", "pt": "Apêndice {id}", "en": "Appendix {id}"},
    "system": {"it": "(sistema)", "pt": "(sistema)", "en": "(system)"},
    "k_image": {"it": "IMMAGINE", "pt": "IMAGEM", "en": "IMAGE"},
    "k_sticker": {"it": "STICKER", "pt": "STICKER", "en": "STICKER"},
    "k_audio": {"it": "AUDIO", "pt": "ÁUDIO", "en": "AUDIO"},
    "k_voice": {"it": "MESSAGGIO VOCALE", "pt": "MENSAGEM DE VOZ", "en": "VOICE MESSAGE"},
    "k_video": {"it": "VIDEO", "pt": "VÍDEO", "en": "VIDEO"},
    "k_document": {"it": "DOCUMENTO", "pt": "DOCUMENTO", "en": "DOCUMENT"},
    "k_other": {"it": "FILE", "pt": "FICHEIRO", "en": "FILE"},
    "k_missing": {
        "it": "ALLEGATO NON INCLUSO NELL'ESPORTAZIONE",
        "pt": "ANEXO NÃO INCLUÍDO NA EXPORTAÇÃO",
        "en": "ATTACHMENT NOT INCLUDED IN THE EXPORT",
    },
    "m_duration": {"it": "durata {v}", "pt": "duração {v}", "en": "duration {v}"},
    "m_language": {"it": "lingua {v}", "pt": "idioma {v}", "en": "language {v}"},
    "m_pages": {"it": "pagine: {v}", "pt": "páginas: {v}", "en": "pages: {v}"},
    "m_slides": {"it": "diapositive: {v}", "pt": "diapositivos: {v}", "en": "slides: {v}"},
    "m_sheets": {"it": "fogli: {v}", "pt": "folhas: {v}", "en": "sheets: {v}"},
    "m_ocr_pages": {"it": "pagine lette con OCR: {v}", "pt": "páginas lidas com OCR: {v}", "en": "pages read with OCR: {v}"},
    "m_title": {"it": "titolo: {v}", "pt": "título: {v}", "en": "title: {v}"},
    "m_author": {"it": "autore: {v}", "pt": "autor: {v}", "en": "author: {v}"},
    "m_created": {"it": "creato: {v}", "pt": "criado: {v}", "en": "created: {v}"},
    "m_taken": {"it": "scattata: {v}", "pt": "captada: {v}", "en": "taken: {v}"},
    "m_camera": {"it": "fotocamera: {v}", "pt": "câmara: {v}", "en": "camera: {v}"},
    "m_gps": {"it": "GPS: {v}", "pt": "GPS: {v}", "en": "GPS: {v}"},
    "m_recorded": {"it": "registrato: {v}", "pt": "gravado: {v}", "en": "recorded: {v}"},
    "m_animated": {"it": "animata", "pt": "animada", "en": "animated"},
    "x_error": {"it": "(errore di estrazione: {e})", "pt": "(erro de extração: {e})", "en": "(extraction error: {e})"},
    "x_no_speech": {"it": "(nessun parlato riconosciuto)", "pt": "(nenhuma fala reconhecida)", "en": "(no speech recognised)"},
    "x_transcript": {"it": "Trascrizione", "pt": "Transcrição", "en": "Transcript"},
    "x_ocr": {"it": "Testo nell'immagine (OCR)", "pt": "Texto na imagem (OCR)", "en": "Text in image (OCR)"},
    "x_content": {"it": "Contenuto", "pt": "Conteúdo", "en": "Content"},
    "x_excerpt": {
        "it": "{h} — estratto, testo completo in Appendice {id}{n}:",
        "pt": "{h} — excerto, texto completo no Apêndice {id}{n}:",
        "en": "{h} — excerpt, full text in Appendix {id}{n}:",
    },
    "x_truncated": {
        "it": " (troncato a {a} di {b} caratteri)",
        "pt": " (truncado a {a} de {b} caracteres)",
        "en": " (truncated to {a} of {b} characters)",
    },
    "x_caption": {"it": "Didascalia/testo: ", "pt": "Legenda/texto: ", "en": "Caption/text: "},
    "n_video_off": {"it": "trascrizione video disattivata", "pt": "transcrição de vídeo desativada", "en": "video transcription disabled"},
    "n_audio_off": {"it": "trascrizione audio disattivata", "pt": "transcrição de áudio desativada", "en": "audio transcription disabled"},
    "n_no_audio_track": {"it": "nessuna traccia audio", "pt": "sem faixa de áudio", "en": "no audio track"},
    "n_heic": {
        "it": "formato HEIC non leggibile",
        "pt": "formato HEIC ilegível",
        "en": "HEIC format not readable",
    },
    "n_pdf_password": {"it": "PDF protetto da password", "pt": "PDF protegido por palavra-passe", "en": "password-protected PDF"},
    "c_sheet": {"it": "[Foglio: {v}]", "pt": "[Folha: {v}]", "en": "[Sheet: {v}]"},
    "c_table": {"it": "[Tabella {v}]", "pt": "[Tabela {v}]", "en": "[Table {v}]"},
    "c_slide": {"it": "[Diapositiva {v}]", "pt": "[Diapositivo {v}]", "en": "[Slide {v}]"},
    "c_notes": {"it": "Note: ", "pt": "Notas: ", "en": "Notes: "},
    "c_page": {"it": "[Pagina {v}]", "pt": "[Página {v}]", "en": "[Page {v}]"},
    "c_rows_omitted": {"it": "[... righe successive omesse]", "pt": "[... linhas seguintes omitidas]", "en": "[... further rows omitted]"},
    "weekdays": {
        "it": ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"],
        "pt": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"],
        "en": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
}

_lang = "it"


def set_lang(lang: str) -> None:
    global _lang
    _lang = lang if lang in LANGS else "en"


def get_lang() -> str:
    return _lang


def t(key: str, **kw):
    v = T[key][_lang]
    return v.format(**kw) if kw and isinstance(v, str) else v
