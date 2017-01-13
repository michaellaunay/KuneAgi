# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

from novaideo import _

""" The contents of e-mails"""

PORTAL_SIGNATURE = """Cordialement,
                                                                                
La Plateforme {novaideo_title}
"""

PORTAL_PRESENTATION = u"""{novaideo_title} est une plateforme participative qui permet à tout membre d'initier des idées pouvant être utilisées dans des propositions améliorées par des groupes de travail. Une fois améliorées, ces propositions peuvent être soumises à l'appréciation des membres et faire l'objet d'une décision d'un comité d'examen.

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

""" +  PORTAL_PRESENTATION + PORTAL_SIGNATURE


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

"""+ PORTAL_SIGNATURE


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

"""+ PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} « {subject_title} » qui fait partie de vos favoris vient de changer d'état"""


CONTENTMODIFIEF_MESSAGE = u"""
Bonjour {recipient_first_name},

{subject_type} « {subject_title} » qui fait partie de vos favoris vient de passer de l'état {state_source} à l'état {state_target}. Vous pouvez la consulter sous {subject_url}.

"""+ PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Décision des modérateurs d'archiver l'idée « {subject_title} »"""


ARCHIVEIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

L'idée « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante: 

{explanation}

Vous pouvez retrouver votre idée sous {subject_url}.

"""+ PORTAL_SIGNATURE

ARCHIVEPROPOSAL_SUBJECT = u"""Décision des modérateurs d'archiver la proposition « {subject_title} »"""


ARCHIVEPROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » vient d'être archivée par les modérateurs pour la raison suivante: 

{explanation}

Vous pouvez retrouver votre proposition sous {subject_url}.

"""+ PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Avis du Comité d'examen sur la proposition « {subject_title} »"""


ALERTOPINION_MESSAGE = u"""
Bonjour {recipient_first_name},

Le Comité d'examen a émis un avis « {opinion} » sur la proposition « {subject_title} » avec l'explication suivante : « {explanation} ».

"""+ PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u"""Avis d'un Examinateur sur l'idée « {subject_title} »"""


ALERTOPINIONIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

Un Examinateur a émis un avis « {opinion} » sur l'idée « {subject_title} » avec l'explication suivante : « {explanation} ».

"""+ PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Décision des modérateurs de publier l'idée « {subject_title} »"""


PUBLISHEDIDEA_MESSAGE = u"""
Bonjour {recipient_first_name},

L'idée « {subject_title} » qui se trouve sous {subject_url} vient d'être publiée par les modérateurs sur la plateforme {novaideo_title}. Cette idée peut maintenant être utilisée par n'importe quel membre de la plateforme pour une proposition.

"""+ PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""Décision des modérateurs de publier la proposition « {subject_title} »"""


PUBLISHEDPROPOSAL_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » qui se trouve sous {subject_url} vient d'être publiée par les modérateurs sur la plateforme {novaideo_title}.

"""+ PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Suppression de la proposition « {subject_title} »"""


PROPOSALREMOVED_MESSAGE = u"""
Bonjour {recipient_first_name},

La proposition « {subject_title} » viens d'être supprimée par les modérateurs pour le motif suivant:

« {explanation} »

"""+ PORTAL_SIGNATURE 


REFUSE_INVITATION_SUBJECT = u"""Refus de {user_first_name} {user_last_name} de rejoindre la plateforme {novaideo_title}"""


REFUSE_INVITATION_MESSAGE = u"""
Bonjour,

Nous vous signalons que {user_first_name} {user_last_name} a refusé votre invitation de rejoindre la plateforme {novaideo_title}.

"""+ PORTAL_SIGNATURE 


ACCEPT_INVITATION_SUBJECT = u"""Acceptation de {user_first_name} {user_last_name} de rejoindre la plateforme {novaideo_title}"""


ACCEPT_INVITATION_MESSAGE = u"""
Bonjour {recipient_first_name},

{user_first_name} {user_last_name} a accepté votre invitation de rejoindre la plateforme {novaideo_title}.

"""+ PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""Votre nouveau mot de passe sur la plateforme {novaideo_title}"""


RESETPW_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous souhaitez avoir un nouveau votre mot de passe sur la plateforme {novaideo_title}, merci de cliquer sur l'adresse {reseturl} et de saisir votre nouveau mot de passe.

"""+ PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


PREREGISTRATION_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous devez à présent cliquer sur le lien {url} pour finaliser votre inscription. Ce lien a une durée de validité de 48 heures, votre inscription doit se faire avant le {deadline_date}.
Nous nous réjouissons de vous compter parmi nos membres, et espérons que votre participation sera pour vous une expérience positive et enrichissante, dans un cadre pleinement démocratique. Bienvenue !

"""+ PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


PREREGISTRATION_MOD_MESSAGE = u"""
Bonjour {recipient_first_name},

Les Vérificateurs tirés au sort lors de votre inscription ont validé la concordance entre les Informations d'Identité que vous avez saisies sur la plate-forme et celles des documents officiels d'identité dont vous leur avez transmis la copie en direct.
Nous sommes à présents sûrs que vous êtes la seule personne inscrite sous ces Informations d'Identité sur la plateforme participative {novaideo_title}, et donc que, comme tou(te)s les autres participant(e)s, vous n'avez qu'un seul compte, et contribuerez donc à respecter le principe démocratique "1 personne = 1 voix".
Vous devez à présent cliquer sur le lien {url} pour finaliser votre inscription. Ce lien a une durée de validité de 48 heures, votre inscription doit se faire avant le {deadline_date}.
Nous nous réjouissons de vous compter parmi nos membres, et espérons que votre participation sera pour vous une expérience positive et enrichissante, dans un cadre pleinement démocratique. Bienvenue !

"""+ PORTAL_SIGNATURE


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

La durée de la vérification est de {duration} jour(s), soit jusqu'au {date_end_vote}. Au-delà de cette durée, la vérification sera clôturée, et votre avis ne sera pas pris en compte. Si aucun Vérificateur n'a voté à cette date, l'inscription sera refusée. 

"""+ PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Nouveau contenu sur la plateforme participative {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous avez été choisi par la plateforme {novaideo_title} afin de modérer un nouveau contenu ajouté à la plateforme.

À chaque nouvel ajout à la plateforme {novaideo_title} d'un contenu (idée ou proposition), le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération {url_moderation_rules}.

Pour exercer votre rôle de Modérateur sur ce nouveau contenu, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y donner votre avis sur la conformité de ce contenu avec la Charte de Modération.

La durée de la Modération est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la Modération sera clôturée, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun Modérateur n'a voté pour Modérer ce contenu à cette date, le contenu sera accepté.

"""+ PORTAL_SIGNATURE


ADMIN_REPORT_SUBJECT = u"""Nouvelle signalisation sur la plateforme participative {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Bonjour {recipient_first_name},

Vous avez été choisi par la plateforme {novaideo_title} afin de modérer un contenu signalé sur la plateforme comme étant potentiellement non conforme à la Charte de Modération {url_moderation_rules}.

À chaque signalement d'un contenu sur la plateforme {novaideo_title} d'un contenu comme étant potentiellement non conforme à la Charte de Modération, le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération.

Pour exercer votre rôle de Modérateur sur ce contenu, il vous suffit de vous connecter à la plateforme à l'adresse suivante {subject_url} et d'y donner votre avis sur la conformité de ce contenu avec la Charte de Modération.

La durée de la Modération est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la Modération sera clôturée, et votre vote ne sera plus pris en compte. Attention ! Par défaut, si aucun Modérateur n'a voté pour Modérer ce contenu à cette date, le contenu sera accepté.

"""+ PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Nouvelle signalisation sur la plateforme participative {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Bonjour {recipient_first_name},

Votre contenu {subject_url} a été signalé par un Membre comme potentiellement contraire à la Charte de Modération {url_moderation_rules}.

À chaque nouvel fois qu'un contenu est signalé comme potentiellement contraire à la Charte de Modération, le système tire au sort trois membres afin que ceux-ci statuent sur la conformité de ce contenu avec la Charte de Modération .

La durée de la vérification est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la vérification sera clôturée, et vous serez informé(e) de son résultat.

"""+ PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Bonjour {recipient_first_name},

Les Vérificateurs tirés au sort lors de votre inscription N'ont PAS validé la concordance entre les Informations d'Identité que vous avez saisies sur la plate-forme et celles des documents officiels d'identité dont vous leur avez transmis la copie.

Nous regrettons de devoir donc refuser votre inscription sur la plateforme {novaideo_title}, car une même personne physique pourrait s'inscrire plusieurs fois, à chaque fois avec de petites variations dans ses Informations d'Identité, et ainsi avoir plusieurs comptes, et voter plusieurs fois. Ce serait contraire au principe démocratique "1 personne = 1 voix". 

"""+ PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Inscription à la plateforme participative {novaideo_title}"""


ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Bonjour {recipient_first_name},

Votre inscription a été soumise à vérification de votre identité.

À chaque nouvelle inscription à la plateforme {novaideo_title} le système sélectionne aléatoirement trois membres existants afin de vérifier l'identité de la personne inscrite. En effet, il faut vérifier que chaque membre de la plate-forme correspond à une personne physique et une seule, et ainsi éviter qu'une même personne ne puisse voter plusieurs fois sous plusieurs identités différentes.

Afin que votre identité puisse être ainsi vérifiée, nous vous demandons d'adresser à chacune des personnes suivantes, dans trois courriels séparés, avant le {date_end_vote}, la copie scannée d'un document d'identité officiel. Cette copie devra faire apparaître clairement votre(vos) prénom(s), votre(vos) nom(s) de famille, votre date de naissance et votre lieu de naissance. Au-delà du {date_end_vote}, si les Vérificateurs n'ont pas reçu de copie de votre document d'identité officiel, ils ont instruction de refuser votre inscription.

Les modérateurs assignés à la vérification de votre inscription sont:
{moderators}

Vous recevrez le résultat de cette procédure de vérification d'identité à la fin de la période laissée aux Vérificateurs pour travailler, soit le {date_end_vote} au plus tard.

"""+ PORTAL_SIGNATURE


ADMIN_CONTENT_SUB_SUBJECT = u"""Nouveau contenu sur la plateforme participative {novaideo_title}"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Bonjour {recipient_first_name},

Votre contenu a été soumis à Modération.

À chaque nouvel ajout à la plateforme {novaideo_title} d'un contenu, le système tire au sort trois membres afin que ceux-ci vérifient la conformité de ce contenu avec la Charte de Modération {url_moderation_rules}.

La durée de la vérification est de {duration} jour(s). Au-delà de la date du {date_end_vote}, la vérification sera clôturée, et vous serez informé(e) de son résultat.

"""+ PORTAL_SIGNATURE


MODERATOR_DATA = u"""
Modérateur {index}:
  Email: {subject_email}
"""

ALERTCOMMENT_SUBJECT = u"""Nouveau commentaire sur {subject_type} « {subject_title} »"""


ALERTCOMMENT_MESSAGE = u"""
Bonjour {recipient_first_name},

Un nouveau commentaire a été fait sur {subject_type} « {subject_title} ».

"{comment_content}"

Vous pouvez le retrouver sous {comment_url} et lui apporter une réponse.

"""+ PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Nouveau message ajouté à votre discussion avec « {subject_title} »"""


ALERTDISCUSS_MESSAGE = u"""
Bonjour {recipient_first_name},

Un nouveau message a été ajouté à votre discussion avec « {subject_title} ».

"{comment_content}"

Vous pouvez le retrouver sous {comment_url} et lui apporter une réponse.

"""+ PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Une personne a donné une réponse à un commentaire sur {subject_type} « {subject_title} »"""


ALERTRESPONS_MESSAGE = u"""
Bonjour {recipient_first_name},

Une personne a donné une réponse à un commentaire sur {subject_type} « {subject_title} » qui se trouve sous {comment_url}.

"{comment_content}"

"""+ PORTAL_SIGNATURE


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


DEFAULT_SITE_MAILS = {
    'invitation': {
              'title': _("Invitation"),
              'subject': INVITATION_SUBJECT,
              'template': INVITATION_MESSAGE
    },
    'refuse_invitation': {
              'title': _("Refuse the invitation"),
              'subject': REFUSE_INVITATION_SUBJECT,
              'template': REFUSE_INVITATION_MESSAGE
    },
    'accept_invitation': {
              'title': _("Accept the invitation"),
              'subject': ACCEPT_INVITATION_SUBJECT,
              'template': ACCEPT_INVITATION_MESSAGE
    },
    'reset_password': {
              'title': _("Reset the password"),
              'subject': RESETPW_SUBJECT,
              'template': RESETPW_MESSAGE
    },
    'registration_confiramtion': {
              'title': _("Registration confirmation"),
              'subject': CONFIRMATION_SUBJECT,
              'template': CONFIRMATION_MESSAGE
    },
    'preregistration': {
              'title': _("Pre-registration of users"),
              'subject': PREREGISTRATION_SUBJECT,
              'template': PREREGISTRATION_MESSAGE
    },
    'preregistration_moderation': {
              'title': _("Pre-registration of users with moderation"),
              'subject': PREREGISTRATION_MOD_SUBJECT,
              'template': PREREGISTRATION_MOD_MESSAGE
    },

    'presentation_idea': {
              'title': _("Presentation of an idea"),
              'subject': PRESENTATION_IDEA_SUBJECT,
              'template': PRESENTATION_IDEA_MESSAGE
    },

    'presentation_proposal': {
              'title': _("Presentation of a proposal"),
              'subject': PRESENTATION_PROPOSAL_SUBJECT,
              'template': PRESENTATION_PROPOSAL_MESSAGE
    },
    'presentation_amendment': {
              'title': _('Presentation of an amendment'),
              'subject': PRESENTATION_AMENDMENT_SUBJECT,
              'template': PRESENTATION_AMENDMENT_MESSAGE
    },
    'first_start_work': {
              'title': _('Start of the improvement cycle'),
              'subject': AMENDABLE_FIRST_SUBJECT,
              'template': AMENDABLE_FIRST_MESSAGE
    },
    'start_work': {
              'title': _('Start of the improvement cycle'),
              'subject': AMENDABLE_SUBJECT,
              'template': AMENDABLE_MESSAGE
    },
    'alert_amendment': {
              'title': _("Inactivity alert"),
              'subject': ALERT_SUBJECT,
              'template': ALERT_MESSAGE
    },
    'alert_end': {
              'title': _("End of the improvement cycle"),
              'subject': ALERT_END_SUBJECT,
              'template': ALERT_END_MESSAGE
    },
    'vote_amendment_result': {
              'title': _("Result of the ballot (amendments)"),
              'subject': RESULT_VOTE_AMENDMENT_SUBJECT,
              'template': RESULT_VOTE_AMENDMENT_MESSAGE
    },
    'publish_proposal': {
              'title': _("Publication of the proposal"),
              'subject': PUBLISHPROPOSAL_SUBJECT,
              'template': PUBLISHPROPOSAL_MESSAGE
    },
    'start_vote_publishing': {
              'title': _("Start of the ballot (publication of the proposal)"),
              'subject': VOTINGPUBLICATION_SUBJECT,
              'template': VOTINGPUBLICATION_MESSAGE
    },
    'start_vote_amendments': {
              'title': _("Start of the ballot (amendments)"),
              'subject': VOTINGAMENDMENTS_SUBJECT,
              'template': VOTINGAMENDMENTS_MESSAGE
    },
    'withdeaw': {
              'title': _("Withdraw"),
              'subject': WITHDRAW_SUBJECT,
              'template': WITHDRAW_MESSAGE
    },
    'wg_wating_list_participation': {
              'title': _("Automatic addition of a participant in the working group that was on the waiting list"),
              'subject': PARTICIPATE_WL_SUBJECT,
              'template': PARTICIPATE_WL_MESSAGE
    },
    'wg_participation': {
              'title': _("Participation in the working group"),
              'subject': PARTICIPATE_SUBJECT,
              'template': PARTICIPATE_MESSAGE
    },
    'wg_resign': {
              'title': _("Resignation from the working group"),
              'subject': RESIGN_SUBJECT,
              'template': RESIGN_MESSAGE
    },
    'wg_exclude': {
              'title': _("Exclusion from the working group"),
              'subject': EXCLUDE_SUBJECT,
              'template': EXCLUDE_MESSAGE
    },
    'wating_list': {
              'title': _("Registration on the waiting list"),
              'subject': WATINGLIST_SUBJECT,
              'template': WATINGLIST_MESSAGE
    },
    'alert_new_content': {
              'title': _("Alert (new content)"),
              'subject': NEWCONTENT_SUBJECT,
              'template': NEWCONTENT_MESSAGE
    },
    'alert_content_modified': {
              'title': _("Alert (content modified)"),
              'subject': CONTENTMODIFIEF_SUBJECT,
              'template': CONTENTMODIFIEF_MESSAGE
    },
    'archive_idea_decision': {
              'title': _("Moderation: Archive the idea"),
              'subject': ARCHIVEIDEA_SUBJECT,
              'template': ARCHIVEIDEA_MESSAGE
    },
    'opinion_proposal': {
              'title': _("Moderation: Opinion on the proposal"),
              'subject': ALERTOPINION_SUBJECT,
              'template': ALERTOPINION_MESSAGE
    },
    'opinion_idea': {
              'title': _("Moderation: Opinion on the idea"),
              'subject': ALERTOPINIONIDEA_SUBJECT,
              'template': ALERTOPINIONIDEA_MESSAGE
    },
    'publish_idea_decision': {
              'title': _("Moderation: Publish the idea"),
              'subject': PUBLISHEDIDEA_SUBJECT,
              'template': PUBLISHEDIDEA_MESSAGE
    },
    'archive_proposal_decision': {
              'title': _("Moderation: Archive the proposal"),
              'subject': ARCHIVEPROPOSAL_SUBJECT,
              'template': ARCHIVEPROPOSAL_MESSAGE
    },
    'publish_proposal_decision': {
              'title': _("Moderation: Publish the proposal"),
              'subject': PUBLISHEDPROPOSAL_SUBJECT,
              'template': PUBLISHEDPROPOSAL_MESSAGE
    },
    'delete_proposal': {
              'title': _("Moderation: Delete the proposal"),
              'subject': PROPOSALREMOVED_SUBJECT,
              'template': PROPOSALREMOVED_MESSAGE
    },
    'alert_comment': {
              'title': _("Warning: new comment"),
              'subject': ALERTCOMMENT_SUBJECT,
              'template': ALERTCOMMENT_MESSAGE
    },
    'alert_discuss': {
              'title': _("Warning: new discussion"),
              'subject': ALERTDISCUSS_SUBJECT,
              'template': ALERTDISCUSS_MESSAGE
    },
    'alert_respons': {
              'title': _("Alert: answer"),
              'subject': ALERTRESPONS_SUBJECT,
              'template': ALERTRESPONS_MESSAGE
    },
    'newsletter_subscription': {
              'title': _("Subscription to the newsletter"),
              'subject': NEWSLETTER_SUBSCRIPTION_SUBJECT,
              'template': NEWSLETTER_SUBSCRIPTION_MESSAGE
    },
    'newsletter_unsubscription': {
              'title': _("Unsubscription from the newsletter"),
              'subject': NEWSLETTER_UNSUBSCRIPTION_SUBJECT,
              'template': NEWSLETTER_UNSUBSCRIPTION_MESSAGE
    },
    'moderate_preregistration': {
              'title': _("New registration"),
              'subject': ADMIN_PREREGISTRATION_SUBJECT,
              'template': ADMIN_PREREGISTRATION_MESSAGE
    },
    'moderate_preregistration_refused': {
              'title': _("Registration refused"),
              'subject': ADMIN_PREREGISTRATION_REF_SUBJECT,
              'template': ADMIN_PREREGISTRATION_REF_MESSAGE
    },
    'preregistration_submit': {
              'title': _("Registration submission"),
              'subject': ADMIN_PREREGISTRATION_SUB_SUBJECT,
              'template': ADMIN_PREREGISTRATION_SUB_MESSAGE
    },
    'close_proposal': {
              'title': _("Close the proposal"),
              'subject': SYSTEM_CLOSE_PROPOSAL_SUBJECT,
              'template': SYSTEM_CLOSE_PROPOSAL_MESSAGE
    },
    'moderate_content': {
              'title': _("New content to moderate"),
              'subject': ADMIN_CONTENT_SUBJECT,
              'template': ADMIN_CONTENT_MESSAGE
    },
    'content_submit': {
              'title': _("Submission of a content"),
              'subject': ADMIN_CONTENT_SUB_SUBJECT,
              'template': ADMIN_CONTENT_SUB_MESSAGE
    },
    'moderate_report': {
              'title': _("Report a content as potentially contrary to the Moderation rules"),
              'subject': ADMIN_REPORT_SUBJECT,
              'template': ADMIN_REPORT_MESSAGE
    },
    'alert_report': {
              'title': _("Alert the author of the reported content"),
              'subject': AUTHOR_REPORT_SUBJECT,
              'template': AUTHOR_REPORT_MESSAGE
    },
    'exclude_participant': {
              'title': _("Exclude a participant"),
              'subject': EXCLUDE_PARTICIPANT_SUBJECT,
              'template': EXCLUDE_PARTICIPANT_MESSAGE
    },
    'new_participant': {
              'title': _("New participation"),
              'subject': NEW_PARTICIPANT_SUBJECT,
              'template': NEW_PARTICIPANT_MESSAGE
    },
    'participation_submission': {
              'title': _("New participation"),
              'subject': PARTICIPATE_SUB_SUBJECT,
              'template': PARTICIPATE_SUB_MESSAGE
    },
    'member_notation': {
              'title': _("Give a mark to a member's cooperative behaviour"),
              'subject': NOTING_MEMBER_SUBJECT,
              'template': NOTING_MEMBER_MESSAGE
    },
    'member_notation_excluded': {
              'title': _("Give a mark to a participant's cooperative behaviour"),
              'subject': NOTING_PARTICIPANT_SUBJECT,
              'template': NOTING_PARTICIPANT_MESSAGE
    },
    'members_notation': {
              'title': _("Give a mark to the cooperative behaviour of members"),
              'subject': NOTING_MEMBERS_SUBJECT,
              'template': NOTING_MEMBERS_MESSAGE
    }
}
