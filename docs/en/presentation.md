# Nova-Ideo, agile participatory innovation

**Author:** Michaël Launay — **Source:** Ecréall article, edition
number 57, 30 September 2021 ("Free participatory innovation").
**Transcription note (18 July 2026):** this document is the faithful
markdown transcription of the functional presentation article — the
product's best documentation, according to the audit. The 2021 text is
kept as is: the offers, addresses and perspectives it cites are of
their time (see the README and [`audit.md`](audit.md) for the current
state). The screenshots are those of the 2021 interface; their
automatic regeneration is described at the end of the document.
Version française : [`../fr/presentation.md`](../fr/presentation.md).

> Whether for "participatory democracy" or "participatory innovation",
> most CivicTech tools rest on the work of crowds; we present here a
> tool that makes the crowd think (brainstorming).

## 1. Participatory?

From 7 to 9 December 2016, Paris hosted the Open Government
Partnership, a forum gathering many so-called "participatory
democracy" initiatives. Very much in fashion, the term expresses a
need for citizens to reclaim decision-making. Yet many associations,
including La Quadrature du Net, pointed out that for now it was mostly
political communication [http://lqdn.fr/node/10118].

The flagship tool of participatory democracy is the dematerialisation
of citizen consultations, and many solutions exist, some of them open
source or free software, that are beginning to meet that need.

Participatory democracy has its counterpart in the corporate world,
participatory innovation, which often takes the shape of a digital
suggestion box.

In both cases, the point is to ask people's opinion by having them
vote or comment on texts, and to let ideas, proposals or
counter-proposals emerge using the wisdom of the crowd.

In both cases, the pitfall is to raise enthusiasm without being able
to cope with too many ideas or comments.

We detail here one of the solutions selected by Etalab for the OGP
Toolbox [https://ogptoolbox.org/fr/tools/7873] and made available to
administrations: the participatory-innovation solution Nova-Ideo,
under the free AGPL v3 licence.

Written in Python 3 with Pyramid, its purpose is to foster
interactions between the members of a collective, to improve the
harvesting of ideas, to organise the co-writing of action proposals,
to create "challenges" answering a given problem; finally it lets
everyone support or reject the published ideas, questions, answers or
proposals.

Its strength is to get proposals produced using the collaboration and
competition mechanisms (coopetition) found in the iterative work
cycles of open-source projects — in short, this tool is strongly
oriented towards human interaction.

## 2. Installing Nova-Ideo, or SaaS

Nova-Ideo is available on GitHub and is dockerised, hence available on
Docker Hub.

To install it locally, simply follow the instructions of the README
file at https://github.com/ecreall/nova-ideo. In that case no free
support is provided by Ecréall and maintenance would be the subject of
a specific contract.

However, Nova-Ideo can be used directly as SaaS from
https://www.nova-ideo.com; free of charge provided the content is
public, under a "Basic" subscription if the content must be
confidential, under a "Business" subscription if the solution must be
tied to an information system.

## 3. First use: creating an idea or a question

Creating an idea or a question is very simple. Either press the green
content-creation button, which pops up the entry form, or start
filling the input field, which reveals the rest of the form.

The difference between an idea, a question or a remark is made at
entry time. Nova-Ideo takes care of treating the content differently
by showing only the actions relevant to that content type.

The user enters the idea or question, its keywords, and can attach one
or several files. They can then directly publish the idea and
automatically create a working group, only publish the idea, or save
the idea or question to work on it later; finally they can abandon the
edit.

When entering a question, the user can create an open question or a
questionnaire by entering the choices.

For an open question, the answers are free texts aggregated directly
under the idea, and every Member of the platform can support or reject
the proposed answers. Answers are displayed under the question in
support order.

For choices, each answering Member selects the desired choice and then
argues the selection.

All of this is fairly fluid, but each action has consequences that
commit the nature of the work.

![Idea entry form](../images/presentation/fig-01-idea-form.png)

*Illustration 1: Idea entry form; here the member adds an idea they
called "Questions flash".*

## 4. The problem space

### 4.1 The idea is personal while the proposal is collective

People naturally identify with their idea, so criticising an idea
often amounts to criticising its author. In short, keeping some
distance from one's productions is necessary to work collectively with
serenity. Conversely, as much as authors will fight for their idea,
they will naturally keep their distance when the work is collective —
so a motivation must be found for the work to get done.

Nova-Ideo considers the idea as a document with a single author which,
once published, can no longer be modified — only duplicated to be
modified ("fork").

Nova-Ideo displays the set of ideas as a list or as boxes, whose
search and sort criteria can be chosen.

![Home page, list view](../images/presentation/fig-02-home-list.jpg)

*Illustration 2: Home page showing the list of ideas; this view is
configurable.*

![Home page, block view](../images/presentation/fig-03-home-blocks.jpg)

*Illustration 3: Home page showing the ideas as blocks; this view is
also configurable.*

### 4.2 Forking content

Duplicating an idea lets anyone appropriate somebody else's idea and
modify it while acknowledging the previous author's paternity.

Duplicating a proposal lets a new working group build a new proposal
from another group's work, whatever its state. Work is thus never
lost, but endlessly malleable to explore new paths.

Nova-Ideo keeps a version history, accessible from the actions menu.

![Forking an idea](../images/presentation/fig-04-idea-fork.jpg)

*Illustration 4: Duplicating (forking) an idea — this naturally
yields the tree of ideas.*

### 4.3 Content maps

Nova-Ideo traces content duplications and reuse and lets one navigate
the graph of content parentage and links.

![Dependency graph](../images/presentation/fig-05-dependency-graph.png)

*Illustration 5: Display of a content's dependency graph.*

### 4.4 Idea Challenges

The application allows creating idea challenges, thus organising the
platform's presentation by making those challenges visible upon
arrival.

Challenges can also structure the presentation of ideas by grouping
ideas or questions by theme.

Challenges can be open to all Members or restricted to a subset of
Members.

A deadline can also be given to a Challenge, beyond which contributing
is no longer possible.

![Creating a challenge](../images/presentation/fig-06-challenge-create.jpg)

*Illustration 6: Creating a challenge.*

Once created, the Challenge produces a natural coopetition of ideas:
every Member sees what the others proposed and can in turn propose
newer, more innovative ideas, improve the existing ones, or create or
join working groups around the Challenge's ideas.

![Published challenge at the top of the site](../images/presentation/fig-07-challenge-published.jpg)

*Illustration 7: The published challenge is visible at the top of the
site.*

### 4.5 Group work

Humans behave in an essentially cooperative way [see 8 min of
https://youtu.be/Adm-8rNBrCU]. They form groups to solve problems
collaboratively; communication then becomes the main activity
sustaining the reflection: the more the group exchanges, the better
its chances of reaching a solution. The more complementary the
participants' experiences/profiles, the better their solutions.
However, if the participants of a group have different cultures, they
may need time to understand each other. And if their convictions are
opposed, the debates must be orchestrated to transform their richness
and avoid score-settling
[http://www.cornu.eu.org/texts/guide-de-l-animateur].

For this, Nova-Ideo puts group work forward and lets it be
orchestrated through a business process configurable from the
administration interface, or fully adaptable by modifying the code —
pending an integrated process editor.

Groups are created either when an idea is published, or by clicking
the "Create a working group" action; the working group will then have
to co-write the content of a Proposal automatically created from the
initial idea and assigned to that group.

The Proposal's edit form allows rich text. That rich text can have its
formatting constrained by the administrator so as to follow a document
template.

![Creating a proposal](../images/presentation/fig-08-proposal-from-idea.png)

*Illustration 8: Creating a proposal from an idea — the idea is taken
up in the summary. The rich text allows, for instance, explaining how
the idea can be put into practice. It is an input area allowing
co-writing.*

### 4.6 The optimal group size

As soon as a group exceeds about ten people, it becomes hard for its
participants to know each other well enough to be confident, hence
spontaneous and effective.

Not only will participants withdraw, but the number of discussions
before action grows with the factorial of the number of participants
[https://fr.wikipedia.org/wiki/Le_Mythe_du_mois-homme].

It is counter-intuitive, but to recover the effectiveness of a small
group of fewer than 12 participants, one must exceed a hundred
participants — in a large group, the low probability of action is
compensated by a large number of actors
[http://ebook.coop-tic.eu/francais/wakka.php?wiki=CommentProduireUnDocumentAPlusieursCentai].

Moreover, the participants of a large group seek to organise
themselves, which very often ends in a classic pyramidal hierarchy
that ends up smothering the ideas of its base.

We go in circles, because the embryo of good ideas and answers comes
from anyone, and for an idea, a question, an answer or a proposal to
be good, it must have been worked on collectively to reflect all
points of view.

The simplest solution is to have several small groups working in
competition on the same subject, even if another group merges the
different proposals.

That is why Nova-Ideo limits group size to 12 participants by default
— configurable online, which allows experimenting.

Every member can join a working group by clicking the "Join the group"
button, but as soon as the participant limit is reached, the member is
added to the list of candidates waiting for a seat.

The maximum number of groups joined by a participant is itself
configurable; by default it is 5.

![Joining a group](../images/presentation/fig-09-group-join.png)

*Illustration 9: To join a group, just click the "Participate"
button.*

### 4.7 Iterative work and the co-writing modes

Even with a group of reasonable size, it is rare to write a perfect
proposal on the first try — all the more so when several participants
of a working group co-write the text.

In short, work must be organised in iterations!

Various development methods have shown the necessity of "short"
deadlines.

Nova-Ideo bets on taking up the "timeboxing" mechanism of agile
methods to organise the iterations, but leaves the choice of their
duration to the group's participants.

![Iteration cycle state](../images/presentation/fig-10-iteration-state.jpg)

*Illustration 10: The state of a Proposal's iterative improvement
cycle is visible by clicking the blue process tab.*

![Voting the iteration duration](../images/presentation/fig-11-iteration-vote.png)

*Illustration 11: Vote on the duration of a Proposal's improvement
iteration.*

![Voting the iteration duration (continued)](../images/presentation/fig-12-iteration-vote-result.png)

*Illustration 12: Vote on the duration of a Proposal's improvement
iteration.*

#### Choosing the work mode and the iteration duration

For each work iteration, the participants vote on publishing the
proposal or starting a new iteration; and should a new iteration
start, they vote on its duration and its work mode.

Three co-writing modes are currently possible: wiki-style without
validation, sequential with validation, parallel with amendments.
These modes are detailed below.

The purpose of these co-writing modes is to converge towards a
proposal reaching the group's consensus, published for support.

The modes can be enabled depending on the number of participants of
the working group.

At any moment, a participant may leave their group; and since any
member can duplicate a working group's proposal to create a new
dynamic, efforts are expected never to be lost, but reused and
transformed.

Centring the work on short cycles is meant to prevent a working group
from bogging down.

Nova-Ideo reminds the participants of the iteration's end or of the
need to vote on publication.

![Choosing the work mode](../images/presentation/fig-13-work-mode-choice.png)

*Illustration 13: Choosing the work mode of a Proposal's improvement
iteration.*

#### The wiki mode (no validation of changes)

In the wiki-style work mode, the participants' changes need not be
validated by the other participants of the working group: upon saving
they generate a new version of the proposal. Very simple, this mode
suits 80 % of cases, but its main criticism is giving disproportionate
weight to the last modification — hence to running down the clock
before the publication vote.

#### The validation mode

Working with validation consists, for each modification of a proposal,
in having it accepted, rejected or modified by another participant of
the working group.

The process is sequential and allows only one edit at a time. It is
nevertheless well suited to syntactic-correction-style changes.

![Validating changes](../images/presentation/fig-14-change-validation.png)

*Illustration 14: Validating a Proposal's changes — the participant
can accept, reject or modify the change submitted by the previous
participant.*

#### The amendment mode

Co-writing happens in parallel: each participant modifies the proposal
on their side without knowing the others' changes. Those changes will
therefore be put in competition.

For instance, a participant modifies a proposal to generalise its
meaning and takes the opportunity to rephrase some sentences. Here we
have several modifications of the proposal: some concern the
generalisation of meaning and impact several sentences at different
places of the text, others are rephrasings independent of one another.

For that reason, when a participant has finished working, they must
group and explain their changes. Once done, they must prepare their
amendments and describe their intention. An amendment thus contains
one or several correlated modifications.

In our example, the participant will create one amendment containing
the various rewrites about the generalisation of meaning, and separate
amendments for the other rephrasings.

At the iteration's deadline, the amendments are put to the vote under
the majority-judgment ballot detailed below.

The participants vote the proposed amendments against one another and
against the original version, only when they bear on the same parts of
the proposal or have the same intention.

Using this voting method makes consensus attainable.

![Creating amendments](../images/presentation/fig-15-amendments-creation.png)

*Illustration 15: Creating a Proposal's amendments — just group the
changes and justify them.*

Once the vote on the amendments is done, Nova-Ideo determines the
changes that reached consensus and applies them. It creates a new
version of the proposal and submits it to the group for a vote on
publication or on starting a new work iteration.

### 4.8 Majority judgment

Majority judgment is a voting method stemming from the research of
Rida Laraki and Michel Balinski
[https://fr.wikipedia.org/wiki/Jugement_majoritaire]; it is clearly
explained by David Louapre on his YouTube channel "Science étonnante"
[https://youtu.be/ZoGH7d51bvc].

It answers the problems of classic voting, where one does not express
an opinion on every choice and ends up voting for the lesser evil
closest to one's view.

Here Nova-Ideo asks each participant to give every amendment,
including the original text, a grade ranging from "Excellent", "Very
good", "Good", "Fairly good", "Passable", "Insufficient" to "To
reject". Nova-Ideo computes the median of the grades received by each
amendment and keeps the one with the best majority grade. We thus have
a consensus allowing, at the end of each round, the generation of a
new version of the proposal.

![Majority judgment](../images/presentation/fig-16-majority-judgment.png)

*Illustration 16: Majority judgment of a Proposal's amendments.*

![New version](../images/presentation/fig-17-new-version.png)

*Illustration 17: Generation of a new version of the Proposal.*

### 4.9 Discussion threads

Nova-Ideo provides discussion-thread mechanisms usable on every
content or directly on conversation topics.

To leave a comment or answer one, just go to the right place and click
the comment button.

Comments can include images, links, files or carousels.

![Discussion threads](../images/presentation/fig-18-discussions.jpg)

*Illustration 18: Members can feed discussion threads on the
contents, but also in general threads reachable by clicking the blue
bubble on the left.*

### 4.10 Notifications

Nova-Ideo can use the browsers' notification mechanism to alert on any
kind of event, such as the creation of a content, the publication of a
comment, the expiry of a date.

![Notifications](../images/presentation/fig-19-notifications.jpg)

*Illustration 19: Members can be alerted through notifications.*

### 4.11 Supporting or rejecting content

When an idea, a proposal or an answer to a question is published,
every member can support or reject it.

Once again, Nova-Ideo uses a "social" trick: the scarcity of support
tokens. Each member owns 7 tokens they can place to support or reject
a content. Having used all their tokens, they must arbitrate and move
some of them to allocate them to other contents. Nova-Ideo records
those moves, making the evolution of support visible — which allows,
for instance, finding seasonality in support.

Suppose, for example, that a bicycle-sharing proposal is made in an
organisation: one can bet the members will have removed their token in
winter and put it back in summer.

Support is given using the elevator-style buttons on the left of the
contents.

#### Steering-committee opinions

Nova-Ideo can manage decision committees, which can rule on putting
proposals into practice.

For that, the committee ranks the proposals or ideas by, for instance,
their number of supports, then rules and publishes its opinion.

Nova-Ideo offers several sorting algorithms which can use the support
history.

For instance, if a steering committee always meets in winter and ranks
proposals by support count, it will never see the bicycle-sharing
proposal described above. Now, if it adds a historical sort criterion,
it will find the proposal and note its interest for the coming summer.

Once its decision is taken, the committee publishes its opinion on the
contents, materialised as a traffic light.

![Steering committee opinion](../images/presentation/fig-20-steering-opinion.jpg)

*Illustration 20: Steering-committee members can give an opinion,
which releases all the tokens positioned on the content.*

## 5. The code and contributions

The project stems from the proof of concept of Amen Souissi's PhD
thesis, "Business-process-centred modelling for the complete
generation of collaborative portals", published on HAL at
[https://ori-nuxeo.univ-lille1.fr/nuxeo/site/esupversions/40ca4edc-ad93-4fbe-b70e-eb1b33b50e6a].

The research showed it was possible to generate 100 % of a
collaborative portal's code from the modelling of a company's business
processes. The result was functionally correct, but the interface
hardly usable.

It was then decided to invert the method: start from an "almost
perfect" code written by hand as if it had been generated, in order to
develop the libraries, then rewrite the whole transformation chain and
the diagrams behind the "ideal" tool.

Currently the libraries are written, and the code of the Nova-Ideo
application is to serve as the guiding thread for writing a new
transformation chain, elaborating a modelling formalism merging UML
and BPMN, and developing a Modeller based on that notation.
[http://video-pyconfr2015.paulla.asso.fr/112_-_Michael_Launay_-_Nova-Ideo,_une_boite_a_idees_collaborative.html]

Nova-Ideo is based on those business-process modelling libraries:
creating a process amounts to instantiating various Python classes and
nesting them into one another.

A Nova-Ideo programming API was developed in GraphQL; it allows
consulting and creating contents from other programs.

You can contribute to Nova-Ideo's evolution and propose your
improvement ideas by registering on evolutions.nova-ideo.com — which
is of course a Nova-Ideo instance.

## 6. Five years of innovation: an assessment

Although he left Ecréall in early 2019, Amen Souissi, the main
developer, sporadically continued the project's development, which was
then supported more intensely by Michaël Launay and partially by
Vincent Fretin.

The feedback from Engie/Axima and from KuneAgi led to the following
observations:

- a need to anonymise participations;
- a need to simplify the majority-vote process, either through an
  intelligent assistant or through human-machine-interface nudges;
- a need to merge the notions of idea and proposal — an AI based on
  CamemBERT (https://camembert-model.fr/) is to identify ideas and
  automate the highlighting of links between ideas and proposals;
- the business-process engine, fruit of Ecréall's R&D, would have
  everything to gain from a migration to Rust.

These new steps are the object of the 2021 work.

## 7. Conclusion

Nova-Ideo is a rich application that trusts everyone's will to
collaborate; yet participatory democracy or participatory innovation
are not only a matter of tools, and much social experimentation will
still be needed to find the right springs for everyone to speak and be
heard. But one may think that with the improving knowledge of how
human groups work, new solutions will come, and that one day holacracy
[https://fr.wikipedia.org/wiki/Holacratie] will not be just a concept.

*Michaël Launay — Founding manager of Ecréall. GNU/Linux user since
2003.*

---

## Appendix (2026): updating the screenshots

The twenty figures of this document carry **stable semantic names**
(`docs/images/presentation/fig-NN-<subject>.<ext>`): regenerating them
is enough to bring the document up to date, without touching the text.

The [`tools/docshots.py`](../../tools/docshots.py) script automates
that regeneration with Playwright: it logs into an instance (URL and
credentials via environment variables), walks the documented journeys
and rewrites each figure under the same name. First use:

```bash
pip install playwright && playwright install chromium
DOCSHOTS_BASE_URL=https://my-instance \
DOCSHOTS_LOGIN=admin DOCSHOTS_PASSWORD=... \
python tools/docshots.py            # every figure
python tools/docshots.py fig-02 fig-03   # a selection
```

The script is a deliberately readable scaffold: the `SHOTS` table at
the top of the file maps each figure to its page and to the gestures
bringing it on screen — that table is what gets refined on the first
run against the modernised instance (the current captures date from
the 2021 interface).
