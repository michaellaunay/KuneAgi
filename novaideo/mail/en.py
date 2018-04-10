# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, *

from . import add_mail_template

""" The contents of e-mails"""

PORTAL_SIGNATURE = """Kind regards,

The {novaideo_title} platform.
"""

PORTAL_PRESENTATION = u"""{novaideo_title} is an on-line democracy platform with which any member can initiate ideas for public policy. These ideas can then be improved in spontaneous working groups as public policy proposals. Once improved and adopted by the working group, these public policy proposals are subject to the appreciation of all members.

"""

INVITATION_SUBJECT = u"""Invitation to join the {novaideo_title} on-line democracy platform"""

INVITATION_MESSAGE = u"""
Dear,

{recipient_first_name} your are invited to join the the {novaideo_title} on-line democracy platform as {roles}.

In order to validate your invitation, you must click on the following link {invitation_url} and follow the instructions.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PRESENTATION_IDEA_SUBJECT = u"""Presentation of the idea "{subject_title}"""


PRESENTATION_IDEA_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you the idea "{subject_title}" on the {novaideo_title} platform. You can access this idea at: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Confirmation of your registration on the {novaideo_title} on-line democracy platform"""

CONFIRMATION_MESSAGE = u"""
Welcome on the {novaideo_title} platform!

We confirm hereby that you are registered on the {novaideo_title} on-line democracy platform.

Share your ideas with us by connecting to the {login_url} address!

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PRESENTATION_PROPOSAL_SUBJECT = u"""Presentation of the proposal "{subject_title}"""


PRESENTATION_PROPOSAL_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you the proposal "{subject_title}" on the {novaideo_title} platform. You can access this proposal at: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PRESENTATION_AMENDMENT_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you the amendment "{subject_title}" on the {novaideo_title} platform. You can access this amendment at: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PRESENTATION_AMENDMENT_SUBJECT = u"""« {subject_title} »"""


PRESENTATION_QUESTION_SUBJECT = u"""Presentation of the question "{subject_title}"""


PRESENTATION_QUESTION_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you the question "{subject_title}" on the {novaideo_title} platform. You can access this question at: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE

PRESENTATION_ANSWER_SUBJECT = u"""Presentation of an answer to the question "{subject_title}"""


PRESENTATION_ANSWER_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you an answer to the question "{subject_title}" on the {novaideo_title} platform. You can access this answer at: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE

AMENDABLE_FIRST_SUBJECT = u"""Start of the improvement cycle of the proposal "{subject_title}"""

# Le chiffre trois est un paramètre de l'application. Il ne devrait pas apparaître en dur dans le code.
AMENDABLE_FIRST_MESSAGE = u"""
Dear {recipient_first_name},

You are now three participants in the working group on the proposal "{subject_title}", which is accessible at {subject_url}. You can start improving it.

Each participant can suggest improvements, which the other participants can either accept, or refuse. Once the improvement cycle is finished, all participants vote, either to continue improving the proposal, or to submit it to the assessment of the members of the platform.

The improvement cycle ends on {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Start of the improvement cycle of the proposal "{subject_title}"""


AMENDABLE_MESSAGE = u"""
Dear {recipient_first_name},

The working group on the proposal "{subject_title}", which is accessible at {subject_url}, voted in majority to continue improving it.

Each participant can suggest improvements, which the other participants can either accept, or refuse. Once the improvement cycle is finished, all participants vote, either to continue improving the proposal, or to submit it to the assessment of the members of the platform.

The improvement cycle ends on {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""End of the improvement cycle of the proposal "{subject_title}" with no improvemt"""

ALERT_MESSAGE = u"""
Dear {recipient_first_name},

While the improvement cycle is finished, no improvement was brought to the proposal "{subject_title}", which can be accessed at {subject_url}. You will need to vote on whether you want to submit the proposal as it is, or to start again a new improvement cycle.  

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERT_END_SUBJECT = u"""Last improvements before the end of the end of the improvement cycle of the proposal "{subject_title}"""

ALERT_END_MESSAGE = u"""
Dear {recipient_first_name},

The improvement cycle of the proposal "{subject_title}", which can be accessed at {subject_url}, is almost to an end. You can still improve it, before the working group votes to submit the proposal as it is or to start again a new improvement cycle.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
RESULT_VOTE_AMENDMENT_SUBJECT = u"""The results of the vote on the amendements related to the proposal "{subject_title}"""

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>
Dear {recipient_first_name},

{message_result}
</div>
""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PUBLISHPROPOSAL_SUBJECT = u"""Decision to submit the proposal "{subject_title}" to the assessment of the members of the platform"""

PUBLISHPROPOSAL_MESSAGE = u"""
Dear {recipient_first_name},

The working group on the proposal "{subject_title}", which can be accessed at {subject_url}, voted in majority to submit the proposal to the assessment of the other members of the platform.

Every member of the platform can now suppport or oppose the proposal.

""" + PORTAL_SIGNATURE

# Bogue dans la version FR: le "à l'appréciation des membres de la plateforme" est de trop
# J'ai repris la formulation de l'état "En attente d'atteinte du quorum" plutôt que "Ouverte à un groupe de travail"
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Decision to close the proposal "{subject_title}"""

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Dear {recipient_first_name},

The working group on the proposal "{subject_title}", which can be accessed at {subject_url}, has not been active over several cycles, each lasting more than a week.

For this reason, the working group has been dissolved, and the proposal is now back to the stage "expecting the working group to reach the quorum".

""" + PORTAL_SIGNATURE

# La durée de 24 heures pour voter est-elle inscrite en dur dans le code? Si c'est le cas, c'est beaucoup trop court
# ou alors cela demanderait à être paramétré par l'administrateur ou par les membres du groupe eux-mêmes sur des durées
# plus longues. La décision par défaut en l'absence de vote exprimé ne suffit pas: elle ouvre la voie à une décision 
# unilatérale d'un seul participant.
VOTINGPUBLICATION_SUBJECT = u"""Start of the vote to improve the proposal "{subject_title}" or to submit it to the assessment of the members of the platform"""

VOTINGPUBLICATION_MESSAGE = u"""
Dear {recipient_first_name},

The improvement cycle of the proposal "{subject_title}", which can be accessed at {subject_url}, is now finished. You are invited to participate in the vote to decide whether the proposal should be further improved, or whether it should be submitted to the assessment of the members of the platform.

You have 24 hours to vote. After this period of time, the ballots will be counted, and the outcome will be decided by the majority of expressed votes. If no ballot is cast, a new improvement cycle starts for one week.

""" + PORTAL_SIGNATURE

#Ici, il faudrait donner la date de fin du vote
VOTINGAMENDMENTS_SUBJECT = u"""Start of the votes on the amendments to the proposal "{subject_title}"""

VOTINGAMENDMENTS_MESSAGE = u"""
Dear {recipient_first_name},

The votes on the amendments to the proposal "{subject_title}", which can be accessed at {subject_url}, have started. You are kindly requested to  participate in the votes.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
WITHDRAW_SUBJECT = u"""Withdrawal from the waiting list of the working group related to the proposal "{subject_title}"""

WITHDRAW_MESSAGE = u"""
Dear {recipient_first_name},

You are not any more on the waiting list of the working group related to the proposal {subject_title}, which can be accessed at {subject_url}, following your decision to withdraw from this waiting list.

You can attempt at any time to join again the working group related to the proposal, if it still is being improved.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""Participation in the working group related to the proposal "{subject_title}"""

PARTICIPATE_WL_MESSAGE = u"""
Dear {recipient_first_name},

A participant has left the working group related to the proposal {subject_title}, which can be accessed at {subject_url}. His/her departure has opened a free place for you in the working group. You are now part of the working group related to the proposal {subject_title}.

As a participant in the working group, you can improve the proposal, and at the end of the improvement cycle, vote on whether to continue improving it or to submit it to the assessment of the members of the platform.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Your participation in the working group related to the proposal "{subject_title}"""

PARTICIPATE_MESSAGE = u"""
Dear {recipient_first_name},

You are part of the working group related to the proposal {subject_title}, which can be accessed at {subject_url}.

As a participant in the working group, you can improve the proposal, and at the end of the improvement cycle, vote on whether to continue improving it or to submit it to the assessment of the members of the platform.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PARTICIPATE_SUB_SUBJECT = u"""Your request to participate in the working group related to the proposal "{subject_title} is being submitted to the participants in the group"""

#Dans le message en Français, il est fait état de "vérification": cela me paraît être un copier-coller rapide. 
#Je proposerais "inclusion dans le groupe"
PARTICIPATE_SUB_MESSAGE = u"""

Dear {recipient_first_name},

Your request to participate in the working group related to the proposal "{subject_title}", which can be accessed at {subject_url}, has been submitted to the participants in the group.

At each request to participate, the participants in the groupe decide upon the acceptance or not of the request.

The decision process lasts {duration} day(s). On {date_end_vote} at the latest, the ballot on including you or not in the group will be closed, and you will be informed of the result.

"""+ PORTAL_SIGNATURE

#Dans le texte en Français, on dit "Vous pourrez à tout moment le rejoindre de nouveau"
#Je préférerais: "Vous pourrez à tout moment demander de nouveau à le rejoindre"

#Le chiffre d'un maximum de cinq groupes de travail est inscrit en dur dans le code, alors que c'est un
#paramètre défini par l'administrateur
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
RESIGN_SUBJECT = u"""Your departure from the working group related to the proposal "{subject_title}"""

RESIGN_MESSAGE = u"""
Dear {recipient_first_name},

We confirm you hereby that you are not any more a participant in the working group related to the proposal "{subject_title}", which can be accessed at {subject_url}.

At any time, you can request again to participate in it, if however you are not already a participant, or on the waiting list, of a total of five working groups, which is the maximum number of working groups that a given member is allowed to participate in or be on the waiting list of.

""" + PORTAL_SIGNATURE

# J'ai introduit l'idée qu'une nouvelle candidature à ce même groupe n'est possible au plus tôt qu'à une date donnée
# pour suivre la logique du ticket "Durée de validité des décisions" - mais il faut écrire le code pour la #DATE
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
EXCLUDE_SUBJECT = u"""Exclusion from working group related to the proposal "{subject_title}"""

EXCLUDE_MESSAGE = u"""
Dear {recipient_first_name},

The participants in the working group have decided to exclude you from the working group. You are not any more a participant in the working group related to the proposal "{subject_title}", which can be accessed at {subject_url}.

At any time, you can request to participate in a new working group, if however you are not already a participant, or on the waiting list, of a total of five working groups, which is the maximum number of working groups that a given member is allowed to participate in or be on the waiting list of.

You will be again allowed to request being member of this working group, related to the proposal "{subject_title}, on #DATE at the earliest.


""" + PORTAL_SIGNATURE

# Dans le texte Français, ajouter à la fin: "Il ne sera pas possible de demander à nouveau l'exclusion de
# {user_first_name} {user_last_name} avant le #DATE" (définie par le ticket "Durée de validité des décisions"
EXCLUDE_PARTICIPANT_SUBJECT = u"""You are invited to vote on the request to exclude {user_first_name} {user_last_name} out of the du Working Group related to the proposal "{subject_title}"""

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Dear {recipient_first_name},

{user_first_name} {user_last_name} has just been the purpose of a request to exclude him/her out of the Working Group related to the proposal "{subject_title}".

You are invited to vote on this exlcusion request. To do so, you just need to connect to the platform at the following address {subject_url}, and to vote on the request to exclude {user_first_name} {user_last_name} out of the Working Group related to the proposal "{subject_title}".

The ballot process lasts {duration} day(s). After the {date_end_vote}, the ballot process will be closed, and your vote willl not be taken into account. 

Beware! By default, if no participant has voted at that date on the exclusion of {user_first_name} {user_last_name} out of the Working Group related to the proposal "{subject_title}", {user_first_name} {user_last_name} will be maintainted in the working group. It will not be allowed to request to exclude {user_first_name} {user_last_name} out of the working group before #DATE at the earliest.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""You are invited to give a mark to the cooperative behaviour of {user_first_name}"""

NOTING_MEMBER_MESSAGE = u"""
Dear {recipient_first_name},

{user_title} has just left the working group, because s/he quitted, or because s/he was excluded out of it. 

Each time a participant leaves a working group, the platform request the remaining participants in the working group to evaluate the quality of his/her cooperative behaviour, as these remaining participants have been able to assess it in the framework of this group's operations.

Therefore, you are invited to give a mark to the quality of the cooperative behaviour of {user_title} in the framework of the group related to the  proposal {subject_title}. The possible marks are:
-1 = cooperative behaviour below what I was expecting in the framework of a working group
0 = cooperative behaviour in line with what I was expecting in the framework of a working group
+1 = cooperative behaviour above what I was expecting in the framework of a working group

In order to give your mark to the cooperative behaviour of {user_title}, you just need to access this URL {subject_url} and to give one mark among those being proposed.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""You are invited to give a mark to the cooperative behaviour of the remaining participants of the working group related to the proposal "{subject_title}"""

NOTING_PARTICIPANT_MESSAGE = u"""
Dear {recipient_first_name},

You have just left the working group related to the proposal {subject_title}, because you quitted it, or because you were excluded out of it. 

Each time a member leaves a working group, the platform request this member to evaluate the quality of the cooperative behaviour of the remaining participants in the working group, as this leaving member has been able to assess it in the framework of this group's operations.

Therefore, you are invited to allocate a mark to the quality of the cooperative behaviour of the remaining participants in the working group related to the  proposal {subject_title}. The possible marks are:
-1 = cooperative behaviour below what I was expecting in the framework of a working group
0 = cooperative behaviour in line with what I was expecting in the framework of a working group
+1 = cooperative behaviour above what I was expecting in the framework of a working group

In order to give your mark to the cooperative behaviour of {user_title}, you just need to access this URL {subject_url} and to give one mark among those being proposed, to each remaining participant in this working group.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""You are invited to give a mark to the cooperative behaviour of the other members of the working group related to the proposal "{subject_title}"""

NOTING_MEMBERS_MESSAGE = u"""
Dear {recipient_first_name},


The working group related to the proposal {subject_title} has just published it, and submitted it to the assessment of the other members of the platform. It has thus finished its work. It is dissolved, and its members can dedicate themselves to other proposals. 

Each time a working group ceases its activities, the platform requests each of its former participants to evaluate the quality of the cooperative behaviour of the other former participants in the working group, as s/he has been able to assess it in the framework of this group's operations.

Therefore, you are invited to allocate a mark to the quality of the cooperative behaviour of the other former participants in the working group related to the  proposal {subject_title}. The possible marks are:
-1 = cooperative behaviour below what I was expecting in the framework of a working group
0 = cooperative behaviour in line with what I was expecting in the framework of a working group
+1 = cooperative behaviour above what I was expecting in the framework of a working group

In order to give your mark to the cooperative behaviour of {user_title}, you just need to access this URL {subject_url} and to give one mark among those being proposed, to each former participant in this working group.


""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""You are invited to vote on the application of {user_first_name} {user_last_name} to the Working Group related to the proposal "{subject_title}"""

NEW_PARTICIPANT_MESSAGE = u"""

Dear {recipient_first_name},

{user_first_name} {user_last_name} has just applied to participate in the Working Group related to the proposal "{subject_title}".

You are invited to vote on this application. In order to do so, you just need to access this URL {subject_url} and to vote on the application of {user_first_name} {user_last_name} to the Working Group related to the proposal "{subject_title}".

The duration of the vote is {duration} day(s). After the {date_end_vote}, the ballot will be closed, and your vote will not be taken into account. Beware! By default, if no participant has voted by this date on the application of {user_first_name} {user_last_name} to the Working Group related to the proposal "{subject_title}", then {user_first_name} {user_last_name} will be accepted in the working group.

""" + PORTAL_SIGNATURE

# Le chiffre de 12 comme étant le nombre maximal de participants dans le groupe de travail est inscrit en dur dans le code
# C'est en réalité un paramètre de l'application
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
WATINGLIST_SUBJECT = u"""Registration in the waiting list of the working group related to the proposal "{subject_title}"""

WATINGLIST_MESSAGE = u"""
Dear {recipient_first_name},

You wish to participate in the working group related to the proposal "{subject_title}", which can be accessed at {subject_url}. However, the number of participants has already reached 12, which is the maximum number of participants in a working group.

You are therefore on the waiting list of this working group, and will automatically become a participant in it, as soon as a place is free.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
NEWCONTENT_SUBJECT = u"""{subject_type} "{subject_title}", which contains a keyword among your topics of interest, has just been published."""

NEWCONTENT_MESSAGE = u"""
Dear {recipient_first_name},

{subject_type} "{subject_title}", which contains a keyword among your topics of interest, has just been published. You can access it at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
CONTENTMODIFIEF_SUBJECT = u"""{subject_type} "subject_title}", which is among your favourites, has changed its status"""

CONTENTMODIFIEF_MESSAGE = u"""
Dear {recipient_first_name},

{subject_type} "subject_title}", which is among your favourites, has just switched from the status {state_source} to the status {state_target}. You can access it at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ARCHIVEIDEA_SUBJECT = u"""Decision by the moderators to archive the idea "{subject_title}"""

ARCHIVEIDEA_MESSAGE = u"""
Dear {recipient_first_name},

The idea "{subject_title}" has just been archived by the moderators, for the following reason:

{explanation}

You can access your idea at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Decision by the moderators to archive the content "{subject_title}"""


ARCHIVECONTENT_MESSAGE = u"""
Dear {recipient_first_name},

The content "{subject_title}" has just been archived by the moderators, for the following reason:

{explanation}

You can access your content at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ARCHIVEPROPOSAL_SUBJECT = u"""Decision by the moderators to archive the proposal "{subject_title}"""

ARCHIVEPROPOSAL_MESSAGE = u"""
Dear {recipient_first_name},

The proposal "{subject_title}" has just been archived by the moderators, for the following reason:

{explanation}

You can access your proposal at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERTOPINION_SUBJECT = u"""Opinion of the Examination Committee on the proposal "{subject_title}"""

ALERTOPINION_MESSAGE = u"""
Dear {recipient_first_name},

The Examination Committee has expressed the following opinion "{opinion}" on the proposal "{subject_title}", with the following explanation:  "{explanation}".

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERTOPINIONIDEA_SUBJECT = u"""Opinion of an Examiner on the idea "{subject_title}"""

ALERTOPINIONIDEA_MESSAGE = u"""
Dear {recipient_first_name},

An Examiner has expressed the following opinion "{opinion}" on the idea "{subject_title}", with the following explanation:  "{explanation}".

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PUBLISHEDIDEA_SUBJECT = u"""Decision by the moderators to publish the idea "{subject_title}"""

PUBLISHEDIDEA_MESSAGE = u"""
Dear {recipient_first_name},

The idea "{subject_title}", which is accessible at the URL {subject_url}, has just been published by the moderators. This idea can now be used by any member of the platform to build a proposal.

""" + PORTAL_SIGNATURE


#J'ai introduit l'idée de quorum pour le groupe de travail
PUBLISHEDPROPOSAL_SUBJECT = u"""Decision by the moderators to publish the proposal "{subject_title}"""

PUBLISHEDPROPOSAL_MESSAGE = u"""
Dear {recipient_first_name},

The proposal "{subject_title}", which can be accessed at {subject_url}, has just been published by the moderators. The working group is created, and is waiting to reach the quorum.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
PROPOSALREMOVED_SUBJECT = u"""Suppression of proposal "{subject_title}"""

PROPOSALREMOVED_MESSAGE = u"""
Dear {recipient_first_name},

The proposal "{subject_title}" has just been suppressed by the moderators for the following reason:

« {explanation} »

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
REFUSE_INVITATION_SUBJECT = u"""{user_first_name} {user_last_name} has refused to join the platform {novaideo_title}"""

REFUSE_INVITATION_MESSAGE = u"""
Dear,

We inform you that {user_first_name} {user_last_name} has refused your invitation to join the platform {novaideo_title}.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ACCEPT_INVITATION_SUBJECT = u"""{user_first_name} {user_last_name} has accepted to join the platform {novaideo_title}"""

ACCEPT_INVITATION_MESSAGE = u"""
Dear {recipient_first_name},

We inform you that {user_first_name} {user_last_name} has accepted your invitation to join the platform {novaideo_title}.

""" + PORTAL_SIGNATURE

#Cette URL est-t-elle permanente, ou sa durée de validité est-elle limitée ?  
#Si la durée de validité est limitée, il serait important d'indiquer date de fin de validité dans le message.
RESETPW_SUBJECT = u"""Your new password on the platform {novaideo_title}"""

RESETPW_MESSAGE = u"""
Dear {recipient_first_name},

You have asked for a new password on the platform {novaideo_title}. Please click on the following URL {reseturl} and provide your new password.

""" + PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""Finalise your registration on the {novaideo_title} on-line democracy platform"""


PREREGISTRATION_MESSAGE = u"""
Dear {recipient_first_name},

You have registered on the {novaideo_title} on-line democracy platform.

In order to finalise your registration, you must now click on the following link {url}. This link is valid for 48 hours. You must therefore complete your registration on or before {deadline_date}.

We are happy to count you among our members. We hope that your participation will be for you a positive and rewarding experience, in a fully democractic framework. Welcome!

"""+ PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Your registration on the {novaideo_title} on-line democracy platfom"""


PREREGISTRATION_MOD_MESSAGE = u"""
Dear {recipient_first_name},

The Verifiers that had been randomly selected upon your registration have validated the adequacy between the Identity Data that you had provided upon registration on the platform, and that of the official identity documents that you had sent them directly a copy of.

We are now sure that you are the only person registered under this Identity Data on the {novaideo_title} on-line democracy platfom. Like all other members, you have only one account, and will contribute to upholding the democratic principle "1 person = 1 vote".

YIn order to finalise your registration, you must now click on the following link {url}. This link is valid for 48 hours. You must therefore complete your registration on or before {deadline_date}.

We are happy to count you among our members. We hope that your participation will be for you a positive and rewarding experience, in a fully democractic framework. Welcome!

"""+ PORTAL_SIGNATURE

#Il faudra compléter avec le lieu de naissance
ADMIN_PREREGISTRATION_SUBJECT = u"""Please contribute to verify a new registration on the {novaideo_title} on-line democracy platfom"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
Dear {recipient_first_name},


You have been randomly selected by the {novaideo_title} on-line democracy platfom to act as a Verifier, whose task is to verify the identity of a person that has just registered on line.

At each new registration on the {novaideo_title} platfom, the system randomly selects three existing members, and requests them to verify the identity of the newly registered person. Indeed, it is important to check that each member on the platform is related to one natural person, and to one only. Thereby, we avoid that a given natural person vote several times on the platform under several different pseudonyms.

In order to perform this verification of this person's identity, you just need to follow the following steps:
1. you will receive on or before the {date_end_vote} an e-mail from the person that has just registered on the platform. The e-mail address of this person, from which s/he will send you his/her e-mail, is {subject_email}. This e-mail will contain the copy of an official identity document
2. as soon as you have received this e-mail, or if you haven't received it by {date_end_vote}, connect on the platform at the following URL: {subject_url}. On this page, you will decide whether the Identity Data received from this person (which are reproduced below) match those present on the official identity document, a copy of which you will have received by e-mail. Be very careful! In order for you to accept the registration, ALL elements must be strictly IDENTICAL between the Identity Data received upon registration, and those on the copied official identity document. In all other cases, even with a single, minor difference, if you doubt the authenticity of the copied official identity document, or if you have not received the copy of the official identity document by {date_end_vote}, you MUST refuse the registration.

The Identity Data received from the person upon his/her registration is the following:

  Family name(s): {subject_last_name}
  Given name(s): {subject_first_name}
  Date of birth: {birth_date}
  Place of birth: {birthplace}

The Verification process lasts {duration} day(s), i.e. it must be completed on or before {date_end_vote}. Beyond this date, the Verification process will be closed, and your decision will not be taken into account. By default, if no Verifier has voted upon this date, the registration will be refused.

"""+ PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Invitation to moderate a new content on the {novaideo_title} on-line democracy platform"""


ADMIN_CONTENT_MESSAGE = u"""
Dear {recipient_first_name},


You have been randomly selected by the {novaideo_title} on-line democracy platfom to moderate a new content added to the platform.

Each time a new content (idea or proposal) is added to the {novaideo_title} platform, the system randomly selects three members, and requests them to verify the compliance of the content with the Moderation Rules {url_moderation_rules}. By randomly distributing the Moderation, we avoid that this important control function be concentrated in a few hands. We contribute thereby to the democratic nature of the platform.

In order for you to exert your function as Moderator on this new content, you just need to connect to the platform at the following URL {subject_url}, and to assess the compliance of this new content with the Moderation Rules.

The Moderation process lasts {duration} day(s), i.e. it must be completed on or before {date_end_vote}. Beyond this date, the Moderation process will be closed, and your assessment will not be taken into account. By default, if no Moderator has voted upon this date, the new content will be accepted.

"""+ PORTAL_SIGNATURE


ADMIN_REPORT_SUBJECT = u"""Invitation to moderate a content signalled as potentially non-compliant with the Moderation Rules on the {novaideo_title} on-line democracy platform"""


ADMIN_REPORT_MESSAGE = u"""
Dear {recipient_first_name},


You have been randomly selected by the {novaideo_title} on-line democracy platfom to moderate a conten which has been signalled on the platform as potentially non-compliant with the Moderation Rules {url_moderation_rules}.

Each time a content is signalled as potentially non-compliant with the Moderation Rules on the {novaideo_title} platform, the system randomly selects three members, and requests them to verify the compliance of the content with the Moderation Rules. By randomly distributing the Moderation, we avoid that this important control function be concentrated in a few hands. We contribute thereby to the democratic nature of the platform.

In order for you to exert your function as Moderator on this signalled content, you just need to connect to the platform at the following URL {subject_url}, and to assess the compliance of this signalled content with the Moderation Rules.

The Moderation process lasts {duration} day(s), i.e. it must be completed on or before {date_end_vote}. Beyond this date, the Moderation process will be closed, and your assessment will not be taken into account. By default, if no Moderator has voted upon this date, the signalled content will be accepted.

"""+ PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
AUTHOR_REPORT_SUBJECT = u"""Your content has been signalled as potentially non-compliant with the Moderation Rules on the {novaideo_title} on-line democracy platform"""

AUTHOR_REPORT_MESSAGE = u"""

Dear {recipient_first_name},

Your content {subject_url} has been signalled by a member as being potentially non-compliant with the Moderation Rules {url_moderation_rules}.

Each time a content is signalled as potentially non-compliant with the Moderation Rules on the {novaideo_title} platform, the system randomly selects three members, and requests them to verify the compliance of the content with the Moderation Rules. By randomly distributing the Moderation, we avoid that this important control function be concentrated in a few hands. We contribute thereby to the democratic nature of the platform.

The Moderation process lasts {duration} day(s). On {date_end_vote} at the latest, the Moderation process will be closed, and you will be informed of its result.

"""+ PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Your registration on the {novaideo_title} on-line democracy platform has been refused"""

ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Dear {recipient_first_name},


The Verifiers that had been randomly selected upon your registration have NOT validated the adequacy between the Identity Data that you had provided on the platform and those on the official identity documents that you had sent them a copy of.

We therefore regret to inform you that your registration on the {novaideo_title} has been refused. 

We must be very rigorous in this verification. If we allowed even minor discrepancies between the two, a single natural person could register several times, each time with small variations in his/her Identity Data, open several accounts, and vote several times. This would breach the democratic principle "one person = one vote". 

"""+ PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Your registration on the {novaideo_title} on-line democracy platform is being processed"""

ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Dear {recipient_first_name},


Your registration on the {novaideo_title} on-line democracy platform is now subject to the verification of your identity.

At each new registration on the {novaideo_title} platfom, the system randomly selects three existing members (the Verifiers of this specific registration), and requests them to verify the identity of the newly registered person. Indeed, it is important to check that each member on the platform is related to one natural person, and to one only. Thereby, we avoid that a given natural person vote several times on the platform under several different pseudonyms.

In order for your identity to be verified, we kindly request you to send to each of the following persons, in separate e-mails, on or before the {date_end_vote}, a scanned copy of an official identity document. This copy must display clearly your family name(s), your given name(s), your birth date and your birth place, written in the Latin alphabet. Beyond the {date_end_vote}, if the Verifiers have not received a copy of  your official identity document, they are instructed to refuse your registration. 

The Verifiers assigned to the verification of your identity are:
{moderators}

You will receive the result of this identity verification process at the end of the time given for the Verifiers to process this verification, i.e. on {date_end_vote} at the latest.

"""+ PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ADMIN_CONTENT_SUB_SUBJECT = u"""Your content on the {novaideo_title} on-line democracy platform is being moderated"""

ADMIN_CONTENT_SUB_MESSAGE = u"""
Dear {recipient_first_name},

Your content has been submitted to Moderation.  

Each time a new content (idea or proposal) is added to the {novaideo_title} platform, the system randomly selects three members, and requests them to verify the compliance of the content with the Moderation Rules {url_moderation_rules}. By randomly distributing the Moderation, we avoid that this important control function be concentrated in a few hands. We contribute thereby to the democratic nature of the platform.

The Moderation process lasts {duration} day(s). On {date_end_vote} at the latest, the Moderation process will be closed, and you will be informed of its result.

"""+ PORTAL_SIGNATURE


MODERATOR_DATA = u"""
Verifier {index}:
  Email: {subject_email}
"""

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERTCOMMENT_SUBJECT = u"""New comment on {subject_type} "{subject_title}"""


ALERTCOMMENT_MESSAGE = u"""
Dear {recipient_first_name},

A new comment has been added on the {subject_type} "{subject_title}".

"{comment_content}"

You can access it at the following URL {comment_url} and answer it.

"""+ PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""New answer given to {subject_type} "{subject_title}"""

ALERTANSWER_MESSAGE = u"""
Dear {recipient_first_name},

A new answer was given to {subject_type} "{subject_title}".

"{comment_content}"

You can access it at the following URL {comment_url} and answer it.

""" + PORTAL_SIGNATURE

#BUG POTENTIEL: s'il s'agit d'une discussion avec une personne, pourquoi le contenu est-il désigné comme {subject_title}?
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERTDISCUSS_SUBJECT = u"""New message added to your discussion with "subject_title}"""


ALERTDISCUSS_MESSAGE = u"""
Dear {recipient_first_name},

A new message has been added to your discussion with "{subject_title}".

"{comment_content}"

You can access it at the following URL {comment_url} and answer it.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
ALERTRESPONS_SUBJECT = u"""A person has given an answer to a comment on the {subject_type} "{subject_title}"""

ALERTRESPONS_MESSAGE = u"""
Dear {recipient_first_name},

A person has given an answer to a comment on the {subject_type} "{subject_title}, which can be accessed at the following URL{comment_url}.

"{comment_content}"

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Subscription to the newsletter"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Dear {first_name} {last_name},

Your subscription to the newsletter {newsletter_title} is now confirmed.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE: 
#Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur
NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Unsubscription from the newsletter"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Dear {first_name} {last_name},

Your subscription to the newsletter {newsletter_title} is now cancelled.

""" + PORTAL_SIGNATURE

PUBLISHEDCHALLENGE_SUBJECT = u"""Decision by the moderators to publish the challenge "{subject_title}"""

PUBLISHEDCHALLENGE_MESSAGE = u"""
Dear {recipient_first_name},

The challenge "{subject_title}", which can be accessed at {subject_url}, has just been published by the moderators.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Decision by the moderators to archive the challenge "{subject_title}"""

ARCHIVECHALLENGE_MESSAGE = u"""
Dear {recipient_first_name},

The challenge "{subject_title}" has just been archived by the moderators, for the following reason:

{explanation}

You can access your challenge at the following URL {subject_url}.

""" + PORTAL_SIGNATURE

PRESENTATION_CHALLENGE_SUBJECT = u"""Presentation of the challenge "{subject_title}""" 

PRESENTATION_CHALLENGE_MESSAGE = u"""
Dear,

{my_first_name} {my_last_name} wishes to present to you the challenge "{subject_title}" on the {novaideo_title} platform. You can access this challenge at: {subject_url}.
""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Request to quit sent from your account on the {novaideo_title} platform"""

QUIT_REQUEST_MESSAGE = u"""
Dear {recipient_first_name} {recipient_last_name},

We received on your account on the {novaideo_title} platform a request to quit.
If you have indeed requested to quit the platform, click on the following confirmation link: {url}, before the date {deadline_date}.

BEWARE: this action CANNOT BE UNDONE. If you click on this link, you will lose any access to the platform, your account will be destroyed and all contents related to your account will irrevertibly be attributed to an anonymous author.
You will not be able to register again on the platform, thereby creating a new, blank account, before a duration equal to {tquarantaine} days.

If you have not requested to quit the platform, simply ignore this e-mail, and your account will be kept active.
We recommend however that you change your password, to prevent your account from being hacked.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Your decision to quit the on-line democracy platform {novaideo_title} has been executed"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Dear {recipient_first_name} {recipient_last_name},

You have decided to quit the on-line democracy platform {novaideo_title}. We regret of course your decision, but respect your choice. We hereby inform you that:
* Your account has been disactivated. You will receive in the future only one message from us (see below);
* All content associated with your account has irreversibly been attributed to an Anonymous author
* The Identity Data that you had transmitted to us upon registration (Given Names, Family Names, date and location of birth) and your e-mail address will be kept in our records for {tquarantaine} days, so that you will not be able to register again during this period. The purpose of this is to prevent people who would have had an inappropriate behaviour on the platform (and thus earned a bad reputation) from re-registering immediately under a new pseudonym and with a virgin reputation
* At the end of this period, i.e. on {date_tquarantaine}, you will receive from us an e-mail informing you that your Identity Data and your e-mail address have been erased from our database.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""Your Identity Data and your e-mail address have been erased from the database of the {novaideo_title} platform"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Dear {recipient_first_name} {recipient_last_name},

Today, your Identity Data (Given Names, Family Names, date and location of birth) and your e-mail address have been erased from our database. You will receive no further e-mail from us.

""" + PORTAL_SIGNATURE


mail_locale = 'en'

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