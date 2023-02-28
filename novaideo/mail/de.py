# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, *

from . import add_mail_template

PORTAL_SIGNATURE = """Mit freundlichen Grüßen,

Die Plattform {novaideo_title}
229, rue Solférino
59000 Lille (Frankreich)
"""

PORTAL_PRESENTATION = u"""{novaideo_title} ist eine partizipative Plattform, die es jedem Mitglied ermöglicht, Ideen einzubringen, die in Vorschlägen verwendet werden können, die von Arbeitsgruppen verbessert werden. Nach der Verbesserung können diese Vorschläge den Mitgliedern zur Bewertung vorgelegt und von einem Prüfungsausschuss entschieden werden.

"""

FIRST_INVITATION_SUBJECT = u"""Einladung zur Teilnahme an der partizipativen Plattform {novaideo_title}"""

FIRST_INVITATION_MESSAGE = u"""
Guten Tag,

Wir danken Ihnen für Ihr Interesse an Nova-Ideo.

{recipient_first_name} Sie sind eingeladen, der partizipativen Plattform Nova-Ideo als Administrator der Website beizutreten.

Um Ihre Einladung zu bestätigen, müssen Sie auf den Link {invitation_url} klicken und den Anweisungen folgen.

Wir möchten Sie daran erinnern, dass Nova-Ideo eine Online-Lösung für partizipative Innovation ist, die die folgenden Probleme lösen kann:
- Sie möchten eine partizipative Innovationslösung einführen;
- Sie haben bereits eine Ideenbox, aber sie ist entweder leer oder so voll, dass es unmöglich ist, die richtigen Ideen zu finden;
- Sie haben keine Zeit, um die Ideen zu verwalten und verpassen so viele Möglichkeiten, was bei denjenigen, die Ideen haben, zu Enttäuschungen führt.

Nova-Ideo ermöglicht es, die Ideen eines Kollektivs zu sammeln, gute Ideen zu finden und sie in umsetzbare Vorschläge umzuwandeln, die alle Standpunkte widerspiegeln.

Nova-Ideo nutzt dazu Crowdsourcing, indem es die "Menge" an der Umwandlung von Ideen in Vorschläge arbeiten lässt.

Nova-Ideo vereint das Beste aus der Ideenbox, dem kollaborativen Portal und den internen Kommunikationstools und bietet fortschrittliche Lösungen für soziale Innovation wie die Verwendung von Mehrheitsurteilen oder die Organisation der Knappheit von Unterstützungen/Ablehnungen.

Besuchen Sie unsere Seite https://www.nova-ideo.com und insbesondere die Dokumentationsseite https://www.nova-ideo.com/documentation.

Folgen Sie unserem Twitter-Account: https://twitter.com/NovaIdeo

Unsere ausführliche Präsentation von Nova-Ideo finden Sie unter http://fr.slideshare.net/MichaelLaunay/20160911-novaideo-linnovation-participative-en-ligne.

Der Code von Nova-Ideo unter der freien Lizenz AGPL V3 ist zugänglich unter: https://github.com/ecreall/nova-ideo

Das Video, das während der PyConFR aufgenommen wurde, erklärt, woher Nova-Ideo kommt und warum es frei ist: http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html

Wir haben auch eine Reihe von Videos, die die Verwaltung und den Betrieb von Nova-Ideo erklären, die auf der Dokumentationsseite unserer Website https://www.nova-ideo.com/documentation zu finden sind.

Wir können Nova-Ideo an Ihre spezifischen Bedürfnisse anpassen, also zögern Sie nicht, uns zu kontaktieren, wir werden Ihre Fragen beantworten!

Sie können auch Ihre Anmerkungen und Vorschläge zur Weiterentwicklung machen, indem Sie ein Konto auf https://evolutions.nova-ideo.com einrichten.

Mit freundlichen Grüßen
Ihr Ecréall-Team
Dienstleistungen und Lösungen im Bereich Freie Software
Wissenschaftspark Haute Borne
Hub Innovation Building
11, rue de l'Harmonie
59650 Villeneuve d'Ascq
Website: http://www.ecreall.com
Tel.: 03 20 79 32 90
Mob: 06 16 85 91 12
Fax: 09 56 94 39 44
"""

FIRST_INVITATION_SMS_MESSAGE = u"""
Guten Tag,

Vielen Dank für Ihr Interesse an Nova-Ideo.

{recipient_first_name} Sie sind eingeladen, der partizipativen Plattform Nova-Ideo als Administrator der Website beizutreten.

Um Ihre Einladung zu bestätigen, müssen Sie auf den Link {invitation_url} klicken und den Anweisungen folgen.

Mit freundlichen Grüßen
Das Team von Ecréall
"""

INVITATION_SUBJECT = u"""Einladung zur Teilnahme an der partizipativen Plattform {novaideo_title}"""

INVITATION_MESSAGE = u"""
Hallo {recipient_first_name}, 

Sie wurden eingeladen, der partizipativen Plattform {novaideo_title} als {roles} beizutreten.

Wir würden uns sehr freuen, Sie zu unseren aktiven Mitgliedern zählen zu dürfen! Um Ihre Einladung zu bestätigen, klicken Sie einfach auf den Link {invitation_url} und folgen Sie den Anweisungen. Bis bald auf der Plattform {novaideo_title}!

""" + PORTAL_SIGNATURE


PRESENTATION_IDEA_SUBJECT = u"""Vorstellung der Idee " {subject_title} """


PRESENTATION_IDEA_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen die Idee "{subject_title}" vorstellen, die auf der Plattform {novaideo_title} zu finden ist. Diese Idee ist unter folgender Adresse zugänglich: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Bestätigung Ihrer Anmeldung bei der Plattform für deliberative Demokratie {novaideo_title}"""

CONFIRMATION_MESSAGE = u"""
Guten Tag {recipient_first_name},

Wir bestätigen Ihre Anmeldung für die Plattform für deliberative Demokratie {novaideo_title}. Herzlich willkommen bei uns!

Mit freundlichen Grüßen,
                                                                                
Die Plattform für deliberative Demokratie {novaideo_title}.
""" + PORTAL_SIGNATURE


PRESENTATION_PROPOSAL_SUBJECT = u"""Präsentation des Vorschlags " {subject_title} """


PRESENTATION_PROPOSAL_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen das Angebot "{subject_title}" vorstellen, das auf der Plattform {novaideo_title} zu finden ist. Dieser Vorschlag ist unter der Adresse: {subject_url} zugänglich.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen den Änderungsantrag "{subject_title}" vorstellen, der auf der Plattform {novaideo_title} unter {subject_url} aufgeführt ist.

""" + \
    PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_SUBJECT = u""" {subject_title} """


PRESENTATION_QUESTION_SUBJECT = u"""Vorstellung der Frage " {subject_title} """


PRESENTATION_QUESTION_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen die Frage "{subject_title}" vorstellen, die auf der Plattform {novaideo_title} zu finden ist. Diese Frage ist unter der Adresse {subject_url} abrufbar.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_ANSWER_SUBJECT = u"""Präsentation der Antwort auf eine Frage " {subject_title} """


PRESENTATION_ANSWER_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen die Antwort auf eine Frage "{subject_title}" vorstellen, die auf der Plattform {novaideo_title} zu finden ist. Diese Antwort ist unter der Adresse {subject_url} abrufbar.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


AMENDABLE_FIRST_SUBJECT = u"""Beginn des Zyklus zur Verbesserung des Vorschlags " {subject_title} """


AMENDABLE_FIRST_MESSAGE = u"""
Hallo {recipient_first_name},

Sie sind nun drei Teilnehmer der Arbeitsgruppe für den Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, und Sie können damit beginnen, ihn zu verbessern.

Jeder Teilnehmer kann Verbesserungsvorschläge machen, die von den anderen Teilnehmern entweder angenommen oder abgelehnt werden können. Wenn der Verbesserungszyklus abgeschlossen ist, stimmen alle Teilnehmer darüber ab, ob der Vorschlag weiter verbessert werden soll oder ob er den Mitgliedern der Plattform zur Bewertung vorgelegt werden soll.

Der Verbesserungszyklus endet am {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Beginn des Verbesserungszyklus für den Vorschlag " {subject_title} """


AMENDABLE_MESSAGE = u"""
Guten Tag {recipient_first_name},

Die Arbeitsgruppe zum Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, stimmte mehrheitlich dafür, den Vorschlag weiter zu verbessern.

Jeder Teilnehmer kann Verbesserungsvorschläge machen, die von den anderen Teilnehmern entweder angenommen oder abgelehnt werden können. Wenn die Verbesserungsrunde abgeschlossen ist, stimmen alle Teilnehmer darüber ab, ob der Vorschlag weiter verbessert werden soll oder ob er den Mitgliedern der Plattform zur Bewertung vorgelegt werden soll.

Der Verbesserungszyklus endet am {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""Ende des Verbesserungszyklus des Vorschlags " {subject_title} " " ohne jegliche Verbesserung"""

ALERT_MESSAGE = u"""
Hallo {recipient_first_name},

Während der Verbesserungszyklus abgeschlossen ist, wurden keine Verbesserungen am Vorschlag "{subject_title}" unter {subject_url} vorgenommen. Sie müssen nun darüber abstimmen, ob Sie den Vorschlag in seiner jetzigen Form einreichen oder einen neuen Verbesserungszyklus beginnen wollen.

""" + PORTAL_SIGNATURE

ALERT_END_SUBJECT = u"""Letzte Verbesserungen vor dem Ende des Verbesserungszyklus für den Vorschlag " {subject_title} """

ALERT_END_MESSAGE = u"""
Hallo {recipient_first_name},

Der Verbesserungszyklus für den Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, nähert sich dem Ende. Sie können noch Verbesserungen vornehmen, bevor die Arbeitsgruppe darüber abstimmt, ob sie den Vorschlag in seiner jetzigen Form einreichen oder einen neuen Verbesserungszyklus beginnen soll.

""" + PORTAL_SIGNATURE


RESULT_VOTE_AMENDMENT_SUBJECT = u"""Die Ergebnisse der Abstimmung über die Änderungsanträge zum Vorschlag "{subject_title} " """

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>.
Hallo {recipient_first_name},

{message_result}
</div>.
""" + PORTAL_SIGNATURE


PUBLISHPROPOSAL_SUBJECT = u"""Entscheidung, den Vorschlag {subject_title} den Mitgliedern der Plattform zur Bewertung vorzulegen"""

PUBLISHPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Die Arbeitsgruppe für den Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, stimmte mehrheitlich dafür, den Vorschlag den Mitgliedern der Plattform zur Beurteilung vorzulegen.

Jedes Mitglied der Plattform kann nun den Vorschlag unterstützen oder ablehnen.

""" + PORTAL_SIGNATURE


SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Entscheidung, den Vorschlag "{subject_title}" zu schließen"""

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Die Arbeitsgruppe zum Vorschlag "{subject_title}", die unter {subject_url} zu finden ist, ist seit einigen Zyklen von mehr als einer Woche nicht mehr aktiv.
Aus diesem Grund wurde die Arbeitsgruppe aufgelöst und der Vorschlag ist nun für eine Arbeitsgruppe offen.

""" + PORTAL_SIGNATURE


VOTINGPUBLICATION_SUBJECT = u"""Beginn der Abstimmung, um den Vorschlag "{subject_title}" zu verbessern oder ihn den Mitgliedern der Plattform zur Bewertung vorzulegen"""

VOTINGPUBLICATION_MESSAGE = u"""
Hallo {recipient_first_name},

Der Verbesserungszyklus des Vorschlags "{subject_title}" unter {subject_url} ist abgeschlossen und Sie werden aufgefordert, an der Abstimmung teilzunehmen, um den Vorschlag zu verbessern oder ihn den Mitgliedern der Plattform zur Bewertung vorzulegen.

Sie haben 24 Stunden Zeit, um Ihre Stimme abzugeben, danach wird die Abstimmung unter Berücksichtigung der Entscheidung der Mehrheit der Abstimmenden ausgezählt. Wenn keine Abstimmung stattfindet, beginnt ein neuer Verbesserungszyklus für eine Woche.

""" + PORTAL_SIGNATURE


VOTINGAMENDMENTS_SUBJECT = u"""Beginn der Abstimmungen über die Änderungsanträge zum Vorschlag " {subject_title} """

VOTINGAMENDMENTS_MESSAGE = u"""
Guten Tag {recipient_first_name},

Die Abstimmung über die Änderungsanträge zum Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, hat begonnen. Bitte nehmen Sie an den Abstimmungen teil.

""" + PORTAL_SIGNATURE

WITHDRAW_SUBJECT = u"""Vorschlag "{subject_title}" von der Warteliste der Arbeitsgruppe streichen """

WITHDRAW_MESSAGE = u"""
Hallo {recipient_first_name},

Sie sind nicht mehr auf der Warteliste der Arbeitsgruppe für den Vorschlag {subject_title}" unter {subject_url}, nachdem Sie von der Warteliste gestrichen wurden.

Sie können jederzeit wieder versuchen, der Arbeitsgruppe des Vorschlags beizutreten, wenn dieser noch verbessert wird.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""Sie können ab jetzt an der Arbeitsgruppe zu dem Vorschlag " {subject_title} " teilnehmen"""

PARTICIPATE_WL_MESSAGE = u"""
Hallo {recipient_first_name},

Sie sind Mitglied der Arbeitsgruppe für den Vorschlag {subject_title}", der unter {subject_url} zu finden ist, nachdem einer der Teilnehmer die Gruppe verlassen hat.

Als Teilnehmer der Arbeitsgruppe können Sie den Vorschlag verbessern und am Ende des Verbesserungszyklus können Sie darüber abstimmen, ob Sie den Vorschlag weiter verbessern oder ihn den Mitgliedern der Plattform zur Bewertung vorlegen möchten.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Sie können ab jetzt an der Arbeitsgruppe zu dem Vorschlag " {subject_title} " teilnehmen"""

PARTICIPATE_MESSAGE = u"""
Hallo {recipient_first_name},

Sie sind Mitglied der Arbeitsgruppe für den Vorschlag {subject_title}, der unter {subject_url} zu finden ist.

Als Teilnehmer der Arbeitsgruppe können Sie den Vorschlag verbessern, wenn er sich in der Verbesserungsphase befindet, und Sie können am Ende des Verbesserungszyklus darüber abstimmen, ob Sie den Vorschlag weiter verbessern oder ihn den Mitgliedern der Plattform zur Bewertung vorlegen wollen.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUB_SUBJECT = u"""Bitte entschuldigen Sie Ihre Teilnahme an der Arbeitsgruppe für den Vorschlag " {subject_title} """


PARTICIPATE_SUB_MESSAGE = u"""

Hallo {recipient_first_name},

Ihr Antrag auf Teilnahme an der Arbeitsgruppe für den Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, wurde den Mitgliedern der Gruppe vorgelegt.

Bei jedem neuen Antrag auf Teilnahme entscheiden die Gruppenmitglieder, ob der Antrag angenommen wird oder nicht.

Die Dauer der Abstimmung über Ihren Antrag beträgt {Duration} Tag(e). Nach dem Datum {date_end_vote} wird die Abstimmung über Ihren Antrag geschlossen, und Sie werden über das Ergebnis informiert.

""" + PORTAL_SIGNATURE


RESIGN_SUBJECT = u"""Ihr Ausscheiden aus der Arbeitsgruppe für den Vorschlag " {subject_title} """

RESIGN_MESSAGE = u"""
Guten Tag {recipient_first_name},

Wir bestätigen Ihnen, dass Sie nicht länger Mitglied der Arbeitsgruppe für den Vorschlag "{subject_title}" sind, die unter {subject_url} zu finden ist.

Sie können der Arbeitsgruppe jederzeit wieder beitreten, sofern Sie nicht bereits fünf anderen Arbeitsgruppen angehören. Dies ist die maximale Anzahl an Arbeitsgruppen, an denen ein Mitglied gleichzeitig teilnehmen darf.

""" + PORTAL_SIGNATURE


EXCLUDE_SUBJECT = u"""Ausschluss aus der Arbeitsgruppe des Vorschlags " {subject_title} """

EXCLUDE_MESSAGE = u"""
Guten Tag {recipient_first_name},

Die Arbeitsgruppe hat beschlossen, Sie aus der Gruppe auszuschließen. Sie sind nicht länger Mitglied der Arbeitsgruppe für den Vorschlag "{subject_title}", der unter {subject_url} zu finden ist.

Sie können jederzeit einer anderen Arbeitsgruppe beitreten, wenn Sie nicht bereits fünf anderen Arbeitsgruppen angehören, was die maximale Anzahl von Arbeitsgruppen ist, an denen ein Mitglied gleichzeitig teilnehmen darf.

""" + PORTAL_SIGNATURE


EXCLUDE_PARTICIPANT_SUBJECT = u"""Sie werden gebeten, über den Antrag auf Ausschluss von {user_first_name} {user_last_name} aus der Arbeitsgruppe für den Vorschlag "{subject_title}" abzustimmen. """

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Hallo {recipient_first_name},

{user_first_name} {user_last_name} wurde soeben ein Antrag auf Ausschluss aus der Arbeitsgruppe gestellt, die sich auf den Vorschlag "{subject_title}" bezieht.

Sie werden gebeten, über diesen Ausschlussantrag abzustimmen. Dazu loggen Sie sich einfach auf der Plattform unter {subject_url} ein und stimmen über den Antrag auf Ausschluss von {user_first_name} {user_last_name} aus der Arbeitsgruppe für den Vorschlag "{subject_title}" ab.

Die Dauer der Abstimmung beträgt {duration} Tag(e). Nach dem Datum {date_end_vote} wird die Abstimmung geschlossen und Ihre Stimme wird nicht mehr berücksichtigt. Bitte beachten Sie! Wenn bis zu diesem Datum kein Teilnehmer über den Ausschluss von {user_first_name} {user_last_name} aus der Arbeitsgruppe für den Vorschlag "{subject_title}" abgestimmt hat, wird {user_first_name} {user_last_name} standardmäßig in der Arbeitsgruppe verbleiben.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""Sie werden gebeten, das kooperative Verhalten von " {user_first_name} " zu bewerten."""

NOTING_MEMBER_MESSAGE = u"""
Hallo {recipient_first_name},

{user_title} hat soeben die Arbeitsgruppe verlassen, entweder durch Rücktritt oder weil er/sie von der Arbeitsgruppe ausgeschlossen wurde. Jedes Mal, wenn ein Mitglied eine Arbeitsgruppe verlässt, bittet das System die verbleibenden Mitglieder der Arbeitsgruppe, die Qualität seines kooperativen Verhaltens zu beurteilen, wie es die verbleibenden Mitglieder im Rahmen der Arbeit der Arbeitsgruppe wahrgenommen haben.

Daher werden Sie gebeten, eine Note für die Qualität des kooperativen Verhaltens von {user_title} in der Gruppe zu vergeben, die mit dem Vorschlag {subject_title} verknüpft ist. Die möglichen Noten sind:
-1 = kooperatives Verhalten, das unter dem liegt, was ich im Rahmen einer Arbeitsgruppe erwarte
0 = kooperatives Verhalten entspricht dem, was ich von einer Arbeitsgruppe erwarte.
+1 = Kooperatives Verhalten, das besser ist als das, was ich in einer Arbeitsgruppe erwarte.

Um das kooperative Verhalten von {user_title} zu bewerten, rufen Sie einfach diese URL {subject_url} auf und geben Sie eine der vorgeschlagenen Bewertungen ab.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""Sie werden gebeten, das kooperative Verhalten der anderen Gruppenmitglieder in Bezug auf den Vorschlag "{subject_title}" zu bewerten. """

NOTING_PARTICIPANT_MESSAGE = u"""
Hallo {recipient_first_name},

Sie haben soeben die Arbeitsgruppe verlassen, die mit dem Vorschlag {subject_title} verbunden ist, entweder durch Rücktritt oder weil Sie ausgeschlossen wurden. Jedes Mal, wenn ein Mitglied eine Arbeitsgruppe verlässt, bittet das System dieses Mitglied, die Qualität des kooperativen Verhaltens aller verbleibenden Teilnehmer der Arbeitsgruppe zu beurteilen, so wie das ausscheidende Mitglied sie im Rahmen der Arbeit der Arbeitsgruppe wahrgenommen hat.

Daher werden Sie gebeten, der Qualität des kooperativen Verhaltens der anderen Teilnehmer der Gruppe, die sich auf den Vorschlag {subject_title} bezieht, eine Note zu geben. Die möglichen Noten sind:
-1 = kooperatives Verhalten, das unter dem liegt, was ich von einer Arbeitsgruppe erwarte.
0 = kooperatives Verhalten entspricht dem, was ich von einer Arbeitsgruppe erwarte.
+1 = Kooperatives Verhalten, das besser ist als das, was ich in einer Arbeitsgruppe erwarte.

Um Ihre Bewertung für das kooperative Verhalten der anderen Teilnehmer der Arbeitsgruppe, die sich auf den Vorschlag {subject_title} bezieht, abzugeben, rufen Sie einfach diese URL {subject_url} auf und geben Sie jedem der verbleibenden Teilnehmer dieser Gruppe eine der vorgeschlagenen Bewertungen.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""Sie werden gebeten, das kooperative Verhalten der anderen Gruppenmitglieder in Bezug auf den Vorschlag "{subject_title}" zu bewerten. """

NOTING_MEMBERS_MESSAGE = u"""
Hallo {recipient_first_name},

Die Arbeitsgruppe, die mit dem Vorschlag {subject_title} verbunden ist, hat diesen soeben veröffentlicht und den anderen Mitgliedern der Plattform zur Beurteilung vorgelegt. Damit ist ihre Arbeit beendet. Die Arbeitsgruppe wird aufgelöst und ihre Mitglieder können sich anderen Vorschlägen widmen.

Jedes Mal, wenn eine Arbeitsgruppe ihre Tätigkeit einstellt und sich auflöst, bittet das System jedes Mitglied, die Qualität des kooperativen Verhaltens der anderen Mitglieder zu beurteilen, so wie es das Mitglied im Rahmen der Arbeit der Gruppe wahrgenommen hat.

Daher werden Sie gebeten, eine Note für die Qualität des kooperativen Verhaltens der anderen Mitglieder der Gruppe zu vergeben, die mit dem Vorschlag {subject_title} verknüpft ist. Die möglichen Noten sind:
-1 = kooperatives Verhalten unterhalb meiner Erwartungen an eine Arbeitsgruppe
0 = kooperatives Verhalten entspricht dem, was ich von einer Arbeitsgruppe erwarte.
+1 = Kooperatives Verhalten, das besser ist als das, was ich in einer Arbeitsgruppe erwarte.

Um Ihre Bewertung für das kooperative Verhalten der anderen Mitglieder der Arbeitsgruppe, die sich auf den Vorschlag {subject_title} bezieht, abzugeben, rufen Sie einfach diese URL {subject_url} auf und geben Sie jedem anderen Mitglied der Arbeitsgruppe eine der vorgeschlagenen Bewertungen.

""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""Sie werden gebeten, über die Kandidatur von {user_first_name} {user_last_name} für die Arbeitsgruppe für den Vorschlag {subject_title} abzustimmen"""

NEW_PARTICIPANT_MESSAGE = u"""

Hallo {recipient_first_name},

{user_first_name} {user_last_name} hat sich soeben für die Teilnahme an der Arbeitsgruppe zum Vorschlag "{subject_title}" beworben.

Sie sind aufgefordert, über diese Kandidatur abzustimmen. Dazu loggen Sie sich einfach auf der Plattform unter {subject_url} ein und stimmen über die Kandidatur von {user_first_name} {user_last_name} für die Arbeitsgruppe zum Vorschlag "{subject_title}" ab.

Die Dauer der Abstimmung beträgt {duration} Tag(e). Nach dem {date_end_vote} wird die Abstimmung geschlossen und Ihre Stimme wird nicht mehr berücksichtigt. Bitte beachten Sie! Standardmäßig wird {user_first_name} {user_last_name} in die Arbeitsgruppe für den Vorschlag "{subject_title}" aufgenommen, wenn bis zu diesem Datum kein Teilnehmer über die Kandidatur von {user_first_name} {user_last_name} abgestimmt hat.

""" + PORTAL_SIGNATURE

# Le chiffre de 12 comme étant le nombre maximal de participants dans le groupe de travail est inscrit en dur dans le code
# C'est en réalité un paramètre de l'application
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


WATINGLIST_SUBJECT = u"""Aufnahme in die Warteliste der Arbeitsgruppe für den Vorschlag " {subject_title} """

WATINGLIST_MESSAGE = u"""
Hallo {recipient_first_name},

Sie möchten an der Arbeitsgruppe für den Vorschlag "{subject_title}" teilnehmen, der unter {subject_url} zu finden ist, aber die Teilnehmerzahl hat bereits 12 Personen erreicht, was die maximale Teilnehmerzahl in einer Arbeitsgruppe ist.

Sie stehen auf der Warteliste dieser Arbeitsgruppe und werden automatisch aufgenommen, sobald ein Platz frei wird.

""" + PORTAL_SIGNATURE


NEWCONTENT_SUBJECT = u"""{subject_type} " {subject_title}, die eines der Schlüsselwörter enthält, die zu Ihren Interessengebieten gehören, wurde gerade veröffentlicht."""


NEWCONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

{subject_type} "{subject_title}", die eines der Schlüsselwörter aus Ihrem Interessenbereich enthält, wurde soeben veröffentlicht. Sie können es unter {subject_url} einsehen.

""" + PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} " {subject_title} ", das zu Ihren Favoriten gehört, hat gerade seinen Status geändert"""


CONTENTMODIFIEF_MESSAGE = u"""
Hallo {recipient_first_name},

{subject_type} "{subject_title}", der zu Ihren Favoriten gehört, wurde soeben vom Status {state_source} in den Status {state_target} geändert. Sie können ihn unter {subject_url} aufrufen.

""" + PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Entscheidung der Moderatoren, die Idee " {subject_title} " zu archivieren."""


ARCHIVEIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Die Idee "{subject_title}" wurde soeben von den Moderatoren aus folgendem Grund archiviert:

{explanation}

Sie können Ihre Idee unter {subject_url} finden.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Entscheidung der Moderatoren, den Inhalt " {subject_title} " zu archivieren."""


ARCHIVECONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

Der Inhalt "{subject_title}" wurde von den Moderatoren aus folgendem Grund archiviert:

{explanation}

Sie können Ihren Inhalt unter {subject_url} wiederfinden.

""" + PORTAL_SIGNATURE


ARCHIVEPROPOSAL_SUBJECT = u"""Entscheidung der Moderatoren, den Vorschlag zu archivieren " {subject_title} """


ARCHIVEPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Der Vorschlag "{subject_title}" wurde soeben von den Moderatoren aus folgendem Grund archiviert:

{explanation}

Sie können Ihren Vorschlag unter {subject_url} finden.

""" + PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Stellungnahme des Prüfungsausschusses zum Vorschlag " {subject_title} """


ALERTOPINION_MESSAGE = u"""
Guten Tag {recipient_first_name},

Der Prüfungsausschuss gab eine Stellungnahme "{opinion}" zum Vorschlag "{subject_title}" mit der folgenden Erklärung ab: "{explanation}"

""" + PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u"""Stellungnahme eines Prüfers zur Idee " {subject_title}" """


ALERTOPINIONIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Ein Prüfer hat eine Stellungnahme "{opinion}" zur Idee "{subject_title}" mit der folgenden Erklärung abgegeben: "{explanation}"

""" + PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Entscheidung der Moderatoren, die Idee " {subject_title}" zu veröffentlichen """


PUBLISHEDIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Die Idee "{subject_title}", die unter {subject_url} zu finden ist, wurde soeben von den Moderatoren auf der Plattform {novaideo_title} veröffentlicht. Diese Idee kann nun von jedem Mitglied der Plattform für einen Vorschlag verwendet werden.

""" + PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""Entscheidung der Moderatoren, den Vorschlag zu veröffentlichen " {subject_title} """


PUBLISHEDPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Der Vorschlag "{subject_title}", der unter {subject_url} zu finden ist, wurde soeben von den Moderatoren auf der Plattform {novaideo_title} veröffentlicht.

""" + PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Vorschlag entfernen " {subject_title} """


PROPOSALREMOVED_MESSAGE = u"""
Hallo {recipient_first_name},

Der Vorschlag "{subject_title}" wurde soeben von den Moderatoren aus folgendem Grund gelöscht:

" {explanation} "

""" + PORTAL_SIGNATURE


REFUSE_INVITATION_SUBJECT = u"""Weigerung von {user_first_name} {user_last_name}, der Plattform {novaideo_title} beizutreten"""


REFUSE_INVITATION_MESSAGE = u"""
Guten Tag,

Wir möchten Sie darauf hinweisen, dass {user_first_name} {user_last_name} Ihre Einladung, der Plattform {novaideo_title} beizutreten, abgelehnt hat.

""" + PORTAL_SIGNATURE


ACCEPT_INVITATION_SUBJECT = u"""Annahme von {user_first_name} {user_last_name}, der Plattform {novaideo_title} beizutreten"""


ACCEPT_INVITATION_MESSAGE = u"""
Hallo {recipient_first_name},

{user_first_name} {user_last_name} hat Ihre Einladung angenommen, der Plattform {novaideo_title} beizutreten.

""" + PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""Ihr neues Kennwort für die Plattform {novaideo_title}"""


RESETPW_MESSAGE = u"""
Hallo {recipient_first_name},

Sie möchten ein neues Passwort für die Plattform {novaideo_title}, bitte klicken Sie auf die Adresse {reseturl} und geben Sie Ihr neues Passwort ein.

""" + PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""Bitte schließen Sie Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie ab"""


PREREGISTRATION_MESSAGE = u"""
LiebeR {recipient_first_name},


Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie ist fast abgeschlossen. Sie müssen nur noch einen letzten Schritt machen.

Um Ihre Anmeldung abzuschließen, müssen Sie jetzt auf den folgenden Link {url} klicken. Dieser Link ist 48 Stunden lang gültig, d.h. Sie müssen Ihre Anmeldung am oder vor {deadline_date} abschließen.

Wir freuen uns, Sie zu unseren Mitgliedern zählen zu dürfen. Wir hoffen, dass Ihre Teilnahme für Sie eine positive und lohnende Erfahrung sein wird, und zwar in einem völlig demokratischen Rahmen. Herzlich willkommen!

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.""" + PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Bitte schließen Sie Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie ab"""


PREREGISTRATION_MOD_MESSAGE = u"""
LiebeR {recipient_first_name},

die bei Ihrer Anmeldung nach dem Zufallsprinzip ausgewählten Prüfer haben die Übereinstimmung zwischen den Identitätsdaten, die Sie bei der Anmeldung auf der Plattform angegeben haben, und den offiziellen Ausweisdokumenten, die Sie ihnen direkt in Kopie zugesandt oder bei den Visokonferenzen vorgelegt haben, überprüft.

Wir sind nun sicher, dass Sie die einzige Person sind, die unter diesen Identitätsdaten auf der {novaideo_title} Plattform für deliberative Demokratie angemeldet sind. Wie alle anderen Mitglieder haben auch Sie nur ein Konto und tragen zur Einhaltung des demokratischen Grundsatzes "1 Person = 1 Stimme" bei.

Es bleibt Ihnen nur noch ein Vorgang, um Ihre Anmeldung abzuschließen: Klicken Sie auf den folgenden Link {url}. Dieser Link ist 48 Stunden lang gültig, d.h. Sie müssen Ihre Anmeldung am oder vor {deadline_date} abschließen.

Wir freuen uns, Sie zu unseren Mitgliedern zählen zu dürfen. Wir hoffen, dass Ihre Teilnahme für Sie eine positive und lohnende Erfahrung sein wird, und zwar in einem völlig demokratischen Rahmen. Herzlich willkommen!

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.""" + PORTAL_SIGNATURE

# Il faudra compléter avec le lieu de naissance
ADMIN_PREREGISTRATION_SUBJECT = u"""Bitte tragen Sie zur Verifizierung einer neuen Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie bei"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
LiebeR {recipient_first_name},


Sie wurden von der {novaideo_title} Plattform für deliberative Demokratie nach dem Zufallsprinzip ausgewählt worden. Ihre Aufgabe ist es, die Identität einer Person zu überprüfen, die sich gerade online angemeldet hat.

Bei jeder neuen Anmeldung auf der {novaideo_title} platfom wählt das System nach dem Zufallsprinzip drei bestehende Mitglieder aus und bittet sie, die Identität der neu angemeldeten Person zu überprüfen. Es ist nämlich wichtig zu überprüfen, dass jede natürliche Person mit einem Mitglied auf der Plattform verbunden ist, und zwar nur mit einem. Dadurch vermeiden wir, dass eine bestimmte natürliche Person mehrmals unter verschiedenen Pseudonymen auf der Plattform abstimmt.


Um diese Überprüfung der Identität dieser Person durchzuführen, müssen Sie nur die folgenden Schritte befolgen:
1. Sie erhalten am oder vor dem {date_send_id_data} eine E-Mail von der Person, die sich gerade auf der Plattform angemeldet hat. Die E-Mail-Adresse dieser Person, von der aus er/sie Ihnen seine/ihre E-Mail sendet, lautet {subject_email}. Diese E-Mail wird enthalten:
   - entweder einen Scan eines amtlichen Ausweises. Aus Sicherheitsgründen raten wir der Person, die sich gerade angemeldet hat, ihr Foto beim Scannen zu verbergen: die Kopie wird absichtlich unvollständig sein;
- oder eine Einladung zu einer kurzen Videokonferenzsitzung (Datum, Uhrzeit, Login-Link), in der die Person Ihnen ihren Ausweis zeigt, damit Sie dessen Inhalt lesen können.
   
2. Sie antworten der Person gegebenenfalls, indem Sie angeben, welches der drei vorgeschlagenen Daten und Uhrzeiten für die Videokonferenzsitzung für Sie am günstigsten ist, und Sie nehmen an der Sitzung an dem angegebenen Tag und zu der angegebenen Uhrzeit teil. 

3. Sobald Sie die E-Mail mit der Kopie des amtlichen Ausweises erhalten haben oder die Videokonferenz abgehalten haben, oder wenn Sie keine Kopie des amtlichen Ausweises oder eine Einladung zu einer Videokonferenzsitzung erhalten haben, am {date_send_id_data}: 
      (a) Melden Sie sich bei der Plattform {novaideo_title} an und dann 
      (b) rufen Sie die folgende URL auf: {subject_url}. Auf dieser Seite werden Sie entscheiden, ob die von dieser Person erhaltenen Identitätsdaten (die unten wiedergegeben sind) mit denen des offiziellen Ausweises übereinstimmen, von dem Sie eine Kopie per E-Mail erhalten haben oder den Sie während der Videokonferenzsitzung gesehen haben. Seien Sie sehr vorsichtig! Damit Sie die Anmeldung akzeptieren können, müssen ALLE Elemente zwischen den bei der Anmeldung erhaltenen Identitätsdaten und denen auf dem amtlichen Ausweis strikt IDENTISCH sein. In allen anderen Fällen, selbst bei einem einzigen, geringfügigen Unterschied, wenn Sie die Echtheit des amtlichen Ausweises anzweifeln oder wenn Sie die Kopie des amtlichen Ausweises oder eine Einladung zu einem Treffen per Videokonferenz bis {date_send_id_data} nicht erhalten haben, MÜSSEN Sie die Anmeldung ablehnen.
      
4. Sobald Sie diesen Vorgang durchgeführt haben, bitten wir Sie, unabhängig von seinem Ergebnis, alle Kopien des amtlichen Ausweises, die Sie von der neu angemeldeten Person erhalten haben, gegebenenfalls von Ihrem Computer zu vernichten und sie über diese Vernichtung zu informieren, indem Sie ihr eine E-Mail an {subject_email} schicken.

###

Die von der Person bei ihrer Anmeldung erhaltenen Identitätsdaten sind die folgenden:

  Familienname(n): {subject_last_name}
  Vorname(n): {subject_first_name}
  Geburtsdatum: {birth_date}
  Geburtsort: {birthplace}
  Staatsangehörigkeit: {citizenship}

###

Der Verifizierungsprozess dauert {duration} Tag(e), d.h. er muss am oder vor {date_end_vote} abgeschlossen sein. Nach diesem Datum wird der Überprüfungsprozess abgeschlossen und Ihre Entscheidung wird nicht berücksichtigt. Wenn bis zu diesem Datum kein Überprüfer abgestimmt hat, wird die Anmeldung standardmäßig abgelehnt.

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.""" + PORTAL_SIGNATURE

ADMIN_CONTENT_SUBJECT = u"""Neuer Inhalt auf der Mitmachplattform {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

Sie wurden von der Plattform {novaideo_title} ausgewählt, um einen neuen Inhalt zu moderieren, der der Plattform hinzugefügt wurde.

Jedes Mal, wenn ein neuer Inhalt (Idee oder Vorschlag) zur Plattform {novaideo_title} hinzugefügt wird, zieht das System drei Mitglieder, die den Inhalt auf die Einhaltung der Moderationsrichtlinien {url_moderation_rules} überprüfen. Indem wir die Moderation nach dem Zufallsprinzip verteilen, vermeiden wir, dass diese wichtige Kontrollfunktion in wenigen Händen konzentriert wird. Wir tragen damit zum demokratischen Charakter der Plattform bei.

Um Ihre Rolle als Moderator für diesen neuen Inhalt auszuüben, loggen Sie sich einfach auf der Plattform unter {subject_url} ein und geben Ihre Meinung dazu ab, ob dieser Inhalt mit der Moderationsrichtlinie übereinstimmt.

Die Dauer der Moderation beträgt {duration} Tag(e). Nach dem Datum {date_end_vote} wird die Moderation beendet und Ihre Stimme wird nicht mehr berücksichtigt. Bitte beachten Sie! Standardmäßig wird der Inhalt akzeptiert, wenn bis zu diesem Datum kein Moderator für die Moderation dieses Inhalts gestimmt hat.

""" + PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""Neue Antwort auf {subject_type} " {subject_title} """


ALERTANSWER_MESSAGE = u"""
Hallo {recipient_first_name},

Eine neue Antwort wurde auf {subject_type} "{subject_title}" gegeben.

"{comment_content}"

Sie können es unter {comment_url} finden und eine Antwort darauf geben.

""" + PORTAL_SIGNATURE

ADMIN_REPORT_SUBJECT = u"""Neue Beschilderung auf der partizipativen Plattform {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Hallo {recipient_first_name},

Sie wurden von der Plattform {novaideo_title} ausgewählt, um einen Inhalt zu moderieren, der auf der Plattform als möglicherweise nicht konform mit der Moderationsrichtlinie {url_moderation_rules} gemeldet wurde. 

Bei jeder Meldung von Inhalten auf der Plattform {novaideo_title}, die möglicherweise gegen die Moderationsrichtlinien verstoßen, zieht das System drei Mitglieder, die den Inhalt auf seine Übereinstimmung mit den Moderationsrichtlinien überprüfen. Indem wir die Moderation nach dem Zufallsprinzip verteilen, vermeiden wir, dass diese wichtige Kontrollfunktion in wenigen Händen konzentriert wird. Wir tragen damit zum demokratischen Charakter der Plattform bei.

Um Ihre Rolle als Moderator dieses Inhalts auszuüben, loggen Sie sich einfach auf der Plattform unter {subject_url} ein und geben Ihre Meinung zur Übereinstimmung dieses Inhalts mit der Moderationsrichtlinie ab.

Die Dauer der Moderation beträgt {duration} Tag(e). Nach dem Datum {date_end_vote} wird die Moderation beendet und Ihre Stimme wird nicht mehr berücksichtigt. Bitte beachten Sie! Standardmäßig wird der Inhalt akzeptiert, wenn bis zu diesem Datum kein Moderator für die Moderation dieses Inhalts gestimmt hat.

""" + PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Neue Beschilderung auf der partizipativen Plattform {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Hallo {recipient_first_name},

Ihr Inhalt {subject_url} wurde von einem Mitglied als potenzieller Verstoß gegen die Moderationsrichtlinien {url_moderation_rules} gemeldet.

Jedes Mal, wenn ein Inhalt als potenziell gegen die Moderationsrichtlinien verstoßend gemeldet wird, werden drei Mitglieder ausgelost, um zu entscheiden, ob dieser Inhalt mit den Moderationsrichtlinien übereinstimmt.

Die Dauer der Überprüfung beträgt {duration} Tag(e). Nach dem {date_end_vote} wird die Überprüfung beendet und Sie werden über das Ergebnis informiert.

""" + PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie wurde abgelehnt"""

ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
LiebeR {recipient_first_name},


die Prüfer, die bei Ihrer Anmeldung nach dem Zufallsprinzip ausgewählt wurden, haben die Übereinstimmung zwischen den Identitätsdaten, die Sie auf der Plattform angegeben haben, und den offiziellen Ausweisdokumenten, die Sie ihnen in Kopie geschickt oder bei Ihren Videokonferenzen gezeigt haben, NICHT überprüft.

Wir bedauern daher, Ihnen mitteilen zu müssen, dass Ihre Anmeldung auf der {novaideo_title} abgelehnt worden ist. 

Wir müssen bei dieser Überprüfung sehr streng sein. Wenn wir auch nur geringfügige Abweichungen zulassen würden, könnte sich eine einzige natürliche Person mehrmals anmelden, jedes Mal mit kleinen Abweichungen in ihren Identitätsdaten, mehrere Konten eröffnen und mehrere Male abstimmen. Dies würde gegen das demokratische Prinzip "eine Person = eine Stimme" verstoßen. 

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie: Nächste Schritte"""

ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
LiebeR {recipient_first_name},


Sie haben sich soeben bei der {novaideo_title} Plattform für deliberative Demokratie angemeldet. Vielen Dank und herzlichen Glückwunsch! Wir freuen uns, Sie als Mitglied begrüßen zu dürfen.

Wie in unserem Anmeldeformular beschrieben, muss Ihre Anmeldung in einem recht einfachen, aber strengen Verfahren validiert werden. 

Bei jeder neuen Anmeldung auf der {novaideo_title} Plattform wählt das System nach dem Zufallsprinzip drei bestehende Mitglieder (die Überprüfer dieser speziellen Anmeldung) aus und bittet sie, die Identität der neu angemeldeten Person zu überprüfen. Es ist in der Tat wichtig zu überprüfen, dass jede natürliche Person mit einem Mitglied der Plattform verbunden ist, und zwar nur mit einem. Auf diese Weise vermeiden wir, dass eine natürliche Person mehrmals unter verschiedenen Pseudonymen auf der Plattform abstimmt. Auf diese Weise wahren wir das demokratische Prinzip "1 Person = 1 Stimme"

Damit Ihre Identität überprüft werden kann, bitten wir Sie, jeder der folgenden Personen in separaten E-Mails am oder vor dem {date_send_id_data}:
   - entweder eine eingescannte Kopie (oder ein Smartphone-Foto) eines amtlichen Ausweises. Aus dieser Kopie oder diesem Foto müssen Ihr(e) Vorname(n), Nachname(n), Geburtsdatum und -ort sowie Ihre Staatsangehörigkeit deutlich hervorgehen. Aus Sicherheitsgründen empfehlen wir Ihnen, beim Einscannen oder Fotografieren Ihres amtlichen Ausweises Ihr Foto und Ihre Unterschrift zu verdecken, so dass das Bild absichtlich unvollständig ist;
- oder drei Vorschläge für eine Videokonferenzsitzung, die für jeden Vorschlag das Datum im Format TT-mmm-JJJJ (Tag zweistellig, Monat dreibuchstabig, Jahr vierstellig), die Uhrzeit (unter Angabe Ihres Wohnorts) und den Link zur Videokonferenz enthalten, zum Beispiel über die freie und offene Plattform https://meet.jit.si/. Alle von Ihnen vorgeschlagenen Daten und Uhrzeiten müssen vor {date_end_vote} liegen, d.h. vor dem Ende der Frist, die den Prüfern für ihre Entscheidung zur Verfügung steht.

Wenn die Prüfer nach {date_send_id_data} keine Kopie Ihres amtlichen Ausweises oder eine Einladung zu einer Videokonferenz erhalten haben, sind sie angewiesen, Ihre Anmeldung abzulehnen.

Während der Videokonferenz mit jedem der Prüfer (falls Sie sich dafür entscheiden) zeigen Sie ihm Ihren amtlichen Ausweis, wobei Sie Ihren Vornamen, Ihren Nachnamen, Ihr Geburtsdatum und Ihren Geburtsort sowie Ihre Staatsangehörigkeit sichtbar machen und Ihr Foto und Ihre Unterschrift verbergen, falls Sie dies wünschen. 

Die mit der Überprüfung Ihrer Identität beauftragten Prüfer sind:
{moderators}

Das Ergebnis dieser Identitätsüberprüfung erhalten Sie nach Ablauf der Zeit, die den Überprüfern für ihre Entscheidung zur Verfügung steht, d.h. spätestens am {date_end_vote}.

Die Prüfer wurden angewiesen, gegebenenfalls alle Dateien mit der Kopie Ihres amtlichen Ausweises zu vernichten, sobald sie die Überprüfung Ihrer Identitätsdaten durchgeführt haben, und Ihnen anschließend Bericht zu erstatten. 

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.
""" + PORTAL_SIGNATURE


REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""ERINNERUNG - ABLAUFFRIST MORGEN: Bitte aktivieren Sie die Überprüfung Ihrer Identität, um sich auf der {novaideo_title} Plattform für deliberative Demokratie anzumelden"""

REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
## Wenn Sie den Prüfern bereits eine Kopie Ihres offiziellen Ausweises geschickt oder eine Videokonferenzsitzung vorgeschlagen haben, ignorieren Sie bitte diese E-Mail und nehmen Sie unsere Entschuldigung an ##

LiebeR {recipient_first_name},

wie Sie sich vielleicht erinnern, ist Ihre Anmeldung auf der {novaideo_title} Plattform für deliberative Demokratie nun von der Überprüfung Ihrer Identität abhängig. Die Frist, bis zu der Sie den Überprüfern eine Kopie Ihres offiziellen Ausweises oder eine Einladung zu einem Treffen per Videokonferenz zukommen lassen müssen, ist MORGEN {date_send_id_data}.

Nachstehend finden Sie eine Erinnerung an das einzuhaltende Verfahren (einschließlich der E-Mail-Adressen der Überprüfer) und die Begründung für dieses Verfahren.

Wir freuen uns darauf, Sie bei unseren Aktivitäten begrüßen zu dürfen!

Mit freundlichen Grüßen,

Die {novaideo_title} Plattform.

## Erinnerung an das Verfahren und seine Begründung ##
Bei jeder neuen Anmeldung auf der {novaideo_title} Plattform wählt das System nach dem Zufallsprinzip drei bestehende Mitglieder (die Überprüfer dieser speziellen Anmeldung) aus und bittet sie, die Identität der neu angemeldeten Person zu überprüfen. Es ist in der Tat wichtig zu überprüfen, dass jede natürliche Person mit einem Mitglied der Plattform verbunden ist, und zwar nur mit einem. Auf diese Weise vermeiden wir, dass eine bestimmte natürliche Person mehrmals unter verschiedenen Pseudonymen auf der Plattform abstimmt.

Damit Ihre Identität überprüft werden kann, bitten wir Sie, jeder der folgenden Personen am oder vor dem {date_send_id_data} eine separate E-Mail zu schicken:
   - entweder eine eingescannte Kopie (oder ein Smartphone-Foto) eines amtlichen Ausweises. Aus dieser Kopie oder diesem Foto müssen Ihr(e) Vorname(n), Ihr(e) Nachname(n), Ihr Geburtsdatum und Ihr Geburtsort sowie Ihre Staatsangehörigkeit deutlich hervorgehen. Aus Sicherheitsgründen empfehlen wir Ihnen, Ihr Foto und Ihre Unterschrift beim Einscannen oder Fotografieren Ihres amtlichen Ausweises zu verdecken, so dass das Bild absichtlich unvollständig ist;
- oder drei Vorschläge für eine Videokonferenzsitzung, die für jeden Vorschlag das Datum im Format TT-mmm-JJJJ (Tag zweistellig, Monat dreibuchstabig, Jahr vierstellig), die Uhrzeit (unter Angabe Ihres Wohnorts) und den Link zur Videokonferenz enthalten, zum Beispiel über die freie und offene Plattform https://meet.jit.si/. Alle von Ihnen vorgeschlagenen Daten und Uhrzeiten müssen vor {date_end_vote} liegen, d.h. vor dem Ende der Frist, die den Prüfern für ihre Entscheidung zur Verfügung steht.

Wenn die Prüfer nach {date_send_id_data} keine Kopie Ihres amtlichen Ausweises oder eine Einladung zu einer Videokonferenz erhalten haben, sind sie angewiesen, Ihre Anmeldung abzulehnen.

Während der Videokonferenz mit jedem der Prüfer (falls Sie sich dafür entscheiden) zeigen Sie ihm/ihr Ihren amtlichen Ausweis, wobei Sie Ihren Vornamen, Ihren Nachnamen, Ihr Geburtsdatum und Ihren Geburtsort sowie Ihre Staatsangehörigkeit sichtbar machen und Ihr Foto und Ihre Unterschrift verbergen, falls Sie dies wünschen. 

Die mit der Überprüfung Ihrer Identität beauftragten Prüfer sind:
{moderators}

Das Ergebnis dieser Identitätsüberprüfung erhalten Sie nach Ablauf der Frist, die den Überprüfern für ihre Entscheidung eingeräumt wurde, d.h. spätestens am {date_end_vote}.
""" + PORTAL_SIGNATURE


PUBLISHEDCHALLENGE_SUBJECT = u"""Entscheidung der Moderatoren, die Challenge zu veröffentlichen " {subject_title} """


PUBLISHEDCHALLENGE_MESSAGE = u"""
Hallo {recipient_first_name},

Die Challenge "{subject_title}", die unter {subject_url} zu finden ist, wurde soeben von den Moderatoren auf der Plattform {novaideo_title} veröffentlicht.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Entscheidung der Moderatoren, die Challenge " {subject_title} " zu archivieren."""


ARCHIVECHALLENGE_MESSAGE = u"""
Hallo {recipient_first_name},

Die Challenge "{subject_title}" wurde soeben von den Moderatoren aus folgendem Grund archiviert:

{explanation}

Sie können Ihre Challenge unter {subject_url} finden.

""" + PORTAL_SIGNATURE


PRESENTATION_CHALLENGE_SUBJECT = u"""Präsentation der Challenge " {subject_title} """


PRESENTATION_CHALLENGE_MESSAGE = u"""
Guten Tag,

{my_first_name} {my_last_name} möchte Ihnen die Herausforderung "{subject_title}" vorstellen, die auf der Plattform {novaideo_title} zu finden ist. Diese Herausforderung ist zugänglich unter der Adresse: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


ADMIN_CONTENT_SUB_SUBJECT = u"""Neuer Inhalt auf der Mitmach-Plattform {novaideo_title}"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Hallo {recipient_first_name},

Ihr Inhalt wurde zur Moderation eingereicht.

Jedes Mal, wenn ein neuer Inhalt zur Plattform {novaideo_title} hinzugefügt wird, werden drei Mitglieder ausgelost, die den Inhalt auf die Einhaltung der Moderationsrichtlinien {url_moderation_rules} überprüfen.

Die Dauer der Überprüfung beträgt {duration} Tag(e). Nach dem Datum {date_end_vote} wird die Überprüfung beendet und Sie werden über das Ergebnis informiert.

""" + PORTAL_SIGNATURE


ALERTCOMMENT_SUBJECT = u"""Neuer Kommentar zu {subject_type} " {subject_title} """


ALERTCOMMENT_MESSAGE = u"""
Hallo {recipient_first_name},

Es wurde ein neuer Kommentar zu {subject_type} "{subject_title}" abgegeben.

"{comment_content}"

Sie können ihn unter {comment_url} finden und eine Antwort darauf geben.

""" + PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Neue Nachricht zu Ihrer Diskussion auf " {subject_title} " hinzugefügt."""


ALERTDISCUSS_MESSAGE = u"""
Hallo {recipient_first_name},

Eine neue Nachricht wurde zu Ihrem Thema mit "{subject_title}" hinzugefügt.

"{comment_content}"

Sie finden ihn unter {comment_url} und können ihn beantworten.

""" + PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Eine Person hat eine Antwort auf einen Kommentar zu {subject_type} " {subject_title} " gegeben."""


ALERTRESPONS_MESSAGE = u"""
Hallo {recipient_first_name},

Eine Person hat eine Antwort auf einen Kommentar zu {subject_type} " {subject_title} " gegeben, der unter {comment_url} zu finden ist.

"{comment_content}"

""" + PORTAL_SIGNATURE


NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Newsletter-Anmeldung"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Hallo {first_name} {last_name},

Sie haben sich jetzt für den Newsletter {newsletter_title} angemeldet.

""" + PORTAL_SIGNATURE

NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Abmeldung vom Newsletter"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Hallo {first_name} {last_name},

Sie haben sich jetzt vom Newsletter {newsletter_title} abgemeldet.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Aufforderung zur Abmeldung von Ihrem Konto auf der Plattform {novaideo_title}"""

QUIT_REQUEST_MESSAGE = u"""
Sehr geehrte(r) {recipient_first_name} {recipient_last_name},

Wir haben auf Ihrem Konto bei der Plattform {novaideo_title} eine Aufforderung zur Kündigung erhalten.
Wenn Sie die Kündigung beantragt haben, klicken Sie bitte auf den folgenden Bestätigungslink: {url}, vor dem Datum {deadline_date}.

ACHTUNG: Diese Aktion ist nicht umkehrbar. Wenn Sie auf diesen Link klicken, haben Sie keinen Zugang mehr zur Plattform, Ihr Konto wird zerstört und alle Inhalte, die mit Ihrem Konto verknüpft sind, werden unwiderruflich einem anonymen Autor zugewiesen.
Sie können sich für einen Zeitraum von {tquarantaine} Tagen nicht erneut auf der Plattform registrieren, indem Sie ein neues leeres Konto erstellen.

Wenn Sie nicht darum gebeten haben, die Plattform zu verlassen, ignorieren Sie diese E-Mail und Ihr Konto wird weiterhin aktiv bleiben.
Wir empfehlen Ihnen jedoch, Ihr Passwort zu ändern, um zu verhindern, dass Ihr Konto gehackt wird.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Ihr Rücktritt von der Plattform für Online-Demokratie {novaideo_title} wurde berücksichtigt"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Sehr geehrte(r) {recipient_first_name} {recipient_last_name},

Sie haben den Wunsch geäußert, von der Plattform für Online-Demokratie {novaideo_title} zurückzutreten. Wir bedauern dies natürlich, respektieren aber Ihre Entscheidung. Wir teilen Ihnen hiermit mit, dass:
* Ihr Konto wurde deaktiviert. Sie werden in Zukunft nur noch eine einzige Nachricht von uns erhalten (siehe unten).
* Alle Inhalte in Ihrem Konto wurden unwiderruflich einem anonymen Autor zugewiesen.
* Die Identitätsinformationen, die Sie uns bei der Registrierung gegeben haben (Vor- und Nachnamen, Geburtsdatum und -ort) und Ihre E-Mail-Adresse werden für {tquarantaine} Tage gespeichert, um zu verhindern, dass Sie sich in dieser Zeit erneut registrieren können. Damit soll verhindert werden, dass Personen, die sich auf der Plattform unangemessen verhalten haben (und daher einen schlechten Ruf haben), sofort unter einem neuen Pseudonym und mit einem sauberen Ruf zurückkehren.
* Nach Ablauf dieses Zeitraums, d.h. am {date_tquarantaine}, werden Sie von uns eine E-Mail erhalten, in der wir Sie darüber informieren, dass Ihre Identitätsdaten und Ihre E-Mail-Adresse endgültig aus unserer Datenbank gelöscht wurden.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""Ihre Identitätsdaten und Ihre E-Mail-Adresse wurden endgültig aus der Datenbank der Plattform {novaideo_title} gelöscht!"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Sehr geehrte(r) {recipient_first_name} {recipient_last_name},

Heute wurden Ihre persönlichen Daten (Vorname, Nachname, Geburtsdatum und -ort) und Ihre E-Mail-Adresse endgültig aus unserer Datenbank gelöscht. Sie werden keine weiteren E-Mails von uns erhalten.

""" + PORTAL_SIGNATURE


mail_locale = 'de'

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
