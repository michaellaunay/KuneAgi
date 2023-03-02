# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, *

from . import add_mail_template

""" The contents of e-mails"""

PORTAL_SIGNATURE = """Cordiali saluti,

La piattaforma {novaideo_title}
229, rue Solférino
59000 Lille (Francia)
"""

PORTAL_PRESENTATION = u"""{novaideo_title} è una piattaforma partecipativa che consente a qualsiasi membro di proporre idee che possono essere utilizzate in proposte che vengono migliorate dai gruppi di lavoro. Una volta migliorate, queste proposte possono essere sottoposte ai soci per essere esaminate e decise da un comitato di revisione.

"""

FIRST_INVITATION_SUBJECT = u"""Invito a partecipare alla piattaforma partecipativa {novaideo_title}"""
FIRST_INVITATION_MESSAGE = u"""
Salve,

Grazie per il suo interesse per Nova-Ideo.

{recipient_first_name} lei è invitato a partecipare alla piattaforma partecipativa Nova-Ideo come amministratore del sito.

Per convalidare il suo invito, deve cliccare sul link {invitation_url} e seguire le istruzioni.

Le ricordiamo che Nova-Ideo è una soluzione di innovazione partecipativa online che le permette di affrontare i seguenti temi
- Vuole creare una soluzione di innovazione partecipativa;
- Lei ha già una cassetta delle idee, ma è vuota o talmente piena che è impossibile trovare le idee giuste;
- Non ha tempo da dedicare alla gestione delle idee e quindi perde molte opportunità e crea delusione in coloro che hanno idee.

Nova-Ideo le permette di raccogliere le idee di un gruppo, di trovare quelle buone e di trasformarle in proposte realizzabili che riflettano tutti i punti di vista.

Per farlo, Nova-Ideo utilizza il crowdsourcing, facendo lavorare la 'folla' per trasformare le idee in proposte.

Nova-Ideo fonde il meglio della cassetta delle idee, del portale collaborativo e degli strumenti di comunicazione interna e offre soluzioni di innovazione sociale all'avanguardia, come l'uso del giudizio di maggioranza o l'organizzazione della scarsità di sostegno/rifiuto.

Visiti la nostra pagina https://www.nova-ideo.com e in particolare la pagina di documentazione https://www.nova-ideo.com/documentation.

Segua il nostro account Twitter: https://twitter.com/NovaIdeo

Può consultare la nostra presentazione dettagliata di Nova-Ideo http://fr.slideshare.net/MichaelLaunay/20160911-novaideo-linnovation-participative-en-ligne

Il codice di Nova-Ideo con licenza libera AGPL V3 è disponibile all'indirizzo: https://github.com/ecreall/nova-ideo

Il video girato durante il PyConFR che spiega da dove viene Nova-Ideo e perché è gratuito: http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html

Produciamo anche una serie di video che spiegano l'amministrazione e il funzionamento di Nova-Ideo, a cui si può accedere dalla pagina Documentazione del nostro sito web https://www.nova-ideo.com/documentation.

Possiamo adattare Nova-Ideo alle sue esigenze specifiche, quindi non esiti a contattarci, risponderemo alle sue domande!

Può anche inviarci i suoi commenti e suggerimenti di miglioramento creando un account su https://evolutions.nova-ideo.com.

Cordiali saluti
Il team Ecréall
Servizi e soluzioni di software libero
Parco Scientifico Haute Borne
Edificio Hub Innovazione
11, rue de l'Harmonie
59650 Villeneuve d'Ascq
sito : http://www.ecreall.com
tel : 03 20 79 32 90
mob : 06 16 85 91 12
Fax : 09 56 94 39 44
"""

FIRST_INVITATION_SMS_MESSAGE = u"""
Salve,

Grazie per il suo interesse per Nova-Ideo.

{recipient_first_name} lei è invitato a partecipare alla piattaforma partecipativa Nova-Ideo come amministratore del sito.

Per convalidare il suo invito, deve cliccare sul link {invitation_url} e seguire le istruzioni.

Cordiali saluti
Il team Ecréall
"""

INVITATION_SUBJECT = u"""Invito a partecipare alla piattaforma partecipativa {novaideo_title}"""

INVITATION_MESSAGE = u"""
Salve {recipient_first_name}, 

Lei è stato invitato a partecipare alla piattaforma partecipativa {novaideo_title} come {roles}.

Saremmo molto felici di averla come membro attivo! Per convalidare l'invito, basta cliccare sul link {invitation_url} e seguire le istruzioni. Ci vediamo presto sulla piattaforma {novaideo_title}!

""" + PORTAL_SIGNATURE


PRESENTATION_IDEA_SUBJECT = u"""Presentazione dell'idea " {subject_title} """


PRESENTATION_IDEA_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentare l'idea " {subject_title} " sulla piattaforma {novaideo_title}. Questa idea è accessibile all'indirizzo: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Conferma della sua iscrizione alla piattaforma di democrazia deliberativa {novaideo_title}"""

CONFIRMATION_MESSAGE = u"""
Salve {recipient_first_name},

Confermiamo la sua registrazione alla piattaforma di democrazia deliberativa {novaideo_title}. Benvenuto sulla piattaforma!

Cordiali saluti,
                                                                                
La piattaforma di democrazia deliberativa {novaideo_title}
""" + PORTAL_SIGNATURE


PRESENTATION_PROPOSAL_SUBJECT = u"""Presentazione della proposta " {subject_title} """


PRESENTATION_PROPOSAL_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentare la proposta "{subject_title}" sulla piattaforma {novaideo_title}. Questa proposta è accessibile all'indirizzo: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentare l'emendamento "{subject_title}" che appare sulla piattaforma {novaideo_title} sotto {subject_url}.

""" + \
    PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_SUBJECT = u""" {subject_title} """


PRESENTATION_QUESTION_SUBJECT = u"""Presentazione della domanda " {subject_title} """


PRESENTATION_QUESTION_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentarle la domanda "{subject_title}" sulla piattaforma {novaideo_title}. Questa domanda può essere consultata all'indirizzo: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_ANSWER_SUBJECT = u"""Presentazione della risposta a una domanda" {subject_title} """


PRESENTATION_ANSWER_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentare la risposta alla domanda " {subject_title} " sulla piattaforma {novaideo_title}. Questa risposta è disponibile all'indirizzo: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


AMENDABLE_FIRST_SUBJECT = u"""Inizio del ciclo di miglioramento della proposta" {subject_title} """


AMENDABLE_FIRST_MESSAGE = u"""
Salve {recipient_first_name},

Ora siete tre partecipanti al gruppo di lavoro per la proposta "{subject_title}" sotto {subject_url}, e potete iniziare a migliorarla.

Ogni partecipante può dare suggerimenti di miglioramento che gli altri partecipanti possono accettare o rifiutare. Al termine del ciclo di miglioramento, tutti i partecipanti votano per continuare a migliorare la proposta o per sottoporla all'approvazione dei membri della piattaforma.

Il ciclo di miglioramento termina il {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Inizio del ciclo di miglioramento delle proposte" {subject_title} """


AMENDABLE_MESSAGE = u"""
Salve {recipient_first_name},

Il gruppo di lavoro sulla proposta "{subject_title}" sotto {subject_url} ha votato a maggioranza per continuare a migliorare la proposta.

Ogni partecipante può dare suggerimenti di miglioramento che gli altri partecipanti possono accettare o rifiutare. Al termine del ciclo di miglioramento, tutti i partecipanti votano per continuare a migliorare la proposta o per sottoporla all'esame dei membri della piattaforma.

Il ciclo di miglioramento termina il {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""Fine del ciclo di miglioramento per la proposta " {subject_title} " senza alcun miglioramento"""

ALERT_MESSAGE = u"""
Salve {recipient_first_name},

Mentre il ciclo di miglioramento è completo, non sono stati apportati miglioramenti alla proposta "{subject_title}" che si trova sotto {subject_url}. Dovrete votare se presentare la proposta così com'è o se iniziare un nuovo ciclo di miglioramenti.

""" + PORTAL_SIGNATURE

ALERT_END_SUBJECT = u"""Ultimi miglioramenti prima della fine del ciclo di miglioramento delle proposte" {subject_title} """

ALERT_END_MESSAGE = u"""
Salve {recipient_first_name},

Il ciclo di miglioramento per la proposta "{subject_title}" sotto {subject_url} è quasi completo. Può ancora apportare miglioramenti, prima che il gruppo di lavoro voti per presentare la proposta così com'è o per avviare un nuovo ciclo di miglioramento.

""" + PORTAL_SIGNATURE

RESULT_VOTE_AMENDMENT_SUBJECT = u"""I risultati della votazione sugli emendamenti relativi alla proposta " {subject_title} """

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>
Salve {recipient_first_name},

{message_result}
</div>
""" + PORTAL_SIGNATURE


PUBLISHPROPOSAL_SUBJECT = u"""Decisione di sottoporre la proposta {subject_title} all'esame dei membri della piattaforma"""

PUBLISHPROPOSAL_MESSAGE = u"""
Salve {recipient_first_name},

Il gruppo di lavoro sulla proposta "{subject_title}" sotto {subject_url} ha votato a maggioranza per sottoporre la proposta all'esame dei membri della piattaforma.

Ogni membro della Piattaforma può ora sostenere o opporsi alla proposta.

""" + PORTAL_SIGNATURE


SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Decisione di chiudere la proposta "{subject_title}" """

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Salve {recipient_first_name},

Il gruppo di lavoro sulla proposta "{subject_title}" sotto {subject_url} non è attivo da alcuni cicli di oltre una settimana.
Per questo motivo, il gruppo di lavoro è stato sciolto e la proposta è ora aperta a un gruppo di lavoro.

""" + PORTAL_SIGNATURE


VOTINGPUBLICATION_SUBJECT = u"""Inizia a votare per migliorare la proposta "{subject_title}" o per sottoporla all'esame dei membri della piattaforma"""

VOTINGPUBLICATION_MESSAGE = u"""
Salve {recipient_first_name},

Il ciclo di miglioramento della proposta "{subject_title}" sotto {subject_url} è stato completato, è invitato a partecipare alla votazione per migliorare la proposta o a sottoporla all'esame dei membri della piattaforma.

Ha 24 ore di tempo per votare, dopodiché il voto sarà conteggiato tenendo conto della scelta della maggioranza dei votanti. Se non c'è una votazione, inizierà un nuovo ciclo di miglioramenti per una settimana.

""" + PORTAL_SIGNATURE


VOTINGAMENDMENTS_SUBJECT = u"""Inizia la votazione sugli emendamenti alla proposta " {subject_title} """

VOTINGAMENDMENTS_MESSAGE = u"""
Salve {recipient_first_name},

La votazione sugli emendamenti alla proposta "{subject_title}" sotto {subject_url} è iniziata. La prego di partecipare alla votazione.

""" + PORTAL_SIGNATURE

WITHDRAW_SUBJECT = u"""Rimozione dalla lista di attesa del gruppo di lavoro della proposta " {subject_title} """

WITHDRAW_MESSAGE = u"""
Salve {recipient_first_name},

Non è più in lista d'attesa per la proposta del gruppo di lavoro {subject_title}" sotto {subject_url}, in seguito alla sua rimozione dalla lista d'attesa.

Può chiedere di rientrare nel gruppo di lavoro della proposta in qualsiasi momento, se è ancora in fase di miglioramento.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""Ora può iniziare a partecipare al gruppo di lavoro relativo alla proposta " {subject_title} """

PARTICIPATE_WL_MESSAGE = u"""
Salve {recipient_first_name},

Lei è un membro del gruppo di lavoro per la proposta {subject_title}" che si trova sotto {subject_url}, dopo la partenza di uno dei partecipanti.

Come partecipante al gruppo di lavoro può migliorare la proposta e alla fine del ciclo di miglioramento può votare per continuare a migliorarla o sottoporla ai membri della piattaforma.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Ora può iniziare a partecipare al gruppo di lavoro relativo alla proposta " {subject_title} """

PARTICIPATE_MESSAGE = u"""
Salve {recipient_first_name},

Lei è un membro del gruppo di lavoro per la proposta {subject_title} che si trova sotto {subject_url}.

Come partecipante al gruppo di lavoro può migliorare la proposta, se viene migliorata, e alla fine del ciclo di miglioramento può votare se continuare a migliorarla o sottoporla ai membri della piattaforma.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUB_SUBJECT = u"""Invia la tua partecipazione al gruppo di lavoro sulle proposte" {subject_title} """


PARTICIPATE_SUB_MESSAGE = u"""

Salve {recipient_first_name},

La sua richiesta di partecipare al gruppo di lavoro della proposta "{subject_title}" sotto {subject_url} è stata presentata ai membri del gruppo.

Ogni volta che viene presentata una nuova domanda, i membri del gruppo decidono se accettarla o meno.

La durata del voto sulla sua domanda è di {duration] giorno/i. Dopo la data di {date_end_vote}, la votazione sulla sua domanda sarà chiusa, e lei sarà informato/a del risultato.

""" + PORTAL_SIGNATURE


RESIGN_SUBJECT = u"""La sua uscita dal gruppo di lavoro sulle proposte" {subject_title} """

RESIGN_MESSAGE = u"""
Salve {recipient_first_name},

Confermiamo che non è più membro del gruppo di lavoro della proposta "{subject_title}" sotto {subject_url}.

Può unirsi nuovamente ad esso in qualsiasi momento, se non è già membro di altri cinque gruppi di lavoro, che è il numero massimo di gruppi di lavoro a cui un membro può partecipare contemporaneamente.

""" + PORTAL_SIGNATURE


EXCLUDE_SUBJECT = u"""Esclusione dal gruppo di lavoro della proposta " {subject_title} """

EXCLUDE_MESSAGE = u"""
Salve {recipient_first_name},

Il gruppo di lavoro ha deciso di escluderla dal gruppo. Non è più membro del gruppo di lavoro per la proposta "{subject_title}" che si trova sotto {subject_url}.

Può unirsi ad un altro gruppo di lavoro in qualsiasi momento, se non è già membro di altri cinque gruppi di lavoro, che è il numero massimo di gruppi di lavoro a cui un membro può partecipare contemporaneamente.

""" + PORTAL_SIGNATURE


EXCLUDE_PARTICIPANT_SUBJECT = u"""Lei è invitato a votare sulla richiesta di escludere {user_first_name} {user_last_name} dal Gruppo di lavoro relativo alla proposta " {subject_title} """

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Salve {recipient_first_name},

{user_first_name} {user_last_name} ha appena chiesto di essere escluso dal Gruppo di lavoro sulla proposta "{subject_title}".

Le viene chiesto di votare su questa richiesta di esclusione. Per farlo, è sufficiente collegarsi alla piattaforma al seguente indirizzo {subject_url} e votare la richiesta di esclusione di {user_first_name} {user_last_name} al di fuori del Gruppo di lavoro collegato alla proposta "{subject_title}".

La durata della votazione è di {duration] giorni. Dopo la data di {date_end_vote}, la votazione sarà chiusa e il suo voto non sarà preso in considerazione. Si prega di notare! Per impostazione predefinita, se nessun Partecipante ha votato entro questa data sull'esclusione di {user_first_name} {user_last_name} dal Gruppo di lavoro relativo alla proposta "{subject_title}", {user_first_name} {user_last_name} sarà mantenuto nel Gruppo di lavoro.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""È invitato a notare il comportamento cooperativo di {user_first_name} """

NOTING_MEMBER_MESSAGE = u"""
Salve {recipient_first_name},

{user_title} ha appena lasciato il Gruppo di lavoro, dimettendosi o venendo escluso. Ogni volta che un membro lascia un Gruppo di lavoro, il sistema chiede ai membri rimanenti del Gruppo di lavoro di giudicare la qualità del suo comportamento cooperativo, come percepito dai membri rimanenti nel lavoro del gruppo.

Pertanto, le viene chiesto di assegnare un punteggio alla qualità del comportamento cooperativo di {user_title} nel gruppo relativo alla proposta {object_title}. I punteggi possibili sono:
-1 = comportamento cooperativo inferiore a quello che mi aspetto in un gruppo di lavoro
0 = comportamento cooperativo in linea con quello che mi aspetto in un gruppo di lavoro
+1 = comportamento cooperativo migliore di quello che mi aspetto in un gruppo di lavoro

Per valutare il comportamento cooperativo di {user_title}, basta andare a questo URL {subject_url} e dare una valutazione dall'elenco.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""Lei è invitato a valutare il comportamento cooperativo degli altri membri del gruppo in relazione alla proposta " {subject_title} """

NOTING_PARTICIPANT_MESSAGE = u"""
Salve {recipient_first_name},

Lei ha appena lasciato il Gruppo di lavoro relativo alla proposta {subject_title}, o per dimissioni o perché è stato escluso. Ogni volta che un membro lascia un gruppo di lavoro, il sistema chiede a quel membro di giudicare la qualità del comportamento cooperativo di ciascuno dei partecipanti rimanenti nel gruppo di lavoro, come percepito da quel membro uscente nel lavoro di quel gruppo.

È quindi invitato a dare un punteggio alla qualità del comportamento cooperativo degli altri partecipanti al gruppo in relazione alla proposta {subject_title}. I punteggi possibili sono:
-1 = comportamento cooperativo inferiore a quello che mi aspetto in un gruppo di lavoro
0 = comportamento cooperativo in linea con quello che mi aspetto in un gruppo di lavoro
+1 = comportamento cooperativo migliore di quello che mi aspetto in un gruppo di lavoro

Per dare il suo punteggio al comportamento cooperativo degli altri Partecipanti al Gruppo di Lavoro in relazione alla proposta {subject_title}, deve solo accedere a questo URL {subject_url} e dare un punteggio tra quelli proposti, a ciascuno dei Partecipanti rimanenti di questo gruppo.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""È invitato a valutare il comportamento cooperativo degli altri membri del gruppo in relazione alla proposta " {subject_title} """

NOTING_MEMBERS_MESSAGE = u"""
Salve {recipient_first_name},

Il gruppo di lavoro collegato alla proposta {subject_title} l'ha appena pubblicata e sottoposta all'esame degli altri membri della piattaforma. Ha quindi terminato il suo lavoro. Viene sciolto e i suoi membri possono concentrarsi su altre proposte.

Quando un gruppo di lavoro cessa le sue attività e si scioglie, il sistema chiede a ciascuno dei suoi membri di giudicare la qualità del comportamento cooperativo degli altri membri, come percepito da quel membro nel lavoro di quel gruppo.

Pertanto, le viene chiesto di assegnare un punteggio alla qualità del comportamento cooperativo degli altri membri del gruppo in relazione alla proposta {subject_title}. I punteggi possibili sono:
-1 = comportamento cooperativo inferiore a quello che mi aspetto in un gruppo di lavoro
0 = comportamento cooperativo in linea con quello che mi aspetto in un gruppo di lavoro
+1 = comportamento cooperativo migliore di quello che mi aspetto in un gruppo di lavoro

Per dare il suo punteggio al comportamento cooperativo degli altri membri del gruppo di lavoro in relazione alla proposta {subject_title}, deve solo accedere a questo URL {subject_url} e dare un punteggio tra quelli proposti, a ciascuno degli altri membri di questo gruppo.

""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""È invitato a votare la candidatura di {user_first_name} {user_last_name} al Gruppo di lavoro relativo alla proposta " {subject_title} """

NEW_PARTICIPANT_MESSAGE = u"""

Salve {recipient_first_name},

{user_first_name} {user_last_name} ha appena chiesto di partecipare al Gruppo di lavoro relativo alla proposta "{subject_title}".

Le viene chiesto di votare su questa domanda. Per farlo, basta collegarsi alla piattaforma al seguente indirizzo {subject_url} e votare la candidatura di {user_first_name} {user_last_name} al Gruppo di lavoro collegato alla proposta "{subject_title}".

La durata della votazione è di {duration] giorni. Dopo la data {date_end_vote}, la votazione sarà chiusa e il suo voto non sarà più preso in considerazione. Si prega di notare! Per impostazione predefinita, se nessun Partecipante ha votato entro questa data sulla domanda di {user_first_name} {user_last_name} al Gruppo di Lavoro relativa alla proposta "{subject_title}", {user_first_name} {user_last_name} sarà accettato nel Gruppo di Lavoro.

""" + PORTAL_SIGNATURE

# Le chiffre de 12 comme étant le nombre maximal de participants dans le groupe de travail est inscrit en dur dans le code
# C'est en réalité un paramètre de l'application
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


WATINGLIST_SUBJECT = u"""Iscrizione alla lista d'attesa del gruppo di lavoro per le proposte" {subject_title} """

WATINGLIST_MESSAGE = u"""
Salve {recipient_first_name},

Vorrebbe partecipare al gruppo di lavoro della proposta "{subject_title}" sotto {subject_url}, ma il numero di partecipanti ha già raggiunto 12, che è il numero massimo di partecipanti a un gruppo di lavoro.

Lei è in lista d'attesa per questo gruppo di lavoro e sarà automaticamente incluso non appena si renderà disponibile un posto.

""" + PORTAL_SIGNATURE


NEWCONTENT_SUBJECT = u"""{subject_type} " {subject_title} che contiene una delle sue parole chiave di interesse è stato pubblicato"""


NEWCONTENT_MESSAGE = u"""
Salve {recipient_first_name},

{subject_type} " {subject_title} " che contiene una delle parole chiave di suo interesse è stato appena pubblicato. Può visualizzarlo sotto {subject_url}.

""" + PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} " {subject_title} " che fa parte dei suoi preferiti ha appena cambiato il suo stato"""


CONTENTMODIFIEF_MESSAGE = u"""
Salve {recipient_first_name},

{subject_type} "{subject_title}", che fa parte dei suoi preferiti, è appena cambiato da {state_source} a {state_target}. Può visualizzarlo sotto {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Decisione dei moderatori di archiviare l'idea " {subject_title} """


ARCHIVEIDEA_MESSAGE = u"""
Salve {recipient_first_name},

L'idea "{subject_title}" è stata archiviata dai moderatori per il seguente motivo:

{explanation}

Può trovare la sua idea sotto {subject_url}.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Decisione dei moderatori di archiviare i contenuti " {subject_title} """


ARCHIVECONTENT_MESSAGE = u"""
Salve {recipient_first_name},

Il contenuto "{subject_title}" è stato archiviato dai moderatori per il seguente motivo:

{explanation}

Può trovare il suo contenuto sotto {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEPROPOSAL_SUBJECT = u"""Decisione dei moderatori di archiviare la proposta" {subject_title} """


ARCHIVEPROPOSAL_MESSAGE = u"""
Salve {recipient_first_name},

La proposta "{subject_title}" è stata archiviata dai moderatori per il seguente motivo:

{explanation}

Può trovare la sua proposta sotto {subject_url}.

""" + PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Parere del Comitato di revisione sulla proposta" {subject_title} """


ALERTOPINION_MESSAGE = u"""
Salve {recipient_first_name},

Il Comitato di revisione ha emesso un parere "{opinion}" sulla proposta "{subject_title}" con la seguente spiegazione: "{explanation}".

""" + PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u"""Opinione del recensore sull'idea " {subject_title} """


ALERTOPINIONIDEA_MESSAGE = u"""
Salve {recipient_first_name},

Un Revisore ha espresso un parere "{opinion}" sull'idea "{subject_title}" con la seguente spiegazione: "{explanation}".

""" + PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Decisione dei moderatori di pubblicare l'idea " {subject_title} """


PUBLISHEDIDEA_MESSAGE = u"""
Salve {recipient_first_name},

L'idea "{subject_title}" sotto {subject_url} è stata pubblicata dai moderatori sulla piattaforma {novaideo_title}. Questa idea può ora essere utilizzata da qualsiasi membro della piattaforma per una proposta.

""" + PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""Decisione dei moderatori di pubblicare la proposta" {subject_title} """


PUBLISHEDPROPOSAL_MESSAGE = u"""
Salve {recipient_first_name},

La proposta "{subject_title}" sotto {subject_url} è stata appena pubblicata dai moderatori sulla piattaforma {novaideo_title}.

""" + PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Cancellazione della proposta " {subject_title} """


PROPOSALREMOVED_MESSAGE = u"""
Salve {recipient_first_name},

La proposta "{subject_title}" è stata cancellata dai moderatori per il seguente motivo:

"{explanation}"

""" + PORTAL_SIGNATURE


REFUSE_INVITATION_SUBJECT = u"""Rifiuto di {user_first_name} {user_last_name} di aderire alla piattaforma {novaideo_title}"""


REFUSE_INVITATION_MESSAGE = u"""
Salve,

La informiamo che {user_first_name} {user_last_name} ha rifiutato il suo invito a partecipare alla piattaforma {novaideo_title}.

""" + PORTAL_SIGNATURE


ACCEPT_INVITATION_SUBJECT = u"""Accettazione di {user_first_name} {user_last_name}  per unirsi alla piattaforma {novaideo_title}"""


ACCEPT_INVITATION_MESSAGE = u"""
Salve {recipient_first_name},

{user_first_name} {user_last_name} ha accettato il suo invito a unirsi alla piattaforma {novaideo_title}.

""" + PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""La sua nuova password sulla piattaforma {novaideo_title}"""


RESETPW_MESSAGE = u"""
Salve {recipient_first_name},

Se desidera avere una nuova password sulla piattaforma {novaideo_title}, clicchi sull'indirizzo {reseturl} e inserisca la nuova password.

""" + PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""La preghiamo di completare la sua registrazione sulla piattaforma {novaideo_title} di democrazia deliberativa"""


PREREGISTRATION_MESSAGE = u"""
Caro/a {recipient_first_name},


la sua registrazione sulla piattaforma di democrazia deliberativa {novaideo_title} è quasi completata. C'è un ultimo passo da compiere.

Per completare la sua registrazione, deve cliccare sul seguente link {url}. Questo link è valido per 48 ore, vale a dire che deve finalizzare la sua registrazione entro e non oltre la {deadline_date}.

Siamo lieti di annoverarla tra i nostri membri. Ci auguriamo che la sua partecipazione sia per lei un'esperienza positiva e gratificante, in un contesto pienamente democratico. Benvenuto!

Cordiali saluti,

La piattaforma {novaideo_title}.
""" + PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""La preghiamo di completare la sua registrazione sulla piattaforma di democrazia deliberativa  {novaideo_title}"""


PREREGISTRATION_MOD_MESSAGE = u"""
Caro/a {recipient_first_name},


i Verificatori selezionati in modo aleatorio al momento della Sua registrazione hanno convalidato la corrispondenza tra i Dati di Identità che Lei ha fornito al momento della registrazione sulla piattaforma e quelli dei documenti di identità ufficiali di cui ha inviato loro direttamente una copia o che ha mostrato loro durante gli incontri in visoconferenza.

Ora siamo sicuri che lei è l'unica persona registrata con questi dati di identità sulla piattaforma di democrazia deliberativa {novaideo_title}. Come tutti gli altri membri, lei ha un solo account e contribuirà a sostenere il principio democratico "1 persona = 1 voto".

Le rimane solo un'operazione per finalizzare la sua registrazione: cliccare sul seguente link {url}. Questo link è valido per 48 ore, vale a dire che deve finalizzare la sua registrazione entro e non oltre la data di scadenza {deadline_date}.

Siamo lieti di annoverarla tra i nostri membri. Ci auguriamo che la sua partecipazione sia per lei un'esperienza positiva e gratificante, in un contesto pienamente democratico. Benvenuto!

Cordiali saluti,

La piattaforma {novaideo_title}.
""" + PORTAL_SIGNATURE

# Il faudra compléter avec le lieu de naissance
ADMIN_PREREGISTRATION_SUBJECT = u"""La preghiamo di contribuire a verificare una nuova registrazione sulla piattaforma {novaideo_title} di democrazia deliberativa"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
Caro/a {recipient_first_name},


Lei è stato selezionato in modo aleatorio dalla piattaforma di democrazia deliberativa {novaideo_title} per svolgere il ruolo di Verificatore, il cui compito è quello di verificare l'identità di una persona che si è appena registrata online.

piattaforma di democrazia deliberativa per svolgere il ruolo di Verificatore, il cui compito è quello di verificare l'identità di una persona che si è appena registrata online.

Ad ogni nuova registrazione sulla piattaforma {novaideo_title} il sistema seleziona in modo aleatorio tre membri esistenti e chiede loro di verificare l'identità della persona appena registrata. Infatti, è importante verificare che ogni persona fisica sia legata ad un membro della piattaforma, e ad uno solo. In questo modo, evitiamo che una determinata persona fisica voti più volte sulla piattaforma con diversi pseudonimi.

Per effettuare la verifica dell'identità di questa persona, deve solo seguire i seguenti passi:
1. riceverà entro e non oltre la {date_send_id_data} un'e-mail dalla persona che si è appena registrata sulla piattaforma. L'indirizzo e-mail di questa persona, da cui le invierà la sua e-mail, è {subject_email}. Questa e-mail conterrà :
   - una scansione di un documento d'identità ufficiale. Per motivi di sicurezza, consigliamo alla persona che si è appena registrata di nascondere la sua fotografia e la sua firma durante la scansione: la copia sarà volutamente incompleta;
   - oppure un invito a un breve incontro in videoconferenza (data, ora, link di accesso) in cui la persona le mostrerà il suo documento d'identità, in modo che lei possa leggerne il contenuto.
   
2. Lei risponde, se del caso, alla persona specificando quale delle tre date e orari proposti è per lei più conveniente per l'incontro in videoconferenza, e partecipa all'incontro nel giorno e all'ora indicati. 

3. Dopo aver ricevuto l'e-mail con la copia del documento d'identità ufficiale o aver tenuto l'incontro in videoconferenza, o se non ha ricevuto una copia del documento d'identità ufficiale, o un invito a un incontro in videoconferenza, il giorno {date_send_id_data}:
      (a) acceda alla piattaforma {novaideo_title} e poi 
      (b) acceda al seguente URL: {subject_url}. In questa pagina, deciderà se i Dati di Identità ricevuti da questa persona (che sono riprodotti di seguito) corrispondono a quelli presenti sul documento di identità ufficiale, di cui avrà ricevuto una copia via e-mail o che avrà visto durante l'incontro in videoconferenza. Faccia molta attenzione! Affinché lei possa accettare la registrazione, TUTTI gli elementi devono essere strettamente IDENTICI tra i Dati di Identità ricevuti al momento della registrazione e quelli presenti sul documento di identità ufficiale. In tutti gli altri casi, anche con una sola, piccola differenza, se dubita dell'autenticità del documento d'identità ufficiale, o se non ha ricevuto la copia del documento d'identità ufficiale o l'invito a un incontro in videoconferenza entro {date_send_id_data}, DEVE rifiutare la registrazione.
      
4. Una volta eseguita questa operazione, e qualunque sia il suo esito, le chiediamo gentilmente di distruggere, se del caso, dal suo computer tutte le copie in suo possesso del documento d'identità ufficiale che ha ricevuto dalla persona appena registrata, e di riferirgli di questa distruzione, inviandogli un'e-mail a {subject_email}.

###

I dati di identità ricevuti dalla persona al momento della sua registrazione sono i seguenti:

  Nome/i di famiglia: {subject_last_name}
  Nome/i di battesimo: {subject_first_name}
  Data di nascita: {birth_date}
  Luogo di nascita: {birthplace}
  Cittadinanza: {citizenship}

###

Il processo di Verifica dura {duration} giorni, vale a dire che deve essere completato entro {date_end_vote}. Oltre questa data, il processo di Verifica sarà chiuso e la sua decisione non sarà presa in considerazione. Per impostazione predefinita, se nessun Verificatore ha votato entro questa data, la registrazione sarà rifiutata.

Cordiali saluti,

La piattaforma {novaideo_title}.
""" + PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Nuovo contenuto sulla piattaforma partecipativa {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Salve {recipient_first_name},

Lei è stato scelto dalla piattaforma {novaideo_title} per moderare i nuovi contenuti aggiunti alla piattaforma.

Ogni volta che un nuovo contenuto (idea o proposta) viene aggiunto alla piattaforma {novaideo_title}, il sistema sorteggia tre membri per verificare la conformità di questo contenuto con la Carta di moderazione {url_moderation_rules}. Distribuendo la moderazione in modo aleatorio, evitiamo che questa importante funzione di controllo si concentri in poche mani. In questo modo contribuiamo alla natura democratica della piattaforma.

Per esercitare il suo ruolo di Moderatore su questo nuovo contenuto, deve solo collegarsi alla piattaforma al seguente indirizzo {subject_url} ed esprimere la sua opinione sulla conformità di questo contenuto con la Carta di Moderazione.

La durata della Moderazione è di {duration} giorni. Dopo la data di {date_end_vote}, la Moderazione sarà chiusa e il suo voto non sarà più preso in considerazione. Si prega di notare! Per impostazione predefinita, se nessun Moderatore ha votato per moderare questo contenuto entro questa data, il contenuto sarà accettato.

""" + PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""Nuova risposta su {subject_type} " {subject_title} """


ALERTANSWER_MESSAGE = u"""
Salve {recipient_first_name},

È stata data una nuova risposta a {subject_type} " {subject_title} ".

"{comment_content}"

Può trovarlo sotto {comment_url} e rispondere.

""" + PORTAL_SIGNATURE

ADMIN_REPORT_SUBJECT = u"""Nuova segnaletica sulla piattaforma partecipativa {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Salve {recipient_first_name},

Lei è stato scelto dalla piattaforma {novaideo_title} per moderare i contenuti segnalati sulla piattaforma come potenzialmente non conformi alla Carta di moderazione {url_moderation_rules}. 

Ogni volta che un contenuto viene segnalato sulla piattaforma {novaideo_title} come potenzialmente non conforme alla Carta di moderazione, il sistema sorteggia tre membri a caso affinché verifichino la conformità di questo contenuto alla Carta di moderazione. Distribuendo la moderazione in modo aleatorio, evitiamo che questa importante funzione di controllo si concentri in poche mani. In questo modo contribuiamo alla natura democratica della piattaforma.

Per esercitare il suo ruolo di Moderatore per questo contenuto, deve solo collegarsi alla piattaforma al seguente indirizzo {subject_url} ed esprimere la sua opinione sulla conformità di questo contenuto alla Carta di Moderazione.

La durata della Moderazione è di {duration} giorni. Dopo la data di {date_end_vote}, la Moderazione sarà chiusa e il suo voto non sarà più preso in considerazione. Si prega di notare! Per impostazione predefinita, se nessun Moderatore ha votato per moderare questo contenuto entro questa data, il contenuto sarà accettato.

""" + PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Nuova segnaletica sulla piattaforma partecipativa {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Salve {recipient_first_name},

Il suo contenuto {subject_url} è stato segnalato da un Membro come potenzialmente in violazione della Politica di Moderazione {url_moderation_rules}.

Ogni volta che un contenuto viene segnalato come potenzialmente contrario alla Carta di moderazione, il sistema sorteggia tre membri a caso, affinché si pronuncino sulla conformità di questo contenuto alla Carta di moderazione.

La durata della verifica è di {duration} giorno/i. Dopo la data di {date_end_vote}, la verifica sarà chiusa e lei sarà informato del suo risultato.

""" + PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""La sua registrazione sulla piattaforma di democrazia deliberativa {novaideo_title} è stata rifiutata"""

ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Caro/a {recipient_first_name},


i Verificatori selezionati in modo aleatorio al momento della Sua registrazione NON hanno convalidato la corrispondenza tra i Dati di Identità da Lei forniti sulla piattaforma e quelli presenti sui documenti di identità ufficiali che Lei ha inviato loro in copia o che ha mostrato loro durante gli incontri di videoconferenza.

Siamo pertanto spiacenti di informarla che la sua registrazione su {novaideo_title} è stata rifiutata. 

Dobbiamo essere molto rigorosi in questa verifica. Se permettessimo anche piccole discrepanze tra i due dati, una singola persona fisica potrebbe registrarsi più volte, ogni volta con piccole variazioni nei suoi dati di identità, aprire diversi conti e votare più volte. Questo violerebbe il principio democratico "una persona = un voto". 

Cordiali saluti,

La piattaforma {novaideo_title}.
""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""La sua registrazione sulla piattaforma {novaideo_title} di democrazia deliberativa: i prossimi passi"""

ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Caro/a {recipient_first_name},


Si è appena registrato sulla piattaforma {novaideo_title} di democrazia deliberativa. Grazie e congratulazioni! Non vediamo l'ora di accoglierla tra i nostri membri.

Come descritto nel nostro modulo di registrazione, la sua iscrizione deve essere convalidata con una procedura piuttosto semplice, ma rigorosa. 

Ad ogni nuova registrazione sulla piattaforma {novaideo_title} il sistema seleziona in modo aleatorio tre membri esistenti (i Verificatori di questa specifica registrazione) e chiede loro di verificare l'identità della persona appena registrata. Infatti, è importante verificare che ogni persona fisica sia collegata a un membro della piattaforma, e a uno solo. In questo modo, evitiamo che una determinata persona fisica voti più volte sulla piattaforma con diversi pseudonimi. In questo modo, sosteniamo il principio democratico "1 persona = 1 voto".

Affinché la sua identità possa essere verificata, le chiediamo gentilmente di inviare a ciascuna delle seguenti persone, in e-mail separate, entro e non oltre la {date_send_id_data}:
   - una copia scannerizzata (o una fotografia con smartphone) di un documento d'identità ufficiale. Questa copia o fotografia deve mostrare chiaramente il suo nome/i, cognome/i, data e luogo di nascita e la sua nazionalità. Per motivi di sicurezza, le consigliamo di mascherare la sua fotografia e la sua firma quando scansiona o fotografa il suo documento d'identità ufficiale, in modo che l'immagine risulti volutamente incompleta;
   - oppure tre proposte di incontro in videoconferenza che includano, per ciascuna proposta, la data nel formato GG-mmm-AAAA (giorno in due cifre, mese in tre lettere, anno in 4 cifre), l'ora (specificando il suo luogo di residenza) e il link alla videoconferenza, ad esempio utilizzando la piattaforma gratuita e aperta https://meet.jit.si/. Tutte le date e gli orari che propone devono essere precedenti a {date_end_vote}, che è la fine del periodo concesso ai Verificatori per prendere la loro decisione.

Dopo {date_send_id_data}, se i Verificatori non hanno ricevuto una copia del suo documento d'identità ufficiale o un invito a un incontro in videoconferenza, sono invitati a rifiutare la sua iscrizione.

Durante l'incontro in videoconferenza con ciascuno dei Verificatori (se questa è la sua scelta), lei mostrerà il suo documento d'identità ufficiale, rendendo visibili i suoi nomi, cognomi, data e luogo di nascita e nazionalità, e nascondendo la sua foto e la sua firma, se lo desidera. 

I Verificatori incaricati di verificare la sua identità sono:
{moderators}

Riceverà il risultato di questo processo di verifica dell'identità al termine del tempo concesso ai Verificatori per prendere la loro decisione, ossia al più tardi il giorno {date_end_vote}.

I Verificatori sono stati incaricati, se del caso, di distruggere tutti i file contenenti la copia del suo documento d'identità ufficiale una volta effettuata la verifica dei suoi dati d'identità, e di riferirle una volta fatto. 

Cordiali saluti,

La piattaforma {novaideo_title}.
""" + PORTAL_SIGNATURE


REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""ATTENZIONE - SCADENZA DOMANI: La preghiamo di abilitare la verifica della sua identità per registrarsi sulla piattaforma di democrazia deliberativa {novaideo_title}."""

REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
## Se ha già inviato la copia del suo documento d'identità ufficiale o ha proposto un incontro in videoconferenza ai Verificatori, la preghiamo di ignorare questa e-mail e di accettare le nostre scuse ##

Caro/a {recipient_first_name},

come forse ricorderà, la sua registrazione sulla piattaforma di democrazia deliberativa {novaideo_title} è ora soggetta alla verifica della sua identità. Il termine ultimo per inviare ai Verificatori una copia del suo documento d'identità ufficiale o un invito a un incontro in videoconferenza è DOMANI {date_send_id_data}.

Di seguito le ricordiamo la procedura da seguire (compresi gli indirizzi e-mail dei Verificatori) e la motivazione di questa procedura.

Saremo lieti di accoglierla nelle nostre attività!

Cordiali saluti,

La piattaforma {novaideo_title}.

## Promemoria della procedura e della sua motivazione ##
Ad ogni nuova registrazione sulla piattaforma {novaideo_title} il sistema seleziona in modo aleatorio tre membri esistenti (i Verificatori di questa specifica registrazione) e chiede loro di verificare l'identità della persona appena registrata. Infatti, è importante verificare che ogni persona fisica sia collegata a un membro della piattaforma, e a uno solo. In questo modo, evitiamo che una determinata persona fisica voti più volte sulla piattaforma con diversi pseudonimi.

Affinché la sua identità possa essere verificata, le chiediamo gentilmente di inviare a ciascuna delle seguenti persone, in e-mail separate, entro e non oltre la {date_send_id_data}:
   - una copia scannerizzata (o una fotografia con smartphone) di un documento d'identità ufficiale. Questa copia o fotografia deve mostrare chiaramente il suo nome/i, cognome/i, data e luogo di nascita e nazionalità. Per motivi di sicurezza, le consigliamo di mascherare la sua fotografia e la sua firma quando scannerizza o fotografa il suo documento d'identità ufficiale, in modo che l'immagine sia volutamente incompleta;
   - oppure tre proposte di incontro in videoconferenza che includano, per ciascuna proposta, la data nel formato GG-mmm-AAAA (giorno in due cifre, mese in tre lettere, anno in 4 cifre), l'ora (specificando il suo luogo di residenza) e il link alla videoconferenza, ad esempio utilizzando la piattaforma gratuita e aperta https://meet.jit.si/. Tutte le date e gli orari che propone devono essere precedenti a {date_end_vote}, che è la fine del periodo concesso ai Verificatori per prendere la loro decisione.

Dopo {date_send_id_data}, se i Verificatori non hanno ricevuto una copia del suo documento d'identità ufficiale o un invito a un incontro in videoconferenza, sono invitati a rifiutare la sua iscrizione.

Durante l'incontro in videoconferenza con ciascuno dei Verificatori (se questa è la sua scelta), lei mostrerà il suo documento d'identità ufficiale, rendendo visibili i suoi nomi, cognomi, data e luogo di nascita e nazionalità, e nascondendo la sua fotografia e la sua firma, se lo desidera. 

I Verificatori incaricati di verificare la sua identità sono:
{moderators}

Riceverà il risultato di questo processo di verifica dell'identità al termine del tempo concesso ai Verificatori per prendere una decisione, ossia al più tardi il giorno {date_end_vote}.
""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur

PUBLISHEDCHALLENGE_SUBJECT = u"""La decisione dei moderatori di pubblicare la sfida " {subject_title} """


PUBLISHEDCHALLENGE_MESSAGE = u"""
Salve {recipient_first_name},

La sfida "{subject_title}" sotto {subject_url} è stata appena pubblicata dai moderatori sulla piattaforma {novaideo_title}.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Decisione dei moderatori di archiviare la sfida" {subject_title} """


ARCHIVECHALLENGE_MESSAGE = u"""
Salve {recipient_first_name},

La sfida "{subject_title}" è stata archiviata dai moderatori per il seguente motivo:

{explanation}

Può trovare la sua sfida sotto {subject_url}.

""" + PORTAL_SIGNATURE


PRESENTATION_CHALLENGE_SUBJECT = u"""Presentazione della sfida " {subject_title} """


PRESENTATION_CHALLENGE_MESSAGE = u"""
Salve,

{my_first_name} {my_last_name} desidera presentarle la sfida " {subject_title} " sulla piattaforma {novaideo_title}. Questa sfida è accessibile all'indirizzo: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


ADMIN_CONTENT_SUB_SUBJECT = u"""Nuovo contenuto sulla piattaforma partecipativa {novaideo_title}"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Salve {recipient_first_name},

Il suo contenuto è stato sottoposto a moderazione.

Ogni volta che un nuovo contenuto viene aggiunto alla piattaforma {novaideo_title}, il sistema richiama tre membri per verificare la conformità di questo contenuto con la Carta di moderazione {url_moderation_rules}.

La durata della verifica è di {duration} giorno/i. Dopo la data di {date_end_vote}, la verifica sarà chiusa e lei sarà informato del suo risultato.

""" + PORTAL_SIGNATURE


ALERTCOMMENT_SUBJECT = u"""Nuovo commento su {subject_type} " {subject_title} """


ALERTCOMMENT_MESSAGE = u"""
Salve {recipient_first_name},

È stato inserito un nuovo commento su {subject_type} "{subject_title}".

"{comment_content}"

Può trovarlo sotto {comment_url} e fornire una risposta.

""" + PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Nuovo messaggio aggiunto alla sua discussione su " {subject_title} """


ALERTDISCUSS_MESSAGE = u"""
Salve {recipient_first_name},

Un nuovo messaggio è stato aggiunto alla sua discussione con "{subject_title}".

"{comment_content}"

Può trovarlo sotto {comment_url} e rispondere.

""" + PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Una persona ha risposto a un commento su {subject_type} " {subject_title} """


ALERTRESPONS_MESSAGE = u"""
Salve {recipient_first_name},

Qualcuno ha risposto a un commento su {subject_type} " {subject_title} " che si trova sotto {comment_url}.

"{comment_content}"

""" + PORTAL_SIGNATURE


NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Iscrizione newsletter"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Salve {first_name} {last_name},

Ora è iscritto alla newsletter {newsletter_title}.

""" + PORTAL_SIGNATURE

NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Cancellazione dalla newsletter"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Salve {first_name} {last_name},

Ora si è cancellato dalla newsletter {newsletter_title}.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Richiesta di dimissioni dal suo account sulla piattaforma {novaideo_title}"""

QUIT_REQUEST_MESSAGE = u"""
Gentile {recipient_first_name} {recipient_last_name},

Abbiamo ricevuto una richiesta di dimissioni sul suo account della piattaforma {novaideo_title}.
Se ha richiesto di dimettersi dalla piattaforma, clicchi sul seguente link di conferma: {url}, prima della data {deadline_date}.

ATTENZIONE: questa azione è IRREVERSIBILE. Se clicca su questo link, non avrà più accesso alla piattaforma, il suo account sarà distrutto e tutti i contenuti collegati al suo account saranno irreversibilmente attribuiti a un autore anonimo.
Non potrà registrarsi nuovamente sulla piattaforma, creando un nuovo account vuoto, prima di un periodo pari a {tquarantaine} giorni.

Se non ha richiesto di lasciare la piattaforma, ignori questa e-mail e il suo account rimarrà attivo.
Tuttavia, le consigliamo di cambiare la password per evitare che il suo account venga violato.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Le sue dimissioni dalla piattaforma di democrazia elettronica {novaideo_title} sono state prese in considerazione"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Caro {recipient_first_name} {recipient_last_name},

Lei ha voluto dimettersi dalla piattaforma di e-democracy {novaideo_title}. Naturalmente ci dispiace, ma rispettiamo la sua scelta. Con la presente la informiamo che:
* Il suo account è stato disattivato. Riceverà un solo messaggio da parte nostra in futuro (vedere sotto).
* tutti i contenuti del suo account sono stati attribuiti in modo irreversibile a un autore anonimo.
* le informazioni sull'identità che ci ha fornito al momento della registrazione (nome, cognome, data e luogo di nascita) e il suo indirizzo e-mail saranno conservati per {tquarantaine}, per evitare che si registri nuovamente durante questo periodo. L'obiettivo è quello di evitare che le persone che si sono comportate in modo inappropriato sulla piattaforma (e quindi hanno una cattiva reputazione) possano tornare immediatamente con un nuovo pseudonimo e con una reputazione pulita.
* Al termine di questo periodo, ossia alla {date_tquarantaine}, riceverà un'e-mail da parte nostra per informarla che le sue Informazioni sull'identità e il suo indirizzo e-mail sono stati eliminati in modo permanente dal nostro database.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""I suoi dati di identità e il suo indirizzo e-mail sono stati eliminati definitivamente dal database della piattaforma {novaideo_title}!"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Caro {recipient_first_name} {recipient_last_name},

Oggi, i suoi dati di identità (nome, cognome, data e luogo di nascita) e il suo indirizzo e-mail sono stati eliminati in modo permanente dal nostro database. Non riceverà più alcuna e-mail da parte nostra.

""" + PORTAL_SIGNATURE


mail_locale = 'it'

add_mail_template('invitation', {'locale': mail_locale,
                                 'subject': INVITATION_SUBJECT,
                                 'template': INVITATION_MESSAGE})

add_mail_template('refuse_invitation', {'locale': mail_locale,
                                        'subject': REFUSE_INVITATION_SUBJECT,
                                        'template': REFUSE_INVITATION_MESSAGE})

add_mail_template('accept_invitation', {'locale': mail_locale,
                                        'subject': ACCEPT_INVITATION_SUBJECT,
                                        'template': ACCEPT_INVITATION_MESSAGE})

add_mail_template('reset_password', {'locale': mail_locale,
                                     'subject': RESETPW_SUBJECT,
                                     'template': RESETPW_MESSAGE})

add_mail_template('registration_confiramtion', {'locale': mail_locale,
                                                'subject': CONFIRMATION_SUBJECT,
                                                'template': CONFIRMATION_MESSAGE})

add_mail_template('preregistration', {'locale': mail_locale,
                                      'subject': PREREGISTRATION_SUBJECT,
                                      'template': PREREGISTRATION_MESSAGE})


add_mail_template('presentation_idea', {'locale': mail_locale,
                                        'subject': PRESENTATION_IDEA_SUBJECT,
                                        'template': PRESENTATION_IDEA_MESSAGE})


add_mail_template('presentation_proposal', {'locale': mail_locale,
                                            'subject': PRESENTATION_PROPOSAL_SUBJECT,
                                            'template': PRESENTATION_PROPOSAL_MESSAGE})

add_mail_template('presentation_amendment', {'locale': mail_locale,
                                             'subject': PRESENTATION_AMENDMENT_SUBJECT,
                                             'template': PRESENTATION_AMENDMENT_MESSAGE})

add_mail_template('first_start_work', {'locale': mail_locale,
                                       'subject': AMENDABLE_FIRST_SUBJECT,
                                       'template': AMENDABLE_FIRST_MESSAGE})

add_mail_template('start_work', {'locale': mail_locale,
                                 'subject': AMENDABLE_SUBJECT,
                                 'template': AMENDABLE_MESSAGE})

add_mail_template('alert_amendment', {'locale': mail_locale,
                                      'subject': ALERT_SUBJECT,
                                      'template': ALERT_MESSAGE})

add_mail_template('alert_end', {'locale': mail_locale,
                                'subject': ALERT_END_SUBJECT,
                                'template': ALERT_END_MESSAGE})

add_mail_template('vote_amendment_result', {'locale': mail_locale,
                                            'subject': RESULT_VOTE_AMENDMENT_SUBJECT,
                                            'template': RESULT_VOTE_AMENDMENT_MESSAGE})

add_mail_template('publish_proposal', {'locale': mail_locale,
                                       'subject': PUBLISHPROPOSAL_SUBJECT,
                                       'template': PUBLISHPROPOSAL_MESSAGE})

add_mail_template('start_vote_publishing', {'locale': mail_locale,
                                            'subject': VOTINGPUBLICATION_SUBJECT,
                                            'template': VOTINGPUBLICATION_MESSAGE})

add_mail_template('start_vote_amendments', {'locale': mail_locale,
                                            'subject': VOTINGAMENDMENTS_SUBJECT,
                                            'template': VOTINGAMENDMENTS_MESSAGE})

add_mail_template('withdeaw', {'locale': mail_locale,
                               'subject': WITHDRAW_SUBJECT,
                               'template': WITHDRAW_MESSAGE})

add_mail_template('wg_wating_list_participation', {'locale': mail_locale,
                                                   'subject': PARTICIPATE_WL_SUBJECT,
                                                   'template': PARTICIPATE_WL_MESSAGE})

add_mail_template('wg_participation', {'locale': mail_locale,
                                       'subject': PARTICIPATE_SUBJECT,
                                       'template': PARTICIPATE_MESSAGE})

add_mail_template('wg_resign', {'locale': mail_locale,
                                'subject': RESIGN_SUBJECT,
                                'template': RESIGN_MESSAGE})

add_mail_template('wating_list', {'locale': mail_locale,
                                  'subject': WATINGLIST_SUBJECT,
                                  'template': WATINGLIST_MESSAGE})

add_mail_template('alert_new_content', {'locale': mail_locale,
                                        'subject': NEWCONTENT_SUBJECT,
                                        'template': NEWCONTENT_MESSAGE})

add_mail_template('alert_content_modified', {'locale': mail_locale,
                                             'subject': CONTENTMODIFIEF_SUBJECT,
                                             'template': CONTENTMODIFIEF_MESSAGE})

add_mail_template('archive_idea_decision', {'locale': mail_locale,
                                            'subject': ARCHIVEIDEA_SUBJECT,
                                            'template': ARCHIVEIDEA_MESSAGE})

add_mail_template('opinion_proposal', {'locale': mail_locale,
                                       'subject': ALERTOPINION_SUBJECT,
                                       'template': ALERTOPINION_MESSAGE})

add_mail_template('opinion_idea', {'locale': mail_locale,
                                   'subject': ALERTOPINIONIDEA_SUBJECT,
                                   'template': ALERTOPINIONIDEA_MESSAGE})

add_mail_template('publish_idea_decision', {'locale': mail_locale,
                                            'subject': PUBLISHEDIDEA_SUBJECT,
                                            'template': PUBLISHEDIDEA_MESSAGE})

add_mail_template('archive_proposal_decision', {'locale': mail_locale,
                                                'subject': ARCHIVEPROPOSAL_SUBJECT,
                                                'template': ARCHIVEPROPOSAL_MESSAGE})

add_mail_template('publish_proposal_decision', {'locale': mail_locale,
                                                'subject': PUBLISHEDPROPOSAL_SUBJECT,
                                                'template': PUBLISHEDPROPOSAL_MESSAGE})

add_mail_template('delete_proposal', {'locale': mail_locale,
                                      'subject': PROPOSALREMOVED_SUBJECT,
                                      'template': PROPOSALREMOVED_MESSAGE})

add_mail_template('alert_comment', {'locale': mail_locale,
                                    'subject': ALERTCOMMENT_SUBJECT,
                                    'template': ALERTCOMMENT_MESSAGE})

add_mail_template('alert_discuss', {'locale': mail_locale,
                                    'subject': ALERTDISCUSS_SUBJECT,
                                    'template': ALERTDISCUSS_MESSAGE})

add_mail_template('alert_respons', {'locale': mail_locale,
                                    'subject': ALERTRESPONS_SUBJECT,
                                    'template': ALERTRESPONS_MESSAGE})

add_mail_template('newsletter_subscription', {'locale': mail_locale,
                                              'subject': NEWSLETTER_SUBSCRIPTION_SUBJECT,
                                              'template': NEWSLETTER_SUBSCRIPTION_MESSAGE})

add_mail_template('newsletter_unsubscription', {'locale': mail_locale,
                                                'subject': NEWSLETTER_UNSUBSCRIPTION_SUBJECT,
                                                'template': NEWSLETTER_UNSUBSCRIPTION_MESSAGE})

add_mail_template('moderate_preregistration', {'locale': mail_locale,
                                               'subject': ADMIN_PREREGISTRATION_SUBJECT,
                                               'template': ADMIN_PREREGISTRATION_MESSAGE})

add_mail_template('moderate_preregistration_refused', {'locale': mail_locale,
                                                       'subject': ADMIN_PREREGISTRATION_REF_SUBJECT,
                                                       'template': ADMIN_PREREGISTRATION_REF_MESSAGE})

add_mail_template('preregistration_submit', {'locale': mail_locale,
                                             'subject': ADMIN_PREREGISTRATION_SUB_SUBJECT,
                                             'template': ADMIN_PREREGISTRATION_SUB_MESSAGE})

add_mail_template('reminder_preregistration_submit', {'locale': mail_locale,
                                                      'subject': REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT,
                                                      'template': REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE})

add_mail_template('close_proposal', {'locale': mail_locale,
                                     'subject': SYSTEM_CLOSE_PROPOSAL_SUBJECT,
                                     'template': SYSTEM_CLOSE_PROPOSAL_MESSAGE})


add_mail_template('presentation_question', {'locale': mail_locale,
                                            'subject': PRESENTATION_QUESTION_SUBJECT,
                                            'template': PRESENTATION_QUESTION_MESSAGE})

add_mail_template('presentation_answer', {'locale': mail_locale,
                                          'subject': PRESENTATION_ANSWER_SUBJECT,
                                          'template': PRESENTATION_ANSWER_MESSAGE})

add_mail_template('alert_answer', {'locale': mail_locale,
                                   'subject': ALERTANSWER_SUBJECT,
                                   'template': ALERTANSWER_MESSAGE})

add_mail_template('archive_content_decision', {'locale': mail_locale,
                                               'subject': ARCHIVECONTENT_SUBJECT,
                                               'template': ARCHIVECONTENT_MESSAGE})

add_mail_template('archive_challenge_decision', {'locale': mail_locale,
                                                 'subject': ARCHIVECHALLENGE_SUBJECT,
                                                 'template': ARCHIVECHALLENGE_MESSAGE})

add_mail_template('publish_challenge_decision', {'locale': mail_locale,
                                                 'subject': PUBLISHEDCHALLENGE_SUBJECT,
                                                 'template': PUBLISHEDCHALLENGE_MESSAGE})

add_mail_template('presentation_challenge', {'locale': mail_locale,
                                             'subject': PRESENTATION_CHALLENGE_SUBJECT,
                                             'template': PRESENTATION_CHALLENGE_MESSAGE})

add_mail_template('preregistration_moderation', {'locale': mail_locale,
                                                 'subject': PREREGISTRATION_MOD_SUBJECT,
                                                 'template': PREREGISTRATION_MOD_MESSAGE})

add_mail_template('wg_exclude', {'locale': mail_locale,
                                 'subject': EXCLUDE_SUBJECT,
                                 'template': EXCLUDE_MESSAGE})

add_mail_template('moderate_content', {'locale': mail_locale,
                                       'subject': ADMIN_CONTENT_SUBJECT,
                                       'template': ADMIN_CONTENT_MESSAGE})

add_mail_template('content_submit', {'locale': mail_locale,
                                     'subject': ADMIN_CONTENT_SUB_SUBJECT,
                                     'template': ADMIN_CONTENT_SUB_MESSAGE})

add_mail_template('moderate_report', {'locale': mail_locale,
                                      'subject': ADMIN_REPORT_SUBJECT,
                                      'template': ADMIN_REPORT_MESSAGE})

add_mail_template('alert_report', {'locale': mail_locale,
                                   'subject': AUTHOR_REPORT_SUBJECT,
                                   'template': AUTHOR_REPORT_MESSAGE})

add_mail_template('exclude_participant', {'locale': mail_locale,
                                          'subject': EXCLUDE_PARTICIPANT_SUBJECT,
                                          'template': EXCLUDE_PARTICIPANT_MESSAGE})

add_mail_template('new_participant', {'locale': mail_locale,
                                      'subject': NEW_PARTICIPANT_SUBJECT,
                                      'template': NEW_PARTICIPANT_MESSAGE})

add_mail_template('participation_submission', {'locale': mail_locale,
                                               'subject': PARTICIPATE_SUB_SUBJECT,
                                               'template': PARTICIPATE_SUB_MESSAGE})

add_mail_template('member_notation', {'locale': mail_locale,
                                      'subject': NOTING_MEMBER_SUBJECT,
                                      'template': NOTING_MEMBER_MESSAGE})

add_mail_template('member_notation_excluded', {'locale': mail_locale,
                                               'subject': NOTING_PARTICIPANT_SUBJECT,
                                               'template': NOTING_PARTICIPANT_MESSAGE})

add_mail_template('members_notation', {'locale': mail_locale,
                                       'subject': NOTING_MEMBERS_SUBJECT,
                                       'template': NOTING_MEMBERS_MESSAGE})

add_mail_template('quit_request', {'locale': mail_locale,
                                   'subject': QUIT_REQUEST_SUBJECT,
                                   'template': QUIT_REQUEST_MESSAGE})

add_mail_template('quit_request_confiramtion', {'locale': mail_locale,
                                                'subject': QUIT_REQUEST_CONFIRMATION_SUBJECT,
                                                'template': QUIT_REQUEST_CONFIRMATION_MESSAGE})

add_mail_template('quit_request_deletion', {'locale': mail_locale,
                                            'subject': QUIT_REQUEST_DELETION_SUBJECT,
                                            'template': QUIT_REQUEST_DELETION_MESSAGE})
