# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, *

from . import add_mail_template

""" The contents of e-mails"""

PORTAL_SIGNATURE = """Hoogachtend,

Het platform {novaideo_title}
229, rue Solférino
59000 Lille (Frankrijk)
"""

PORTAL_PRESENTATION = u"""{novaideo_title} is een participatief platform waarmee elk lid ideeën kan initiëren die kunnen worden gebruikt in voorstellen die door werkgroepen worden verbeterd. Na verbetering kunnen deze voorstellen aan de leden worden voorgelegd ter overweging en besluitvorming door een beoordelingspanel.

"""

FIRST_INVITATION_SUBJECT = u"""Uitnodiging om deel te nemen aan het participatieplatform {novaideo_title}"""

FIRST_INVITATION_MESSAGE = u"""
Hallo,

Bedankt voor uw interesse in Nova-Ideo.

{recipient_first_name} wordt u uitgenodigd om als sitebeheerder toe te treden tot het participatieplatform Nova-Ideo.

Om uw uitnodiging te valideren, moet u op de link {invitation_url} klikken en de instructies volgen.

Wij herinneren u eraan dat Nova-Ideo een online participatieve innovatieoplossing is waarmee u de volgende zaken kunt aanpakken
- U wilt een participatieve innovatieoplossing opzetten;
- U hebt al een ideeënbus, maar die is leeg of zo vol dat het onmogelijk is de juiste ideeën te vinden;
- U hebt geen tijd om ideeën te beheren en laat zo veel kansen liggen, en creëert teleurstelling bij degenen die ideeën hebben.

Met Nova-Ideo kunt u ideeën van een groep verzamelen, de goede ideeën vinden en ze omzetten in werkbare voorstellen die alle standpunten weerspiegelen.

Hiervoor gebruikt Nova-Ideo crowdsourcing, waarbij de "menigte" werkt aan het omzetten van ideeën in voorstellen.

Nova-Ideo combineert het beste van de ideeënbus, het samenwerkingsportaal en de interne communicatiemiddelen en biedt geavanceerde oplossingen voor sociale innovatie, zoals het gebruik van het meerderheidsoordeel of de organisatie van steun/afwijzing schaarste.

Bezoek onze pagina https://www.nova-ideo.com en in het bijzonder de documentatiepagina https://www.nova-ideo.com/documentation.

Volg ons twitteraccount: https://twitter.com/NovaIdeo

U kunt onze gedetailleerde presentatie van Nova-Ideo http://fr.slideshare.net/MichaelLaunay/20160911-novaideo-linnovation-participative-en-ligne raadplegen.

De code van Nova-Ideo onder de vrije AGPL V3 licentie is beschikbaar op: https://github.com/ecreall/nova-ideo

De video gefilmd tijdens het PyConFR waarin wordt uitgelegd waar Nova-Ideo vandaan komt en waarom het gratis is: http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html

Wij produceren ook een reeks video's waarin het beheer en de werking van Nova-Ideo worden uitgelegd; deze zijn toegankelijk via de pagina Documentatie van onze website https://www.nova-ideo.com/documentation .

Wij kunnen Nova-Ideo aanpassen aan uw specifieke behoeften, dus aarzel niet om contact met ons op te nemen, wij zullen uw vragen beantwoorden!

U kunt ons ook uw opmerkingen en suggesties voor verbetering sturen door een account aan te maken op https://evolutions.nova-ideo.com.

Met vriendelijke groet
Het Ecréall-team
Gratis software diensten en oplossingen
Wetenschapspark Haute Borne
Hub Innovatiegebouw
11, rue de l'Harmonie
59650 Villeneuve d'Ascq
site : http://www.ecreall.com
tel : 03 20 79 32 90
mob : 06 16 85 91 12
Fax : 09 56 94 39 44
"""

FIRST_INVITATION_SMS_MESSAGE = u"""
Hallo,

Bedankt voor uw interesse in Nova-Ideo.

{recipient_first_name} wordt u uitgenodigd om als sitebeheerder toe te treden tot het participatieplatform Nova-Ideo.

Om uw uitnodiging te valideren, moet u op de link {invitation_url} klikken en de instructies volgen.

Met vriendelijke groet
Het Ecréall-team
"""

INVITATION_SUBJECT = u"""Uitnodiging om deel te nemen aan het {novaideo_title} participatieve platform"""

INVITATION_MESSAGE = u"""
Hallo {recipient_first_name},

U bent uitgenodigd om deel te nemen aan het {novaideo_title} participatieplatform als {roles}.

Wij zouden heel blij zijn met u als actief lid! Om uw uitnodiging te valideren, klikt u op de link {invitation_url} en volgt u de instructies. Tot ziens op het {novaideo_title} platform!

""" + PORTAL_SIGNATURE


PRESENTATION_IDEA_SUBJECT = u"""Presentatie van het idee " {subject_title} """


PRESENTATION_IDEA_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil graag het idee " {subject_title} " presenteren op het platform {novaideo_title}. Dit idee is toegankelijk op het adres: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Bevestiging van uw inschrijving op het platform voor overlegdemocratie {novaideo_title}"""

CONFIRMATION_MESSAGE = u"""
Hallo {recipient_first_name},

Wij bevestigen uw inschrijving op het platform voor overlegdemocratie {novaideo_title}. Welkom op het platform!

Met vriendelijke groet,
                                                                                
Het platform voor overlegdemocratie {novaideo_title}
""" + PORTAL_SIGNATURE


PRESENTATION_PROPOSAL_SUBJECT = u"""Presentatie van het voorstel" {subject_title} """


PRESENTATION_PROPOSAL_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil graag het voorstel "{subject_title}" indienen op het {novaideo_title} platform. Dit voorstel is toegankelijk op {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil graag het amendement "{subject_title}" indienen dat op het {novaideo_title} platform verschijnt onder {subject_url}.

""" + \
    PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_SUBJECT = u""" {subject_title} """


PRESENTATION_QUESTION_SUBJECT = u"""Presentatie van de vraag " {subject_title} """


PRESENTATION_QUESTION_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil u graag kennis laten maken met de vraag "{subject_title}" op het {novaideo_title} platform. Deze vraag is toegankelijk op: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_ANSWER_SUBJECT = u"""Presentatie van het antwoord op een vraag" {subject_title} """


PRESENTATION_ANSWER_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil graag het antwoord geven op een vraag " {subject_title} " op het platform {novaideo_title}. Dit antwoord is te vinden op: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


AMENDABLE_FIRST_SUBJECT = u"""Begin van de verbeteringscyclus van het voorstel" {subject_title} """


AMENDABLE_FIRST_MESSAGE = u"""
Hallo {recipient_first_name},

U bent nu drie deelnemers in de werkgroep voor het voorstel "{subject_title}" onder {subject_url}, en u kunt beginnen met het verbeteren ervan.

Elke deelnemer kan suggesties voor verbetering doen die de andere deelnemers kunnen aanvaarden of verwerpen. Wanneer de verbeteringscyclus voorbij is, stemmen alle deelnemers om het voorstel verder te verbeteren of om het ter goedkeuring voor te leggen aan de leden van het platform.

De verbeteringscyclus eindigt op {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Begin van verbeteringscyclus voorstel" {subject_title} """


AMENDABLE_MESSAGE = u"""
Hallo {recipient_first_name},

De werkgroep voor het voorstel "{subject_title}" onder {subject_url} heeft bij meerderheid gestemd voor verdere verbetering van het voorstel.

Elke deelnemer kan suggesties voor verbetering doen die de andere deelnemers kunnen aanvaarden of verwerpen. Wanneer de verbeteringscyclus voorbij is, stemmen alle deelnemers om het voorstel verder te verbeteren of om het ter overweging voor te leggen aan de leden van het platform.

De verbeteringscyclus eindigt op {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""Einde van de verbeteringscyclus voor het voorstel " {subject_title} " zonder enige verbetering"""

ALERT_MESSAGE = u"""
Hallo {recipient_first_name},

Hoewel de onderhoudscyclus is voltooid, zijn er geen verbeteringen aangebracht in het voorstel "{subject_title}" dat onder {subject_url} staat. U zult moeten stemmen over de vraag of u het voorstel indient zoals het is, of dat u een nieuwe verbeteringsronde start.

""" + PORTAL_SIGNATURE

ALERT_END_SUBJECT = u"""Laatste verbeteringen voor het einde van de verbeteringscyclus van het voorstel" {subject_title} """

ALERT_END_MESSAGE = u"""
Hallo {recipient_first_name},

De onderhoudscyclus voor het "{subject_title}" voorstel onder {subject_url} is bijna voltooid. U kunt nog steeds verbeteringen aanbrengen, voordat de werkgroep stemt om het voorstel in te dienen zoals het is of om een nieuwe verbeteringscyclus te starten.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


RESULT_VOTE_AMENDMENT_SUBJECT = u"""De uitslag van de stemming over de amendementen met betrekking tot het voorstel " {subject_title} """

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>
Hallo {recipient_first_name},

{message_result}
</div>
""" + PORTAL_SIGNATURE


PUBLISHPROPOSAL_SUBJECT = u"""Besluit om het voorstel " {subject_title}" in te dienen ter overweging door de leden van het platform"""

PUBLISHPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

De werkgroep over het voorstel "{subject_title}" onder {subject_url} heeft bij meerderheid gestemd om het voorstel ter overweging voor te leggen aan de leden van het platform.

Elk platformlid kan nu het voorstel steunen of zich ertegen verzetten.

""" + PORTAL_SIGNATURE


SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Besluit om het "{subject_title}" voorstel te sluiten"""

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

De werkgroep voor het "{subject_title}" voorstel onder {subject_url} is al een paar cycli langer dan een week niet actief geweest.
Daarom is de werkgroep ontbonden en staat het voorstel nu open voor een werkgroep.

""" + PORTAL_SIGNATURE


VOTINGPUBLICATION_SUBJECT = u"""Begin met stemmen om het voorstel "{subject_title}" te verbeteren of dien het in ter overweging door de leden van het platform"""

VOTINGPUBLICATION_MESSAGE = u"""
Hallo {recipient_first_name},

De verbeteringscyclus voor het voorstel "{subject_title}" onder {subject_url} is afgerond, u wordt uitgenodigd om deel te nemen aan de stemming om het voorstel te verbeteren of het ter overweging voor te leggen aan de leden van het platform.

U heeft 24 uur de tijd om te stemmen, waarna de stem wordt geteld rekening houdend met de keuze van de meerderheid van de stemmers. Als er niet wordt gestemd, begint een nieuwe verbeteringsronde van een week.

""" + PORTAL_SIGNATURE


VOTINGAMENDEMENTS_SUBJECT = u"""De stemming over amendementen op het voorstel {subject_title} begint ."""

VOTINGAMENDEMENTS_MESSAGE = u"""
Hallo {recipient_first_name},

De stemming over de amendementen op het voorstel "{subject_title}" onder {subject_url} is begonnen. Neem deel aan de stemming.

""" + PORTAL_SIGNATURE

WITHDRAW_SUBJECT = u"""Verwijdering van de wachtlijst van de werkgroep van het voorstel " {subject_title} """

WITHDRAW_MESSAGE = u"""
Hallo {recipient_first_name},

U staat niet langer op de wachtlijst voor het voorstel werkgroep {subject_title}" onder {subject_url}, na uw verwijdering van de wachtlijst.

U kunt zich te allen tijde weer bij de werkgroep voorstellen voegen als deze nog wordt verbeterd.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""U kunt nu beginnen deel te nemen aan de werkgroep in verband met het voorstel {subject_title} """

PARTICIPATE_WL_MESSAGE = u"""
Hallo {recipient_first_name},

U bent lid van de werkgroep voor het voorstel {subject_title}" dat onder {subject_url} staat, na het vertrek van een van de deelnemers.

Als deelnemer aan de werkgroep kunt u het voorstel verbeteren en aan het einde van de verbeteringscyclus kunt u stemmen om het voorstel verder te verbeteren of het voorleggen aan de leden van het platform.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""U kunt nu beginnen deel te nemen aan de werkgroep in verband met het voorstel" {subject_title} """

PARTICIPATE_MESSAGE = u"""
Hallo {recipient_first_name},

U bent lid van de werkgroep voor het voorstel {subject_title} dat te vinden is onder {subject_url}.

Als deelnemer aan de werkgroep kunt u het voorstel verbeteren, als het wordt verbeterd, en aan het einde van de verbeteringscyclus kunt u stemmen over de vraag of het voorstel verder wordt verbeterd of wordt voorgelegd aan de leden van het platform.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Dien uw deelname in aan de voorstelwerkgroep" {subject_title} """


PARTICIPATE_SUB_MESSAGE = u"""

Hallo {recipient_first_name},

Uw verzoek tot deelname aan de werkgroep "{subject_title}" voorstel onder {subject_url} is ingediend bij de leden van de groep.

Bij elk nieuw verzoek tot deelname beslissen de groepsleden of ze het verzoek al dan niet aanvaarden.

De duur van de stemming over uw aanvraag is {duration} dag(en). Na de datum van {date_end_vote} wordt de stemming over uw aanvraag gesloten,

""" + PORTAL_SIGNATURE


RESIGN_SUBJECT = u"""Uw vertrek uit de werkgroep voorstellen" {subject_title} """

RESIGN_MESSAGE = u"""
Hallo {recipient_first_name},

Wij bevestigen dat u niet langer lid bent van de werkgroep "{subject_title}" van het voorstel onder {subject_url}.

U kunt er te allen tijde weer lid van worden, als u niet al lid bent van vijf andere werkgroepen, wat het maximum aantal werkgroepen is waaraan een lid tegelijkertijd mag deelnemen.

""" + PORTAL_SIGNATURE


EXCLUDE_SUBJECT = u"""Uitsluiting van de werkgroep van het voorstel " {subject_title} """

EXCLUDE_MESSAGE = u"""
Hallo {recipient_first_name},

De werkgroep heeft besloten u van de groep uit te sluiten. U bent niet langer lid van de werkgroep voor het voorstel "{subject_title}" dat zich bevindt onder {subject_url}.

U kunt te allen tijde lid worden van een andere werkgroep, als u nog geen lid bent van vijf andere werkgroepen, wat het maximum aantal werkgroepen is waaraan een lid tegelijkertijd mag deelnemen.

""" + PORTAL_SIGNATURE


EXCLUDE_PARTICIPANT_SUBJECT = u"""U wordt uitgenodigd te stemmen over het verzoek om {user_first_name} {user_last_name} uit te sluiten van de werkgroep met betrekking tot het voorstel " {subject_title} """

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Hallo {recipient_first_name},

{user_first_name} {user_last_name} is zojuist gevraagd om te worden uitgesloten van de werkgroep over het voorstel "{subject_title}".

U wordt verzocht te stemmen over dit verzoek om uitsluiting. Om dit te doen, hoeft u alleen maar verbinding te maken met het platform op het volgende adres {subject_url} en te stemmen op het uitsluitingsverzoek van {user_first_name} {user_last_name} buiten de werkgroep die gekoppeld is aan het voorstel "{subject_title}".

De duur van de stemming is {duration} dag(en). Na de datum van {date_end_vote} wordt de stemming gesloten en wordt uw stem niet meer in aanmerking genomen. Let op! Indien op deze datum geen enkele deelnemer heeft gestemd over de uitsluiting van {user_first_name} {user_last_name} uit de werkgroep met betrekking tot het voorstel "{subject_title}", wordt {user_first_name} {user_last_name} standaard in de werkgroep gehandhaafd.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""U wordt verzocht kennis te nemen van het coöperatieve gedrag van {user_first_name} """

NOTING_MEMBER_MESSAGE = u"""
Hallo {recipient_first_name},

{user_title} heeft zojuist de werkgroep verlaten, hetzij door ontslag te nemen, hetzij door uitgesloten te worden. Wanneer een lid een werkgroep verlaat, vraagt het systeem de resterende leden van de werkgroep de kwaliteit van zijn/haar coöperatief gedrag te beoordelen, zoals die door de resterende leden in het werk van de groep wordt waargenomen.

Daarom wordt u gevraagd een score te geven aan de kwaliteit van het coöperatieve gedrag van {user_title} in de groep met betrekking tot het voorstel {subject_title}. De mogelijke scores zijn:
-1 = coöperatief gedrag beneden wat ik verwacht in een werkgroepsetting
0 = coöperatief gedrag in overeenstemming met wat ik verwacht in een werkgroep
+1 = coöperatief gedrag beter dan wat ik verwacht in een werkgroep

Om het coöperatieve gedrag van {user_title} te beoordelen, gaat u gewoon naar deze URL {subject_url} en geeft u een beoordeling uit de lijst.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""U wordt uitgenodigd om het coöperatieve gedrag van de andere leden van de groep met betrekking tot het voorstel " {subject_title} " te beoordelen."""

NOTING_PARTICIPANT_MESSAGE = u"""
Hallo {recipient_first_name},

U hebt zojuist de werkgroep met betrekking tot het voorstel {subject_title} verlaten, hetzij door ontslag te nemen, hetzij omdat u bent uitgesloten. Wanneer een lid een werkgroep verlaat, vraagt het systeem dat lid om de kwaliteit van het samenwerkingsgedrag van elk van de resterende deelnemers aan de werkgroep te beoordelen, zoals dat vertrekkende lid die waarneemt in het werk van die groep.

Daarom wordt u verzocht een score te geven aan de kwaliteit van het coöperatieve gedrag van de andere deelnemers in de groep met betrekking tot het voorstel {subject_title}. De mogelijke scores zijn:
-1 = coöperatief gedrag beneden wat ik verwacht in een werkgroep
0 = coöperatief gedrag in overeenstemming met wat ik verwacht in een werkgroep
+1 = coöperatief gedrag beter dan wat ik verwacht in een werkgroep

Om uw score te geven aan het coöperatieve gedrag van de andere deelnemers van de werkgroep met betrekking tot het voorstel {subject_title}, hoeft u alleen maar naar deze URL {subject_url} te gaan en een score te geven aan elk van de overige deelnemers van deze groep.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""U wordt uitgenodigd om het coöperatieve gedrag van de andere leden van de groep met betrekking tot het voorstel " {subject_title} " te beoordelen."""

NOTING_MEMBERS_MESSAGE = u"""
Hallo {recipient_first_name},

De werkgroep gekoppeld aan het {subject_title} voorstel heeft het zojuist gepubliceerd en ter overweging voorgelegd aan de andere leden van het platform. Het is dus klaar met zijn werk. Het wordt ontbonden, en de leden ervan kunnen zich op andere voorstellen concentreren.

Wanneer een werkgroep zijn activiteiten staakt en ontbindt, vraagt het systeem elk van de leden om de kwaliteit van het coöperatieve gedrag van de andere leden te beoordelen, zoals dat lid dat waarneemt bij het werk van die groep.

Daarom wordt u gevraagd een score te geven aan de kwaliteit van het coöperatieve gedrag van de andere leden van de groep met betrekking tot het voorstel {subject_title}. De mogelijke scores zijn:
-1 = coöperatief gedrag beneden wat ik verwacht in een werkgroep
0 = coöperatief gedrag in overeenstemming met wat ik verwacht in een werkgroep
+1 = coöperatief gedrag beter dan wat ik verwacht in een werkgroep

Om uw score te geven aan het coöperatieve gedrag van de andere leden van de werkgroep met betrekking tot het voorstel {subject_title}, hoeft u alleen maar naar deze URL {subject_url} te gaan en een score te geven aan elk van de andere leden van deze groep.

""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""U wordt uitgenodigd te stemmen over de kandidatuur van {user_first_name} {user_last_name} voor de werkgroep met betrekking tot het voorstel " {subject_title} """

NEW_PARTICIPANT_MESSAGE = u"""

Hallo {recipient_first_name},

{user_first_name} {user_last_name} heeft zich zojuist aangemeld voor deelname aan de werkgroep met betrekking tot het voorstel "{subject_title}".

U wordt verzocht over deze aanvraag te stemmen. Om dit te doen, hoeft u alleen maar verbinding te maken met het platform op het volgende adres {subject_url} en te stemmen op de kandidatuur van {user_first_name} {user_last_name} voor de werkgroep die gekoppeld is aan het voorstel "{subject_title}".

De duur van de stemming is {duration} dag(en). Na de datum {date_end_vote} wordt de stemming gesloten en wordt er geen rekening meer gehouden met uw stem. Let op! Indien op deze datum geen enkele deelnemer heeft gestemd op de aanvraag van {user_first_name} {user_last_name} voor de werkgroep met betrekking tot het voorstel "{subject_title}", wordt {user_first_name} {user_last_name} standaard aanvaard in de werkgroep.

""" + PORTAL_SIGNATURE

# Le chiffre de 12 comme étant le nombre maximal de participants dans le groupe de travail est inscrit en dur dans le code
# C'est en réalité un paramètre de l'application
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


WATINGLIST_SUBJECT = u"""Inschrijving op de wachtlijst van de voorstelwerkgroep" {subject_title} """

WATINGLIST_MESSAGE = u"""
Hallo {recipient_first_name},

U wilt deelnemen aan de werkgroep van het voorstel "{subject_title}" onder {subject_url}, maar het aantal deelnemers heeft al 12 bereikt, wat het maximum aantal deelnemers aan een werkgroep is.

U staat op de wachtlijst voor deze werkgroep en wordt automatisch opgenomen zodra er een plaats vrijkomt.

""" + PORTAL_SIGNATURE


NEWCONTENT_SUBJECT = u"""{subject_type} " {subject_title} die een van uw trefwoorden van interesse bevat is gepubliceerd."""


NEWCONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

{subject_type} " {subject_title} " die een van uw trefwoorden bevat is zojuist gepubliceerd. U kunt het bekijken onder {subject_url}.

""" + PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} " {subject_title} " die deel uitmaakt van uw favorieten heeft zojuist zijn status gewijzigd"""


CONTENTMODIFIEF_MESSAGE = u"""
Hallo {recipient_first_name},

{subject_type} "{subject_title}" die deel uitmaakt van uw favorieten is zojuist gewijzigd van {state_source} naar {state_target}. U kunt het bekijken onder {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Moderators' decision to archive the idea " {subject_title} """


ARCHIVEIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Het idee "{subject_title}" is gearchiveerd door de moderators om de volgende reden:

{explanation}

U kunt uw idee vinden onder {subject_url}.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Moderators' decision to archive content " {subject_title} """


ARCHIVECONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

De inhoud "{subject_title}" is gearchiveerd door de moderators om de volgende reden:

{explanation}

U kunt uw inhoud vinden onder {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEPROPOSAL_SUBJECT = u"""Moderators' decision to archive the proposal" {subject_title} """


ARCHIVEPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Het voorstel "{subject_title}" is door de moderatoren gearchiveerd om de volgende reden:

{explanation}

U kunt uw voorstel vinden onder {subject_url}.

""" + PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Advies van het beoordelingscomité over het voorstel" {subject_title} """


ALERTOPINION_MESSAGE = u"""
Hallo {recipient_first_name},

Het toetsingscomité heeft een advies "{opinion}" uitgebracht over het voorstel "{subject_title}" met de volgende toelichting: "{explanation}".

""" + PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u""" Advies van het beoordelingscomité over het idee " {subject_title} """


ALERTOPINIONIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Een recensent heeft een advies "{opinion}" uitgebracht over het idee "{subject_title}" met de volgende toelichting: "{explanation}".

""" + PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Moderators' decision to publish idea " {subject_title} """


PUBLISHEDIDEA_MESSAGE = u"""
Hallo {recipient_first_name},

Het idee "{subject_title}" onder {subject_url} is door de moderators gepubliceerd op het {novaideo_title} platform. Dit idee kan nu door elk lid van het platform worden gebruikt voor een voorstel.

""" + PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""beslissing van de moderatoren om het voorstel te publiceren" {subject_title} """


PUBLISHEDPROPOSAL_MESSAGE = u"""
Hallo {recipient_first_name},

Het voorstel "{subject_title}" onder {subject_url} is zojuist door de moderators gepubliceerd op het {novaideo_title} platform.

""" + PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Schrapping van het voorstel " {subject_title} """


PROPOSALREMOVED_MESSAGE = u"""
Hallo {recipient_first_name},

Het voorstel "{subject_title}" is om de volgende reden door de moderators verwijderd:

"{explanation}"

""" + PORTAL_SIGNATURE


REFUSE_INVITATION_SUBJECT = u"""Weigering van {user_first_name} {user_last_name} om lid te worden van het {novaideo_title} platform"""


REFUSE_INVITATION_MESSAGE = u"""
Hallo,

Wij wijzen u erop dat {user_first_name} {user_last_name} uw uitnodiging om lid te worden van het {novaideo_title} platform heeft afgewezen.

""" + PORTAL_SIGNATURE


ACCEPT_INVITATION_SUBJECT = u"""Acceptatie van {user_first_name} {user_last_name} om toe te treden tot het {novaideo_title} platform"""


ACCEPT_INVITATION_MESSAGE = u"""
Hallo {recipient_first_name},

{user_first_name} {user_last_name} heeft uw uitnodiging om lid te worden van het {novaideo_title} platform geaccepteerd.

""" + PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""Uw nieuwe wachtwoord op het {novaideo_title} platform"""


RESETPW_MESSAGE = u"""
Hallo {recipient_first_name},

U wenst een nieuw wachtwoord op het {novaideo_title} platform, klik dan op het {reseturl} adres en voer uw nieuwe wachtwoord in.

""" + PORTAL_SIGNATURE

PREREGISTRATION_SUBJECT = u"""Gelieve uw registratie op het {novaideo_title} platform voor deliberatieve democratie"""


PREREGISTRATION_MESSAGE = u"""
Beste {recipient_first_name},


Uw registratie op het {novaideo_title} platform voor deliberatieve democratie is bijna voltooid. Er is nog een laatste stap te zetten.

Om je registratie te voltooien, moet je nu op de volgende link {url} klikken. Deze link is 48 uur geldig, d.w.z. je moet je registratie op of voor {deadline_date} afronden.

We zijn blij je tot onze leden te mogen rekenen. We hopen dat je deelname voor jou een positieve en lonende ervaring zal zijn, in een volledig democratisch kader. Welkom!

Met vriendelijke groeten,
""" + PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Gelieve uw registratie op het {novaideo_title} platform voor deliberatieve democratie"""


PREREGISTRATION_MOD_MESSAGE = u"""
Beste {recipient_first_name},


De Verificateurs die bij uw registratie willekeurig zijn geselecteerd, hebben de overeenstemming gevalideerd tussen de Identiteitsgegevens die u bij uw registratie op het platform hebt verstrekt, en die van de officiële identiteitsdocumenten waarvan u hen rechtstreeks een kopie hebt gestuurd of die u hen tijdens de visoconferentiebijeenkomsten hebt getoond.

We weten nu zeker dat jij de enige persoon bent die onder deze Identiteitsgegevens op het {novaideo_title} platform voor deliberatieve democratie. Net als alle andere leden heb je maar één account, en draag je bij aan het handhaven van het democratische principe "1 persoon = 1 stem".

Je hoeft nog maar één handeling te verrichten om je registratie af te ronden: klik op de volgende link {url}. Deze link is 48 uur geldig, d.w.z. je moet je registratie op of voor {deadline_date} afronden.


We zijn blij je tot onze leden te mogen rekenen. We hopen dat je deelname voor jou een positieve en lonende ervaring zal zijn, in een volledig democratisch kader. Welkom!


""" + PORTAL_SIGNATURE

# Il faudra compléter avec le lieu de naissance
ADMIN_PREREGISTRATION_SUBJECT = u"""Werk mee om een nieuwe registratie op het {novaideo_title} overlegdemocratie platfom"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
Beste {recipient_first_name},


U bent willekeurig geselecteerd door het {novaideo_title} deliberatieve democratie platfom op te treden als een Verifier, wiens taak het is om de identiteit te verifiëren van een persoon die zich zojuist online heeft geregistreerd.

Bij elke nieuwe registratie op het {novaideo_title} platfom selecteert het systeem willekeurig drie bestaande leden, en vraagt hen de identiteit van de nieuw geregistreerde persoon te verifiëren. Het is namelijk belangrijk om te controleren of elke natuurlijke persoon gerelateerd is aan één lid op het platform, en aan slechts één lid. Zo voorkomen we dat een bepaalde natuurlijke persoon meerdere keren op het platform stemt onder verschillende pseudoniemen.

Om deze verificatie van de identiteit van deze persoon uit te voeren, hoef je slechts de volgende stappen te volgen:
1. je ontvangt op of voor de {date_send_id_data} een e-mail van de persoon die zich zojuist op het platform heeft geregistreerd. Het e-mailadres van deze persoon, van waaruit hij/zij jou zijn/haar e-mail zal sturen, is {subject_email}. Deze e-mail bevat :
   - ofwel een scan van een officieel identiteitsbewijs. Om veiligheidsredenen raden we de persoon die zich zojuist heeft ingeschreven aan om zijn/haar foto en handtekening bij het scannen te verbergen: de kopie zal opzettelijk onvolledig zijn;
   - of een uitnodiging voor een korte videoconferentievergadering (datum, tijd, inloglink) waarin de persoon je zijn/haar identiteitsdocument laat zien, zodat je de inhoud ervan kunt lezen.
   
2. Je reageert, indien van toepassing, op de persoon door aan te geven welke van de drie voorgestelde data en tijdstippen jou het beste uitkomt voor de videoconferentievergadering, en je neemt deel aan de vergadering op de dag en het tijdstip dat is aangegeven. 

3. Zodra je de e-mail met de kopie van het officiële identiteitsbewijs hebt ontvangen of de videoconferentievergadering hebt gehouden, of als je geen kopie van het officiële identiteitsbewijs of een uitnodiging voor een videoconferentievergadering hebt ontvangen, op {date_end_vote}: 
      (a) inloggen op het platform {novaideo_title} en dan 
      (b) de volgende URL openen: {subject_url}. Op deze pagina bepaal je of de Identiteitsgegevens die je van deze persoon hebt ontvangen (en die hieronder zijn weergegeven) overeenkomen met die op het officiële identiteitsbewijs, waarvan je een kopie per e-mail hebt ontvangen of die je tijdens de videoconferentievergadering hebt gezien. Wees zeer voorzichtig! Om de registratie te kunnen accepteren, moeten ALLE elementen strikt IDENTIEK zijn tussen de Identiteitsgegevens die je bij de registratie hebt ontvangen, en die op het officiële identiteitsdocument dat je per e-mail hebt ontvangen of dat je tijdens de videoconferentievergadering hebt gezien. In alle andere gevallen, zelfs bij een enkel, klein verschil, als je twijfelt aan de echtheid van het gekopieerde officiële identiteitsdocument, of als je de kopie van het officiële identiteitsdocument of een uitnodiging voor een vergadering per videoconferentie niet hebt ontvangen voor {date_end_vote}, MOET je de registratie weigeren.
      
4. Zodra je deze handeling hebt uitgevoerd, en ongeacht het resultaat ervan, verzoeken wij je vriendelijk om, indien van toepassing, alle kopieën die je hebt van het officiële identiteitsdocument dat je van de nieuw geregistreerde persoon hebt ontvangen, van je computer te vernietigen, en hem/haar over deze vernietiging te rapporteren, door hem/haar een e-mail te sturen naar {subject_email}.

###

De Identiteitsgegevens die van de persoon zijn ontvangen bij zijn/haar registratie zijn de volgende:

  Familienaam/-namen: {subject_last_name}
  Voornaam/-namen: {subject_first_name}
  Geboortedatum: {birth_date}
  Geboorteplaats: {birthplace}
  Burgerschap: {citizenship}

###

Het Verificatieproces duurt {duration} dag(en), d.w.z. het moet op of voor {date_end_vote} voltooid zijn. Na deze datum wordt het Verificatieproces afgesloten, en wordt er geen rekening gehouden met je beslissing. Als geen enkele Verificateur op deze datum heeft gestemd, wordt de registratie standaard geweigerd.

""" + PORTAL_SIGNATURE

ADMIN_CONTENT_SUBJECT = u"""Nieuwe inhoud op het participatieplatform {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Hallo {recipient_first_name},

U bent gekozen door het {novaideo_title} platform om nieuwe inhoud die aan het platform wordt toegevoegd te modereren.

Telkens wanneer een nieuwe inhoud (idee of voorstel) wordt toegevoegd aan het {novaideo_title} platform, trekt het systeem drie leden aan om de conformiteit van deze inhoud met het {url_moderation_rules} Moderation Charter te controleren. Door de moderatie random te verdelen, vermijden we dat deze belangrijke controlefunctie in enkele handen wordt geconcentreerd. Zo dragen wij bij tot het democratische karakter van het platform.

Om uw rol als Moderator over deze nieuwe inhoud uit te oefenen, hoeft u alleen maar verbinding te maken met het platform op het volgende adres {subject_url} en uw mening te geven over de conformiteit van deze inhoud met het Moderation Charter.

De duur van de Moderatie is {duration} dag(en). Na de datum van {date_end_vote} wordt de moderatie gesloten, en wordt er geen rekening meer gehouden met uw stem. Let op! Als er op deze datum nog geen Moderator heeft gestemd om deze inhoud te modereren, wordt de inhoud standaard geaccepteerd.

""" + PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""Nieuw antwoord op {subject_type} " {subject_title} """


ALERTANSWER_MESSAGE = u"""
Hallo {recipient_first_name},

Er is een nieuw antwoord gegeven op {subject_type} " {subject_title} ".

"{comment_content}"

U kunt het vinden onder {comment_url} en er een reactie op geven.

""" + PORTAL_SIGNATURE

ADMIN_REPORT_SUBJECT = u"""Nieuwe bewegwijzering op het participatieplatform {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Hallo {recipient_first_name},

U bent gekozen door het platform {novaideo_title} om inhoud te modereren die op het platform is gemeld als mogelijk niet in overeenstemming met het Moderation Charter {url_moderation_rules}.

Telkens wanneer een inhoud op het platform {novaideo_title} wordt gemeld als mogelijk niet-conform met het Moderation Charter, trekt het systeem drie willekeurige leden om de conformiteit van deze inhoud met het Moderation Charter te controleren. Door de moderatie random te verdelen, vermijden we dat deze belangrijke controlefunctie in enkele handen wordt geconcentreerd. Zo dragen wij bij tot het democratische karakter van het platform.

Om uw rol als Moderator voor deze inhoud uit te oefenen, hoeft u alleen maar verbinding te maken met het platform op het volgende adres {subject_url} en uw mening te geven over de conformiteit van deze inhoud met het Moderation Charter.

De duur van de Moderatie is {duration} dag(en). Na de datum van {date_end_vote} wordt de moderatie gesloten, en wordt er geen rekening meer gehouden met uw stem. Let op! Als er op deze datum nog geen Moderator heeft gestemd om deze inhoud te modereren, wordt de inhoud standaard geaccepteerd.

""" + PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Nieuwe bewegwijzering op het participatieplatform {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Hallo {recipient_first_name},

Uw inhoud {subject_url} is door een Lid gemarkeerd als mogelijk in strijd met het Moderatiebeleid {url_moderation_rules}.

Telkens wanneer een inhoud wordt gerapporteerd als potentieel strijdig met het Moderation Charter, trekt het systeem drie willekeurige leden om zich uit te spreken over de conformiteit van deze inhoud met het Moderation Charter.

De duur van de verificatie is {duration} dag(en). Na de datum van {date_end_vote} wordt de verificatie afgesloten, en wordt u op de hoogte gebracht van het resultaat.

""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Uw registratie op het {novaideo_title} platform voor overlegdemocratie is geweigerd"""

ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Beste {recipient_first_name},


De verificateurs die bij uw registratie willekeurig zijn geselecteerd, hebben de overeenstemming tussen de identiteitsgegevens die u op het platform hebt verstrekt en de gegevens op de officiële identiteitsdocumenten waarvan u hen een kopie hebt gestuurd of die u hen tijdens uw videoconferenties hebt getoond, NIET gevalideerd.

Het spijt ons u daarom te moeten meedelen dat uw registratie op de {novaideo_title} is geweigerd. 

We moeten zeer streng zijn bij deze controle. Als we zelfs maar kleine verschillen tussen beide zouden toestaan, zou een enkele natuurlijke persoon zich meerdere keren kunnen registreren, telkens met kleine variaties in zijn/haar Identiteitsgegevens, meerdere rekeningen kunnen openen en meerdere keren kunnen stemmen. Dit zou in strijd zijn met het democratische beginsel "één persoon = één stem". 


""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Uw registratie op het {novaideo_title} platform voor deliberatieve democratie: volgende stappen"""

ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Beste {recipient_first_name},


U heeft zich zojuist geregistreerd op het {novaideo_title} platform voor deliberatieve democratie. Bedankt en gefeliciteerd! We kijken ernaar uit je te verwelkomen onder onze leden.

Zoals beschreven in ons registratieformulier, moet je registratie worden gevalideerd in een vrij eenvoudige, maar strenge procedure. 

Bij elke nieuwe registratie op het {novaideo_title} platfom, selecteert het systeem willekeurig drie bestaande leden (de Verificateurs van deze specifieke registratie), en vraagt hen de identiteit van de nieuw geregistreerde persoon te verifiëren. Het is namelijk belangrijk om te controleren of elke natuurlijke persoon gerelateerd is aan één lid op het platform, en aan slechts één lid. Zo voorkomen we dat een bepaalde natuurlijke persoon meerdere keren op het platform stemt onder verschillende pseudoniemen. Zo houden we ons aan het democratische principe "1 persoon = 1 stem".

Om je identiteit te kunnen verifiëren, verzoeken we je vriendelijk om op of voor de {date_send_id_data} in afzonderlijke e-mails aan elk van de volgende personen te sturen
   - ofwel een gescande kopie (of smartphone foto) van een officieel identiteitsbewijs. Op deze kopie of foto moeten duidelijk je voornaam/voornamen, achternaam/voornamen, geboortedatum en -plaats en je nationaliteit staan. Om veiligheidsredenen raden we je aan om bij het scannen of fotograferen van je officiële identiteitsdocument je foto en handtekening te maskeren, zodat het beeld bewust onvolledig is;
   - of drie voorstellen voor een videoconferentievergadering met voor elk voorstel de datum in het formaat DD-mmm-YYYYY (dag in twee cijfers, maand in drie letters, jaar in vier cijfers), het tijdstip (met vermelding van je woonplaats) en de link naar de videoconferentie, bijvoorbeeld via het gratis en open platform https://meet.jit.si/. Alle data en tijden die je voorstelt moeten vóór {date_end_vote} liggen, dat is het einde van de periode waarin de Verificateurs hun beslissing kunnen nemen.

Na {date_send_id_data}, als de Verificateurs geen kopie van je officiële identiteitsbewijs of een uitnodiging voor een videoconferentievergadering hebben ontvangen, krijgen ze de opdracht je inschrijving te weigeren.

Tijdens de videoconferentievergadering met elk van de Verificateurs (als dit je keuze is) toon je hem/haar je officiële identiteitsdocument, waarbij je je voornamen, achternamen, geboortedatum en -plaats en nationaliteit zichtbaar maakt, en desgewenst je foto en je handtekening verbergt. 

De Verificateurs die zijn aangewezen voor de verificatie van je identiteit zijn:
{moderators}

Je ontvangt het resultaat van deze identiteitscontrole aan het einde van de tijd dieREMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT de controleurs hebben gekregen om hun beslissing te nemen, dus uiterlijk op {date_end_vote}.

De verificateurs hebben de opdracht gekregen om, indien van toepassing, alle bestanden met de kopie van uw officiële identiteitsbewijs te vernietigen zodra zij de verificatie van uw identiteitsgegevens hebben uitgevoerd, en u daarvan verslag uit te brengen. 
""" + PORTAL_SIGNATURE


REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""HERINNERING - DUITSLUITING MORGEN: maak de verificatie van je identiteit mogelijk om je te registreren op het {novaideo_title} platform voor deliberatieve democratie"""

REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
## Als u de kopie van uw officiële identiteitsbewijs al naar de verificateurs heeft gestuurd of een videoconferentie heeft voorgesteld, kunt u deze e-mail negeren en onze excuses aanvaarden.##

Beste {recipient_first_name},

Zoals u zich wellicht herinnert, is uw registratie op het {novaideo_title} platform voor overlegdemocratie nu onderworpen aan de verificatie van uw identiteit. De deadline voor u om de Verificateurs een kopie van uw officiële identiteitsbewijs of een uitnodiging voor een vergadering per videoconferentie te sturen is OMROEP {date_send_id_data}.

Hieronder vindt u de herinnering aan de te volgen procedure (inclusief de e-mailadressen van de Verificateurs) en de beweegredenen voor deze procedure.

Wij verheugen ons erop u bij onze activiteiten te mogen verwelkomen!

Met vriendelijke groeten,

Het {novaideo_title} platform.

## Herinnering aan de procedure en de grondgedachte ervan ##
Bij elke nieuwe registratie op het {novaideo_title} platfom selecteert het systeem willekeurig drie bestaande leden (de Verificateurs van deze specifieke registratie), en vraagt hen de identiteit van de nieuw geregistreerde persoon te verifiëren. Het is namelijk belangrijk om te controleren of elke natuurlijke persoon gerelateerd is aan één lid op het platform, en aan slechts één lid. Zo voorkomen we dat een bepaalde natuurlijke persoon meerdere keren op het platform stemt onder verschillende pseudoniemen.

Om je identiteit te kunnen verifiëren, verzoeken we je vriendelijk om op of voor de {date_send_id_data} in afzonderlijke e-mails aan elk van de volgende personen te sturen:
   - ofwel een gescande kopie (of smartphone foto) van een officieel identiteitsbewijs. Op deze kopie of foto moeten duidelijk je voor- en achternaam (-namen), geboortedatum en -plaats en nationaliteit vermeld staan. Om veiligheidsredenen raden we je aan om bij het scannen of fotograferen van je officiële identiteitsbewijs je foto en handtekening te maskeren, zodat het beeld bewust onvolledig is;
   - of drie voorstellen voor een videoconferentievergadering met voor elk voorstel de datum in het formaat DD-mmm-YYYY (dag in twee cijfers, maand in drie letters, jaar in vier cijfers), het tijdstip (met vermelding van je woonplaats) en de link naar de videoconferentie, bijvoorbeeld via het gratis en open platform https://meet.jit.si/. Alle data en tijden die je voorstelt moeten vóór {date_end_vote} liggen, dat is het einde van de periode waarin de Verificateurs hun beslissing kunnen nemen.

Na {date_send_id_data}, als de Verificateurs geen kopie van je officiële identiteitsbewijs of een uitnodiging voor een videoconferentievergadering hebben ontvangen, krijgen ze de opdracht je inschrijving te weigeren.

Tijdens de videoconferentievergadering met elk van de Verificateurs (als dit je keuze is) toon je hem/haar je officiële identiteitsdocument, waarbij je je voornamen, achternamen, geboortedatum en -plaats en nationaliteit zichtbaar maakt, en je foto en handtekening desgewenst verbergt. 

De Verificateurs die zijn aangewezen voor de verificatie van je identiteit zijn:
{moderators}

Je ontvangt het resultaat van deze identiteitscontrole aan het einde van de tijd die de controleurs hebben gekregen om hun beslissing te nemen, dus uiterlijk op {date_end_vote}.
""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur

PUBLISHEDCHALLENGE_SUBJECT = u""" Besluit van de moderators om de uitdaging te publicieren " {subject_title} """


PUBLISHEDCHALLENGE_MESSAGE = u"""
Hallo {recipient_first_name},

De uitdaging "{subject_title}" onder {subject_url} is zojuist gepubliceerd door de moderators op het {novaideo_title} platform.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Besluit van de moderators om de uitdaging te archiveren" {subject_title} """


ARCHIVECHALLENGE_MESSAGE = u"""
Hallo {recipient_first_name},

De uitdaging "{subject_title}" is door de moderators gearchiveerd om de volgende reden:

{explanation}

U kunt uw uitdaging vinden onder {subject_url}.

""" + PORTAL_SIGNATURE


PRESENTATION_CHALLENGE_SUBJECT = u"""Uitdagingspresentatie " {subject_title} """


PRESENTATION_CHALLENGE_MESSAGE = u"""
Hallo,

{my_first_name} {my_last_name} wil u graag laten kennismaken met de uitdaging " {subject_title} " op het platform {novaideo_title}. Deze uitdaging is toegankelijk op: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


ADMIN_CONTENT_SUB_SUBJECT = u"""Nieuwe inhoud op het {novaideo_title} participatieplatform"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Hallo {recipient_first_name},

Uw inhoud is voorgelegd aan Moderatie.

Telkens wanneer een nieuwe inhoud wordt toegevoegd aan het platform {novaideo_title}, trekt het systeem drie leden aan om de conformiteit van deze inhoud met het Moderation Charter {url_moderation_rules} te controleren.

De duur van de verificatie is {duration} dag(en). Na de datum van {date_end_vote} wordt de verificatie afgesloten, en wordt u op de hoogte gebracht van het resultaat.

""" + PORTAL_SIGNATURE


ALERTCOMMENT_SUBJECT = u"""Nieuw commentaar op {subject_type} " {subject_title} """


ALERTCOMMENT_MESSAGE = u"""
Hallo {recipient_first_name},

Er is een nieuw commentaar gemaakt op {subject_type} "{subject_title}".

"{comment_content}"

U kunt het vinden onder {comment_url} en een reactie geven.

""" + PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Nieuw bericht toegevoegd aan uw discussie over " {subject_title} """


ALERTDISCUSS_MESSAGE = u"""
Hallo {recipient_first_name},

Een nieuw bericht is toegevoegd aan uw thread met "{subject_title}".

"{comment_content}"

U kunt het vinden onder {comment_url} en een antwoord geven.

""" + PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Een persoon heeft gereageerd op een commentaar op {subject_type} " {subject_title} """


ALERTRESPONS_MESSAGE = u"""
Hallo {recipient_first_name},

Iemand heeft gereageerd op een commentaar op {subject_type} " {subject_title} " dat staat onder {comment_url}.

"{comment_content}"

""" + PORTAL_SIGNATURE


NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Inschrijving nieuwsbrief"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Hallo {first_name} {last_name},

U bent nu geabonneerd op de nieuwsbrief {newsletter_title}.

""" + PORTAL_SIGNATURE

NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Afmelden voor de nieuwsbrief"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Hallo {first_name} {last_name},

U bent nu uitgeschreven voor de nieuwsbrief {newsletter_title}.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Verzoek om ontslag te nemen van uw account op het {novaideo_title} platform"""

QUIT_REQUEST_MESSAGE = u"""
Geachte {recipient_first_name} {recipient_last_name},

Wij hebben een ontslagaanvraag ontvangen op uw {novaideo_title} platform account.
Als u hebt verzocht om uit het platform te stappen, klik dan op de volgende bevestigingslink: {url}, vóór de datum {deadline_date}.

WAARSCHUWING: deze actie is IRREVERSIBEL. Als u op deze link klikt, hebt u geen toegang meer tot het platform, wordt uw account vernietigd en wordt alle inhoud die aan uw account is gekoppeld onherroepelijk toegeschreven aan een anonieme auteur.
U kunt zich niet opnieuw registreren op het platform, door een nieuwe lege account aan te maken, voor een periode gelijk aan {tquarantaine} dagen.

Als u niet hebt gevraagd het platform te verlaten, negeer dan deze e-mail en uw account blijft actief.
Wij raden u echter aan uw wachtwoord te wijzigen om te voorkomen dat uw account wordt gehackt.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Er is rekening gehouden met uw ontslag bij het e-democratieplatform {novaideo_title}"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Geachte {recipient_first_name} {recipient_last_name},

U heeft ontslag willen nemen van het e-democratieplatform {novaideo_title}. Wij betreuren dit uiteraard, maar respecteren uw keuze. Hierbij informeren wij u dat:
* uw account is gedeactiveerd. U zult in de toekomst slechts één bericht van ons ontvangen (zie hieronder)
* alle inhoud van uw account is onherroepelijk toegeschreven aan een Anonieme auteur
* de identiteitsgegevens die u ons bij uw registratie hebt verstrekt (voornamen, achternamen, geboortedatum en -plaats) en uw e-mailadres worden {tquarantaine} dagen bewaard, om te voorkomen dat u zich gedurende deze periode opnieuw registreert. Het doel is te voorkomen dat mensen die zich ongepast hebben gedragen op het platform (en dus een slechte reputatie hebben) onmiddellijk terugkeren onder een nieuw pseudoniem en met een schone reputatie.
* Na deze periode, d.w.z. op {date_tquarantaine}, ontvangt u een e-mail van ons met de mededeling dat uw identiteitsgegevens en e-mailadres definitief uit onze database zijn verwijderd.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""Uw identiteitsgegevens en e-mailadres zijn permanent verwijderd uit de database van het {novaideo_title} platform!"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Geachte {recipient_first_name} {recipient_last_name},

Vandaag zijn uw identiteitsgegevens (voornaam, achternaam, geboortedatum en -plaats) en uw e-mailadres definitief uit onze database verwijderd. U zult geen e-mails meer van ons ontvangen.

""" + PORTAL_SIGNATURE

mail_locale = 'nl'

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
