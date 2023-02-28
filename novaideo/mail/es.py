# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi, *

from . import add_mail_template

""" The contents of e-mails"""

PORTAL_SIGNATURE = """Atentamente,

La Plataforma {novaideo_title}
229, rue Solférino
59000 Lille (Francia)
"""

PORTAL_PRESENTATION = u"""{novaideo_title} es una plataforma participativa que permite a cualquier miembro iniciar ideas que pueden ser utilizadas en propuestas que son mejoradas por grupos de trabajo. Una vez mejoradas, estas propuestas pueden someterse a la consideración de los miembros y a la decisión de un grupo de revisión.

"""

FIRST_INVITATION_SUBJECT = u"""Invitación a unirse a la plataforma participativa {novaideo_title}"""

FIRST_INVITATION_MESSAGE = u"""
Hola,

Gracias por su interés en Nova-Ideo.

{recipient_first_name} le invitamos a unirse a la plataforma participativa Nova-Ideo como administrador del sitio.

Para validar su invitación, debe hacer clic en el enlace {invitation_url} y seguir las instrucciones.

Le recordamos que Nova-Ideo es una solución de innovación participativa en línea que le permite abordar las siguientes cuestiones
- Quiere poner en marcha una solución de innovación participativa;
- Ya tiene una caja de ideas, pero está vacía o tan llena que es imposible encontrar las ideas adecuadas;
- No tiene tiempo para dedicarse a la gestión de ideas, por lo que pierde muchas oportunidades y crea decepción en los que tienen ideas.

Nova-Ideo le permite recopilar ideas de un grupo, encontrar las buenas ideas y transformarlas en propuestas viables que reflejen todos los puntos de vista.

Para ello, Nova-Ideo utiliza el crowdsourcing, haciendo trabajar a la "multitud" para transformar las ideas en propuestas.

Nova-Ideo fusiona lo mejor del buzón de ideas, el portal colaborativo y las herramientas de comunicación interna y ofrece soluciones de innovación social de vanguardia como el uso del juicio mayoritario o la organización de la escasez de apoyo/rechazo.

Visite nuestra página https://www.nova-ideo.com y en particular su página de Documentación https://www.nova-ideo.com/documentation

Siga nuestra cuenta de twitter: https://twitter.com/NovaIdeo

Puede consultar nuestra presentación detallada de Nova-Ideo http://fr.slideshare.net/MichaelLaunay/20160911-novaideo-linnovation-participative-en-ligne

El código de Nova-Ideo bajo la licencia libre AGPL V3 está disponible en: https://github.com/ecreall/nova-ideo

El vídeo filmado durante la PyConFR en el que se explica de dónde procede Nova-Ideo y por qué es gratuito: http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html

También producimos una serie de vídeos explicativos sobre la administración y el funcionamiento de Nova-Ideo, a los que puede acceder desde la página de Documentación de nuestro sitio web https://www.nova-ideo.com/documentation.

Podemos adaptar Nova-Ideo a sus necesidades específicas, así que no dude en ponerse en contacto con nosotros, ¡responderemos a sus preguntas!

También puede enviarnos sus comentarios y sugerencias de mejora creando una cuenta en https://evolutions.nova-ideo.com.

Atentamente
El equipo de Ecréall
Servicios y soluciones de software libre
Parque Científico de Haute Borne
Edificio Hub Innovation
11, rue de l'Harmonie
59650 Villeneuve d'Ascq
sitio : http://www.ecreall.com
tel : 03 20 79 32 90
móvil : 06 16 85 91 12
Fax : 09 56 94 39 44
"""

FIRST_INVITATION_SMS_MESSAGE = u"""
Hola,

Gracias por su interés en Nova-Ideo.

{recipient_first_name} le invitamos a unirse a la plataforma participativa Nova-Ideo como administrador del sitio.

Para validar su invitación, debe hacer clic en el enlace {invitation_url} y seguir las instrucciones.

Atentamente
El equipo de Ecréall
"""

INVITATION_SUBJECT = u"""Invitación a unirse a la plataforma participativa {novaideo_title}"""

INVITATION_MESSAGE = u"""
Hola {recipient_first_name},

Ha sido invitado a unirse a la plataforma participativa {novaideo_title} como {roles}.

¡Estaremos encantados de tenerle como miembro activo! Para validar su invitación, sólo tiene que hacer clic en el enlace {invitation_url} y seguir las instrucciones. ¡Hasta pronto en la plataforma {novaideo_title}!

""" + PORTAL_SIGNATURE


PRESENTATION_IDEA_SUBJECT = u"""Presentación de la idea " {subject_title} """


PRESENTATION_IDEA_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentar la idea " {subject_title} " en la plataforma {novaideo_title}. Esta idea es accesible en la dirección: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


CONFIRMATION_SUBJECT = u"""Confirmación de su inscripción a la plataforma de democracia deliberativa {novaideo_title}"""

CONFIRMATION_MESSAGE = u"""
Hola {recipient_first_name},

Confirmamos su inscripción a la plataforma de democracia deliberativa {novaideo_title}. ¡Bienvenido a la plataforma!

Saludos cordiales,
                                                                                
La plataforma de democracia deliberativa {novaideo_title}
""" + PORTAL_SIGNATURE


PRESENTATION_PROPOSAL_SUBJECT = u"""Presentación de la propuesta " {subject_title} """


PRESENTATION_PROPOSAL_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentar la propuesta "{subject_title}" en la plataforma {novaideo_title}. Puede acceder a esta propuesta en: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentar la enmienda "{subject_title}" que aparece en la plataforma {novaideo_title} bajo {subject_url}.

""" + \
    PORTAL_PRESENTACION + PORTAL_SIGNATURE


PRESENTATION_AMENDMENT_SUBJECT = u""" {subject_title} """


PRESENTATION_QUESTION_SUBJECT = u"""Presentación de la pregunta " {subject_title} """


PRESENTATION_QUESTION_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentarle la pregunta "{subject_title}" en la plataforma {novaideo_title}. Puede acceder a esta pregunta en: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


PRESENTATION_ANSWER_SUBJECT = u"""Presentación de la respuesta a una pregunta" {subject_title} """


PRESENTATION_ANSWER_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentar la respuesta a una pregunta " {subject_title} " en la plataforma {novaideo_title}. Puede encontrar esta respuesta en: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


AMENDABLE_FIRST_SUBJECT = u"""Inicio del ciclo de mejora de la propuesta" {subject_title} """


AMENDABLE_FIRST_MESSAGE = u"""
Hola {recipient_first_name},

Ya son tres los participantes en el grupo de trabajo para la propuesta "{subject_title}" bajo {subject_url}, y pueden empezar a mejorarla.

Cada participante puede hacer sugerencias de mejora que los demás pueden aceptar o rechazar. Una vez finalizado el ciclo de mejora, todos los participantes votan para seguir mejorando la propuesta o para presentarla a los miembros de la plataforma para su aprobación.

El ciclo de mejora finaliza el {duration}.

""" + PORTAL_SIGNATURE

AMENDABLE_SUBJECT = u"""Inicio del ciclo de mejora de la propuesta" {subject_title} """


AMENDABLE_MESSAGE = u"""
Hola {recipient_first_name},

El grupo de trabajo sobre la propuesta "{subject_title}" bajo {subject_url} votó por mayoría continuar mejorando la propuesta.

Cada participante puede hacer sugerencias de mejora que los demás pueden aceptar o rechazar. Una vez finalizado el ciclo de mejora, todos los participantes votan para seguir mejorando la propuesta o para someterla a la consideración de los miembros de la plataforma.

El ciclo de mejora finaliza el {duration}.

""" + PORTAL_SIGNATURE

ALERT_SUBJECT = u"""Fin del ciclo de mejora de la propuesta " {subject_title} " sin ninguna mejora"""

ALERT_MESSAGE = u"""
Hola {recipient_first_name},

Aunque el ciclo de mejora está completo, no se han realizado mejoras en la propuesta "{subject_title}" que se encuentra bajo {subject_url}. Tendrá que votar si presenta la propuesta tal como está o si inicia una nueva ronda de mejoras.

""" + PORTAL_SIGNATURE

ALERT_END_SUBJECT = u"""Últimas mejoras antes del final del ciclo de mejora de la propuesta" {subject_title} """

ALERT_END_MESSAGE = u"""
Hola {recipient_first_name},

El ciclo de mejora de la propuesta "{subject_title}" en {subject_url} está casi terminado. Aún puede introducir mejoras en ella, antes de que el grupo de trabajo vote para presentar la propuesta tal cual o para iniciar un nuevo ciclo de mejoras.

""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


RESULT_VOTE_AMENDMENT_SUBJECT = u"""Los resultados de la votación sobre las enmiendas relativas a la propuesta " {subject_title} """

RESULT_VOTE_AMENDMENT_MESSAGE = u"""
<div>
Hola {recipient_first_name},

{message_result}
</div>
""" + PORTAL_SIGNATURE


PUBLISHPROPOSAL_SUBJECT = u"""Decisión de someter la propuesta " {subject_title} " a la consideración de los miembros de la plataforma"""

PUBLISHPROPOSAL_MESSAGE = u"""
Hola {recipient_first_name},

El grupo de trabajo sobre la propuesta "{subject_title}" bajo {subject_url} ha votado por mayoría someter la propuesta a la consideración de los miembros de la plataforma.

Cada miembro de la Plataforma puede ahora apoyar u oponerse a la propuesta y el grupo de revisión puede estudiarla.

""" + PORTAL_SIGNATURE


SYSTEM_CLOSE_PROPOSAL_SUBJECT = u"""Decisión de cerrar la propuesta "{subject_title}"""

SYSTEM_CLOSE_PROPOSAL_MESSAGE = u"""
Hola {recipient_first_name},

El grupo de trabajo sobre la propuesta "{subject_title}" bajo {subject_url} no ha estado activo durante algunos ciclos más de una semana.
Por esta razón, el grupo de trabajo se ha disuelto y la propuesta está ahora abierta a un grupo de trabajo.

""" + PORTAL_SIGNATURE


VOTINGPUBLICATION_SUBJECT = u"""Empiece a votar para mejorar la propuesta "{subject_title}" o sométala a la consideración de los miembros de la plataforma"""

VOTINGPUBLICATION_MESSAGE = u"""
Hola {recipient_first_name},

El ciclo de mejora de la propuesta "{subject_title}" en {subject_url} ha finalizado, le invitamos a participar en la votación para mejorar la propuesta o someterla a la consideración de los miembros de la plataforma.

Dispone de 24 horas para votar, transcurridas las cuales el voto se contabilizará teniendo en cuenta la elección de la mayoría de los votantes. Si no hay votación, se iniciará una nueva ronda de mejoras durante una semana.

""" + PORTAL_SIGNATURE


VOTINGAMENDMENTS_SUBJECT = u"""Comienza la votación de las enmiendas a la propuesta " {subject_title} """

VOTINGAMENDMENTS_MESSAGE = u"""
Hola {recipient_first_name},

La votación de las enmiendas a la propuesta "{subject_title}" bajo {subject_url} ha comenzado. Por favor, participe en la votación.

""" + PORTAL_SIGNATURE

WITHDRAW_SUBJECT = u"""Retirada de la lista de espera del grupo de trabajo de la propuesta " {subject_title} """

WITHDRAW_MESSAGE = u"""
Hola {recipient_first_name},

Ya no está en la lista de espera para la propuesta grupo de trabajo {subject_title}" bajo {subject_url}, tras su eliminación de la lista de espera.

Puede intentar reincorporarse al grupo de trabajo de la propuesta en cualquier momento, si aún se está mejorando.

""" + PORTAL_SIGNATURE

PARTICIPATE_WL_SUBJECT = u"""Ya puede empezar a participar en el grupo de trabajo relacionado con la propuesta " {subject_title} """

PARTICIPATE_WL_MESSAGE = u"""
Hola {recipient_first_name},

Usted es miembro del grupo de trabajo para la propuesta {subject_title}" que se encuentra bajo {subject_url}, tras la marcha de uno de los participantes.

Como participante en el grupo de trabajo puede mejorar la propuesta y al final del ciclo de mejora puede votar para seguir mejorándola o presentarla a los miembros de la plataforma.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Ya puede empezar a participar en el grupo de trabajo relacionado con la propuesta " {subject_title} """

PARTICIPATE_MESSAGE = u"""
Hola {recipient_first_name},

Usted es miembro del grupo de trabajo de la propuesta {subject_title} que puede encontrar en {subject_url}.

Como participante en el grupo de trabajo puede mejorar la propuesta, si es que se está mejorando, y al final del ciclo de mejora puede votar si desea seguir mejorándola o presentarla a los miembros de la plataforma.

""" + PORTAL_SIGNATURE

PARTICIPATE_SUBJECT = u"""Envíe su participación en el grupo de trabajo de propuestas" {subject_title} """


PARTICIPATE_SUB_MESSAGE = u"""

Hola {recipient_first_name},

Su solicitud para participar en el grupo de trabajo de la propuesta "{subject_title}" bajo {subject_url} ha sido enviada a los miembros del grupo.

Con cada nueva solicitud de participación, los miembros del grupo deciden si la aceptan o no.

La duración de la votación de su solicitud es de {duration} día(s). Después de la fecha de {date_end_vote}, la votación sobre su solicitud quedará cerrada, y se le informará del resultado.

""" + PORTAL_SIGNATURE


RESIGN_SUBJECT = u"""Su salida del grupo de trabajo de propuestas" {subject_title} """

RESIGN_MESSAGE = u"""
Hola {recipient_first_name},

Confirmamos que ya no es miembro del grupo de trabajo de la propuesta "{subject_title}" bajo {subject_url}.

Puede volver a unirse a él en cualquier momento, si no es ya miembro de otros cinco grupos de trabajo, que es el número máximo de grupos de trabajo en los que un miembro puede participar simultáneamente.

""" + PORTAL_SIGNATURE


EXCLUDE_SUBJECT = u"""Exclusión del grupo de trabajo de la propuesta " {subject_title} """

EXCLUDE_MESSAGE = u"""
Hola {recipient_first_name},

El grupo de trabajo ha decidido excluirle del grupo. Ya no es miembro del grupo de trabajo de la propuesta "{subject_title}" que se encuentra en {subject_url}.

Puede unirse a otro grupo de trabajo en cualquier momento, si no es ya miembro de otros cinco grupos de trabajo, que es el número máximo de grupos de trabajo en los que un miembro puede participar simultáneamente.

""" + PORTAL_SIGNATURE


EXCLUDE_PARTICIPANT_SUBJECT = u"""Se le invita a votar sobre la solicitud de excluir a {user_first_name} {user_last_name} del Grupo de Trabajo relacionado con la propuesta " {subject_title} """

EXCLUDE_PARTICIPANT_MESSAGE = u"""
Hola {recipient_first_name},

{user_first_name} {user_last_name} acaba de solicitar su exclusión del Grupo de Trabajo sobre la propuesta "{subject_title}".

Se les pide que voten sobre esta solicitud de exclusión. Para ello, sólo tiene que conectarse a la plataforma en la siguiente dirección {subject_url} y votar la solicitud de exclusión de {user_first_name} {user_last_name} fuera del Grupo de Trabajo vinculado a la propuesta "{subject_title}".

La duración de la votación es de {duration} día(s). Después de la fecha de {date_end_vote}, la votación quedará cerrada y su voto no se tendrá en cuenta. ¡Tenga en cuenta! Por defecto, si ningún Participante ha votado en esta fecha sobre la exclusión de {user_first_name} {user_last_name} del Grupo de Trabajo relacionado con la propuesta "{subject_title}", {user_first_name} {user_last_name} se mantendrá en el Grupo de Trabajo.

""" + PORTAL_SIGNATURE


NOTING_MEMBER_SUBJECT = u"""Le invitamos a observar el comportamiento cooperativo de {user_first_name} """

NOTING_MEMBER_MESSAGE = u"""
Hola {recipient_first_name},

{user_title} acaba de abandonar el Grupo de Trabajo, ya sea por dimisión o por exclusión. Cada vez que un miembro abandona un grupo de trabajo, el sistema pide a los miembros restantes del grupo de trabajo que juzguen la calidad de su comportamiento cooperativo, tal y como lo perciben esos miembros restantes en el trabajo del grupo.

Por lo tanto, se le pide que puntúe la calidad del comportamiento cooperativo de {user_title} en el grupo relacionado con la propuesta {subject_title}. Las puntuaciones posibles son:
-1 = comportamiento cooperativo por debajo de lo que espero en un grupo de trabajo
0 = comportamiento cooperativo acorde con lo que espero en un grupo de trabajo
+1 = comportamiento cooperativo mejor de lo que espero en un grupo de trabajo

Para calificar el comportamiento cooperativo de {user_title}, sólo tiene que ir a esta URL {subject_url} y dar una calificación de la lista.

""" + PORTAL_SIGNATURE

NOTING_PARTICIPANT_SUBJECT = u"""Le invitamos a valorar el comportamiento cooperativo de los demás miembros del grupo en relación con la propuesta " {subject_title} """

NOTING_PARTICIPANT_MESSAGE = u"""
Hola {recipient_first_name},

Acaba de abandonar el grupo de trabajo relacionado con la propuesta {subject_title}, ya sea por dimisión o porque ha sido excluido. Cada vez que un miembro abandona un grupo de trabajo, el sistema pide a ese miembro que juzgue la calidad del comportamiento cooperativo de cada uno de los participantes restantes del grupo de trabajo, tal y como lo percibe ese miembro que abandona el grupo en el trabajo de ese grupo.

Por lo tanto, le invitamos a dar una puntuación a la calidad del comportamiento cooperativo de los demás participantes del grupo en relación con la propuesta {subject_title}. Las puntuaciones posibles son:
-1 = comportamiento cooperativo por debajo de lo que espero en un grupo de trabajo
0 = comportamiento cooperativo acorde con lo que espero en un grupo de trabajo
+1 = comportamiento cooperativo mejor de lo que espero en un grupo de trabajo

Para dar su puntuación al comportamiento cooperativo de los demás Participantes del Grupo de Trabajo relacionado con la propuesta {subject_title}, sólo tiene que acceder a esta URL {subject_url} y dar una puntuación entre las propuestas, a cada uno de los restantes Participantes de este grupo.

""" + PORTAL_SIGNATURE

NOTING_MEMBERS_SUBJECT = u"""Le invitamos a valorar el comportamiento cooperativo de los demás miembros del grupo en relación con la propuesta " {subject_title} """

NOTING_MEMBERS_MESSAGE = u"""
Hola {recipient_first_name},

El grupo de trabajo vinculado a la propuesta {subject_title} acaba de publicarla y someterla a la consideración de los demás miembros de la plataforma. Por lo tanto, ha terminado su trabajo. Se disuelve y sus miembros pueden centrarse en otras propuestas.

Cada vez que un grupo de trabajo cesa sus actividades y se disuelve, el sistema pide a cada uno de sus miembros que juzgue la calidad del comportamiento cooperativo de los demás miembros, tal y como ese miembro lo percibe en el trabajo de ese grupo.

Por lo tanto, se le pide que puntúe la calidad del comportamiento cooperativo de los demás miembros del grupo en relación con la propuesta {subject_title}. Las puntuaciones posibles son:
-1 = comportamiento cooperativo por debajo de lo que espero en un grupo de trabajo
0 = comportamiento cooperativo acorde con lo que espero en un grupo de trabajo
+1 = comportamiento cooperativo mejor de lo que espero en un grupo de trabajo

Para dar su puntuación al comportamiento cooperativo de los demás miembros del grupo de trabajo relacionado con la propuesta {subject_title}, sólo tiene que acceder a esta URL {subject_url} y dar una puntuación entre las propuestas, a cada uno de los demás miembros de este grupo.

""" + PORTAL_SIGNATURE


NEW_PARTICIPANT_SUBJECT = u"""Le invitamos a votar sobre la candidatura de {user_first_name} {user_last_name} al Grupo de Trabajo relacionado con la propuesta " {subject_title} """

NEW_PARTICIPANT_MESSAGE = u"""

Hola {recipient_first_name},

{user_first_name} {user_last_name} acaba de solicitar participar en el Grupo de Trabajo relacionado con la propuesta "{subject_title}".

Se les pide que voten sobre esta solicitud. Para ello, sólo tiene que conectarse a la plataforma en la siguiente dirección {subject_url} y votar la candidatura de {user_first_name} {user_last_name} al Grupo de Trabajo vinculado a la propuesta "{subject_title}".

La duración de la votación es de {duration} día(s). Después de la fecha {date_end_vote}, la votación se cerrará y su voto ya no se tendrá en cuenta. ¡Tenga en cuenta! Por defecto, si ningún Participante ha votado en esta fecha la solicitud de {user_first_name} {user_last_name} al Grupo de Trabajo relacionada con la propuesta "{subject_title}", {user_first_name} {user_last_name} será aceptado en el Grupo de Trabajo.

""" + PORTAL_SIGNATURE

# Le chiffre de 12 comme étant le nombre maximal de participants dans le groupe de travail est inscrit en dur dans le code
# C'est en réalité un paramètre de l'application
# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur


WATINGLIST_SUBJECT = u"""Inscripción en la lista de espera del grupo de trabajo de propuestas" {subject_title} """

WATINGLIST_MESSAGE = u"""
Hola {recipient_first_name},

Le gustaría participar en el grupo de trabajo de la propuesta "{subject_title}" bajo {subject_url}, pero el número de participantes ya ha alcanzado los 12, que es el número máximo de participantes en un grupo de trabajo.

Está usted en la lista de espera para este grupo de trabajo y se le incluirá automáticamente en cuanto haya una plaza disponible.

""" + PORTAL_SIGNATURE


NEWCONTENT_SUBJECT = u"""{subject_type} " {subject_title} que contiene una de sus palabras clave de interés ha sido publicado."""


NEWCONTENT_MESSAGE = u"""
Hola {recipient_first_name},

{subject_type} " {subject_title} " que contiene una de sus palabras clave de interés acaba de ser publicado. Puede verlo en {subject_url}.

""" + PORTAL_SIGNATURE


CONTENTMODIFIEF_SUBJECT = u"""{subject_type} " {subject_title} " que forma parte de sus favoritos acaba de cambiar de estado"""


CONTENTMODIF_MESSAGE = u"""
Hola {recipient_first_name},

{subject_type} "{subject_title}" que forma parte de sus favoritos acaba de cambiar de {state_source} a {state_target}. Puede verlo en {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEIDEA_SUBJECT = u"""Decisión de los moderadores de archivar la idea " {subject_title} """


ARCHIVEIDEA_MESSAGE = u"""
Hola {recipient_first_name},

La idea "{subject_title}" ha sido archivada por los moderadores por el siguiente motivo:

{explanation}

Puede encontrar su idea en {subject_url}.

""" + PORTAL_SIGNATURE

ARCHIVECONTENT_SUBJECT = u"""Decisión de los moderadores de archivar el contenido " {subject_title} """


ARCHIVECONTENT_MESSAGE = u"""
Hola {recipient_first_name},

El contenido "{subject_title}" ha sido archivado por los moderadores por el siguiente motivo:

{explanation}

Puede encontrar su contenido en {subject_url}.

""" + PORTAL_SIGNATURE


ARCHIVEPROPOSAL_SUBJECT = u"""Decisión de los moderadores de archivar la propuesta" {subject_title} """


ARCHIVEPROPOSAL_MESSAGE = u"""
Hola {recipient_first_name},

La propuesta "{subject_title}" ha sido archivada por los moderadores por el siguiente motivo:

{explanation}

Puede encontrar su propuesta en {subject_url}.

""" + PORTAL_SIGNATURE


ALERTOPINION_SUBJECT = u"""Opinión del Comité de Revisión sobre la propuesta" {subject_title} """


ALERTOPINION_MESSAGE = u"""
Hola {recipient_first_name},

El Comité de Examen ha emitido un dictamen "{opinion}" sobre la propuesta "{subject_title}" con la siguiente explicación: "{explanation}".

""" + PORTAL_SIGNATURE


ALERTOPINIONIDEA_SUBJECT = u"""Opinión del revisor sobre la idea " {subject_title} """


ALERTOPINIONIDEA_MESSAGE = u"""
Hola {recipient_first_name},

Un revisor ha emitido una opinión "{opinion}" sobre la idea "{subject_title}" con la siguiente explicación: "{explanation}".

""" + PORTAL_SIGNATURE


PUBLISHEDIDEA_SUBJECT = u"""Decisión de los moderadores de publicar la idea " {subject_title} """


PUBLISHEDIDEA_MESSAGE = u"""
Hola {recipient_first_name},

La idea "{subject_title}" bajo {subject_url} ha sido publicada por los moderadores en la plataforma {novaideo_title}. Esta idea puede ser utilizada ahora por cualquier miembro de la plataforma para una propuesta.

""" + PORTAL_SIGNATURE


PUBLISHEDPROPOSAL_SUBJECT = u"""Decisión de los moderadores de publicar la propuesta" {subject_title} """


PUBLISHEDPROPOSAL_MESSAGE = u"""
Hola {recipient_first_name},

La propuesta "{subject_title}" bajo {subject_url} acaba de ser publicada por los moderadores en la plataforma {novaideo_title}.

""" + PORTAL_SIGNATURE


PROPOSALREMOVED_SUBJECT = u"""Supresión de la propuesta " {subject_title} """


PROPOSALREMOVED_MESSAGE = u"""
Hola {recipient_first_name},

La propuesta "{subject_title}" ha sido eliminada por los moderadores por el siguiente motivo:

"{explanation}"

""" + PORTAL_SIGNATURE


REFUSE_INVITATION_SUBJECT = u"""Rechazo de {user_first_name} {user_last_name} a unirse a la plataforma {novaideo_title}"""


REFUSE_INVITATION_MESSAGE = u"""
Hola,

Le informamos de que {user_first_name} {user_last_name} ha declinado su invitación para unirse a la plataforma {novaideo_title}.

""" + PORTAL_SIGNATURE


ACCEPT_INVITATION_SUBJECT = u"""Aceptación de {user_first_name} {user_last_name} para unirse a la plataforma {novaideo_title}"""


ACCEPT_INVITATION_MESSAGE = u"""
Hola {recipient_first_name},

{user_first_name} {user_last_name} ha aceptado su invitación para unirse a la plataforma {novaideo_title}.

""" + PORTAL_SIGNATURE


RESETPW_SUBJECT = u"""Su nueva contraseña en la plataforma {novaideo_title}"""


RESETPW_MESSAGE = u"""
Hola {recipient_first_name},

Si desea una nueva contraseña en la plataforma {novaideo_title}, haga clic en la dirección {reseturl} e introduzca su nueva contraseña.

""" + PORTAL_SIGNATURE


PREREGISTRATION_SUBJECT = u"""Por favor, finaliza tu inscripción en la plataforma de democracia deliberativa {novaideo_title}"""


PREREGISTRATION_MESSAGE = u"""
Estimado/a {recipient_first_name},


Tu inscripción en la plataforma de democracia deliberativa {novaideo_title} está casi completada. Queda un último paso por hacer.

Para finalizar tu inscripción, debes hacer clic en el siguiente enlace {url}. Este enlace es válido durante 48 horas, es decir, debes finalizar tu inscripción antes de la {deadline_date}.

Nos complace contarte entre nuestros miembros. Esperamos que tu participación sea para ti una experiencia positiva y gratificante, en un marco plenamente democrático. ¡Bienvenido/a!

Un cordial saludo,

La plataforma {novaideo_title}.""" + PORTAL_SIGNATURE


PREREGISTRATION_MOD_SUBJECT = u"""Por favor, finaliza tu inscripción en la plataforma de democracia deliberativa {novaideo_title}"""


PREREGISTRATION_MOD_MESSAGE = u"""
Estimado/a {recipient_first_name},


Los Verificadores seleccionados al azar en el momento de tu registro han validado la coincidencia entre los Datos de Identidad que habías proporcionado al registrarte en la plataforma, y la de los documentos oficiales de identidad de los que les habías enviado directamente una copia o que les habías mostrado en las reuniones de visoconferencia.

Ahora estamos seguros de que eres la única persona registrada con estos Datos de Identidad en la {novaideo_title} plataforma de democracia deliberativa. Al igual que los demás miembros, sólo tienes una cuenta, y contribuirás a mantener el principio democrático "1 persona = 1 voto".

Sólo te queda una operación para finalizar tu inscripción: haz clic en el siguiente enlace {url}. Este enlace es válido durante 48 horas, es decir, debes finalizar tu inscripción antes de la {deadline_date}.


Nos complace contarte entre nuestros miembros. Esperamos que tu participación sea para ti una experiencia positiva y gratificante, en un marco plenamente democrático. ¡Bienvenido/a!

Un cordial saludo,

La plataforma {novaideo_title}.
""" + PORTAL_SIGNATURE

# Il faudra compléter avec le lieu de naissance
ADMIN_PREREGISTRATION_SUBJECT = u"""Por favor, contribuye a verificar un nuevo registro en la plataforma de democracia deliberativa {novaideo_title}"""


ADMIN_PREREGISTRATION_MESSAGE = u"""
Estimado {recipient_first_name},


Has sido seleccionado al azar por la plataforma de democracia deliberativa {novaideo_title} para actuar como Verificador, cuya tarea es verificar la identidad de una persona que acaba de registrarse en línea.

En cada nuevo registro en la plataforma {novaideo_title}, el sistema selecciona aleatoriamente a tres miembros existentes y les pide que verifiquen la identidad de la persona recién registrada. De hecho, es importante comprobar que cada persona física está relacionada con un miembro de la plataforma, y sólo con uno. De este modo, evitamos que una determinada persona física vote varias veces en la plataforma con varios seudónimos diferentes.

Para realizar esta verificación de la identidad de esta persona, sólo tienes que seguir los siguientes pasos
1. recibirás el día {date_send_id_data} o antes un correo electrónico de la persona que se acaba de registrar en la plataforma. La dirección de correo electrónico de esta persona, desde la que te enviará su correo electrónico, es {subject_email}. Este correo electrónico contendrá
   - o bien un escaneo de un documento de identidad oficial. Por razones de seguridad, aconsejamos a la persona que acaba de inscribirse que oculte su fotografía y su firma al escanearlo: la copia estará deliberadamente incompleta;
   - o una invitación a una breve reunión por videoconferencia (fecha, hora, enlace de acceso) en la que la persona te mostrará su documento de identidad para que puedas leer su contenido.
   
2. Respondes, en su caso, a la persona especificando cuál de las tres fechas y horas propuestas es la más conveniente para ti para la reunión por videoconferencia, y participas en la reunión el día y la hora especificados. 

3. Una vez que hayas recibido el correo electrónico con la copia del documento oficial de identidad o celebrado la reunión por videoconferencia, o si no has recibido una copia del documento oficial de identidad, o una invitación a una reunión por videoconferencia, el día {date_end_vote} 
      (a) conéctate a la plataforma {novaideo_title} y luego 
      (b) accede a la siguiente URL: {subject_url}. En esta página, decidirás si los datos de identidad recibidos de esta persona (que se reproducen a continuación) coinciden con los presentes en el documento de identidad oficial, cuya copia habrás recibido por correo electrónico o que habrás visto durante la reunión por videoconferencia. ¡Ten mucho cuidado! Para que aceptes la inscripción, TODOS los elementos deben ser estrictamente IDÉNTICOS entre los Datos de Identidad recibidos en el momento de la inscripción, y los que figuran en el documento de identidad oficial recibido por correo electrónico o mostrado en la reunión por videoconferencia. En todos los demás casos, incluso con una única y pequeña diferencia, si dudas de la autenticidad del documento de identidad oficial copiado, o si no has recibido la copia del documento de identidad oficial o una invitación a una reunión por videoconferencia antes de {date_end_vote}, DEBES rechazar la inscripción.
      
4. Una vez realizada esta operación, y sea cual sea su resultado, te rogamos que destruyas, en su caso, de tu ordenador todas las copias que tengas del documento oficial de identidad que hayas recibido de la persona recién registrada, y que le informes de esta destrucción, enviándole un correo electrónico a {subject_email}.

###

Los datos de identidad recibidos de la persona en el momento de su inscripción son los siguientes

  Apellido(s): {subject_last_name}
  Nombre(s): {subject_first_name}
  Fecha de nacimiento: {birth_date}
  Lugar de nacimiento: {birthplace}
  Ciudadanía: {citizenship}

###

El proceso de Verificación dura {duration} día(s), es decir, debe completarse en o antes de {date_end_vote}. Más allá de esta fecha, el proceso de Verificación se cerrará, y tu decisión no se tendrá en cuenta. Por defecto, si ningún Verificador ha votado en esa fecha, la inscripción será rechazada.

Saludos cordiales,

La plataforma {novaideo_title}.
""" + PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Nuevo contenido en la plataforma participativa {novaideo_title}"""


ADMIN_CONTENT_MESSAGE = u"""
Hola {recipient_first_name},

Usted ha sido elegido por la plataforma {novaideo_title} para moderar los nuevos contenidos añadidos a la plataforma.

Cada vez que se añade un nuevo contenido (idea o propuesta) a la plataforma {novaideo_title}, el sistema sortea a tres miembros para comprobar la conformidad de este contenido con la {url_moderation_rules} Carta de Moderación. Al distribuir aleatoriamente la moderación, evitamos que esta importante función de control se concentre en unas pocas manos. Contribuimos así a la naturaleza democrática de la plataforma.

Para ejercer su papel de Moderador sobre este nuevo contenido, sólo tiene que conectarse a la plataforma en la siguiente dirección {subject_url} y dar su opinión sobre la conformidad de este contenido con la Carta de Moderación.

La duración de la Moderación es de {duration} día(s). Después de la fecha de {date_end_vote}, la Moderación se cerrará y su voto ya no se tendrá en cuenta. ¡Tenga en cuenta! Por defecto, si ningún moderador ha votado para moderar este contenido en esta fecha, el contenido será aceptado.

""" + PORTAL_SIGNATURE

ALERTANSWER_SUBJECT = u"""Nueva respuesta sobre {subject_type} " {subject_title} """


ALERTANSWER_MESSAGE = u"""
Hola {recipient_first_name},

Se ha dado una nueva respuesta a {subject_type} " {subject_title} ".

"{coment_content}"

Puede encontrarla en {comment_url} y responder a ella.

""" + PORTAL_SIGNATURE

ADMIN_REPORT_SUBJECT = u"""Nueva señalización en la plataforma participativa {novaideo_title}"""


ADMIN_REPORT_MESSAGE = u"""
Hola {recipient_first_name},

Usted ha sido elegido por la plataforma {novaideo_title} para moderar el contenido reportado en la plataforma como potencialmente no conforme con la Carta de Moderación {url_moderation_rules}.

Cada vez que un contenido es denunciado en la plataforma {novaideo_title} como potencialmente no conforme con la Carta de Moderación, el sistema sortea tres miembros al azar para que comprueben la conformidad de este contenido con la Carta de Moderación. Al distribuir aleatoriamente la moderación, evitamos que esta importante función de control se concentre en unas pocas manos. Contribuimos así a la naturaleza democrática de la plataforma.

Para ejercer su papel de Moderador de este contenido, sólo tiene que conectarse a la plataforma en la siguiente dirección {subject_url} y dar su opinión sobre la conformidad de este contenido con la Carta de Moderación.

La duración de la Moderación es de {duration} día(s). Después de la fecha de {date_end_vote}, la Moderación se cerrará y su voto ya no se tendrá en cuenta. ¡Tenga en cuenta! Por defecto, si ningún moderador ha votado para moderar este contenido en esta fecha, el contenido será aceptado.

""" + PORTAL_SIGNATURE


AUTHOR_REPORT_SUBJECT = u"""Nueva señalización en la plataforma participativa {novaideo_title}"""


AUTHOR_REPORT_MESSAGE = u"""

Hola {recipient_first_name},

Su contenido {subject_url} ha sido marcado por un Miembro como potencialmente violatorio de la Política de Moderación {url_moderation_rules}.

Cada vez que un contenido es denunciado como potencialmente contrario a la Carta de Moderación, el sistema sortea a tres miembros al azar para que dictaminen sobre la conformidad de este contenido con la Carta de Moderación.

La duración de la verificación es de {duration} día(s). Después de la fecha de {date_end_vote}, se cerrará la verificación y se le informará de su resultado.

""" + PORTAL_SIGNATURE


ADMIN_PREREGISTRATION_REF_SUBJECT = u"""Tu inscripción en la plataforma de democracia deliberativa {novaideo_title} ha sido rechazada"""

ADMIN_PREREGISTRATION_REF_MESSAGE = u"""
Estimado {recipient_first_name},


Los Verificadores que habían sido seleccionados aleatoriamente en el momento de tu registro NO han validado la coincidencia entre los Datos de Identidad que habías facilitado en la plataforma y los que figuran en los documentos oficiales de identidad de los que les habías enviado copia o que les mostraste en tus reuniones de videoconferencia.

Por lo tanto, lamentamos informarte de que tu registro en la plataforma {novaideo_title} ha sido rechazada. 

Debemos ser muy rigurosos en esta verificación. Si permitiéramos incluso pequeñas discrepancias entre ambos, una misma persona física podría registrarse varias veces, cada vez con pequeñas variaciones en sus datos de identidad, abrir varias cuentas y votar varias veces. Esto vulneraría el principio democrático "una persona = un voto". 

Saludos cordiales,

La plataforma {novaideo_title} plataforma.""" + PORTAL_SIGNATURE

ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""Tu inscripción en la {novaideo_title} plataforma de democracia deliberativa: próximos pasos"""

ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
Estimado/a {recipient_first_name},


Acabas de registrarte en la plataforma {novaideo_title} plataforma de democracia deliberativa. Gracias y enhorabuena. Estamos deseando darte la bienvenida entre nuestros miembros.

Como se describe en nuestro formulario de inscripción, tu registro debe ser validado mediante un procedimiento bastante sencillo, pero riguroso. 

En cada nuevo registro en la plataforma {novaideo_title} el sistema selecciona al azar a tres miembros existentes (los verificadores de este registro específico), y les pide que verifiquen la identidad de la persona recién registrada. De hecho, es importante comprobar que cada persona física está relacionada con un miembro de la plataforma, y sólo con uno. De este modo, evitamos que una determinada persona física vote varias veces en la plataforma con varios seudónimos diferentes. De este modo, mantenemos el principio democrático "1 persona = 1 voto".

Para que se pueda verificar tu identidad, te rogamos que envíes a cada una de las siguientes personas, en correos electrónicos separados, el día {date_send_id_data} o antes
   - una copia escaneada (o una fotografía de un smartphone) de un documento de identidad oficial. Esta copia o fotografía debe mostrar claramente tu(s) nombre(s), apellido(s), fecha y lugar de nacimiento y tu nacionalidad. Por razones de seguridad, te aconsejamos que enmascares tu fotografía y tu firma al escanear o fotografiar tu documento oficial de identidad, de modo que la imagen sea deliberadamente incompleta;
   - o tres propuestas de reunión por videoconferencia que incluyan, para cada propuesta, la fecha en el formato DD-mmm-AAAA (día en dos dígitos, mes en tres letras, año en 4 dígitos), la hora (especificando tu lugar de residencia) y el enlace a la videoconferencia, por ejemplo utilizando la plataforma libre y gratuita https://meet.jit.si/. Todas las fechas y horas que propongas deben ser anteriores a {date_end_vote}, que es el final del periodo permitido para que los Verificadores tomen su decisión.

Después de {date_send_id_data}, si los Verificadores no han recibido una copia de tu documento oficial de identidad o una invitación a una reunión por videoconferencia, tienen instrucciones de rechazar tu inscripción.

Durante la reunión por videoconferencia con cada uno de los Verificadores (si así lo eliges), le mostrarás tu documento oficial de identidad, haciendo visibles tus nombres, apellidos, fecha y lugar de nacimiento y nacionalidad, y ocultando tu fotografía y tu firma si lo deseas. 

Los Verificadores asignados a la comprobación de tu identidad son
{moderators}

Recibirás el resultado de este proceso de verificación de la identidad al final del tiempo dado para que los Verificadores tomen su decisión, es decir, a más tardar el {date_end_vote}.

Los Verificadores tienen instrucciones, en su caso, de destruir todos los archivos que contengan la copia de tu documento oficial de identidad una vez que hayan realizado la verificación de tus datos de identidad, y de informarte una vez que lo hayan hecho. 

Un cordial saludo,

La plataforma {novaideo_title}.""" + PORTAL_SIGNATURE


REMINDER_ADMIN_PREREGISTRATION_SUB_SUBJECT = u"""RECORDATORIO - FECHA LÍMITE MAÑANA: Por favor, activa la verificación de tu identidad para registrarte en la {novaideo_title} plataforma de democracia deliberativa"""

REMINDER_ADMIN_PREREGISTRATION_SUB_MESSAGE = u"""
## Si ya enviaste la copia de tu documento oficial de identidad o propusiste una reunión por videoconferencia a los Verificadores, por favor ignora este correo electrónico y acepta nuestras disculpas ##

Estimado/a {recipient_first_name},

Como recordarás, tu inscripción en la plataforma de democracia deliberativa {novaideo_title} plataforma de democracia deliberativa está ahora sujeta a la verificación de tu identidad. El plazo para que envíes a los verificadores una copia de tu documento oficial de identidad o una invitación a una reunión por videoconferencia es MAÑANA {date_send_id_data}.

A continuación encontrarás el recordatorio del procedimiento a seguir (incluyendo las direcciones de correo electrónico de los Verificadores) y de la justificación de este procedimiento.

Esperamos recibirte en nuestras actividades.

Un cordial saludo,

La plataforma {novaideo_title}.

## Recordatorio del procedimiento y de su justificación ##
En cada nueva inscripción en la plataforma {novaideo_title} el sistema selecciona aleatoriamente a tres miembros existentes (los Verificadores de este registro específico), y les pide que verifiquen la identidad de la persona recién registrada. De hecho, es importante comprobar que cada persona física está relacionada con un miembro de la plataforma, y sólo con uno. De este modo, evitamos que una determinada persona física vote varias veces en la plataforma con varios seudónimos diferentes.

Para que tu identidad sea verificada, te rogamos que envíes a cada una de las siguientes personas, en correos electrónicos separados, en o antes de la {date_send_id_data}:
   - una copia escaneada (o una fotografía de un smartphone) de un documento de identidad oficial. Esta copia o fotografía debe mostrar claramente tu(s) nombre(s), apellido(s), fecha y lugar de nacimiento y nacionalidad. Por razones de seguridad, te aconsejamos que enmascares tu fotografía y tu firma al escanear o fotografiar tu documento oficial de identidad, de modo que la imagen sea deliberadamente incompleta;
   - o tres propuestas de reunión por videoconferencia que incluyan, para cada propuesta, la fecha en el formato DD-mmm-AAAA (día en dos dígitos, mes en tres letras, año en 4 dígitos), la hora (especificando tu lugar de residencia) y el enlace a la videoconferencia, por ejemplo utilizando la plataforma libre y gratuita https://meet.jit.si/. Todas las fechas y horas que propongas deben ser anteriores a {date_end_vote}, que es el final del periodo permitido para que los Verificadores tomen su decisión.

Después de {date_send_id_data}, si los Verificadores no han recibido una copia de tu documento oficial de identidad o una invitación a una reunión por videoconferencia, tienen instrucciones de rechazar tu inscripción.

Durante la reunión por videoconferencia con cada uno de los Verificadores (si así lo eliges), le mostrarás tu documento oficial de identidad, haciendo visibles tus nombres, apellidos, fecha y lugar de nacimiento y nacionalidad, y ocultando tu foto y firma si así lo deseas. 

Los Verificadores asignados a la comprobación de tu identidad son
{moderators}

Recibirás el resultado de este proceso de verificación de la identidad al final del tiempo dado para que los Verificadores tomen su decisión, es decir, a más tardar el {date_end_vote}.
""" + PORTAL_SIGNATURE

# INFORMATION SANS QU'UNE ACTION SOIT REQUISE:
# Pourrait faire l'objet d'une simple alerte interne, sans mobiliser un courriel spammant la boîte de l'utilisateur

PUBLISHEDCHALLENGE_SUBJECT = u"""Decisión de los moderadores de publicar el desafío " {subject_title} """


PUBLISHEDCHALLENGE_MESSAGE = u"""
Hola {recipient_first_name},

El reto "{subject_title}" bajo {subject_url} acaba de ser publicado por los moderadores en la plataforma {novaideo_title}.

""" + PORTAL_SIGNATURE

ARCHIVECHALLENGE_SUBJECT = u"""Decisión de los moderadores de archivar el desafío" {subject_title} """


ARCHIVECHALLENGE_MESSAGE = u"""
Hola {recipient_first_name},

El reto "{subject_title}" ha sido archivado por los moderadores por el siguiente motivo:

{explanation}

Puede encontrar su reto en {subject_url}.

""" + PORTAL_SIGNATURE


PRESENTATION_CHALLENGE_SUBJECT = u"""Presentación del desafío " {subject_title} """


PRESENTATION_CHALLENGE_MESSAGE = u"""
Hola,

{my_first_name} {my_last_name} desea presentarle el desafío " {subject_title} " en la plataforma {novaideo_title}. Puede acceder a este desafío en: {subject_url}.

""" + PORTAL_PRESENTATION + PORTAL_SIGNATURE


ADMIN_CONTENT_SUBJECT = u"""Nuevo contenido en la plataforma participativa {novaideo_title}"""


ADMIN_CONTENT_SUB_MESSAGE = u"""
Hola {recipient_first_name},

Su contenido ha sido sometido a moderación.

Cada vez que se añade un nuevo contenido a la plataforma {novaideo_title}, el sistema sortea a tres miembros para comprobar la conformidad de este contenido con la Carta de Moderación {url_moderation_rules}.

La duración de la verificación es de {duration} día(s). Después de la fecha de {date_end_vote}, se cerrará la verificación y se le informará de su resultado.

""" + PORTAL_SIGNATURE


ALERTCOMMENT_SUBJECT = u"""Nuevo comentario sobre {subject_type} " {subject_title} """


ALERTCOMMENT_MESSAGE = u"""
Hola {recipient_first_name},

Se ha realizado un nuevo comentario sobre {subject_type} "{subject_title}".

"{comment_content}"

Puede encontrarlo en {comment_url} y dar una respuesta.

""" + PORTAL_SIGNATURE

ALERTDISCUSS_SUBJECT = u"""Nuevo mensaje añadido a su discusión sobre " {subject_title} """


ALERTDISCUSS_MESSAGE = u"""
Hola {recipient_first_name},

Se ha añadido un nuevo mensaje a su hilo con "{subject_title}".

"{comment_content}"

Puede encontrarlo en {comment_url} y hacer una respuesta.

""" + PORTAL_SIGNATURE

ALERTRESPONS_SUBJECT = u"""Una persona ha respondido a un comentario sobre {subject_type} " {subject_title} """


ALERTRESPONS_MESSAGE = u"""
Hola {recipient_first_name},

Alguien ha respondido a un comentario sobre {subject_type} " {subject_title} " que se encuentra bajo {comment_url}.

"{comment_content}"

""" + PORTAL_SIGNATURE


NEWSLETTER_SUBSCRIPTION_SUBJECT = u"""Boletín de inscripción"""

NEWSLETTER_SUBSCRIPTION_MESSAGE = u"""
Hola {first_name} {last_name},

Ya está suscrito al boletín {newsletter_title}.

""" + PORTAL_SIGNATURE

NEWSLETTER_UNSUBSCRIPTION_SUBJECT = u"""Darse de baja del boletín"""

NEWSLETTER_UNSUBSCRIPTION_MESSAGE = u"""
Hola {first_name} {last_name},

Se ha dado de baja del boletín {newsletter_title}.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_SUBJECT = u"""Solicitud de baja de su cuenta en la plataforma {novaideo_title}"""

QUIT_REQUEST_MESSAGE = u"""
Estimado {recipient_first_name} {recipient_last_name},

Hemos recibido una solicitud de renuncia en su cuenta de la plataforma {novaideo_title}.
Si ha solicitado su baja en la plataforma, haga clic en el siguiente enlace de confirmación: {url}, antes de la fecha {deadline_date}.

ADVERTENCIA: esta acción es IRREVERSIBLE. Si hace clic en este enlace, dejará de tener acceso a la plataforma, su cuenta será destruida y todo el contenido vinculado a su cuenta se atribuirá irreversiblemente a un autor anónimo.
No podrá volver a registrarse en la plataforma, creando una nueva cuenta en blanco, antes de un periodo igual a {tquarantaine} días.

Si no ha solicitado abandonar la plataforma, ignore este correo electrónico y su cuenta permanecerá activa.
No obstante, le recomendamos que cambie su contraseña para evitar que su cuenta sea pirateada.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_CONFIRMATION_SUBJECT = u"""Su renuncia a la plataforma de e-democracia {novaideo_title} ha sido tenida en cuenta"""

QUIT_REQUEST_CONFIRMATION_MESSAGE = u"""
Estimado {recipient_first_name} {recipient_last_name},

Usted ha deseado renunciar a la plataforma e-democracia {novaideo_title}. Lo lamentamos, por supuesto, pero respetamos su elección. Por la presente le informamos de que:
* su cuenta ha sido desactivada. Sólo recibirá un mensaje nuestro en el futuro (véase más abajo)
* todo el contenido de su cuenta ha sido atribuido irreversiblemente a un autor Anónimo
* los datos de identidad que nos facilitó al registrarse (nombres, apellidos, fecha y lugar de nacimiento) y su dirección de correo electrónico se conservarán durante {tquarantaine} días, para evitar que pueda volver a registrarse durante este periodo. El objetivo es evitar que las personas que se han comportado de forma inadecuada en la plataforma (y que, por tanto, tienen mala reputación) vuelvan inmediatamente con un nuevo seudónimo y una reputación limpia.
* Transcurrido este periodo, es decir, el {date_tquarantaine}, recibirá un correo electrónico nuestro informándole de que sus Datos de Identidad y su dirección de correo electrónico han sido eliminados definitivamente de nuestra base de datos.

""" + PORTAL_SIGNATURE


QUIT_REQUEST_DELETION_SUBJECT = u"""¡Sus datos de identidad y dirección de correo electrónico han sido eliminados permanentemente de la base de datos de la plataforma {novaideo_title}!"""

QUIT_REQUEST_DELETION_MESSAGE = u"""
Estimado {recipient_first_name} {recipient_last_name},

Hoy, sus datos de identidad (nombre, apellidos, fecha y lugar de nacimiento) y su dirección de correo electrónico han sido eliminados definitivamente de nuestra base de datos. No recibirá más correos electrónicos nuestros.

""" + PORTAL_SIGNATURE


mail_locale = 'es'

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
