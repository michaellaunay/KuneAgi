# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from . import add_mail_template

PORTAL_SIGNATURE = """Cordialement,

La Plateforme {novaideo_title}
"""

PORTAL_PRESENTATION = u"""{novaideo_title} est une plateforme participative qui permet à tout membre d'initier des idées pouvant être utilisées dans des propositions améliorées par des groupes de travail. Une fois améliorées, ces propositions peuvent être soumises à l'appréciation des membres et faire l'objet d'une décision d'un comité d'examen.

"""

FIRST_INVITATION_SUBJECT = u"""Invitation à rejoindre la plateforme participative {novaideo_title}"""

FIRST_INVITATION_MESSAGE = u"""
Bonjour,

Nous vous remercions de l'intérêt que vous portez à Nova-Ideo.

{recipient_first_name} vous êtes invité à rejoindre la plateforme participative Nova-Ideo en tant que administrateur du site.

Pour valider votre invitation, vous devez cliquer sur le lien {invitation_url} et suivre les instructions.

Nous vous rappellons que Nova-Ideo est une solution d'innovation participative en ligne qui permet de répondre aux problèmes suivants :
- Vous souhaitez mettre en place une solution d'innovation participative ;
- Vous avez déjà une boite à idées, mais soit elle est vide, soit si pleine qu'il est impossible de trouver les bonnes idées ;
- Vous n'avez pas de temps à passer à gérer les idées et manquez ainsi de nombreuses opportunités, et créez de la déception chez ceux qui ont des idées.

Nova-Ideo permet de recueillir les idées d'un collectif, de trouver les bonnes idées et de les transformer en propositions applicables reflétant tous les points de vue.

Pour cela Nova-Ideo utilise le crowdsourcing en faisant travailler la "foule" sur la transformation des idées en propositions.

Nova-Ideo fusionne le meilleur de la boite à idées, du portail collaboratif et des outils de communication internes et propose des solutions d'innovation sociale à la pointe comme l'utilisation du jugement majoritaire ou l'organisation de la rareté des soutiens/rejets.

Consultez notre page https://www.nova-ideo.com et notamment sa page Documentation https://www.nova-ideo.com/documentation

Suivez notre compte twitter : https://twitter.com/NovaIdeo

Vous pouvez consulter notre présentation détaillée de Nova-Ideo http://fr.slideshare.net/MichaelLaunay/20160911-novaideo-linnovation-participative-en-ligne

Le code de Nova-Ideo sous licence libre AGPL V3 est accessible sur : https://github.com/ecreall/nova-ideo

La vidéo filmée lors du PyConFR expliquant d'où vient Nova-Ideo et pourquoi il est libre : http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html

Nous réalisons également une série de vidéos expliquant l'administration et le fonctionnement de Nova-Ideo accessible depuis la page Documentation de notre site https://www.nova-ideo.com/documentation .

Nous pouvons adapter Nova-Ideo à vos besoins spécifiques, alors n'hésitez pas à nous contacter, nous répondrons à vos questions !

Vous pouvez aussi faire part de vos remarques et proposer des évolutions en créant un compte sur https://evolutions.nova-ideo.com

Cordialement
L'équipe d'Ecréall
Services et Solutions en Logiciels Libres
Parc scientifique de la Haute Borne
Bâtiment Hub Innovation
11, rue de l'Harmonie
59650 Villeneuve d'Ascq
site : http://www.ecreall.com
tél : 03 20 79 32 90
mob : 06 16 85 91 12
Fax : 09 56 94 39 44
"""

FIRST_INVITATION_SMS_MESSAGE = u"""
Bonjour,

Nous vous remercions de l'intérêt que vous portez à Nova-Ideo.

{recipient_first_name} vous êtes invité à rejoindre la plateforme participative Nova-Ideo en tant que administrateur du site.

Pour valider votre invitation, vous devez cliquer sur le lien {invitation_url} et suivre les instructions.

Cordialement
L'équipe d'Ecréall
"""

INVITATION_SUBJECT = u"""Invitation à rejoindre la plateforme participative {novaideo_title}"""

INVITATION_MESSAGE = u"""
Bonjour,

{recipient_first_name} vous êtes invité à rejoindre la plateforme participative {novaideo_title} en tant que {roles}.

Pour valider votre invitation, vous devez cliquer sur le lien {invitation_url} et suivre les instructions.

""" + PORTAL_SIGNATURE


PRESENTATION_IDEA_SUBJECT = u"""Présentation de l'idée « {subject_title} »"""


PRESENTATION_IDEA_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter l'idée « {subject_title} » figurant sur la plateforme {novaideo_title}. Cette idée est accessible à l'adresse : {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Confirmation de votre inscription à la plateforme participative {novaideo_title}"""

CONFIRMATION_MESSAGE = u"""
Bienvenue sur la plateforme {novaideo_title}, nous vous confirmons votre inscription à la plateforme participative {novaideo_title}.

Faites-nous part de vos idées en vous connectant à l'adresse {login_url}.

""" + PORTAL_SIGNATURE


PRESENTATION_PROPOSAL_SUBJECT = u"""Présentation de la proposition « {subject_title} »"""


PRESENTATION_PROPOSAL_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter la proposition « {subject_title} » figurant sur la plateforme {novaideo_title}. Cette proposition est accessible à l'adresse : {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter l'amendement « {subject_title} » figurant sur la plateforme {novaideo_title} sous {subject_url}.

""" + \
    PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_SUBJECT = u"""« {subject_title} »"""


PRESENTATION_QUESTION_SUBJECT = u"""Présentation de la question « {subject_title} »"""


PRESENTATION_QUESTION_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter la question « {subject_title} » figurant sur la plateforme {novaideo_title}. Cette question est accessible à l'adresse : {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_ANSWER_SUBJECT = u"""Présentation de la réponse à une question « {subject_title} »"""


PRESENTATION_ANSWER_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter la réponse à une question « {subject_title} » figurant sur la plateforme {novaideo_title}. Cette réponse est accessible à l'adresse : {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


AMENDABLE_FIRST_SUBJECT = u"""Début du cycle d'amélioration de la proposition « {subject_title} »"""


AMENDABLE_FIRST_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous êtes dorénavant trois participants au groupe de travail de la proposition « {subject_title} » qui se trouve sous {subject_url}, vous pouvez commencer à l'améliorer.

Chaque participant peut faire des suggestions d'amélioration que les autres participants peuvent soit accepter, soit refuser. Lorsque le cycle d'amélioration est terminé, l'ensemble des participants votent soit pour continuer à améliorer la proposition, soit pour la soumettre à l'appréciation des membres de la plateforme.

Le cycle d'amélioration se termine le {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Début du cycle d'amélioration de la proposition « {subject_title} »"""


AMENDABLE_MESSAGE = u"""
Bonjour {recipient_first_name},

Le groupe de travail sur la proposition « {subject_title} » qui se trouve sous {subject_url} a voté à la majorité pour continuer à améliorer la proposition.

Chaque participant peut faire des suggestions d'amélioration que les autres participants peuvent soit accepter, soit refuser. Lorsque le cycle d'amélioration est terminé, l'ensemble des participants votent soit pour continuer à améliorer la proposition, soit pour la soumettre à l'appréciation des membres de la plateforme.

Le cycle d'amélioration se termine le {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""Fin du cycle d'amélioration de la proposition « {subject_title} » sans aucune amélioration"""

ALERT_MESSAGE = u"""
Bonjour {recipient_first_name},

Alors que le cycle d'amélioration est terminé, aucune amélioration n'a été apportée à la proposition « {subject_title} » qui se trouve sous {subject_url}. Vous allez devoir procéder au vote pour soumettre la proposition en l'état ou pour recommencer un nouveau cycle d'amélioration.

""" + PORTAL_SIGNATURE

ALERT_END_SUBJECT = u"""Dernières améliorations avant la fin du cycle d'amélioration de la proposition « {subject_title} »"""

ALERT_END_MESSAGE = u"""
Bonjour {recipient_first_name},

Le cycle d'amélioration pour la proposition « {subject_title} » qui se trouve sous {subject_url} touche pratiquement à sa fin. Vous pouvez encore y apporter des améliorations, avant que le groupe de travail vote pour soumettre la proposition en l'état ou pour recommencer un nouveau cycle d'amélioration.

""" + PORTAL_SIGNATURE


RESULT_VOTE_AMENDMENT_SUBJECT = u"""Les résultats du vote sur les amendements liés à la proposition « {subject_title} » """

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>
Bonjour {recipient_first_name},

{message_result}
</div>
""" + PORTAL_SIGNATURE


PUBLISHPROPOSAL_SUBJECT = u"""Décision de soumettre la proposition « {subject_title} » à l'appréciation des membres de la plateforme"""

PUBLISHPROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

Le groupe de travail sur la proposition « {subject_title} » qui se trouve sous {subject_url} a voté à la majorité pour soumettre la proposition à l'appréciation des membres de la plateforme.

Chaque membre de la plateforme peut dorénavant soutenir ou s'opposer à la proposition et le Comité d'examen peut l'examiner.

""" + PORTAL_SIGNATURE


SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Décision de cloturer la proposition « {subject_title} » à l'appréciation des membres de la plateforme"""

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

Le groupe de travail sur la proposition « {subject_title} » qui se trouve sous {subject_url} n'est plus actif depuis quelques cycles de plus d'une semaine.
Pour cette raison, le groupe de travail a été dissout et la proposition est maintenant ouverte à un groupe de travail.

""" + PORTAL_SIGNATURE


VOTINGPUBLICATION_SUBJECT = u"""Début du vote pour améliorer la proposition « {subject_title} » ou la soumettre à l'appréciation des membres de la plateforme """

VOTINGPUBLICATION_MESSAGE = u"""
Bonjour {recipient_first_name},

Le cycle d'amélioration de la proposition « {subject_title} » qui se trouve sous {subject_url} est terminé, vous êtes invité à prendre part au vote pour améliorer la proposition ou la soumettre à l'appréciation des membres de la plateforme.

Vous disposez de 24 heures pour voter, après quoi le vote sera dépouillé en tenant compte du choix de la majorité des votants. Si aucun vote n'a lieu, un nouveau cycle d'amélioration commence pour une semaine.

""" + PORTAL_SIGNATURE


VOTINGAMENDMENTS_SUBJECT = u"""Début des votes sur les amendements portant sur la proposition « {subject_title} »"""

VOTINGAMENDMENTS_MESSAGE = u"""
Bonjour {recipient_first_name},

Les votes sur les amendements portant sur la proposition « {subject_title} » qui se trouve sous {subject_url} ont commencé. Merci de prendre part aux votes.

""" + PORTAL_SIGNATURE

WITHDRAW_SUBJECT = u"""Retrait de la liste d'attente du groupe de travail de la proposition « {subject_title} »"""

WITHDRAW_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous ne faites plus partie de la liste d'attente du groupe de travail de la proposition {subject_title} » qui se trouve sous {subject_url}, suite à votre retrait de cette liste d'attente.

Vous pourrez à tout moment chercher à rejoindre à nouveau le groupe de travail de la proposition, si elle est encore en cours d'amélioration.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""Participation au groupe de travail de la proposition « {subject_title} »"""

PARTICIPATE_WL_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous faites partie du groupe de travail de la proposition {subject_title} » qui se trouve sous {subject_url}, suite au départ de l'un des participants.

Vous pouvez en tant que participant au groupe de travail améliorer la proposition et vous pourrez, à la fin du cycle d'amélioration, voter pour continuer à l'améliorer ou la soumettre à l'appréciation des membres de la plateforme.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Votre participation au groupe de travail de la proposition « {subject_title} »"""

PARTICIPATE_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous faites partie du groupe de travail de la proposition {subject_title} qui se trouve sous {subject_url}.

Vous pouvez en tant que participant au groupe de travail améliorer la proposition, s'il elle est en cours d'amélioration, et vous pourrez, à la fin du cycle d'amélioration, voter pour continuer à l'améliorer ou la soumettre à l'appréciation des membres de la plateforme.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUB_SUBJECT = u"""Soumisson de votre participation au groupe de travail de la proposition « {subject_title} »"""


PARTICIPATE_SUB_MESSAGE = u"""

Bonjour {recipient_first_name},

Votre demande de participation au groupe de travail de la proposition « {subject_title} » qui se trouve sous {subject_url} a été soumise aux membres du groupe.

À chaque nouvelle demande de participation, les membres du groupe statuent sur l'acceptation ou pas de la demande.

La durée de la vérification est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la vérification sera clôturée, et vous serez informé(e) de son résultat.

""" + PORTAL_SIGNATURE


RESIGN_SUBJECT = u"""Votre départ du groupe de travail de la proposition « {subject_title} »"""

RESIGN_MESSAGE = u"""
Bonjour {recipient_first_name},

Nous vous confirmons que vous ne faites plus partie du groupe de travail de la proposition « {subject_title} » qui se trouve sous {subject_url}.

Vous pourrez à tout moment le rejoindre de nouveau, si vous ne faites pas partie déjà de cinq autres groupes de travail, qui est le nombre maximum de groupes de travail auxquels un membre a le droit de participer simultanément.

""" + PORTAL_SIGNATURE


EXCLUDE_SUBJECT = u"""Exclusion du groupe de travail de la proposition « {subject_title} »"""

EXCLUDE_MESSAGE = u"""
Bonjour {recipient_first_name},

Le groupe de travail a dessidé de vous exclure du groupe. Vous ne faites plus partie du groupe de travail de la proposition « {subject_title} » qui se trouve sous {subject_url}.

Vous pourrez à tout moment rejoindre un autre groupe de travail, si vous ne faites pas partie déjà de cinq autres groupes de travail, qui est le nombre maximum de groupes de travail auxquels un membre a le droit de participer simultanément.

""" + PORTAL_SIGNATURE


EXCLUDE_PARTICIPANT_SUBJECT = u"""Vous êtes invité(e) à voter sur la demande d'exclusion de {user_first_name} {user_last_name} hors du Groupe de Travail lié à la proposition « {subject_title} »"""

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Bonjour {recipient_first_name},

{user_first_name} {user_last_name} vient de faire l'objet d'une demande d'exclusion hors du Groupe de Travail lié à la proposition « {subject_title} ».

Vous êtes appelé(e) à voter sur cette demande d'exclusion. Pour le faire, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y voter sur la demande d'exclusion de {user_first_name} {user_last_name} hors du Groupe de Travail lié à la proposition « {subject_title} ».

La durée du vote est de {duration} jour(s). Au-delà de la date du {date_end_vote}, le scrutin sera clôturé, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun(e) Participant(e) n'a voté à cette date sur l'exclusion de {user_first_name} {user_last_name} hors du Groupe de Travail lié à la proposition « {subject_title} », {user_first_name} {user_last_name} sera maintenu(e) dans le Groupe de Travail.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""Vous êtes invité(e) à noter le comportement coopératif de « {user_first_name} »"""

NOTING_MEMBER_MESSAGE = u"""
Bonjour {recipient_first_name},

{user_title} vient de quitter le Groupe de Travail, par sa démission ou parce qu'il (elle) en a été exclu(e). À chaque fois qu'un membre quitte un groupe de travail, le système demande aux membres restants du groupe de travail de juger la qualité de son comportement coopératif, tel que ces membres restants ont pu le percevoir dans le cadre du travail de ce groupe.

C'est pourquoi vous êtes invité(e) à attribuer une note à la qualité du comportement coopératif de {user_title} dans le cadre du groupe lié à la proposition {subject_title}. Les notes possibles sont:
-1 = comportement coopératif inférieur à ce que j'attends dans le cadre d'un groupe de travail
0 = comportement coopératif conforme à ce que j'attends dans le cadre d'un groupe de travail
+1 = comportement coopératif meilleur que ce que j'attends dans le cadre d'un groupe de travail

Pour attribuer votre note au comportement coopératif de {user_title}, il vous suffit d'accéder à cette URL {subject_url} et de donner une note parmi celles proposées.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""Vous êtes invité(e) à noter le comportement coopératif des autres membres du groupe lié à la proposition « {subject_title} »"""

NOTING_PARTICIPANT_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous venez de quitter le Groupe de Travail lié à la proposition {subject_title}, par votre démission ou parce que vous en avez été exclu(e). À chaque fois qu'un membre quitte un Groupe de Travail, le système demande à ce membre de juger la qualité du comportement coopératif de chacun des Participant(e)s restant(e)s du groupe de travail, tel que ce membre partant a pu les percevoir dans le cadre du travail de ce groupe.

C'est pourquoi vous êtes invité(e) à attribuer une note à la qualité du comportement coopératif des autres Participant(e)s du groupe lié à la proposition {subject_title}. Les notes possibles sont:
-1 = comportement coopératif inférieur à ce que j'attends dans le cadre d'un groupe de travail
0 = comportement coopératif conforme à ce que j'attends dans le cadre d'un groupe de travail
+1 = comportement coopératif meilleur que ce que j'attends dans le cadre d'un groupe de travail

Pour attribuer votre note au comportement coopératif des autres Participant(e)s du Groupe de Travail lié à la proposition {subject_title}, il vous suffit d'accéder à cette URL {subject_url} et de donner une note parmi celles proposées, à chacun(e) des Participant(e)s restant(e)s de ce groupe.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""Vous êtes invité(e) à noter le comportement coopératif des autres membres du groupe lié à la proposition « {subject_title} »"""

NOTING_MEMBERS_MESSAGE = u"""
Bonjour {recipient_first_name},

Le groupe de travail lié à la proposition {subject_title} vient de la publier, et de la soumettre pour appréciation aux autres membres de la plate-forme. Il a donc fini ses travaux. Il est dissout, et ses membres peuvent se consacrer à d'autres propositions.

À chaque fois qu'un groupe de travail cesse ses activités et se dissout, le système demande à chacun de ses membres de juger la qualité du comportement coopératif des autres membres, tel que ce membre a pu le percevoir dans le cadre du travail de ce groupe.

C'est pourquoi vous êtes invité(e) à attribuer une note à la qualité du comportement coopératif des autres membres du groupe lié à la proposition {subject_title}. Les notes possibles sont:
-1 = comportement coopératif inférieur à ce que j'attends dans le cadre d'un groupe de travail
0 = comportement coopératif conforme à ce que j'attends dans le cadre d'un groupe de travail
+1 = comportement coopératif meilleur que ce que j'attends dans le cadre d'un groupe de travail

Pour attribuer votre note au comportement coopératif des autres membres du groupe de travail lié à la proposition {subject_title}, il vous suffit d'accéder à cette URL {subject_url} et de donner une note parmi celles proposées, à chacun(e) des autres membres de ce groupe.

""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""Vous êtes invité(e) à voter sur la candidature de {user_first_name} {user_last_name} au Groupe de Travail lié à la proposition « {subject_title} »"""

NEW_PARTICIPANT_MESSAGE = u"""

Bonjour {recipient_first_name},

{user_first_name} {user_last_name} vient de présenter sa candidature pour participer au Groupe de Travail lié à la proposition « {subject_title} ».

Vous êtes appelé(e) à voter sur cette candidature. Pour le faire, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y voter sur la candidature de {user_first_name} {user_last_name} au Groupe de Travail lié à la proposition « {subject_title} ».

La durée du vote est de {duration} jour(s). Au-delà de la date du {date_end_vote}, le scrutin sera clôturé, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun(e) Participant(e) n'a voté à cette date sur la candidature de {user_first_name} {user_last_name} au Groupe de Travail lié à la proposition « {subject_title} », {user_first_name} {user_last_name} sera accepté(e) dans le Groupe de Travail.

""" + PORTAL_SIGNATURE


WATINGLIST_SUBJECT = u"""Inscription sur la liste d'attente du groupe de travail de la proposition « {subject_title} »"""

WATINGLIST_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous souhaitez participer au groupe de travail de la proposition « {subject_title} » qui se trouve sous {subject_url}, mais le nombre de participants a déjà atteint 12 personnes, qui est le nombre maximum de participants dans un groupe de travail.

Vous êtes sur la liste d'attente de ce groupe de travail et vous en ferez automatiquement partie, dès qu'une place se sera libérée.

""" + PORTAL_SIGNATURE


NEWCONTENT_SUBJECT = u"""{subject_type} « {subject_title} qui contient un des mots clés faisant partie de vos centres d'intérêt vient d'être publiée."""


NEWCONTENT_MESSAGE = u"""
Bonjour {recipient_first_name},

{subject_type} « {subject_title} » qui contient un des mots clés faisant partie de vos centres d'intérêt vient d'être publiée. Vous pouvez la consulter sous {subject_url}.

""" + PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} « {subject_title} » qui fait partie de vos favoris vient de changer d'état"""


CONTENTMODIFIEF_MESSAGE = u"""
Bonjour {recipient_first_name},

{subject_type} « {subject_title} » qui fait partie de vos favoris vient de passer de l'état {state_source} à l'état {state_target}. Vous pouvez la consulter sous {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Décision des modérateurs d'archiver l'idée « {subject_title} »"""


ARCHIVEIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

L'idée « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante:

{explanation}

Vous pouvez retrouver votre idée sous {subject_url}.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Décision des modérateurs d'archiver le contenu « {subject_title} »"""


ARCHIVECONTENT_MESSAGE = u"""
Bonjour {recipient_first_name},

Le contenu « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante:

{explanation}

Vous pouvez retrouver votre contenu sous {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEPROPOSAL_SUBJECT = u"""Décision des modérateurs d'archiver la proposition « {subject_title} »"""


ARCHIVEPROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante:

{explanation}

Vous pouvez retrouver votre proposition sous {subject_url}.

""" + PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Avis du Comité d'examen sur la proposition « {subject_title} »"""


ALERTOPINION_MESSAGE = u"""
Bonjour {recipient_first_name},

Le Comité d'examen a émis un avis « {opinion} » sur la proposition « {subject_title} » avec l'explication suivante : « {explanation} ».

""" + PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u"""Avis d'un Examinateur sur l'idée « {subject_title} »"""


ALERTOPINIONIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

Un Examinateur a émis un avis « {opinion} » sur l'idée « {subject_title} » avec l'explication suivante : « {explanation} ».

""" + PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Décision des modérateurs de publier l'idée « {subject_title} »"""


PUBLISHEDIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

L'idée « {subject_title} » qui se trouve sous {subject_url} vient d'être publiée par les modérateurs sur la plateforme {novaideo_title}. Cette idée peut maintenant être utilisée par n'importe quel membre de la plateforme pour une proposition.

""" + PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""Décision des modérateurs de publier la proposition « {subject_title} »"""


PUBLISHEDPROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » qui se trouve sous {subject_url} vient d'être publiée par les modérateurs sur la plateforme {novaideo_title}.

""" + PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Suppression de la proposition « {subject_title} »"""


PROPOSALREMOVED_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » viens d'être supprimée par les modérateurs pour le motif suivant:

« {explanation} »

""" + PORTAL_SIGNATURE


REFUSE_INVITATION_SUBJECT = u"""Refus de {user_first_name} {user_last_name} de rejoindre la plateforme {novaideo_title}"""


REFUSE_INVITATION_MESSAGE = u"""
Bonjour,

Nous vous signalons que {user_first_name} {user_last_name} a refusé votre invitation de rejoindre la plateforme {novaideo_title}.

""" + PORTAL_SIGNATURE


ACCEPT_INVITATION_SUBJECT = u"""Acceptation de {user_first_name} {user_last_name} de rejoindre la plateforme {novaideo_title}"""


ACCEPT_INVITATION_MESSAGE = u"""
Bonjour {recipient_first_name},

{user_first_name} {user_last_name} a accepté votre invitation de rejoindre la plateforme {novaideo_title}.

""" + PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""Votre nouveau mot de passe sur la plateforme {novaideo_title}"""


RESETPW_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous souhaitez avoir un nouveau votre mot de passe sur la plateforme {novaideo_title}, merci de cliquer sur l'adresse {reseturl} et de saisir votre nouveau mot de passe.

""" + PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


PREREGISTRATION_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous devez à présent cliquer sur le lien {url} pour finaliser votre inscription. Ce lien a une durée de validité de 48 heures, votre inscription doit se faire avant le {deadline_date}.
Nous nous réjouissons de vous compter parmi nos membres, et espérons que votre participation sera pour vous une expérience positive et enrichissante, dans un cadre pleinement démocratique. Bienvenue !

""" + PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


PREREGISTRATION_MOD_MESSAGE = u"""
Bonjour {recipient_first_name},

Les Vérificateurs tirés au sort lors de votre inscription ont validé la concordance entre les Informations d'Identité que vous avez saisies sur la plate-forme et celles des documents officiels d'identité dont vous leur avez transmis la copie en direct.
Nous sommes à présents sûrs que vous êtes la seule personne inscrite sous ces Informations d'Identité sur la plateforme participative {novaideo_title}, et donc que, comme tou(te)s les autres participant(e)s, vous n'avez qu'un seul compte, et contribuerez donc à respecter le principe démocratique "1 personne = 1 voix".
Vous devez à présent cliquer sur le lien {url} pour finaliser votre inscription. Ce lien a une durée de validité de 48 heures, votre inscription doit se faire avant le {deadline_date}.
Nous nous réjouissons de vous compter parmi nos membres, et espérons que votre participation sera pour vous une expérience positive et enrichissante, dans un cadre pleinement démocratique. Bienvenue !

""" + PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous avez été choisi(e) par la plateforme {novaideo_title} comme Vérificateur, afin de vérifier l'identité d'une personne qui vient de s'inscrire.

À chaque nouvelle inscription à la plateforme {novaideo_title} le système sélectionne aléatoirement trois membres existants afin de vérifier l'identité de la personne inscrite. En effet, il faut vérifier que chaque membre de la plate-forme correspond à une personne physique et une seule, et ainsi éviter qu'une même personne ne puisse voter plusieurs fois sous plusieurs identités différentes.

Pour procéder à cette vérification de l'identité de cette personne, il vous suffit de suivre les étapes suivantes:

- Vous recevrez avant le {date_end_vote} de la part de la personne qui vient de s'inscrire, et dont l'adresse de courriel est {subject_email}, un courriel comprenant une copie de document d'identité officiel
- Lorsque vous aurez reçu ce courriel, ou, si vous ne l'avez pas reçu le {date_end_vote}, connectez-vous à la plateforme à l'adresse suivante {subject_url}. Sur cette page, vous devrez décider si les informations reçues ci-dessous de cette personne lors de son inscription correspondent à celles présentes sur le document d'identité officiel dont vous aurez reçu une copie par courriel. Soyez très attentif(ve) ! Pour que vous approuviez l'inscription, TOUS les éléments doivent être strictement IDENTIQUES entre les informations reçues lors de l'inscription et celles du document d'identité officiel. Dans tous les autres cas, même avec une seule petite différence, ou si vous n'avez pas reçu la copie des documents d'identité à la date du {date_end_vote}, vous devez refuser l'inscription.

Les informations reçues de la personne lors de son inscription sont:
  Nom(s): {subject_last_name}
  Prénom(s): {subject_first_name}
  Date de naissance: {birth_date}
  Lieu de naissance: {birthplace}
  Nationalité: {citizenship}

La durée de la vérification est de {duration} jour(s), soit jusqu'au {date_end_vote}. Au-delà de cette durée, la vérification sera clôturée, et votre avis ne sera pas pris en compte. Si aucun Vérificateur n'a voté à cette date, l'inscription sera refusée.

""" + PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Nouveau contenu sur la plateforme participative {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous avez été choisi par la plateforme {novaideo_title} afin de modérer un nouveau contenu ajouté à la plateforme.

À chaque nouvel ajout à la plateforme {novaideo_title} d'un contenu (idée ou proposition), le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération {url_moderation_rules}.

Pour exercer votre rôle de Modérateur sur ce nouveau contenu, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y donner votre avis sur la conformité de ce contenu avec la Charte de Modération.

La durée de la Modération est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la Modération sera clôturée, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun Modérateur n'a voté pour Modérer ce contenu à cette date, le contenu sera accepté.

""" + PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""Nouvelle réponse sur {subject_type} « {subject_title} »"""


ALERTANSWER_MESSAGE = u"""
Bonjour {recipient_first_name},

Une nouvelle réponse a été donnée à {subject_type} « {subject_title} ».

"{comment_content}"

Vous pouvez le retrouver sous {comment_url} et lui apporter une réponse.

""" + PORTAL_SIGNATURE

ADMIN_REPORT_SUBJECT = u"""Nouvelle signalisation sur la plateforme participative {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous avez été choisi par la plateforme {novaideo_title} afin de modérer un contenu signalé sur la plateforme comme étant potentiellement non conforme à la Charte de Modération {url_moderation_rules}.

À chaque signalement d'un contenu sur la plateforme {novaideo_title} d'un contenu comme étant potentiellement non conforme à la Charte de Modération, le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération.

Pour exercer votre rôle de Modérateur sur ce contenu, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y donner votre avis sur la conformité de ce contenu avec la Charte de Modération.

La durée de la Modération est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la Modération sera clôturée, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun Modérateur n'a voté pour Modérer ce contenu à cette date, le contenu sera accepté.

""" + PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Nouvelle signalisation sur la plateforme participative {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Bonjour {recipient_first_name},

Votre contenu {subject_url} a été signalé par un Membre comme potentiellement contraire à la Charte de Modération {url_moderation_rules}.

À chaque nouvel fois qu'un contenu est signalé comme potentiellement contraire à la Charte de Modération, le système tire au sort trois membres afin que ceux-ci statuent sur la conformité de ce contenu avec la Charte de Modération .

La durée de la vérification est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la vérification sera clôturée, et vous serez informé(e) de son résultat.

""" + PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Bonjour {recipient_first_name},

Les Vérificateurs tirés au sort lors de votre inscription N'ont PAS validé la concordance entre les Informations d'Identité que vous avez saisies sur la plate-forme et celles des documents officiels d'identité dont vous leur avez transmis la copie.

Nous regrettons de devoir donc refuser votre inscription sur la plateforme {novaideo_title}, car une même personne physique pourrait s'inscrire plusieurs fois, à chaque fois avec de petites variations dans ses Informations d'Identité, et ainsi avoir plusieurs comptes, et voter plusieurs fois. Ce serait contraire au principe démocratique "1 personne = 1 voix".

""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Bonjour {recipient_first_name},

Votre inscription a été soumise à vérification de votre identité.

À chaque nouvelle inscription à la plateforme {novaideo_title} le système sélectionne aléatoirement trois membres existants afin de vérifier l'identité de la personne inscrite. En effet, il faut vérifier que chaque membre de la plate-forme correspond à une personne physique et une seule, et ainsi éviter qu'une même personne ne puisse voter plusieurs fois sous plusieurs identités différentes.

Afin que votre identité puisse être ainsi vérifiée, nous vous demandons d'adresser à chacune des personnes suivantes, dans trois courriels séparés, avant le {date_end_vote}, la copie scannée d'un document d'identité officiel. Cette copie devra faire apparaître clairement votre(vos) prénom(s), votre(vos) nom(s) de famille, votre date de naissance et votre lieu de naissance. Au-delà du {date_end_vote}, si les Vérificateurs n'ont pas reçu de copie de votre document d'identité officiel, ils ont instruction de refuser votre inscription.

Les modérateurs assignés à la vérification de votre inscription sont:
{moderators}

Vous recevrez le résultat de cette procédure de vérification d'identité à la fin de la période laissée aux Vérificateurs pour travailler, soit le {date_end_vote} au plus tard.

""" + PORTAL_SIGNATURE


REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""RAPPEL: Inscription à la plateforme participative {novaideo_title}"""


REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Bonjour {recipient_first_name},

Votre inscription a été soumise à vérification de votre identité.

À chaque nouvelle inscription à la plateforme {novaideo_title} le système sélectionne aléatoirement trois membres existants afin de vérifier l'identité de la personne inscrite. En effet, il faut vérifier que chaque membre de la plate-forme correspond à une personne physique et une seule, et ainsi éviter qu'une même personne ne puisse voter plusieurs fois sous plusieurs identités différentes.

Afin que votre identité puisse être ainsi vérifiée, nous vous demandons d'adresser à chacune des personnes suivantes, dans trois courriels séparés, avant le {date_end_vote}, la copie scannée d'un document d'identité officiel. Cette copie devra faire apparaître clairement votre(vos) prénom(s), votre(vos) nom(s) de famille, votre date de naissance et votre lieu de naissance. Au-delà du {date_end_vote}, si les Vérificateurs n'ont pas reçu de copie de votre document d'identité officiel, ils ont instruction de refuser votre inscription.

Les modérateurs assignés à la vérification de votre inscription sont:
{moderators}

Vous recevrez le résultat de cette procédure de vérification d'identité à la fin de la période laissée aux Vérificateurs pour travailler, soit le {date_end_vote} au plus tard.

Si vous avez déjà envoyé la copie de vos documents d'identité aux Vérificateurs, ne tenez pas commpte du présent courriel.

""" + PORTAL_SIGNATURE


PUBLISHEDCHALLENGE_SUBJECT = u"""Décision des modérateurs de publier le challenge « {subject_title} »"""


PUBLISHEDCHALLENGE_MESSAGE = u"""
Bonjour {recipient_first_name},

Le challenge « {subject_title} » qui se trouve sous {subject_url} vient d'être publiée par les modérateurs sur la plateforme {novaideo_title}.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Décision des modérateurs d'archiver le challenge « {subject_title} »"""


ARCHIVECHALLENGE_MESSAGE = u"""
Bonjour {recipient_first_name},

Le challenge « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante:

{explanation}

Vous pouvez retrouver votre challenge sous {subject_url}.

""" + PORTAL_SIGNATURE


PRESENTATION_CHALLENGE_SUBJECT = u"""Présentation du challenge « {subject_title} »"""


PRESENTATION_CHALLENGE_MESSAGE = u"""
Bonjour,

{my_first_name} {my_last_name} souhaite vous présenter le challenge « {subject_title} » figurant sur la plateforme {novaideo_title}. Ce challenge est accessible à l'adresse : {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


ADMIN_CONTENT_SUB_SUBJECT = u"""Nouveau contenu sur la plateforme participative {novaideo_title}"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Bonjour {recipient_first_name},

Votre contenu a été soumis à Modération.

À chaque nouvel ajout à la plateforme {novaideo_title} d'un contenu, le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération {url_moderation_rules}.

La durée de la vérification est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la vérification sera clôturée, et vous serez informé(e) de son résultat.

""" + PORTAL_SIGNATURE


ALERTCOMMENT_SUBJECT = u"""Nouveau commentaire sur {subject_type} « {subject_title} »"""


ALERTCOMMENT_MESSAGE = u"""
Bonjour {recipient_first_name},

Un nouveau commentaire a été fait sur {subject_type} « {subject_title} ».

"{comment_content}"

Vous pouvez le retrouver sous {comment_url} et lui apporter une réponse.

""" + PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Nouveau message ajouté à votre discussion avec « {subject_title} »"""


ALERTDISCUSS_MESSAGE = u"""
Bonjour {recipient_first_name},

Un nouveau message a été ajouté à votre discussion avec « {subject_title} ».

"{comment_content}"

Vous pouvez le retrouver sous {comment_url} et lui apporter une réponse.

""" + PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Une personne a donné une réponse à un commentaire sur {subject_type} « {subject_title} »"""


ALERTRESPONS_MESSAGE = u"""
Bonjour {recipient_first_name},

Une personne a donné une réponse à un commentaire sur {subject_type} « {subject_title} » qui se trouve sous {comment_url}.

"{comment_content}"

""" + PORTAL_SIGNATURE


NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Inscription newsletter"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Bonjour {first_name} {last_name},

Vous êtes maintenant abonné à la newsletter {newsletter_title}.

""" + PORTAL_SIGNATURE

NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Désinscription de la newsletter"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Bonjour {first_name} {last_name},

Vous êtes maintenant désabonné de la newsletter {newsletter_title}.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Demande de démission depuis votre compte sur la plate-forme {novaideo_title}"""

QUIT_REQUEST_MESSAGE = u"""
Cher(e) {recipient_first_name} {recipient_last_name},

Nous avons reçu sur votre compte de la plate-forme {novaideo_title} une demande de démission.
Si vous avez bien demandé à démissionner de la plate-forme, cliquez sur le lien de confirmation suivant: {url}, avant la date {deadline_date}.

ATTENTION: cette action est IRRÉVERSIBLE. Si vous cliquez sur ce lien, vous n'aurez plus accès à la plate-forme, votre compte sera détruit, et tous les contenus liés à votre compte seront irréversiblement attribués à un auteur anonyme.
Vous ne pourrez plus vous réinscrire sur la plate-forme, en créant un nouveau compte vierge, avant une durée égale à {tquarantaine} jours.

Si vous n'avez pas demandé à quitter la plate-forme, ignorez ce courriel, et votre compte sera maintenu actif.
Nous vous recommandons néanmoins de changer votre mot de passe pour éviter que votre compte ne soit piraté.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Votre démission de la plate-forme de démocratie en ligne {novaideo_title} a été prise en compte"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Cher(e) {recipient_first_name} {recipient_last_name},

Vous avez souhaité démissionner de la plate-forme de démocratie en ligne {novaideo_title}. Nous le regrettons bien sûr, mais respectons votre choix. Nous vous informons par la présente que:
* votre compte a été désactivé. Vous ne recevrez à l'avenir plus qu'un seul message de notre part (voir ci-dessous)
* tous les contenus de votre compte ont été irréversiblement attribués à un auteur Anonyme
* les Informations d'Identité que vous nous avez transmises lors de votre inscription (Prénoms, Noms, date et lieu de naissance) et votre adresse de courriel seront conservées pendant {tquarantaine} jours, afin d'éviter que vous ne puissiez vous réinscrire au cours de cette période. L'objectif est d'éviter que les personnes ayant eu un comportement inapproprié sur la plate-forme (et ayant par conséquent une mauvaise réputation), ne reviennent immédiatement sous un nouveau pseudonyme et avec une réputation vierge.
* au terme de cette période, à savoir le {date_tquarantaine}, vous recevrez de notre part un courriel vous informant que vos Informations d'Identité et votre adresse de courriel ont été définitivement effacées de notre base de données.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""Vos Données d'Identité et votre adresse de courriel ont été définitivement effacées de la base de données de la plate-form {novaideo_title} !"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Cher(e) {recipient_first_name} {recipient_last_name},

Aujourd'hui, vos Informations d'Identité (Prénoms, Noms, date et lieu de naissance) et votre adresse de courriel ont été définitivement effacées de notre base de données. Vous ne recevrez plus aucun courriel de notre part.

""" + PORTAL_SIGNATURE


FIRST_INVITATION = {
    'subject': FIRST_INVITATION_SUBJECT,
    'template': FIRST_INVITATION_MESSAGE
}


FIRST_INVITATION_SMS = {
    'subject': FIRST_INVITATION_SUBJECT,
    'template': FIRST_INVITATION_SMS_MESSAGE
}

mail_locale = 'fr'

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
