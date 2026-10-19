# Chapter 1 — AGI and the Meaning of Gradual Transformation

## Abstract

This chapter establishes the conceptual grammar for On Gradual AGI. It first fixes a stipulative, series-wide definition of artificial general intelligence (AGI) using the unaugmented human capability envelope and a partial-order, profile-first representation. It then separates the modifier gradual from that definition. Phenomenal gradualness is a descriptive classification: for a specified AGI-related transformation and declared individuation rule, the transformation is gradual when its relevant realization is not exhausted by one event. Principled graduality is distinct: information-responsive iteration combined with preserved revisability, whose justification depends on the decision setting rather than following from gradualness itself. The chapter then introduces Potential–Realization Separation—the distinction between what AI can do and what becomes realized for specified groups under actual conditions—and illustrates it through Go, mathematics, and radiology. The result is an opening framework that treats AGI definition, capability comparison, realization, and decision principles as related but non-identical objects.

**Keywords.** artificial general intelligence; AGI; Gradual AGI; gradualness; graduality; realization; human capability envelope; partial order; capability profile; Potential–Realization Separation

## Chapter 1 Reader Guide

*AGI and the Meaning of Gradual Transformation*

### One-line summary

This chapter defines AGI independently of gradualness, distinguishes phenomenal gradualness from principled graduality, and establishes Potential–Realization Separation.

### Principal Contributions

This chapter makes the following principal contributions, consolidating definitions and distinctions developed across the Gradual AGI series into the book’s opening conceptual grammar.

1.  **An AGI comparison framework.** Definition 0 specifies AGI through comparison with the best per-domain unaugmented human performance. The comparison requires declared domains, baselines, assistance conditions, and coverage, without reducing generality to a single score.

2.  **A criterion of phenomenal gradualness.** Phenomenal gradualness concerns the form of transformation, rather than subjective experience. Given an individuation rule fixing the transformation under study, a specified AGI-related transformation is gradual when its relevant realization is not exhausted by one event. Gradualness does not require slow, smooth, or continuous change.

3.  **A distinction between phenomenal gradualness and principled graduality.** The former concerns the form of transformation; the latter combines information-responsive iteration with preserved revisability. A description of gradual change does not by itself establish that change ought to proceed gradually.

4.  **Potential–Realization Separation.** The chapter distinguishes what AI can do from what becomes realized for specified groups under specified conditions. Chapter 2 refines this separation by distinguishing realization, realized consequence, and benefit. Chapter 4 formalizes this problem.

### Prerequisites

No earlier chapter is required. The chapter introduces its limited formal notation, including partial-order comparison.

### Reading routes

**Definition path.** Sections 1.1–1.3 establish Definition 0, the comparison profile, and what general means in the book.

**Gradualness and graduality path.** Sections 1.4–1.6 explain what gradual modifies, state the criterion for phenomenal gradualness, and distinguish it from principled graduality.

**Realization path.** Sections 1.7–1.8 shift from capability to realization and illustrate the distinction in Go, mathematics, and radiology.

**Book path.** Chapter 1 opens Part I, Orientation, which Chapter 2 completes. Part II, Architecture (Chapters 3–6), develops the Multi-Plateau Framework, the realization mapping, the synchronization model, and the evaluation of trajectories. Part III, Mediation (Chapters 7–11), examines human, institutional, and temporal processes that shape realization, together with the evidence and epistemic discipline through which claims about it are assessed. Part IV, Integration (Chapter 12), brings the components together provisionally, without claiming a closed or final system.

### Evidence and limits

The declared domain scope is not a fixed catalog of cognitive abilities. Comparisons must state the system boundary and assistance conditions; measured performance is not a complete theory of intelligence.

Definition 0 is stipulative: it provides the book’s comparison grammar rather than demonstrating that AGI has arrived. A single benchmark or aggregate score does not settle the comparison. The gradualness criterion depends on a declared individuation rule fixing the transformation being assessed. Principled graduality does not follow as an ought from phenomenal gradualness, and preserved revisability does not guarantee reversible outcomes.

The Go, mathematics, and radiology cases illustrate the capability–realization distinction rather than validate the framework. They do not establish a general rate of transformation or a forecast of arrival.

## 1.1 Why AGI Needs a Definition Before It Needs a Forecast

Discussions of artificial general intelligence often begin with a date: when will AGI arrive? The question is understandable, but it presupposes that the object being forecast has already been defined with sufficient clarity. In practice, that assumption rarely holds. Different organizations and researchers use AGI to refer to different combinations of breadth, autonomy, human-level performance, economic usefulness, transfer, adaptability, or superhuman capability. A forecast can therefore appear precise while its referent remains unstable. Contemporary definitions illustrate the variation: OpenAI has emphasized highly autonomous systems outperforming humans at most economically valuable work, while Google DeepMind has operationalized AGI through levels of performance and generality, with autonomy treated separately (OpenAI 2018; Morris et al. 2024).

This book takes the opposite order. Before asking when AGI may arrive, whether it has already arrived, or what follows from its arrival, it first fixes what the term means inside the present framework. That definition is stipulative rather than empirical: it specifies the object to be analyzed rather than claiming that the world must conform to one uniquely correct definition of AGI. Policy, industry, and public discourse may use the term differently. The point here is not to invalidate those uses, but to make this book’s referent explicit enough that later claims can be evaluated against it.

The distinction matters because much of the apparent disagreement around AGI is actually disagreement about thresholds. One observer may treat human-level performance across many economically valuable tasks as sufficient. Another may require broad transfer and autonomy. A third may reserve the term for systems that exceed humans across nearly all cognitive domains. These are not merely different estimates of the same quantity. They can be different definitions of the object itself.

The Gradual AGI framework therefore begins by separating three questions that are often collapsed:

What is AGI?

How should progress relative to that object be represented?

How does capability become realized across society?

The first question is answered directly in this chapter. The second begins with the domain-wise, partial-order representation introduced in §1.2 and is developed further by later analytical machinery. The third becomes the central problem of the book: realization.

This ordering also prevents a common mistake. The term Gradual AGI does not mean that the definition of AGI itself contains an assumption of slow or continuous arrival. AGI must first be defined independently. Only then can the modifier gradual be introduced and defended as a separate claim about the form of transformation associated with it.

## 1.2 Definition 0 — Artificial General Intelligence

The book adopts Definition 0 in the settled, series-wide form introduced in Gradual AGI Series \#7 (Contestation) (W.H.L. and Claude 2026g), building on the partial-order representation of trajectories already adopted in Series \#5 (Optimization) (W.H.L. et al. 2026j). The definition fixes a comparison object and reference relation; it does not, by itself, supply a universal binary decision rule for declaring that “AGI has arrived.”

**Definition 0 — Artificial General Intelligence.** AGI denotes artificial intelligence whose capability profile matches or exceeds the best human capability attainable across the domains in which humans exercise intelligence. The reference class is the unaugmented human envelope.

Definition 0 is intentionally compact. The following clarifications specify how it should be used rather than adding new criteria to the definition.

First, “matches or exceeds” is not treated as a comparison on one universal scalar. Human capability is heterogeneous across domains, and this framework assumes no defensible rule that compresses all relevant dimensions into a single quantity. Comparison is therefore represented as a partial order. A system may dominate the human envelope on some declared coordinates while remaining below it on others, and two system profiles may be incomparable. Here dominance means matching or exceeding the human reference value on the declared coordinate. In that case, legitimate claims remain local: one may report dominance on shared coordinates, additions or losses in coverage, or improvement within a declared domain. A total ordering such as “closer to AGI” requires an additional aggregation rule that is explicitly supplied and defended.

Second, the reference class is the unaugmented human envelope. For empirical application, “unaugmented” is not a metaphysical state; it is an analysis-relative assistance policy that must be declared. The default comparison excludes AI assistance in performing the target task while permitting ordinary education, conventional non-AI tools, and institutional supports unless the analysis states otherwise. Thus a calculator or conventional computer algebra system may be admitted under one declared baseline, while an AI proof assistant that materially contributes to the target reasoning may be excluded; a radiology study may likewise distinguish ordinary picture archiving and communication system (PACS) or workstation support from AI diagnostic assistance. Each application should declare both a baseline date and the forms of assistance permitted. The baseline date fixes the empirical comparison environment: the human-performance evidence and tool/assistance regime against which the system is evaluated. It does not purport to freeze a timeless biological distribution of human ability. Because such boundaries will blur as AI-mediated education, AI-designed tools, and hybrid workflows diffuse, the assistance policy must remain explicit. The purpose is to prevent the benchmark from automatically receding with the AI system under comparison, not to claim that human capability is literally static. AI-mediated augmentation remains part of the book’s analysis; it is excluded only from this definitional reference class.

Third, “the best human capability attainable” means the per-domain maximum across humans, not the capability of any single individual and not the collective capacity of institutions and accumulated science. No individual simultaneously embodies the highest human capability in mathematics, clinical diagnosis, scientific reasoning, negotiation, artistic creation, and every other domain. For empirical use, the default should be demonstrated or reproducibly achievable human performance under declared conditions and at the declared baseline date; estimated maxima may be used only when their basis and uncertainty are stated. “Attainable” in Definition 0 refers to this operationalized quantity; it does not license comparison with merely possible human performance. Excluding collective institutional capacity is a simplifying comparator choice, not a denial that many domains are socially organized. Where the relevant human capability is inherently collective, the collective system should be analyzed separately rather than silently folded into Definition 0’s individual-capability envelope.

Fourth, this definition does not make the conventional distinction between AGI and artificial superintelligence (ASI) load-bearing. Once systems enter and continue beyond the human capability envelope, the framework does not posit a second sharply defined threshold at which AGI becomes ASI. The region has no fixed upper bound. Claims commonly associated with superintelligence—such as decisive strategic advantage, extreme autonomy, or recursive self-improvement—remain possible claims, but they must be analyzed separately rather than inferred from a label.

Definition 0 is a comparison schema. It fixes the capability object, the reference class and the comparison relation, and it yields membership in a class of systems only once an analysis declares a domain partition and a coverage criterion. The book endorses no default coverage criterion. Two analyses with different declared criteria can therefore reach different binary verdicts about the same system without either misapplying the definition. Whatever criterion is declared, a claim of general intelligence requires coverage across more than one declared domain; a criterion that a single domain could satisfy cannot support it. The region of capability space is the representation of such a profile across declared domain coordinates, while the “set of domains” is the subset on which a system matches or exceeds the unaugmented human envelope. These are three views of the same analytical object at different levels, not competing definitions. For empirical application, “across the domains” is instantiated over a declared domain partition; a binary statement such as “system X is AGI” additionally requires a declared coverage criterion. A local crossing such as superhuman performance in Go therefore marks one coordinate of the profile rather than, by itself, establishing generality.

This definition is deliberately independent of the book’s claim about gradualness. A discontinuous capability jump can satisfy Definition 0 just as readily as a slow increase can. The definition specifies the capability object; it does not specify the temporal path by which that object is reached. It also uses a different reference object from definitions keyed to economically valuable work or to level-based human-performance categories, so those definitions should not be treated as interchangeable with Definition 0 (OpenAI 2018; Morris et al. 2024).

## 1.3 What “General” Means in This Book

The word *general* carries much of the conceptual burden in AGI, yet it is frequently left undefined. In this book, generality is not identified with success on a large benchmark suite, with average human performance, or with one numerical breadth score.

Generality is carried by the reference class itself.

Humans exercise intelligence across a wide and open-ended range of domains. In this book, a domain is a declared discipline, form of inquiry, or cognitively coherent field of human intelligent activity—not merely an enumerated benchmark task set. No single exhaustive taxonomy is assumed. For a partition to be admissible in an empirical analysis, it should be declared before the result is interpreted, be relevant to the analytical question, group tasks on a defensible cognitive or institutional basis, and not be split or merged post hoc merely to obtain a preferred AGI classification. For example, an analysis might predeclare mathematics, scientific reasoning, clinical reasoning, language, planning, and social negotiation as distinct domains and require dominance on all six for a particular binary claim; changing that partition after observing the system’s strengths would invalidate the comparison. Emergent domains do not violate this rule: a newly coherent field may be added prospectively in a revised analysis, with the change and its rationale recorded, but it should not be used retroactively to rewrite the result of an earlier predeclared partition. Cross-analysis comparisons are strongest when the same partition is shared; where partitions differ, the resulting AGI-profile claims are not automatically comparable. Humans transfer concepts between contexts, adapt to unfamiliar problems, combine knowledge from different fields, and operate under changing conditions. To match or exceed the human capability envelope across such a reference space therefore already entails breadth. No second independent “generality score” is required.

The declared domain scope need not be restricted to a fixed psychometric inventory (a fixed catalog of cognitive abilities): practical and social performance may be included where comparison and evaluation are specified. Measured performance is not a complete theory of intelligence. Comparisons should also declare the artificial system’s tools, memory, and infrastructure, distinguishing model capability from engineered-system performance (W.H.L. with Claude Sonnet 4.5 2025). Chapter 10 develops that evidentiary boundary.

This does not retire Series \#1’s Depth and Width axes. In the mature architecture they have a genealogical status: they remain useful for understanding the project’s development and for describing epistemic reach and epistemic presence, but they are not first-class variables in the realization mapping and do not constitute a second AGI score (W.H.L. et al. 2026o; W.H.L. et al. 2026v).

This interpretation differs from defining AGI as parity with an average person. The relevant comparison is not whether an AI resembles one generalized human individual. It is whether its capability profile enters or exceeds the envelope formed by the strongest human capabilities across declared domains.

The relationship to Series \#1 is developmental rather than identical. Series \#1 rejected representative-human parity as a sufficient account of generality and emphasized applicability across the full range of human knowledge domains. Definition 0 later supplied the more explicit per-domain best unaugmented human envelope while preserving that cross-domain emphasis. The feature-catalog work then separated Series \#1’s earlier continuity language from the mature criterion for phenomenal gradualness (W.H.L. and ChatGPT 2026i; W.H.L. et al. 2026w, 2026o).

Nor does the definition require that all domains cross the human envelope simultaneously. Capability can advance unevenly: a system may become decisively superhuman in one field, approach the envelope in another, and remain far below it elsewhere. Such local changes alter the profile without by themselves settling the broader question of generality.

This is why the framework treats AGI as a region of a multidimensional capability profile rather than as a point on one scalar.

The coverage region can widen, contract in particular implementations, or change shape as systems, measurements, and domain partitions change. Series \#7’s region language is therefore best read here as open-ended rather than as a monotonicity claim (W.H.L. and Claude 2026g). None of these possibilities alters the stipulative reference class in Definition 0.

One implication follows immediately: the question “has AGI arrived?” cannot be answered in this framework by pointing to one benchmark crossing, system release, institutional declaration, or domain threshold. Such events establish local coordinates of the capability profile. Broader claims inherit the partition and coverage rules declared for the analysis; without them, the framework reports the profile rather than manufacturing a universal arrival verdict.

This also prepares the distinction that follows. If AGI is represented through an open-ended capability profile rather than one scalar point, what does it mean to call AGI gradual?

The answer will not be that capability must rise slowly. It will concern the structure of the transformation through which increasingly general capability becomes consequential.

## 1.4 What “Gradual” Modifies

With AGI defined independently, the next question is what the modifier *gradual* adds. The answer is not that the capability profile specified by Definition 0 must grow slowly, continuously, or by small increments. Definition 0 places no restriction on the temporal path by which a system enters or expands within the human capability envelope. A large discontinuous jump in one or several domains is therefore fully compatible with the definition.

The modifier gradual instead characterizes a specified AGI-related transformation through which capability becomes consequential. For present purposes, realization is the relation and process by which capability as possibility becomes a realized state for specified groups or domains under actual conditions; Chapter 4 gives the formal mapping and uses “realized state” for its output. Capability must therefore be distinguished from whether it becomes available, encountered, used, institutionally recognized, contested, incorporated into practice, and consequential for later conditions.

For gradualness specifically, the series developed in stages. Series \#1 framed AGI as more than a single system or decisive moment. Series \#7 later separated the definition of AGI from the independent claim of gradualness. The subsequent feature catalogs made the circularity problem explicit and reduced the mature criterion to the form used here; Chapter 12 then incorporated that criterion into the unified architecture (W.H.L. and ChatGPT 2026i; W.H.L. and Claude 2026g; W.H.L. et al. 2026w, 2026o; W.H.L. et al. 2026v).

Accordingly, Gradual AGI should be read compositionally: AGI names the capability object; gradual characterizes the temporal structure of a specified realization transformation under a declared individuation rule. The modifier does not choose the individuation rule itself, and it does not hide a temporal assumption inside the definition of intelligence.

This compositional reading also prevents a circular argument. If gradualness were built into the definition of AGI, the series could never discover that an AGI-related transformation was not gradual. By defining AGI first and gradualness separately, the framework leaves open the possibility that a specified transformation could be exhausted by one event. In that case, the gradualness claim would fail for that transformation even though Definition 0 could still be satisfied.

## 1.5 Gradualness: A Descriptive Property of the Transformation

The book uses gradualness for a descriptive or phenomenal property of a specified AGI-related transformation. “Phenomenal” is retained as the canonical technical term: it concerns the form a transformation exhibits under the declared individuation rule, not any subjective experience. By contrast, “principled” (§1.6) concerns how action remains information-responsive and revisable.

The canonical formulation of phenomenal gradualness is:

**Phenomenal gradualness. Given an individuation rule fixing the transformation under study, a specified AGI-related transformation is gradual when its relevant realization is not exhausted by one event.**

The phrase *given an individuation rule* is essential. Whether something is gradual depends in part on what transformation is being described, and the book claims no domain-general individuation rule that settles this in advance. The individuation rule is therefore an explicit analytical input chosen and defended by the observer, not an objective physical boundary presumed to exist independently of the analysis. It also fixes which changes count as relevant to the classification. Claims of gradualness are relative to that declared rule and to the stated observation horizon. A model release can occur at a moment. A benchmark can be crossed on a date. A theorem can be announced in a paper. Yet a scientific field, profession, institution, or social practice associated with that event may continue changing before and after it. The framework therefore does not infer the temporal character of the larger transformation from the temporal character of one constituent event.

The individuation rule must fix two things before the classification is made. The first is the transformation: which realization is under study and which changes count as relevant to it. The second is the event grain: what counts as a single event, at what temporal resolution, and when two dated changes are one event or two. Without a declared event grain, any extended transformation can be redescribed as one long event, and any event as many, so the classification would follow the description rather than the evidence. A declared grain may be revised in a later analysis, with the change recorded, but it may not be revised to rescue an earlier classification.

Gradualness, in this sense, does not mean slow. It also does not require smooth, continuous, scalar, homogeneous, monotonic, or uniformly incremental change. A gradual transformation may contain abrupt advances, reversals, plateaus, local thresholds, and punctuated shifts. The criterion asks whether the specified transformation is exhausted by one event, not whether every trajectory inside it has a gentle slope.

The distinction is particularly important for AGI. A system could cross the human capability envelope abruptly in a particular domain, or even across several domains at once, while the associated transformation remained heterogeneous and temporally extended. The criterion can also fail. Suppose the transformation is deliberately individuated as “whether a specified model becomes legally and technically available to a defined user group under a particular license.” If one dated release event fully changes that status and no analytically relevant realization remains outside it, that specified transformation is non-gradual. The empirical content therefore lies partly in the individuation rule: the framework must state what transformation it is classifying and allow the classification to fail.

Gradualness is therefore a contestable but intentionally thin descriptive classification, not a complete theory of social change. It is likely to be satisfied for many broad socially consequential transformations; narrow transformations can fail it only when the individuation rule is fixed in advance and specifies what observation would exhaust the transformation. That requirement, together with the declared event grain, gives the criterion limited but real discriminating power, while leaving the heavier explanatory work to the realization architecture developed later in the book. Evidence that the declared transformation is exhausted by a single event is a direct defeat condition for phenomenal gradualness. The two feature catalogs derive and document this criterion (W.H.L. et al. 2026w, 2026o).

## 1.6 Graduality: A Principle of Revisable Action

The book reserves graduality for a different idea. Whereas gradualness describes a phenomenon, principled graduality names a principle for decision and process design: information-responsive iteration combined with preserved revisability.

**Principled graduality. Proceed through information-responsive iteration while preserving the capacity to revise, redirect, contract, or abandon prior commitments when evidence warrants change.**

The two ideas share a linguistic root but should not be treated as synonyms. A transformation can be phenomenally gradual without actors following the principle of graduality. Institutions may respond rigidly, irreversibly, or poorly even when change unfolds over many stages. Conversely, actors may adopt revisable, information-responsive procedures in a setting where the underlying phenomenon is not gradual in the descriptive sense. The two are therefore neither equivalent nor wholly unrelated: a temporally extended transformation may create additional opportunities for learning and revision, but that fact alone neither requires nor justifies principled graduality.

Most importantly, phenomenal gradualness does not generate an obligation to slow down. Principled graduality requires its own conditional justification. It is most strongly motivated where persistent uncertainty, evolving objectives, nonconvex choices—settings in which locally attractive options need not combine into one globally best path—heterogeneous stakeholder goals, or other conditions make later information decision-relevant. Its rationale weakens where the problem is well bounded, delay is itself costly, or no meaningful revisability can be preserved. Revisability of a procedure is also not the same as reversibility of outcomes: a deployment rule may remain amendable even after an irreversible disclosure, environmental release, or institutional commitment has made some consequences impossible to undo.

The is–ought firewall keeps four kinds of work distinct. Description asks what form the transformation takes. Formal analysis asks what follows under stated assumptions. Empirical inquiry asks what the evidence supports. Normative judgment asks what ought to be preferred. Fairness, legitimacy, participation, safety, or other values may independently support particular decision procedures, but they do not become empirical conclusions merely because a transformation is gradual (W.H.L. et al. 2026o).

The distinction also gives the project a standard for self-correction. A framework committed to principled graduality should be able to revise its own claims when evidence defeats them. Revisability does not mean that every claim is provisional forever, nor does revision erase a prior failure. Repair changes the model when warranted; it does not retrospectively convert an unsuccessful claim into a successful one.

## 1.7 From Capability to Realization

Once AGI, gradualness, and graduality are separated, the central problem of the book becomes visible. Definition 0 tells us what capability object the term AGI refers to. Gradualness tells us how a specified AGI-related transformation may be classified. Neither, by itself, tells us how capability becomes consequential in the world. In the chapters that follow, realization is used in a controlled three-part way: as a relation connecting relevant conditions to an outcome, as the process through which those conditions become consequential, and as a realized state when the output itself is meant. Chapter 4 introduces the formal notation that keeps these three senses distinct.

That gap motivates the book’s realization-centered architecture. A capability can exist without being broadly available. It can be available without reaching a particular population or institution. It can be encountered without being trusted, authorized, incorporated, or acted upon. It can alter practice for one group while leaving another largely untouched. These are analytically distinct relations rather than a mandatory stage sequence.

The book names this foundational boundary Potential–Realization Separation: what artificial intelligence has become capable of doing is not identical to what becomes socially realized, for whom, under what conditions, or with what consequences for what comes next. Chapter 4 formalizes realization as a group- and domain-specific relation among Potential, Availability, Exposure, and domain-specific realization conditions; Chapter 1 uses only the provisional gloss needed to establish the distinction.

Later chapters then examine how Optimization, Governance, Participation, Observation and Evidence, and Feedback and Recursion relate to realization without collapsing into it. Those components are intentionally deferred here.

The result is the conceptual grammar on which the rest of the book depends: AGI is defined first; gradualness characterizes a transformation when it is not exhausted by one event; graduality governs a distinct principle of revisable action; and realization names the problem that connects capability to consequences. Chapter 1’s task is narrower than the chapters that follow: to establish why the larger architecture is needed at all.

The next section illustrates Potential–Realization Separation in three domains—Go, mathematics, and radiology—without yet invoking the full realization mapping.

## 1.8 Three Illustrations of Realization

The distinctions developed in this chapter can be seen without yet invoking the book’s formal realization mapping. Three domains used later in the book—Go, mathematics, and radiology—provide compact illustrations at deliberately different levels of maturity. They are not offered here as demonstrations of the model’s validity. Their purpose is narrower: to show why capability, availability, verification, institutional uptake, and realized consequence should not be treated as one event.

Go provides the clearest starting point. AlphaGo’s 2016 victory over Lee Sedol is the conspicuous capability event used here: a public match in which a machine system defeated one of the world’s strongest professional players. That match alone was not a crossing of Definition 0’s per-domain maximum, because it compared AlphaGo with one elite player rather than the full human envelope. The capability case strengthened further in 2017, when AlphaGo defeated world number one Ke Jie; DeepMind’s contemporaneous and year-end accounts document the Wuzhen match and Ke Jie’s loss, while later AlphaGo versions surpassed earlier systems (Google DeepMind 2017b, 2017a, 2026). The 2016–2017 sequence is useful because it is dateable yet did not exhaust what followed. Professional play continued; training practices changed; human players incorporated machine-discovered strategies; interpretations of good play shifted; and human–AI interaction became part of the domain’s continuing development. Separate longitudinal studies report changes in move quality, alignment with AI solutions, knowledge gains, diversity, and novelty after superhuman Go systems entered the domain (Choi et al. 2025b, 2025a; Shin et al. 2023).

Mathematics makes a different separation visible. A system may produce a candidate result, assist with a proof, formalize an argument, or contribute to a research program, yet those events do not by themselves settle mathematical realization. Verification, provenance, attribution, community scrutiny, publication, institutional acknowledgment, and formal prize determination can remain distinct. The 2026 Navier–Stokes episode is used here as a live case, not as settled history. As of October 6, 2026, OpenAI’s September 8 announcement presents a claimed solution to the Navier–Stokes existence-and-smoothness problem together with a formalization in Lean, a proof assistant; Clay’s Millennium Prize page still lists Navier–Stokes among its active problems (OpenAI 2026d; Clay Mathematics Institute 2026a). OpenAI presents its Navier–Stokes result as establishing Clay alternatives C and D: an initially smooth flow develops a finite-time singularity under a smooth external force. The forced/unforced contrast in the same post concerns related Euler results: OpenAI reports that Levent Alpöge (Anthropic) and Tristan Buckmaster (New York University) obtained a forced Euler result with an internal Anthropic model, recognizes the priority of that work, and reports its own unforced Euler result. OpenAI also reports that its investigation found that Buckmaster’s earlier Codex prompts could not have influenced its system, including through training; attribution across the concurrent work remains a question separate from correctness. On September 11, the Clay Mathematics Institute said the Navier–Stokes problem had “apparently been settled” while emphasizing that analysis, credit, and prize evaluation follow a deliberately unhurried process (Clay Mathematics Institute 2026b). OpenAI has said that it does not intend to claim the Millennium Prize for this result (OpenAI 2026d). A Lean-checked formalization establishes correctness relative to the formalized statement; it does not by itself settle whether that statement captures every intended condition of the mathematical problem. A separate question is whether the Lean proof corresponds to the natural-language proof; an October 6 preprint argues that it does not (Bastounis, Circelli, and Hansen 2026; see Chapter 4). The point here is therefore layered status: public claim, formal verification, community scrutiny, institutional acknowledgment, attribution, and prize determination need not change together.

Radiology supplies a third pattern. A model can demonstrate strong research performance and even become publicly available for research without thereby becoming part of routine clinical practice. Bounded-task expert-level performance is not the same thing as general clinical autonomy or routine clinical realization. Clinical integration depends on additional conditions: validation in the relevant setting, workflow fit, regulatory and institutional requirements, professional acceptance, liability, infrastructure, and the circumstances under which clinicians and patients encounter the system. Availability can therefore increase while clinical realization remains partial, uneven, or unresolved. The 2026 RADAR (Rapid Abdominal Diagnosis with AI and Radiology) work illustrates this distinction: expert-level bounded-task evidence and public research availability do not by themselves establish routine clinical realization (Zhang et al. 2026; Alibaba DAMO Academy 2026).

The three examples differ deliberately. Go emphasizes temporal extension after a conspicuous capability event. Mathematics emphasizes the separation between result, evidence, verification, and institutional acceptance. Radiology emphasizes the gap between research availability and domain-specific deployment. None requires the assumption that capability itself grows slowly. Each instead shows why the object of analysis becomes richer once the question shifts from what AI can do to what becomes realized, for whom, under what conditions, and over what period.

That shift is the organizing problem of the chapters that follow.

## 1.9 How to Read the Book

The book develops its argument through four Parts. These are reader-level movements of inquiry rather than chronological stages, stages of AGI development, or the Multi-Plateau Framework’s plateaus. The sequence is cumulative, but the chapters do not form a single linear mechanism in which every later concept becomes another variable in one equation. Each chapter introduces or disciplines a distinct analytical object, and later synthesis depends on preserving those distinctions.

Part I, Orientation — Chapters 1–2. Chapter 1 defines AGI and distinguishes phenomenal gradualness from principled graduality. Chapter 2 develops AGI-inclusive humanity—the evolving configuration of humans, AI systems, institutions, and infrastructure—and the adopted commitment to the benefit of human beings situated within it (W.H.L. with Claude Sonnet 4 2025). It distinguishes realization, realized consequence, and benefit, while treating purpose as direction rather than a fixed endpoint.

Part II, Architecture — Chapters 3–6. Chapter 3 introduces the Multi-Plateau Framework, which provides the logical architecture for typing, relating, and revising claims without collapsing different kinds of evidence or proposition into one level. Chapter 4 moves from capability or Potential to Realization and introduces the book's central realization mapping. Chapter 5 develops Ceiling–Floor–Slope as a dynamical model for synchronization with bounded applicability. Chapter 6 introduces Optimization, asking how candidate trajectories can be evaluated under differing objectives, constraints, and absorption capacities.

Part III, Mediation — Chapters 7–11. This Part examines human, institutional, and temporal processes that shape realization, together with the evidence and epistemic discipline through which claims about it are assessed. Chapter 7 asks how realization is governed and contested through execution, observation, steering, and procedural adjudication. Chapter 8 develops Participation through the distinction among subjects, acts, and consequences, within a broader reciprocal human–AI thesis. Chapter 9 brings that apparatus into empirical contact and asks which participation claims survive discrimination, consequence testing, and realization-level scrutiny. Chapter 10 separates underlying state, observation, representation, inference, and claim status so that evidence cannot silently inherit conclusions it has not earned. Chapter 11 examines feedback and recursion: how prior realization can alter conditions relevant to what happens next without turning every sequence into recursive self-improvement.

Part IV, Integration — Chapter 12. Chapter 12 brings the architecture together as the Unified Gradual AGI Model, preserving the distinctions among its components rather than reducing them to a single score, threshold, or master equation. This integration is provisional and does not claim a closed or final system. Part IV also supplies the Glossary, Full Notation Guide, and compact Claims and Status Register; the full Canonical Extraction / Provenance Ledger belongs to separate scholarly back matter. Readers who want the whole model in compact form before the detailed chapters can turn first to Figure 12.1 and Table 12.2, “Key ideas in one line,” in §12.2.

Readers therefore need not treat the book as an argument that AGI must arrive at one particular pace or through one predetermined sequence. Its stronger commitment is methodological: capability, realization, institutional conditions, participation, evidence, and feedback should be distinguished before they are related.

The resulting model accommodates heterogeneous forms of realization. Its components can be revised when evidence defeats a distinction, weakens a proposition, or shows that a simpler representation is adequate. Its architecture can itself be revised when repeated empirical contact defeats a load-bearing separation. Gradual AGI is therefore not a device for postponing judgment indefinitely. Revisability is meaningful only if claims can also be contracted, rejected, or retired.

The book begins, then, with a definition rather than a date. From that starting point it asks a different family of questions: what has become possible; what has become available; what has become realized; for whom; under what conditions; through which institutions and acts; on what evidence; and with what consequences for what comes next. Those questions, rather than a single declaration of arrival, define the inquiry that follows.

## Chapter References

### Book and Gradual AGI Sources

W.H.L. with Claude Sonnet 4. 2025. “First Principles of AGI-Inclusive Humanity.” *Champaign Magazine*, June 17, 2025. [https://champaignmagazine.com/2025/06/17/first-principles-of-agi-inclusive-humanity/](https://champaignmagazine.com/2025/06/17/first-principles-of-agi-inclusive-humanity/)

W.H.L. with Claude Sonnet 4.5. 2025. “Problems with Alignment of AGI with CHC Strata II.” *Champaign Magazine*, October 18, 2025. [https://champaignmagazine.com/2025/10/18/problems-with-alignment-of-agi-with-chc-strata-ii/](https://champaignmagazine.com/2025/10/18/problems-with-alignment-of-agi-with-chc-strata-ii/)

W.H.L. & ChatGPT. 2026i. “Gradual AGI as Epistemic Extension.” Gradual AGI Series \#1. *Champaign Magazine,* January 19, 2026. [https://champaignmagazine.com/2026/01/19/gradual-agi-as-epistemic-extension/](https://champaignmagazine.com/2026/01/19/gradual-agi-as-epistemic-extension/)

W.H.L., Claude Sonnet 5, & GPT-5.5. 2026j. “Gradual AGI as Optimization: A Conceptual Framework.” Gradual AGI Series \#5. *Champaign Magazine,* July 22, 2026. [https://champaignmagazine.com/2026/07/22/gradual-agi-as-optimization-a-conceptual-framework/](https://champaignmagazine.com/2026/07/22/gradual-agi-as-optimization-a-conceptual-framework/)

W.H.L. & Claude (Opus 5). 2026g. “Gradual AGI as Contestation: A Framework for Governance.” Gradual AGI Series \#7. *Champaign Magazine,* August 3, 2026. [https://champaignmagazine.com/2026/08/03/gradual-agi-as-contestation-a-framework-for-governance/](https://champaignmagazine.com/2026/08/03/gradual-agi-as-contestation-a-framework-for-governance/)

W.H.L., GPT-5.6 Sol, & Claude Opus 5. 2026w. “What ‘Gradual’ Means in Gradual AGI: A Feature Catalog.” *Champaign Magazine,* August 17, 2026. [https://champaignmagazine.com/2026/08/17/what-gradual-means-in-gradual-agi-a-feature-catalog/](https://champaignmagazine.com/2026/08/17/what-gradual-means-in-gradual-agi-a-feature-catalog/)

W.H.L., GPT-5.6 Sol, & Claude Opus 5. 2026o. “Graduality: A Feature Catalog of Gradual AGI.” *Champaign Magazine,* August 18, 2026. [https://champaignmagazine.com/2026/08/18/graduality-a-feature-catalog-of-gradual-agi/](https://champaignmagazine.com/2026/08/18/graduality-a-feature-catalog-of-gradual-agi/)

W.H.L., GPT-5.6 Sol, & Claude Sonnet 5. 2026v. “The Unified Gradual AGI Model.” *On Gradual AGI,* Chapter 12. *Champaign Magazine,* September 27, 2026. [https://champaignmagazine.com/2026/09/27/the-unified-gradual-agi-model/](https://champaignmagazine.com/2026/09/27/the-unified-gradual-agi-model/)

### External Sources Used in Chapter 1

Alibaba DAMO Academy. 2026. “RADAR: An Expert-Level Generalist AI for Abdominal CT Diagnosis” \[code and model repository\]. Accessed September 28, 2026. [https://github.com/alibaba-damo-academy/damo-radar](https://github.com/alibaba-damo-academy/damo-radar)

Bastounis, Alexander, Fabian Circelli, and Anders C. Hansen. 2026. “Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs.” arXiv:2610.08144, October 6. [https://arxiv.org/abs/2610.08144](https://arxiv.org/abs/2610.08144).

Choi, S., Kang, H., Kim, N., & Kim, J. 2025b. “How Does Artificial Intelligence Improve Human Decision-Making? Evidence from the AI-Powered Go Program.” *Strategic Management Journal* 46(6): 1523–1554. [https://doi.org/10.1002/smj.3694](https://doi.org/10.1002/smj.3694)

Choi, S., Kang, H., Kim, N., & Kim, J. 2025a. “The Dual Edges of AI: Advancing Knowledge While Reducing Diversity.” *PNAS Nexus* 4(5): pgaf138. [https://doi.org/10.1093/pnasnexus/pgaf138](https://doi.org/10.1093/pnasnexus/pgaf138)

Clay Mathematics Institute. 2026b. “Navier-Stokes Announcement.” September 11, 2026. [https://www.claymath.org/news/navier-stokes-announcement/](https://www.claymath.org/news/navier-stokes-announcement/)

Clay Mathematics Institute. 2026a. “The Millennium Prize Problems.” Accessed October 6, 2026. [https://www.claymath.org/millennium-problems/](https://www.claymath.org/millennium-problems/)

Google DeepMind. 2017b. “AlphaGo’s Next Move.” May 27, 2017. [https://deepmind.google/blog/alphagos-next-move/](https://deepmind.google/blog/alphagos-next-move/)

Google DeepMind. 2017a. “2017: DeepMind’s Year in Review.” December 21, 2017. [https://deepmind.google/blog/2017-deepminds-year-in-review/](https://deepmind.google/blog/2017-deepminds-year-in-review/)

Google DeepMind. 2026. “From Games to Biology and Beyond: 10 Years of AlphaGo’s Impact.” March 10, 2026. [https://deepmind.google/blog/10-years-of-alphago/](https://deepmind.google/blog/10-years-of-alphago/)

Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., & Legg, S. 2024. “Position: Levels of AGI for Operationalizing Progress on the Path to AGI.” *Proceedings of the 41st International Conference on Machine Learning,* PMLR 235: 36308–36321. [https://proceedings.mlr.press/v235/morris24b.html](https://proceedings.mlr.press/v235/morris24b.html)

OpenAI. 2018. “OpenAI Charter.” Accessed September 28, 2026. [https://openai.com/charter/](https://openai.com/charter/)

OpenAI. 2026d. “On the Navier–Stokes Millennium Prize Problem.” September 8, 2026. [https://openai.com/index/navier-stokes-solution/](https://openai.com/index/navier-stokes-solution/)

Shin, M., Kim, J., van Opheusden, B., & Griffiths, T. L. 2023. “Superhuman Artificial Intelligence Can Improve Human Decision-Making by Increasing Novelty.” *Proceedings of the National Academy of Sciences* 120(12): e2214840120. [https://doi.org/10.1073/pnas.2214840120](https://doi.org/10.1073/pnas.2214840120)

Zhang, Q., Zhang, J., Cao, W., Lu, Z., Chang, W., et al. 2026. “An Expert-Level Generalist AI for Abdominal CT Diagnosis.” *Science* 393(6817): eaec6129. [https://doi.org/10.1126/science.aec6129](https://doi.org/10.1126/science.aec6129)
