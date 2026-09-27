# Gestione Instagram @dott_promenzio: stato e regole

Aggiornare questo file a ogni cambiamento.

## Regole fisse
- Mai pubblicare nulla (post, reel, storie, risposte ai commenti) senza bozza mostrata ad Alessandro e suo ok esplicito.
- LE STORIE SPARISCONO DAI DATI DOPO 24 ORE. Windsor mostra solo le storie ancora attive: una storia pubblicata due giorni prima risulta identica a una mai pubblicata. Quindi dopo un'interruzione della gestione NON dare per scontato che una storia in coda non sia uscita: chiedere ad Alessandro. Errore fatto il 27/09, la storia del sito era gia' stata pubblicata da lui.
- STORIE PROGRAMMATE: le storie programmate da Meta Business Suite in pubblicazione automatica escono SENZA gli elementi interattivi. Sondaggi, quiz, domande, musica, tag luogo e ADESIVO LINK vengono persi nel passaggio automatico. Verificato il 23/09. Quindi ogni storia con sondaggio o link va pubblicata a mano dall'app, e noi impostiamo un promemoria a orario per Alessandro. Non proporre mai di programmarla e basta.
- BOZZE DEI POST: Alessandro non approva un post dal solo testo. Detto il 20/09: "non si puo' scegliere sulla base di un testo, devo vedere la bozza di post vero". Ogni proposta di post va resa in slide vere e mandata come immagini. Il testo da solo non basta mai.
- IMMAGINI GENERATE: vivono solo nella sessione in cui sono state create. Regola aggiornata il 27/09: NON si caricano piu' i file immagine nel repo (troppo pesanti da trasferire), si carica lo SCRIPT che le rigenera. Gli script stanno in sistema/immagini/ (storia_sito.py, storia_gonfiore.py): si eseguono con python3 e rifanno i file identici in pochi secondi. Ogni nuova grafica va salvata allo stesso modo, uno script per contenuto.
- Invito all'azione: "Scrivimi INFO nei DM".
- Prezzi: prima visita da 120 euro, varia per sede (Bonamed 130, nessun pacchetto); percorsi agevolati solo in alcune sedi. Mai un prezzo unico.
- Cinque sedi in provincia di Verona, piu' la videochiamata: Verona, Settimo di Pescantina, Peschiera del Garda, San Pietro in Cariano, Villafranca.
- Sito professionale online: https://www.dottpromenzio.it , gia' nel link in bio (verificato il 23/09). Contiene servizi, chi sono, sedi, domande frequenti, un quiz breve di orientamento, modulo di prenotazione, WhatsApp e telefono. Niente prezzi, niente blog.
- La composizione corporea si misura solo in studio, mai online.
- Plicometria: esempi con Durnin e Womersley.
- Niente frasi ovvie, niente trattini lunghi, niente foto prima/dopo in intimo.
- Codice PROME10 VitaStrong e post VitaStrong restano (scelta di Alessandro).
- Bio: resta quella attuale (decisione di Alessandro, 17/09).
- Le storie le pubblica Alessandro dall'app; noi forniamo testi, immagini pronte e istruzioni esatte sugli adesivi.
- Alessandro non gira video; il formato reel con solo voce e' in discussione (teme poco coinvolgimento senza il volto).
- Recensioni e testimonianze: si pubblicano (sono gia' pubbliche su Google); Alessandro non vuole la verifica con l'Ordine.
- Post da fissare: niente numeri che invecchiano (conteggio recensioni, media). Le recensioni Google non sono tutte a 5 stelle: mai scriverlo. Da segnalare: la home del sito scrive 24 recensioni a 5 stelle, da correggere se non e' esatto.
- Orario migliore secondo Meta (settimana 14/09): giovedi 19:00. Il 23/09 Business Suite consiglia giovedi 18:00. Alessandro il giovedi ha visite fino alle 18:30, quindi in pratica si pubblica verso le 18:35.
- Link scheda Google (verificato 17/09, anche in incognito): https://share.google/gAXudKOQoKiRNYmxz . Nome scheda: "Dott. Alessandro Promenzio Biologo Nutrizionista - Verona". La scheda non si apre da questo ambiente: robots.txt la blocca. Verifiche sui numeri delle recensioni le fa Alessandro dal telefono.
- Post fissati: 1) "Chi sono" del 19/05 (resta), 2) Recensioni del 17/09 (fissato il 18/09), 3) da decidere a ridosso.
- Leggere SEMPRE questo file prima dei dati Windsor. Alessandro pubblica anche da solo (Meta Business Suite e app) e i dati dei post nuovi arrivano con ritardo: il 17/09 sera un post gia' uscito e' stato proposto come da pubblicare. Errore da non ripetere.
- Commenti semplici (solo emoji, complimenti senza domanda): Alessandro li gestisce da solo con un cuore dall'app, e Windsor non lo vede. Prima di proporre una risposta scritta a un commento del genere, chiedere se lo ha gia' sistemato.
- Alessandro risponde anche da solo ai commenti scritti (18/09, commento di Claudio). Prima di proporre una bozza, controllare su Windsor se esiste gia' una risposta di dott_promenzio con comment_parent_id su quel commento.
- Bozze: Alessandro le vuole in anticipo, non a ridosso della pubblicazione (detto il 18/09). Le bozze mandate in chat vanno salvate anche in sistema/bozze/.
- Storie in evidenza: se ne occupa Alessandro da solo (18/09). Non riproporle come compito.
- Windsor: le metriche dei post con date_preset last_1y tornano vuote; usare date_from/date_to (es. dal 2026-05-01). Notato il 21/09.
- Windsor get_data: il parametro dell'account si chiama `accounts`, non `account`. Notato il 27/09.
- L'API GitHub non e' raggiungibile da questo ambiente (403): per leggere il repo si usa raw.githubusercontent.com, per scrivere il tool Composio. Non provare a elencare i file con l'API.

## DM: questione chiusa il 19/09, non riaprirla
- La risposta automatica (Auto reply) di Meta Business Suite e' stata disattivata il 20/09: partiva al primo messaggio di chiunque. Decisione di Alessandro. Non riproporla.
- Automazioni a parola chiave: NON esistono per questo account. Verificato da Alessandro il 17/09 da desktop. Non riproporre di controllare.
- Domande frequenti nell'app Instagram: fanno registrare solo le domande, non le risposte (verificato il 19/09). Non sono un'automazione.
- NIENTE strumenti di terzi per i DM (ManyChat e simili), ne' a pagamento ne' gratuiti: Alessandro non vuole servizi esterni che possano leggere le sue chat. Non riproporli mai.
- Non esiste su Instagram una risposta automatica che parta solo a chi chiede informazioni, senza strumenti di terzi. Spiegato il 20/09. Non cercarla piu'.
- 22/09: Alessandro ha salvato le domande frequenti (bottoni) nell'app. Nella chat della sua ragazza non compaiono, probabilmente perche' Instagram li mostra solo in una conversazione nuova, prima del primo messaggio. Esito da verificare.
- La gestione dei DM e' manuale, con due appoggi: 1) risposta salvata con scorciatoia "info" (testo in sistema/risposta_automatica.md); 2) l'informazione va messa nei contenuti per ridurre le domande in chat. Ora c'e' anche il sito, che risponde alle domande frequenti.

## Pubblicato
- 15/09/2026 20:47 carosello plicometro (media 17875423812562328, https://www.instagram.com/p/DdUY11qjUYq/). Storia di rilancio condivisa il 16/09 14:45.
- 17/09/2026 19:00 carosello Recensioni v12 (media 18411693961085733, https://www.instagram.com/p/DdZWRIOjph9/). Storia di rilancio con adesivo link il 17/09 alle 19:33. Commenti: applauso del 17/09 gestito con un cuore; commento di Claudio (studio_santelli) del 18/09, risposta di Alessandro il 18/09 alle 18:05.
- STORIA SITO: PUBBLICATA da Alessandro da solo tra il 25 e il 27/09, durante il fermo della gestione. Risultato riferito da lui il 27/09 sera: 7 clic sul link. Data esatta non registrata, la storia era gia' scaduta quando la gestione e' ripresa. Il gancio "quiz di sei domande" funziona: si continua a usare il sito come destinazione delle storie.
- Nessun POST nuovo dal 17/09. Al 27/09 sono dieci giorni. Resta il punto aperto piu' importante.

## In coda (bozze pronte, servono ok)
- Storia sondaggio gonfiore, VARIANTE B. Concetto approvato il 23/09, testo in sistema/bozze/storia_sondaggio_gonfiore.md, immagini rigenerabili con sistema/immagini/storia_gonfiore.py. Ridotta a due schermate il 27/09 (prima erano tre): schermata 1 sondaggio "Spesso / Quasi mai", schermata 2 risposta con l'adesivo link al quiz nello spazio in basso. Immagini mandate in chat il 27/09 sera, proposta per lunedi 28/09 all'ora di pranzo. In attesa di ok.
- Carosello Prima visita v1 e Carosello Gonfiore v1: ARCHIVIATI il 22/09, bocciati da Alessandro ("sempre le stesse foto, sempre lo stesso format, rompe le balle e risulta cringe, perdo follower"). Il formato carosello di testo con il template attuale NON va piu' riproposto. I contenuti del Gonfiore (fretta, bollicine e polioli, fibre aumentate di colpo, intestino pigro, segnali per andare dal medico) restano buoni come materiale per storie.
- Storia detrazione 19%: ANNULLATA il 20/09. Testo in sistema/bozze/storia_20_09.md come riserva. Non riproporla senza un motivo nuovo.
- Testi delle quattro domande e risposte in sistema/bozze/domande_frequenti.md: a magazzino, riutilizzabili per post, storie e risposte in DM.
- Reel bilancia: in pausa, manca decisione sul formato e la voce.

## Fatto lato Alessandro
- 25-27/09: storia del sito pubblicata a mano dall'app, con sondaggio e adesivo link. 7 clic. Compito CHIUSO.
- 22/09: risposta salvata "info" gia' salvata. Compito CHIUSO: non riproporla mai piu'.
- 17/09: bio attuale confermata.
- 17/09: storia di rilancio del carosello Recensioni.
- 17/09: verificato da desktop che le parole chiave non esistono in Meta Business Suite per questo account.
- 18/09: post Recensioni fissato in alto.
- 18/09: commento sul carosello Recensioni gestito con un cuore.
- 18/09: risposta al commento di Claudio (studio_santelli) scritta da Alessandro.
- 19/09: verificato che le Domande frequenti nell'app registrano solo le domande.
- 20/09: risposta automatica (Auto reply) DISATTIVATA in Meta Business Suite.
- 23/09: nuovo sito online e collegato al profilo.

## Aperto lato gestione
- Nessun commento in attesa di risposta al 27/09 sera. Ultimo commento scritto: Claudio (studio_santelli) del 18/09, gia' risposto da Alessandro. Verificato su Windsor il 27/09.
- FERMO 25/09 - 27/09: la gestione si e' interrotta per crediti esauriti, nessun controllo delle 9:00 e delle 19:00 in quei giorni. Detto da Alessandro il 27/09 sera. In quei giorni ha pubblicato la storia del sito da solo.
- Controllo del 20/09 ore 09:00: auto reply disattivata, storia annullata, bozza del post rifiutata nel formato testo.
- Controllo del 21/09 ore 09:00: mandato il messaggio "Oggi" con le slide dei due caroselli.
- Controllo del 22/09 ore 09:00: entrambe le bozze bocciate, nuova linea contenuti decisa.
- Controllo del 23/09 ore 09:00: Alessandro non ha domande di pazienti, non ha foto e non puo' farle, la storia va bene come concetto ma il testo va rivisto.
- Controllo del 24/09 ore 09:00: letta la home del sito: scrive "5,0 su 5 su Google", "24 recensioni" e il link "Leggi tutte le 24 recensioni su Google".
- Controllo del 24/09 ore 19:00 UTC: immagini della storia rigenerate e rimandate con le istruzioni sugli adesivi.
- Ripresa del 27/09 ore 20:50 UTC: controllati commenti (nessuno nuovo dal 18/09), post (nessuno dal 17/09), storie (nessuna attiva). Immagini della storia sito rigenerate inutilmente, poi Alessandro ha detto che l'aveva gia' pubblicata. Salvati nel repo i due script generatori. Preparata e mandata la storia gonfiore variante B, due schermate, proposta per lunedi 28/09 a pranzo.

## Nuova linea contenuti (22/09, Alessandro chiede un mix: rappresentare la sua persona e far crescere i follower; la scelta la lascia al manager)
- Post: uno a settimana, con foto VERE scattate da Alessandro. Niente grafiche a modello, niente testo sull'immagine. Didascalia breve, con un'opinione chiara, tono da persona e non da volantino.
- Ogni due settimane circa: post "domanda vera" (domanda reale di un paziente, anonima, risposta come a voce).
- Storie: tre volte a settimana, sondaggi e quiz semplici, testi e immagini preparati da noi, pubblicati da Alessandro.
- Crescita follower: proporre al momento giusto un post in collaborazione (funzione Collab) con una sede, palestra o collega.
- Reel con sola voce: in pausa.
- BLOCCO del 23/09: Alessandro non puo' scattare foto nuove e non ha domande di pazienti da usare. Il post settimanale con foto vere e il post "domanda vera" restano fermi finche' non arriva materiale. Non insistere chiedendo foto da scattare.
- Ripiego deciso il 23/09: a) chiedere solo di guardare nel rullino foto gia' esistenti; b) per il post "domanda vera" usare le quattro domande gia' in sistema/bozze/domande_frequenti.md; c) finche' manca un'immagine, il post settimanale salta e si tiene il profilo vivo con le storie.
- Il sito e' la destinazione principale delle storie: il quiz di orientamento e' il gancio piu' forte per i clic, confermato dai 7 clic della storia sito.
- Nota di agenda: il giovedi Alessandro e' in visita fino alle 18:30. Tenerne conto quando si fissa un orario.
- Nota del 27/09: dieci giorni senza post. Il blocco delle foto sta fermando tutto il piano. Se al prossimo controllo non arriva nessuna foto dal rullino, proporre un'alternativa che non richieda foto nuove, non restare in attesa.

## Da fare lato Alessandro
- Ok sulla storia gonfiore variante B per lunedi 28/09 a pranzo. Due schermate: sondaggio sulla prima (Spesso / Quasi mai), adesivo link al quiz nello spazio in basso della seconda, testo dell'adesivo "Fai il quiz". Immagini mandate il 27/09 sera.
- Rispondere in DM a chi ha votato nel sondaggio della storia del sito, se non l'ha gia' fatto: una riga e il link.
- Guardare nel rullino se esistono gia' foto utilizzabili. Nessuno scatto nuovo richiesto. Aperto dal 23/09, e' il blocco principale del piano contenuti.
- Controllare i numeri delle recensioni. Il 24/09 letta la home: scrive esattamente "5,0 su 5 su Google", "24 recensioni" e il link "Leggi tutte le 24 recensioni su Google". La scheda Google non e' apribile da questo ambiente, quindi il confronto lo fa Alessandro dal telefono: numero di recensioni e media. Se non coincidono, correggere la frase sul sito.
- CHIUSI il 23/09, non riproporre: richiesta di scattare 5 o 6 foto nuove, richiesta di una domanda vera di un paziente.
