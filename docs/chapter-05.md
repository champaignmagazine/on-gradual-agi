# Chapter 5 — Synchronization: Ceiling, Floor, and Slope

## Abstract

Chapter 4 established a general mapping from Potential to Realization. This chapter asks the temporal question that follows: when capability and realization move on different clocks, how do their gaps, thresholds, delays, and rates evolve over time? It develops Ceiling, Floor, and Slope (CFS) as a bounded realization-dynamics submodel. The chapter defines domain-scoped Ceiling and Floor readouts, distinguishes Slope as an observable from synchronization as the underlying process, derives a minimal discrete-time recurrence and its stability regimes, adds threshold gating, heterogeneous adoption, gap-dependent rates, and a two-tier delay structure, and brings those mechanisms into empirical contact with professional Go, AI-assisted drug development, frontier language models, and autonomous-vehicle deployment. The chapter also states where CFS stops: it is not the general realization mapping, does not automatically model path foreclosure, does not choose an optimal trajectory, and should be declared not presently applicable when its core observables or coupling relation cannot be operationalized. Several empirical and formal questions remain open, including the long-run residual, overtrust, endogenous gate oscillation, the functional form of rate decay, and measurement survival.

**Keywords.** Gradual AGI; synchronization; Ceiling; Floor; Slope; realization; thresholds; heterogeneous adoption; institutional delay; dynamical regimes.

**Scope note.** CFS is treated here as one bounded realization-dynamics submodel inside the broader Chapter 4 architecture. Ceiling is not identical to Potential, Floor is not identical to general Realization, Slope is not an independent causal force, and a smaller gap is not assumed to be normatively better. The chapter consolidates the conceptual vocabulary introduced in Gradual AGI Series \#3 and the formal/empirical model developed in Series \#4, while applying the tighter book-level nesting and boundary rules established by the Unified Gradual AGI framework (W.H.L. and GPT-5.5 2026n; W.H.L. and Claude 2026b).

## Chapter 5 Reader Guide

*Synchronization: Ceiling, Floor, and Slope*

### One-line summary

This chapter develops CFS as a dynamical model of a specified capability–realization gap where interpretable, commensurable readouts and longitudinal evidence permit its use.

### Principal Contributions

This chapter makes the following principal contributions. Its contribution lies in the formulation, interpretation, and integration of CFS, rather than in claiming new mathematics for the baseline recurrence.

1.  **Domain-scoped Ceiling, Floor, and Slope.** Ceiling and Floor are selected capability and realization readouts, rather than identities with the general Potential and realized-state objects. Slope is the observed fraction of the current gap closed during an observation period. The recurrence’s coupling parameter β specifies modeled Floor movement relative to that gap. Under the baseline one-period recurrence, observed Slope and the implied β coincide algebraically; this does not independently validate β or the recurrence.

2.  **A minimal recurrence and its conditional regimes.** The chapter derives gap dynamics and distinguishes monotonic convergence, parity, damped oscillation, marginal oscillation, and divergence under the stated assumptions. The boundary at β = 2 is marginal rather than automatically divergent.

3.  **Thresholds, heterogeneity, and gap-dependent rates.** The chapter relates delayed response, segment-specific thresholds, and changing coupling to synchronization. A shrinking gap can leave a harder residual without identifying one universal limiting rate or uniquely established functional form.

4.  **Continuous realization, institutional gates, and two kinds of delay.** A discrete gated endpoint is distinguished from the continuous Floor used in the gap. Capability-compressible delay is separated from delay that remains insensitive to additional capability within the modeled horizon.

5.  **Measurement discipline and an applicability stop rule.** Proxy revisions require a defensible bridge or a new measurement epoch. Where the realization object, readouts, longitudinal comparison, or plausible coupling cannot be specified adequately, the appropriate verdict is “CFS not presently applicable.”

### Prerequisites

Chapter 4 establishes the broader realization architecture in which CFS is nested. Chapters 1–2 clarify gradualness and the system frame; Chapter 3 helps distinguish formal consequences from empirical support. The chapter introduces discrete-time recurrence notation and parameters; the Notation Quick Reference supports the formal reading.

### Reading routes

**Readout path.** Sections 5.1–5.2 specify the realization object, Ceiling, Floor, gap, and observable Slope.

**Dynamics path.** Sections 5.3–5.7 develop the recurrence, thresholds, heterogeneous adoption, rates, residuals, institutional gates, delay, and dynamical regimes. Regime claims remain conditional on the chosen specification.

**Empirical path.** Section 5.8 examines the inherited domains and later developments without treating mechanism-specific evidence as a fit of the complete model.

**Boundary path.** Sections 5.9–5.10 distinguish CFS from the general mapping, path foreclosure, Optimization, governance, and observation; they also state falsifiers, open questions, and the stop rule.

**Book path.** Within Part II, Architecture, Chapter 5 asks how a specified trajectory evolves. Chapter 6 asks which candidate trajectory should be preferred. Faster gap closure does not answer that second question.

### Evidence and limits

Apparent gap closure must be checked against task-space narrowing, external gates or clocks, population composition, and benchmark saturation before it is attributed to structural coupling.

The recurrence’s regimes are mathematical consequences of stated assumptions, not universal laws of realization. The empirical record supplies longitudinal anchors and mechanism-specific evidence; none of the four original domains supplies a formal statistical fit of the complete recurrence. A fitted curve or a one-period coupling estimate does not independently validate the model.

The limiting rate, long-run residual, possible oscillation when realized reliance overshoots demonstrated capability, changes in gates under contestation, rate functional form, and survival of measurement remain open burdens. Baseline CFS does not solve path foreclosure, explain the governance process that changes a gate, select a desirable trajectory, or identify causal counterfactuals. An apparent shrinking gap may be a measurement artifact. Where simpler models perform as well or the readouts lose meaning, the application should contract or stop.

## 5.1 From Realization to Synchronization

Chapter 4 established a general architecture for analyzing how technological Potential becomes realized in a specified domain and for a specified group:

R<sub>g</sub>(t) = μ<sub>t</sub>(P(t), Av(t), Ex<sub>g</sub>(t), Z<sub>d</sub>(t)).

That mapping is deliberately broad. It can represent differences in availability, exposure, institutional conditions, and other domain-specific constraints without presuming that all realization problems share the same dynamics.

But the architecture leaves a further question open. Even when a relevant capability exists, is available, and can in principle enter a realization pathway, capability and assimilation need not move together. The capability frontier may advance rapidly while institutions, professions, organizations, regulations, and everyday practice adjust on slower clocks. In other cases, the realized state may accelerate after a threshold, stall behind a gate, approach a persistent residual, or respond at different rates across populations.

This temporal asymmetry was the starting point for the Synchronization framework developed earlier in the Gradual AGI series. Series \#3 introduced Ceiling, Floor, and Slope as a vocabulary for the relative movement of frontier capability and realized assimilation. Series \#4 then formalized that relation as a falsifiable dynamical problem with a recurrence, threshold-gated coupling, heterogeneous thresholds, gap-dependent rates, two-tier delay, and a regime classification (W.H.L. and GPT-5.5 2026n; W.H.L. and Claude 2026b).

The book now places that model more precisely. CFS is not a second theory of realization and does not replace the Chapter 4 mapping. It applies to a narrower family of cases in which a domain-specific capability state and a corresponding realized or assimilated state can both be represented over time, and in which their changing relation is analytically meaningful.

This chapter therefore asks:

> *When capability and realization move on different clocks, how do their gaps, thresholds, delays, and rates evolve over time?*

The answer is dynamical rather than normative. CFS can describe faster and slower convergence, persistent lag, overshoot, or heterogeneous synchronization. It does not, by itself, tell us which of those trajectories should be preferred.

### 5.1.1 Where CFS Sits After Chapter 4

The most important book-level clarification is the nesting of CFS inside the general realization architecture.

The Ceiling C<sub>t</sub> is a domain-scoped capability proxy or readout selected for a particular CFS application. It may reflect one relevant slice of broader Potential, but it is not identical to the full Potential state:

C<sub>t</sub> ≠ P(t).

Likewise, the Floor F<sub>t</sub> is a domain-scoped realized or assimilated state for a specified realization object and population. It may be a useful readout of one part of realization, but it is not the general realized state defined in Chapter 4:

F<sub>t</sub> ≠ R<sub>g</sub>(t).

These are claims of analytical non-identity, not independence. The selected Ceiling is derived from the capability side of the broader architecture, and the selected Floor is derived from a specified realization process. The point is to prevent a local operationalization from being mistaken for the whole construct.

The same discipline applies to Slope. Synchronization is the underlying process by which the realized state moves relative to the capability state. Slope is an empirical window onto that process. It is not a separate force acting on the system.

Finally, the CFS gap G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub> is one operationalized, within-domain capability-realization difference. It is not a universal definition of realization failure. Some realization problems may have no defensible scalar Ceiling, no stable Floor, no meaningful subtraction between them, or no plausible coupling relation. Those cases belong in the broader Chapter 4 architecture without being forced into CFS.

Figure 5.1 makes this nesting explicit.

<img src="../media/image5.png" title="Figure 5.1" loading="lazy" alt="Diagram nesting CFS inside the Chapter 4 realization architecture. Potential, availability, exposure, and domain conditions feed the general realization mapping and realized state; selected Ceiling and Floor readouts define a bounded CFS gap. The figure explicitly shows C_t is not identical to P(t) and F_t is not identical to R_g(t)." />

Figure 5.1. CFS nested inside the Chapter 4 realization architecture. Potential and realized state are broader constructs; Ceiling and Floor are selected domain-scoped readouts used for a bounded synchronization analysis. The non-equivalences C<sub>t</sub> ≠ P(t) and F<sub>t</sub> ≠ R<sub>g</sub>(t) are therefore structural safeguards, not claims of independence.

## 5.2 Ceiling, Floor, and Slope

CFS begins with three operational quantities: Ceiling, Floor, and Slope. Their purpose is not to rename familiar ideas, but to make a particular temporal relation measurable. A valid application must specify the domain, the realization object, the relevant population or institutional scope, and the metric used on each side. Different domains need not share a common unit.

### 5.2.1 Ceiling

As established in §5.1.1, Ceiling is a selected, domain-scoped capability readout rather than the full Potential state. In one domain it might be professional-level performance, in another a task-completion horizon, and in another a bounded technical target.

Operationally, the selected Ceiling measure must remain interpretable within the domain over the period being studied. Different domains may therefore use different, noncommensurate capability proxies; what CFS carries across domains is the structure of the relationship between Ceiling and Floor, not a common unit of capability.

When several plausible Ceiling proxies exist, selection should follow the realization object and research question rather than convenience. Prefer one primary proxy that is substantively tied to the capability being realized, remains longitudinally interpretable, and is not already dominated by a known saturation artifact. Alternative plausible proxies should be reported as sensitivity checks rather than averaged into a composite unless the weighting rule has an independent substantive justification. If reasonable proxies point in materially different directions, the CFS result should be reported as proxy-sensitive rather than silently reconciled.

Ceiling should also not be read as the ultimate upper limit of all future capability. It is the capability state relevant to the selected CFS application at time t. A moving frontier can continue to advance after a particular operational Ceiling has been chosen, and the proxy itself may eventually require revision if it saturates or ceases to track what matters.

The 2026 mathematics frontier makes this qualification concrete. OpenAI and Anthropic have reported systems that resolve or materially advance long-standing research problems, produce major formalizations, and, in OpenAI's case, propose a solution to the Navier-Stokes Millennium Prize Problem using an internal model (OpenAI, 2026l, 2026d; Anthropic, 2026e, 2026c). These developments should not be read as identifying an ultimate mathematical Ceiling. They raise the observed lower bound on capability for particular research objects, subject to continuing external scrutiny. Pachocki (2026) similarly argues that contemporary machine intelligence is not well represented by one human-comparable axis and that capabilities that are easy to measure can move differently from those that are difficult to quantify. For CFS, the implication is operational: C<sub>t</sub> remains domain- and realization-object-specific, and a lab-internal frontier readout should not be conflated with public Availability or with a scalar measure of general intelligence.

### 5.2.2 Floor

As established in §5.1.1, Floor is the specified realized or assimilated state whose movement is being studied relative to the Ceiling. It is not generic exposure, access, technical availability, or the mere possibility of use.

A Floor must therefore be scoped. At minimum, the analysis should identify the domain, the realization object, the relevant population or institutional unit, and the metric that makes change over time observable. A consumer-adoption Floor, an enterprise-use Floor, a professional-practice Floor, and a regulatory-approval Floor may all be legitimate, but they are not interchangeable measurements of one undifferentiated quantity.

This matters because realization can be layered. Continuous practice can improve while a discrete institutional outcome remains unchanged. Different groups can assimilate the same technical capability at different rates. Later sections therefore allow the Floor to be segment-indexed and, where needed, separated into continuous and gated forms.

> *Floor is the specified realized or assimilated state whose movement is being studied relative to the Ceiling.*

### 5.2.3 Slope

Slope is the realized synchronization rate: the fraction of the current gap that the Floor closes during one observation period.

S<sub>t</sub> ≡ ΔF<sub>t</sub> / G<sub>t</sub> = (F<sub>t+1</sub> - F<sub>t</sub>) / (C<sub>t</sub> - F<sub>t</sub>).

The numerator measures observed movement in the Floor. The denominator measures the available Ceiling-Floor gap at the beginning of the interval. Slope therefore normalizes realized movement by the distance that could, in principle, have been closed under the chosen operationalization.

This definition also fixes an important epistemic distinction. S<sub>t</sub> is observed. The structural coupling parameter introduced in the recurrence, β<sub>t</sub>, is a model parameter. Under the baseline one-period recurrence they coincide algebraically, so rearranging a single observation cannot independently validate β<sub>t</sub>. The falsifiable content appears only when a constrained multi-period specification predicts a sequence of observed S<sub>t</sub> values better than competing forms.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Sidebar 5.A Synchronization is the process; Slope is the readout</strong></p>
<p>Synchronization is the underlying dynamical process by which the Floor changes relative to the Ceiling.</p>
<p>Slope S<sub>t</sub> is an observable: the realized fraction of the current gap closed in one period.</p>
<p>A one-period match between S<sub>t</sub> and an implied β<sub>t</sub> is algebraic, not independent validation. The empirical test is longitudinal and comparative.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 5.2.4 The Gap

The central state difference in CFS is

G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub>.

A positive gap means that the selected capability state lies ahead of the selected realized state in the chosen domain and metric. The gap can widen, narrow, stabilize, or oscillate depending on how the Ceiling and Floor move.

But a shrinking gap is not automatically evidence of successful realization. It can result from a rising Floor, a slowing Ceiling, metric saturation, or a changing measurement boundary. The same numerical direction can therefore have very different substantive meanings.

Nor is the gap normatively self-interpreting. Slower realization may sometimes reflect inertia or exclusion, but it may also reflect safety review, institutional caution, standing human preference, or a realization object that should not be maximized.

> *G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub> is an operational within-domain synchronization gap, not a general definition of realization failure.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Sidebar 5.B Why a smaller gap is not automatically better</strong></p>
<p>A gap can shrink because the Floor rises - but also because the Ceiling slows, the proxy saturates, or the measurement boundary moves.</p>
<p>A persistent gap can represent unfinished assimilation, deliberate precaution, human preference, institutional protection, or model misspecification.</p>
<p>CFS is descriptive. Whether a gap should be closed is an Optimization question, not a conclusion built into the dynamics.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 5.2 shows the basic relation among a moving Ceiling, a rising Floor, a threshold crossing, Floor movement, and the remaining gap.

<img src="../media/image6.png" title="Figure 5.2" loading="lazy" alt="Illustrative time-series plot of a rising Ceiling and Floor. A threshold crossing precedes stronger Floor movement, and a vertical arrow marks the synchronization gap G_t between Ceiling and Floor at a selected time." />

Figure 5.2. Moving Ceiling, rising Floor, and synchronization gap. The diagram is illustrative rather than empirically fitted. It shows a capability frontier advancing while the realized state responds more slowly, with stronger movement after a threshold crossing. The vertical distance at a selected time is G<sub>t</sub>; the change in Floor across an interval is ΔF<sub>t</sub>.

## 5.3 The Minimal Synchronization Recurrence

The minimal CFS recurrence asks what happens when the Ceiling continues to advance while the Floor closes a fraction of the existing gap.

G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub>.

For a local observation interval, let the Ceiling advance by a constant increment α:

C<sub>t+1</sub> = C<sub>t</sub> + α.

This is a local approximation, not a claim that capability grows linearly forever.

Let the Floor close a fraction β of the current gap during the same period:

F<sub>t+1</sub> = F<sub>t</sub> + βG<sub>t</sub>.

Subtracting the second equation from the first yields the gap recurrence:

G<sub>t+1</sub> = α + (1 - β)G<sub>t</sub>.

The interpretation is straightforward. The Ceiling creates new distance at rate α while synchronization closes a fraction β of the distance already present. The recurrence is intentionally minimal. It does not assume that α or β is universal, constant across domains, or stable over long horizons. Thresholds, heterogeneity, changing rates, and institutional delay are added only when the empirical problem requires them.

The recurrence has the form of a partial-adjustment model, in which a fixed fraction of the remaining gap closes each period (Nerlove, 1956); the same algebra underlies β-convergence in growth economics (Barro & Sala-i-Martin, 1992). CFS contributes the reading of the gap as a capability–realization distance and the regime analysis outside 0 &lt; β ≤ 1, not the adjustment form itself. The closest antecedent is Nelson and Phelps (1966). They separate an advancing theoretical frontier of technology from technology in practice, and let practice close a fraction of the gap between them at a rate that rises with human capital. In discrete time, their adjustment rule has the same proportional gap-closing form as the Floor equation above. CFS differs in three respects. Its Ceiling advances by a constant increment rather than at a constant growth rate, so its steady state is a constant absolute gap α/β rather than a constant ratio. It analyses discrete-time regimes outside 0 &lt; β ≤ 1, including overshoot and oscillation. And it treats the gap as a capability–realization distance for a declared object and population inside the realization architecture.

A simple numerical illustration makes the recurrence concrete. Suppose the initial gap is 4 units, the Ceiling adds 1 unit per period, and the Floor closes half of the existing gap each period. This is only an illustration of the mechanics, not an empirical calibration.

*G*<sub>0</sub> = 4, α = 1, β = 0.5.

*G*<sub>1</sub> = 1 + (1 - 0.5)(4) = 3.

*G*<sub>2</sub> = 1 + 0.5(3) = 2.5, *G*<sub>3</sub> = 2.25.

The sequence approaches the steady-state gap G<sup>\*</sup> = α/β = 2. The Floor keeps advancing, but because the Ceiling also continues to advance, the gap does not collapse to zero. The example is intentionally simple: thresholds, changing rates, heterogeneous segments, and delay can all alter the path.

For positive α and nonzero β, the simple recurrence has the steady-state gap

G<sup>\*</sup> = α / β.

A nonzero steady-state gap therefore does not imply that synchronization has failed. If the Ceiling continues to advance, the Floor can keep moving while a persistent capability-realization distance remains. The existence of that residual does not identify its substantive meaning; that question remains empirical and returns in §5.5.

The stability behavior follows from the coefficient 1 - β. At β = 0 there is no coupling. For 0 &lt; β &lt; 1, deviations converge monotonically. For 1 &lt; β &lt; 2, deviations alternate in sign but shrink, producing damped oscillation. At β = 2, the coefficient equals -1, giving the marginal constant-amplitude boundary. For β \> 2, oscillations diverge.

These regimes are consequences of the stated recurrence, not universal laws of realization. Changing the recurrence can change the boundaries. Within the baseline model, however, they provide falsifiable qualitative predictions.

As established in §5.2.3, the distinction between observed Slope and structural coupling matters here. A single period cannot validate the recurrence because the implied β is algebraically recoverable from that same period. Testing requires multiple periods and comparison against alternative specifications.

The discrete-time form should be read as an observation-scale model. Continuous-time, stochastic, or nonlinear formulations may be useful in some domains, but Chapter 5 does not assume that their stability boundaries or identification properties are equivalent to those of the recurrence above.

The observation interval is itself part of the operationalization. It should be short enough to resolve the substantive dynamics under study, but long enough for Ceiling and Floor to be measured reliably on comparable scales and for meaningful change to occur. If a regime classification changes materially across reasonable observation intervals, that sensitivity should be reported rather than treated as a stable structural result.

## 5.4 Thresholds and Heterogeneous Adoption

The minimal recurrence assumes that coupling is continuously active. Many realization processes do not behave that way. A capability may need to become good enough, cheap enough, reliable enough, trusted enough, or institutionally acceptable before meaningful assimilation begins.

A hard-gated version of the coupling rate can be written

β<sub>t</sub> = β̄ · 1\[C<sub>t</sub> \> H\].

Below threshold H, the modeled coupling is inactive. Above the threshold, coupling operates at rate β̄. The step function is an idealization; a smoothed gate may be more realistic in many domains. The important claim is conditional activation, not that every realization process contains a perfectly sharp cutoff.

Actors and organizations can also face different thresholds:

β<sub>t</sub><sup>(i)</sup> = β̄ · 1\[C<sub>t</sub> \> H<sub>i</sub>\].

The H<sub>i</sub> values can differ because actors face different costs, risks, complementary requirements, legal obligations, standards of evidence, or switching burdens. As a moving Ceiling crosses those thresholds at different times, the share of actors whose coupling is active can rise slow-fast-slow, an S-shaped pattern, without imposing an S-curve as a separate law.

This connects CFS to a longer technology-diffusion tradition without collapsing the two. Ogburn described cultural lag between material and non-material change; David and Bresnahan-Trajtenberg emphasized complementary reorganization around general-purpose technologies; Perez described installation and deployment periods; Rogers characterized heterogeneous adoption across adopter categories; and diffusion and threshold models formalized aspects of that heterogeneity, although Granovetter’s thresholds concern how many others have already acted rather than a capability level (Ogburn, 1922; David, 1990; Bresnahan & Trajtenberg, 1995; Perez, 2002; Rogers, 1962; Griliches, 1957; Bass, 1969; Granovetter, 1978). CFS applies a moving-frontier adjustment model, already present in Nelson and Phelps (1966), to AI capability, and adds threshold gates and discrete-time regimes.

Threshold heterogeneity can recover a Rogers-style S-curve in one specific observable: the share of actors whose coupling is active,

A<sub>t</sub> = (1/N) Σ<sub>i=1</sub><sup>N</sup> 1\[C<sub>t</sub> \> H<sub>i</sub>\].

If the thresholds H<sub>i</sub> have a single-peaked distribution and the Ceiling rises steadily, A<sub>t</sub> rises slowly at first, quickly as the Ceiling passes through the bulk of the thresholds, and slowly again in the tail: A<sub>t</sub> traces the empirical distribution function of the thresholds along the Ceiling’s path. For example, if the thresholds are drawn independently from a logistic distribution (location m, scale s \> 0) and the Ceiling follows the baseline path C<sub>t</sub> = C<sub>0</sub> + αt with α \> 0, the expected active share is E\[A<sub>t</sub>\] = 1/(1 + exp(−(C<sub>0</sub> + αt − m)/s)), an exact logistic curve in time. The realized share A<sub>t</sub> for N actors is its stepwise counterpart: it moves in increments of 1/N and approaches the expected curve as N grows. The Ceiling’s speed sets the timescale, s/α; the shape comes from the threshold distribution. The S-shape therefore comes from threshold crossing as the Ceiling moves, not from gap closure. With an exactly fixed Ceiling, the active set is fixed and each active Floor closes a fixed fraction of its gap, so aggregate increments decline and no S-curve arises. When the Ceiling keeps moving, the problem changes. New capability increments can cross additional thresholds and produce repeated re-acceleration rather than one diffusion wave toward a fixed target. The converse therefore does not follow: CFS can contain Rogers-style diffusion locally without reducing all moving-frontier synchronization to classical diffusion.

That distinction is especially relevant to AI, where organizations and users may still be adapting to one capability tier while the frontier has already moved to the next.

Recent adoption evidence reinforces the same point without identifying a CFS threshold. Anthropic's Economic Index found that US state-level Claude usage continued to converge but more slowly than previously estimated: the implied time to roughly equal per-capita usage lengthened from 2-5 years to 5-9 years, while international usage became slightly more concentrated, with the top 20 countries' population-adjusted share rising from 45% to 48% (Massenkoff et al., 2026). At a different scale, Imam and Temple (2026) show that technology diffusion need not produce productivity convergence and estimate sharply different transition times above and below a human-capital threshold, which they interpret as absorptive capacity. Neither result identifies H for CFS; both show why common technical capability can coexist with different realization trajectories. A complementary scenario model from the Anthropic Institute likewise separates the tasks AI can affect from how widely it is used. Its substantial and extreme scenarios adopt different capability and diffusion assumptions; the stronger assumption about half of knowledge work belongs to the extreme scenario (Korinek et al., 2026). Those scenarios are explicitly conditional, not predictions, but the separation of capability from diffusion is structurally consonant with the CFS problem.

Thresholds are empirical claims. A nonlinear or S-shaped adoption curve is not enough to establish H retrospectively. A credible threshold analysis requires independent evidence for a substantively meaningful capability or institutional condition, then asks whether coupling changes around it. Curve resemblance is not mechanism validation.

Independent threshold evidence can take several forms: a documented benchmark or reliability crossing, a credentialing or certification event, a regulatory decision, a pre-specified cost or performance constraint, or a natural experiment that changes the relevant condition without being inferred from the same adoption curve. Historical analogs can motivate a candidate threshold but do not establish H for the present case. If no independent evidence can distinguish a threshold from ordinary nonlinear uptake, H should remain unidentified and threshold-gated CFS should not be claimed.

Threshold heterogeneity also does not exhaust heterogeneity. Actors can differ in coupling rate, delay, institutional constraints, and even the realization object being measured. The H<sub>i</sub> formulation isolates one mechanism; it does not imply that one β applies universally.

CFS should ordinarily operate at the lowest analytically meaningful segment for which Ceiling and Floor remain commensurable. Aggregation across segments is defensible only when the realization object, measurement scale, and relevant coupling relation are sufficiently shared. If aggregation hides materially different thresholds, rates, delays, or regimes, the analysis should report segment-specific Floors rather than force a single population-wide *F*<sub>t</sub>. Aggregate summaries can still be descriptive, but they should not replace the segment-level dynamics that generate them.

The threshold-gated extension and the gap-dependent-rate extension in the next section are presented separately. A fuller application could combine gated activation with a post-activation rate that changes as the gap changes, but baseline CFS does not require a single composed functional form.

## 5.5 Rates, Residuals, and the Hard Part of the Gap

Threshold crossing determines when meaningful coupling can begin. It does not imply that coupling remains equally strong as synchronization proceeds.

Some parts of a Ceiling-Floor gap may be relatively easy to close. Once a capability becomes sufficiently useful, early adoption can proceed rapidly: obvious applications are taken up, low-cost substitutions occur, and actors already prepared to change can move first.

What remains afterward may be qualitatively harder. The residual may contain practices requiring deeper institutional change, populations facing higher switching costs, tasks for which capability transfers imperfectly, or forms of realization that actors do not wish to assimilate fully. Synchronization can therefore slow as the gap narrows even after the relevant threshold has been crossed.

The inherited CFS paper offered one illustrative candidate specification in which the structural coupling rate depends on the remaining gap:

β(G<sub>t</sub>) = β<sub>∞</sub> + (β<sub>0</sub> - β<sub>∞</sub>)(G<sub>t</sub> / G<sub>0</sub>)<sup>p</sup>.

Here *β<sub>0</sub>* represents the relatively accessible synchronization rate near the beginning of the post-threshold trajectory, *β<sub>∞</sub>* is the limiting coupling rate as the measured gap becomes small, and *p* controls the shape of the transition. For the displayed form to decline monotonically as *G<sub>t</sub>* shrinks from *G<sub>0</sub>* toward zero, require *p* \> 0 and *β<sub>0</sub>* ≥ *β<sub>∞</sub>* ≥ 0; strict decline requires *β<sub>0</sub>* \> *β<sub>∞</sub>*.

The substantive idea matters more than this particular equation. As realization proceeds, the composition of the remaining gap can change. What is left after easy adjustments have occurred need not be a smaller version of what was present at the beginning. It may be systematically harder to close.

This is why CFS treats the synchronization rate as potentially gap-dependent rather than merely time-dependent. The claim is not that assimilation slows because time has passed. It is that the remaining realization problem may change character as the gap narrows.

### The easy gap and the hard residual

This distinction suggests two analytically different parts of a synchronization trajectory. The first is the easily compressed gap: portions of the capability-realization difference that respond comparatively quickly once coupling begins. The second is the hard residual: what remains after those relatively accessible adjustments have occurred.

The distinction is descriptive, not ontological. CFS does not assume that every domain literally contains two separable substances called an easy gap and a hard gap. It captures the more modest possibility that observed coupling may weaken systematically as progressively harder components dominate the remaining distance.

Early convergence therefore does not determine the asymptote. A process can move quickly through its easiest region and then slow sharply. Conversely, an initially slow trajectory can accelerate after thresholds, complementary infrastructure, or institutional conditions change. The observed rate must be interpreted over the trajectory rather than extrapolated mechanically from one phase.

### What happens at the asymptote?

The most important unresolved quantity is the limiting coupling behavior, summarized here by *β<sub>∞</sub>*. But *β<sub>∞</sub>* does not by itself determine whether a permanent gap remains. Long-run gap behavior also depends on how the Ceiling continues to move.

For the baseline recurrence with persistent positive Ceiling growth, a steady-state gap *G<sup>\*</sup>* must satisfy

*α* = *β*(*G<sup>\*</sup>*)*G<sup>\*</sup>*.

Under persistent α \> 0, G<sup>\*</sup> = 0 cannot be a steady state: continued Ceiling growth continually recreates distance. If Ceiling growth later slows toward zero, the gap may in principle close even when β<sub>∞</sub> \> 0; if β<sub>∞</sub> = 0, closure can become increasingly slow as the gap narrows. Series \#4’s published shorthand mapped β<sub>∞</sub> = 0 to eventual full convergence and β<sub>∞</sub> \> 0 to a permanent residual. The book corrects that shorthand: the limiting coupling rate and the Ceiling path must be interpreted jointly, with a steady-state gap under persistent Ceiling growth satisfying α = β(G<sup>\*</sup>)G<sup>\*</sup> (W.H.L. and Claude 2026b).

> The empirical question is joint: what is the limiting coupling rate, how does Ceiling growth evolve, and what residual follows from their interaction? Current cases contain too few same-metric observations in the decelerating tail to estimate that relationship reliably. A meaningful statistical discrimination would require multiple observations in the tail, enough earlier observations to identify the transition, explicit measurement uncertainty, and comparison of zero versus small positive limiting rates under competing functional forms. No universal minimum observation count is implied by CFS; the required density depends on noise, temporal span, and model separation in the domain.

### A residual does not explain itself

Even if a persistent residual were established, its existence would not reveal its cause. A nonzero long-run gap could reflect a technology limitation, a standing human preference, an institutional constraint, a measurement boundary, or some other relation omitted from the CFS specification.

These explanations can produce similar observed trajectories. The gap alone therefore cannot tell us whether a residual should be closed, protected, remeasured, or interpreted as evidence that the model has omitted something important.

This is another place where description must remain separate from optimization. CFS can identify a persistent differential. It does not determine whether that differential is undesirable.

### The functional form remains provisional

The power-law expression for *β*(*G<sub>t</sub>*) is an illustrative candidate parameterization, not an identified law. Exponential, logistic, hyperbolic, or other monotonic forms could express the same qualitative proposition: coupling changes systematically as the remaining gap changes.

The current evidence does not distinguish among these alternatives. A flexible curve should not be treated as confirmed merely because it can be fitted retrospectively to sparse observations. The empirical test must compare constrained multi-period specifications using enough observations to distinguish genuinely different rate structures.

> *CFS permits the synchronization rate to change with the composition and size of the remaining gap; the particular functional form of that change remains empirically unresolved.*

## 5.6 Continuous Practice, Institutional Gates, and Delay

Not every realized state changes continuously. In some domains, practice can improve gradually while the outcome that matters institutionally remains discrete. A research process may become faster before a treatment receives regulatory approval. A technical system may become more capable before certification is granted. Users may change behavior incrementally while an organization, court, regulator, or standards body still requires a formal decision.

For such cases, the original CFS model distinguishes a continuous Floor from a gated Floor:

F<sub>t</sub><sup>gate</sup> = 1\[F<sub>t-τ</sub><sup>cont</sup> ≥ θ\].

Here *F<sub>t</sub><sup>cont</sup>* is the continuously evolving realized state, *θ* is the institutional threshold, *τ* is the delay, and *F<sub>t</sub><sup>gate</sup>* ∈ {0,1} is an endpoint indicator recording whether the institutional gate has fired. It is not the continuous Floor used to compute the synchronization gap or Slope. Unless the Ceiling and the gated endpoint have independently been placed on a common scale, *C<sub>t</sub>* - *F<sub>t</sub><sup>gate</sup>* is not a valid CFS gap. The underlying gap and Slope continue to use the commensurable continuous readout *F<sub>t</sub><sup>cont</sup>*; the gated indicator records when that evolving state becomes institutionally consequential.

### Two kinds of delay

The most important refinement is that delay need not be uniform in its relationship to capability. The inherited decomposition is

τ = τ<sub>compress</sub>(C<sub>t</sub>) + τ<sub>floor</sub>.

d*τ<sub>compress</sub>* / d*C<sub>t</sub>* ≤ 0, d*τ<sub>floor</sub>* / d*C<sub>t</sub>* = 0 (within the modeled horizon).

The first inequality is strict over intervals in which additional capability actually shortens the task. The second is a horizon-specific modeling condition, not a claim that institutions or physical processes can never change.

The first term represents delay arising from work whose duration can shrink as capability improves. Examples include search, design, prediction, analysis, or discovery tasks for which better AI systems materially reduce the amount of time required.

The second term represents delay that is structurally insensitive to further capability improvement over the relevant horizon. This can include biological observation windows, mandatory review periods, legal waiting periods, certification requirements, or other clocks imposed by established reality or institutional procedure.

That distinction explains why rapid technical progress can compress one portion of a realization pathway while leaving total realization time only modestly changed. Faster Ceiling growth does not imply proportionally faster Floor movement.

### Established reality as a temporal constraint

The structurally fixed component is especially important because it marks a limit on what capability acceleration alone can accomplish. Some realization delays are not computational bottlenecks waiting for a better model. They arise because the realized object depends on events, observations, institutional procedures, or physical processes that take time in the world.

CFS refers to this as an established-reality delay. The term does not mean such delays are immutable forever. Institutions can change procedures, regulators can alter rules, and scientific methods can sometimes redesign observation processes. The narrower claim is that, within the CFS application and observation horizon, the relevant delay is not directly compressed merely by increasing C<sub>t</sub>.

### Gates can be actor-dependent

Institutional gates also need not be determined by one actor. A realization object may require approval from several organizations, jurisdictions, professional bodies, or other decision makers. Their thresholds and timing can differ, and the effective gate can therefore depend on how those decisions are combined.

The original CFS model allows such multi-actor gate structures, but the baseline point remains modest: the realized trajectory may depend not only on continuous assimilation but also on discrete institutional decisions whose thresholds and delays are themselves part of the synchronization environment. The book does not add a new aggregation formula here because the baseline model does not uniquely identify one.

### Relation to Chapter 4

After Chapter 4, these structures should be interpreted carefully. Thresholds, delays, and institutional gates can all be manifestations of the broader domain conditions represented in the realization architecture by Z<sub>d</sub>(t). But the relationship is not an identity.

CFS does not decompose Z<sub>d</sub>(t) into θ, τ<sub>compress</sub>, τ<sub>floor</sub>, or any other fixed set of parameters. Nor does Chapter 5 claim that every domain condition enters realization through an institutional gate.

Instead, the CFS formulation identifies one particular way in which domain conditions can become dynamically visible: they can alter whether coupling occurs, when a realized state becomes institutionally consequential, and how long different stages of realization take.

> *θ, τ<sub>compress</sub>, and τ<sub>floor</sub> are parameters of a particular CFS application, not universal components of the general realization mapping.*

Figure 5.3 visualizes the distinction between capability-compressible and established-reality delay.

<img src="../media/image7.png" title="Figure 5.3" loading="lazy" alt="Two-stage delay diagram comparing lower and higher capability. Higher capability shortens the capability-compressible delay component while the established-reality delay remains unchanged before an institutional gate." />

Figure 5.3. Two kinds of delay. Higher capability can compress the work-dependent component τ<sub>compress</sub>(C<sub>t</sub>) while leaving the established-reality component τ<sub>floor</sub> largely unchanged over the relevant horizon. The result can be major acceleration in one stage without proportional reduction in the total time to a gated institutional outcome.

## 5.7 Dynamical Regimes

The mechanisms developed so far - coupling, thresholds, heterogeneous adoption, changing synchronization rates, and institutional delay - can produce qualitatively different trajectories. CFS summarizes these trajectories through a regime classification.

The regimes are not an additional taxonomy imposed on the model. They are derived behaviors of the synchronization dynamics already introduced. In the baseline recurrence, the structural coupling parameter β determines how the Floor responds to the existing gap and therefore what kind of trajectory follows.

The inherited CFS model distinguishes six regimes. The book makes one mathematical boundary explicit and corrects the published Series \#4 grouping: Series \#4 placed β ≥ 2 in the divergent regime, but at exactly β = 2 the recurrence coefficient is 1 - β = -1, producing marginal constant-amplitude oscillation rather than divergence. Genuinely divergent oscillation therefore begins at β \> 2 (W.H.L. and Claude 2026b).

Table 5.1. Six regimes of the baseline CFS recurrence

| **Regime**              | **Structural condition**              | **Characteristic behavior**                                                                                    | **Interpretation**                                                                                                           |
|-------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 0 - Pre-threshold       | Coupling not yet activated            | Coupling inactive: observed Slope is zero while the gap is nonzero (the ratio is undefined only at a zero gap) | The relevant capability or other precondition has not yet crossed the threshold required for this segment to begin coupling. |
| 1 - Stagnation          | β = 0 after the relevant gate is open | Gap continues to grow as the Ceiling advances                                                                  | Capability is sufficiently established, but the Floor does not respond through the modeled synchronization channel.          |
| 2 - Lagging convergence | 0 &lt; β &lt; 1                           | Floor rises while remaining behind the Ceiling                                                                 | The ordinary catch-up case: realization responds positively but closes less than the existing gap per period.                |
| 3 - Steady-state parity | β = 1                                 | Each period's existing gap is closed before the next Ceiling increment                                         | The Floor absorbs the available prior-period gap but remains one capability increment behind a moving Ceiling.               |
| 4 - Overtrust, damped   | 1 &lt; β &lt; 2                           | Gap deviations alternate and shrink around the fixed point                                                     | The inherited overtrust interpretation additionally requires reliance beyond the contemporaneous Ceiling (§5.7).             |
| 5 - Overtrust, runaway  | β \> 2                                | Gap deviations alternate and grow                                                                              | Repeated correction is unstable; an overtrust interpretation also requires a meaningful crossing. β = 2 is marginal.         |

**Note.** Regime 0 and Regime 1 cannot be distinguished from the adoption trajectory alone; independent evidence of threshold crossing is required.

### Regime 0 and Regime 1 are not the same

In Regime 0, synchronization has not begun because the relevant threshold has not yet been crossed. In Regime 1, the relevant capability threshold has already been crossed, but the Floor still fails to respond.

The observed trajectories can look similar - little or no assimilation while the Ceiling continues to move - but they imply different mechanisms. The distinction cannot responsibly be inferred from the adoption curve alone. It requires independent evidence about whether the relevant threshold has actually been crossed. Where that evidence is unavailable, the correct classification is ambiguous between Regimes 0 and 1.

### Regime 2 and the unresolved residual

Regime 2 is the most familiar synchronization pattern. Capability moves ahead; realization follows. The gap narrows or remains bounded because positive coupling exists, but the Floor does not instantaneously absorb the full differential.

The long-run interpretation remains unresolved. Under persistent positive Ceiling growth, the baseline recurrence sustains a positive steady-state gap whenever a stable solution exists; if Ceiling growth later slows toward zero, the gap may continue to close. Current evidence is too sparse to identify the joint tail behavior of Ceiling growth and coupling reliably.

### Regime 3 is not perfect simultaneity

At β = 1, the Floor closes the existing gap completely during each period. But if the Ceiling continues to advance by α, this does not mean F<sub>t</sub> = C<sub>t</sub> at every instant. The recurrence collapses immediately to G<sub>t+1</sub> = α: each capability increment recreates a one-period differential.

Regime 3 is therefore better understood as steady-state tracking than as timeless equality between capability and realization.

### Overtrust as a testable prediction

For a positive gap, $\beta\  > \ 1$ moves the Floor beyond the prior-period Ceiling. With continued Ceiling growth, exceeding the contemporaneous Ceiling requires $(\beta\  - \ 1)G_{t}\  > \ \alpha$. The oscillatory regimes concern deviations around the fixed-point gap; those deviations can change sign while the gap remains positive. Their interpretation as overtrust therefore requires an operationalization of reliance beyond demonstrated capability, rather than the coupling value alone.

For 1 &lt; β &lt; 2, deviations around the fixed-point gap alternate and shrink. For β \> 2, these deviations grow. These regimes matter even though the original empirical study did not confirm a clean multi-period overtrust trajectory in any of its four principal domains.

That absence remains an empirical result. Overtrust may be uncommon, the sample may be too small, observations may be too coarse, AI-specific adoption may favor undertrust, or later evidence may reveal the predicted regime. The current cases cannot decide among those possibilities.

Accordingly, Regimes 4 and 5 should be read as derived, testable predictions rather than claims about empirical prevalence. Their test also depends on operationalization: if an analyst truncates or defines the Floor so that *F<sub>t</sub>* ≤ *C<sub>t</sub>* by construction, overshoot becomes unobservable by definition and such data cannot test crossing beyond the contemporaneous Ceiling, although they may still test oscillation around a positive fixed-point gap.

### Regimes can coexist within one domain

A domain should not automatically receive one regime label. Enterprise users may cross a capability threshold before individual users. One jurisdiction may permit deployment while another blocks it. Regulators and consumers may react to the same capability frontier through different thresholds and coupling structures.

*One Ceiling does not imply one population-wide regime.*

Where meaningful segments can be identified, regime classification should be indexed to those segments rather than averaged into a single domain label.

### What the regimes do not classify

Regimes 4 and 5 describe the Floor oscillating relative to a stable underlying threshold structure. They do not automatically describe a case in which the threshold itself moves back and forth because regulators, institutions, political actors, firms, or other participants repeatedly alter the effective gate.

That is a different mechanism: endogenous gate oscillation. The original CFS empirical work identified it but deliberately did not force it into the six-regime taxonomy. Later Governance and Contestation work provides richer concepts for understanding how actor-dependent gates can change, but Chapter 5 does not retroactively insert those mechanisms into the original recurrence.

A regime is therefore a derived model prediction, not a descriptive label to be assigned whenever a trajectory looks vaguely similar.

## 5.8 Empirical Contact

The formal CFS paper brought the model into contact with four domains: professional Go; AlphaFold and AI-assisted drug development; frontier language-model releases; and autonomous-vehicle deployment.

These cases should not be read as four statistical validations of the recurrence. They were selected because they place different parts of the model under pressure. The empirical question is which mechanisms each case actually exercises, which predictions survive contact with the evidence, and which remain unresolved.

### Professional Go: a clean threshold with a heterogeneous Floor

Professional Go provides the clearest empirical contact with threshold-gated synchronization. The public arrival of superhuman Go systems supplied a distinct capability event, after which professional move quality and alignment with AI recommendations improved, especially in earlier game phases where uncertainty is higher (Choi et al., 2025b).

The case is useful because the Ceiling event is relatively well dated and the domain has little institutional gating compared with the other cases. But the Floor is not homogeneous. A 2026 panel study of 770 professional Go players from 2012 through 2023 found that widespread AI diffusion did not simply level professional performance. Performance became more concentrated and leadership shifted toward younger cohorts better positioned to absorb the AI environment (Shin et al., 2026).

For CFS, the important implication is that even inside a bounded domain with a broadly shared capability shock, realized assimilation can remain strongly heterogeneous. One Ceiling event therefore need not produce one uniform Floor trajectory.

Series \#4 also reported one provisional empirical Slope calibration from two opening-phase, same-metric anchors: G₀ ≈ 2.47 percentage points before 2017 and G₁ ≈ 1.71 percentage points for the 2017–19 average. Annualized over the roughly two-year post-threshold window, these anchors imply Sₜ ≈ 15–17% per year (W.H.L. and Claude 2026b). With only two anchor points, this is a provisional point estimate—not a confidence interval, not evidence for a constant annual rate, and not a statistical fit of the recurrence.

The available same-metric evidence nevertheless remains sparse for estimating long-run synchronization. The sparse Go anchors are compatible with a Regime 2 interpretation over the observed post-threshold interval; they do not identify a fitted recurrence or uniquely establish that regime, but current observations do not identify the joint tail behavior of Ceiling growth, coupling, and the residual.

Go also illustrates a measurement problem. Different portions of a game do not provide equally stable measures of human-AI convergence. Apparent convergence can partly reflect narrowing choice sets rather than genuine synchronization. The choice of metric can manufacture an apparent shrinking gap; §5.9.5 therefore treats this not as a Go-specific caveat but as a general measurement-survival problem.

### AI-assisted drug development: the institutional clock advances

AI-assisted drug development exercises a different part of CFS. Advances in target identification, molecular modeling, and generative design can accelerate parts of discovery even while the eventual realization object - an approved and clinically established treatment - remains behind biological and institutional gates.

The Rentosertib program provides a concrete illustration. The AI-enabled discovery-to-preclinical-candidate process was completed in roughly 18 months, demonstrating substantial compression in an early stage of the pathway (Ren et al., 2025). On July 7, 2026, Insilico Medicine announced initiation of a Phase III trial, moving the program farther into the late-stage clinical clock (Insilico Medicine, 2026).

That progression strengthens the empirical relevance of the two-clock interpretation. A capability-compressible discovery process has handed off into stages governed increasingly by clinical observation, trial duration, and institutional decision. But the terminal gate still has not fired: Phase III entry is not approval, and it does not identify the eventual value of τ<sub>floor</sub>, the long-run Floor, or β<sub>∞</sub>.

A provenance distinction remains important. Rentosertib is an AI-native drug-development case, but it is not a direct AlphaFold-descended calibration. It should remain illustrative evidence for the delay decomposition rather than being converted retrospectively into an AlphaFold-to-approval trajectory.

### Frontier models: heterogeneous Floors, moving Ceilings, and a moving measurement frontier

Frontier language models provide the richest case for heterogeneity. Consumer users, enterprises, firms of different sizes, industries, governments, and jurisdictions can face the same advancing capability frontier while crossing different thresholds and encountering different constraints. A single undifferentiated Floor would conceal much of the relevant structure.

This domain also makes the measurement problem unusually visible. Several bounded benchmarks approached their maximum scales while frontier capabilities continued changing, motivating the use of task-completion time horizon as a less mechanically bounded capability proxy.

By 2026, however, that instrument was itself encountering a measurement frontier. METR warns that time-horizon measurements above roughly 16 hours are unreliable with the current task suite, and its methodological analysis notes that saturation increases sensitivity to modeling assumptions and task-distribution choices (METR, 2026; Barry, 2026).

This sharpens rather than weakens the Chapter 4-5 measurement argument. A proxy chosen partly to escape saturation can itself later encounter saturation or identification limits. Measurement constraints can relocate as the capability frontier moves.

Frontier models also provide empirical contact with heterogeneous thresholds and multi-actor gates. At the same time, policy gates can move under contest among actors. That is endogenous gate oscillation: the threshold itself changes. It is not the same mechanism as Regimes 4 or 5, in which the Floor oscillates relative to a stable threshold structure.

The 2026 mathematics results add a sharper moving-Ceiling stress test. OpenAI reported a set of ten results resolving or materially advancing long-standing problems; Anthropic reported an unreleased system improving a lower bound related to the Riemann hypothesis from 41.6% to 67.2% and later reported a largely autonomous, computer-checked formalization of Fermat's Last Theorem completed over 11 days; and OpenAI subsequently released a proposed Navier-Stokes Millennium Problem solution produced by an internal model (OpenAI, 2026l; Anthropic, 2026e, 2026c; OpenAI, 2026d). If sustained under external scrutiny, these results raise the observed lower bound on selected mathematical capability Ceilings. They do not establish an ultimate Ceiling for mathematics, nor do they imply that one capability proxy has become globally commensurate with human mathematical expertise.

The recurring comparison with AlphaGo's 2016 threshold moment is therefore useful only as an analogy. Go supplied a fixed rule system and a clear performance criterion; research mathematics is open-ended and contains multiple realization objects. A June 2026 benchmark using previously unseen research-level problems still found the tested AI systems below top human mathematicians (Castelvecchi, 2026a). The combined evidence is better read as a rapidly moving and uneven capability frontier than as a single crossing from below-human to above-human mathematics.

The same episode also reveals that Floors can fragment as the Ceiling advances. Solution generation, formal verification, human understanding, method formation, training, and institutional acceptance can move on different clocks. Nature Machine Intelligence (2026) noted that independent verification workflows were not keeping pace with increasing AI use in mathematics and emphasized that mathematical practice cannot be reduced to correct-answer production. Unless a common scale is independently justified, these are separate realization objects rather than components to be averaged into one F<sub>t</sub>.

### Autonomous vehicles: asynchronous gate opening

Autonomous-vehicle deployment provides the clearest contemporary illustration of jurisdictional gating. On June 24, 2026, UNECE adopted the first global regulatory framework enabling fully autonomous driving systems under harmonized safety, testing, validation, and in-service monitoring requirements (UNECE, 2026). That development changes the regulatory environment without eliminating jurisdiction-specific gates.

The European trajectory of Tesla's FSD (Supervised) system illustrates the distinction. By September 8, Slovenia had joined the Netherlands, Lithuania, Estonia, Denmark, and Belgium as the sixth European country to clear the supervised driver-assistance system, while broader European authorization remained under review (Reuters, 2026g). The pattern is therefore not a simple transition from blocked to approved, but a staggered series of jurisdiction-specific gate openings.

A second development makes the realization-object boundary clearer. On September 4, 2026, NHTSA opened an Audit Query into Tesla's self-certification of newly deployed Cybercab vehicles, which lack traditional manual controls (NHTSA, 2026). Cybercab should not be merged into the FSD (Supervised) synchronization series: one concerns supervised driver assistance, the other driverless automated driving. Different realization objects can occupy different gate states simultaneously.

The operational rule is simple: heterogeneous segments may share one CFS application only when the realization object is held fixed. When the realization object changes - as between supervised FSD and driverless Cybercab - the analyst should instantiate separate Ceiling-Floor applications unless cross-object commensurability is independently established. Otherwise, subtracting one object's Floor from another object's Ceiling risks a category error rather than measuring synchronization.

The original autonomous-vehicle case also produced an important negative result that remains intact. It had been selected partly because escalating safety scrutiny might produce the overtrust-and-correction trajectory represented by Regime 4. The available consumer series did not show the expected sustained pullback, and the 2026 updates still do not supply a clean multi-period Regime 4 trace.

Table 5.2. Empirical status across the four CFS domains

| **Domain**                   | **Mechanism most clearly exercised**                                 | **2026 update**                                                                                              | **What remains unresolved**                                                   |
|------------------------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Professional Go              | Threshold crossing; post-threshold convergence                       | New panel evidence strengthens within-domain Floor heterogeneity                                             | Long-run residual; limiting coupling behavior                                 |
| AI-assisted drug development | Two-tier Floor; compressible vs. persistent delay                    | Rentosertib entered Phase III                                                                                | Terminal approval gate; long-run delay and residual                           |
| Frontier models              | Heterogeneous thresholds; segment-specific Floors; multi-actor gates | METR time-horizon suite now encounters upper-range reliability limits                                        | Long-run rate behavior; clean overtrust trace; specific β(G<sub>t</sub>) form |
| Autonomous vehicles          | Jurisdiction-specific gates; threshold heterogeneity                 | Global ADS framework advanced; supervised-FSD gates open asynchronously; Cybercab meets a distinct U.S. gate | Regime 4 still unconfirmed; cross-object trajectories should not be collapsed |

Across the four cases, threshold gating and heterogeneous realization receive repeated empirical contact. The two-tier Floor and delay decomposition receive more selective support. The specific functional form of β(G<sub>t</sub>) has not been statistically fitted in any domain. The value of β<sub>∞</sub> remains unidentified. And no case provides a confirmed multi-period instance of the model's overtrust regimes.

The 2026 updates do not overturn those conclusions. They sharpen them: professional assimilation remains heterogeneous after a common capability shock; a drug-development trajectory has moved farther into its slower clinical clock; a capability metric has encountered a new measurement boundary; and vehicle-deployment gates are opening asynchronously while a different realization object encounters fresh regulatory scrutiny.

> *The four cases provide empirical contact with particular CFS mechanisms and regimes, while several functional, asymptotic, measurement, and regime-level predictions remain unresolved.*

The original calibrations were not formal statistical fits of the complete recurrence, and the new evidence does not change that status. CFS is more than an illustrative metaphor because its mechanisms generate empirical distinctions that cases can support, fail to support, or leave unresolved. But empirical contact is not statistical validation.

## 5.9 Where CFS Stops

A model becomes more useful when its limits are visible. CFS was developed to study one recurring class of realization dynamics: cases in which a domain-specific capability state and a corresponding realized or assimilated state can both be represented over time, and in which their changing relationship can be meaningfully described through gaps, thresholds, coupling rates, and delays.

That is already a substantial domain. It is not the whole of realization. The correct response when a realization process falls outside that region is not to keep enlarging CFS until it fits. It is to say where CFS stops.

### 5.9.1 CFS versus the general realization mapping

R<sub>g</sub>(t) = μ<sub>t</sub>(P(t), Av(t), Ex<sub>g</sub>(t), Z<sub>d</sub>(t)).

CFS does not replace this mapping. Instead, a CFS application selects a domain-scoped capability readout C<sub>t</sub> and a domain-scoped realization or assimilation readout F<sub>t</sub>, then studies their relationship over time.

C<sub>t</sub> ≠ P(t), F<sub>t</sub> ≠ R<sub>g</sub>(t).

The same applies to the gap. Within a CFS application, G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub> is an operational synchronization gap, not a universal representation of every failure or delay in realization.

A realization process can remain poorly realized because capability is unavailable, because relevant populations are not exposed, because the realization object is misidentified, because institutional conditions prevent a mapping from forming, or because path dependence changes which future states remain reachable. Some of those processes may admit useful Ceiling and Floor representations. Others may not.

> *Given interpretable capability and realized states, CFS asks how the relation between them evolves. The general realization mapping asks the prior and broader question: how does Potential become realized at all?*

### 5.9.2 Bottleneck relocation versus path foreclosure

Chapter 4 distinguished two forms of changing constraint. In bottleneck relocation, the dominant obstacle to realization moves. A capability threshold may be crossed, making institutional approval the new limiting factor. A computational task may become cheap enough that infrastructure becomes binding. A discovery bottleneck may disappear while observation time becomes dominant.

CFS can often represent this kind of movement. Thresholds can activate coupling. Different components of delay can dominate at different stages. A shrinking easy gap can leave a harder residual. Institutional gates can become the relevant limiter after capability improves.

A contemporary frontier-lab example makes the relocation logic visible. OpenAI reports that by mid-August 2026 its research organization was using 3.1 agent-workdays for every human workday, and anticipates that as more work becomes automatable, the least automatable tasks will take a larger share of researcher effort and compute may become a more important constraint (OpenAI, 2026j). The mathematics case has a parallel structure: faster proof generation or formalization can make verification, exposition, interpretation, and expert judgment newly binding. These observations are evidence of bottleneck relocation, not evidence that baseline CFS already models path foreclosure.

Path foreclosure is stronger. It occurs when taking one realization path changes the opportunity set itself by removing, degrading, or making unavailable another realization possibility. That is not automatically represented by G<sub>t</sub> = C<sub>t</sub> - F<sub>t</sub>, nor by changing β, θ, or τ.

> *Bottleneck relocation may occur inside ordinary CFS dynamics. Path foreclosure does not automatically belong to baseline CFS.*

A case in which foreclosure is central therefore requires either an explicitly extended model or analysis at the broader realization level. CFS should not silently absorb the distinction by relabeling foreclosure as an unusually large delay or an unusually small coupling rate.

### 5.9.3 Synchronization versus Optimization

CFS is a dynamical model. It describes how a trajectory evolves under specified assumptions. It does not determine which trajectory ought to be preferred.

A smaller gap is not necessarily better. Faster assimilation is not necessarily desirable. A higher synchronization rate is not automatically socially optimal. A persistent residual may represent failure, but it may also represent precaution, institutional protection, standing preference, or a realization object that should not be maximized.

The distinction is straightforward: synchronization characterizes the dynamics of a trajectory; choosing among possible trajectories is a different problem. Prior Optimization work in the Gradual AGI series takes up that normative problem explicitly (W.H.L. et al. 2026j). Chapter 5 does not answer it in advance.

#### When synchronization is contested

A persistent gap should not automatically be interpreted as failed adoption. In some domains, actors may contest whether the capability represented by the Ceiling should be fully realized, or whether the selected Floor captures the realization object they value. The IMU-endorsed Leiden Declaration, for example, calls for disclosure, independent verification, human responsibility, appropriate attribution, and preservation of research autonomy in AI-assisted mathematics; Weinreich (2026) articulates a much stronger position of opposition. These positions differ substantively, but together they demonstrate that non-synchronization can be intentional rather than merely delayed.

The first analytical response is therefore to re-check the realization object. Solution production, formal verification, mathematical understanding, method formation, training, and institutional acceptance are not interchangeable Floors. If the specified object is humanly assimilated mathematical knowledge, a machine-generated correct proof need not constitute the same realized state as answer production. Different objects should ordinarily be modeled in separate CFS applications unless their commensurability has been independently established.

Observable resistance can alter a CFS trajectory only through something that becomes behaviorally or institutionally measurable: a lower effective coupling rate, a changed threshold, a longer delay, a new gate, or a re-specified realization object. Concern alone is not a parameter change. **CFS measures synchronization to a specified realization object; it does not presume that maximal synchronization to that object is desirable.** Once the question becomes whether preserving or closing the gap is preferable, the analysis has crossed into Optimization.

### 5.9.4 Governance and endogenous gate changes

Governance can alter CFS parameters. A regulator may raise or lower an approval threshold. A legislature may impose a waiting period. An institution may change the conditions under which a system is permitted. Different actors may hold effective vetoes over different parts of a realization pathway.

These interventions can appear inside a CFS application as changes in θ, τ, or the effective coupling structure. But CFS does not explain the governance process that produced those changes.

This is where the distinction between an exogenous gate and an endogenously changing gate becomes important. The threshold-gated formulation in §5.4 assumes that the threshold can be represented as sufficiently stable for the synchronization problem being modeled. Yet the empirical evidence reviewed in §5.8 showed cases in which the gate itself moves under contest among actors.

Series \#4 already experimented with a provisional multi-actor gate formulation in which an effective local threshold was represented by an aggregation function Φ over actor-specific thresholds and time-varying influence weights, together with a veto-max interpretation in which the most restrictive sufficiently influential actor could become binding. The book intentionally does not retain that extension as baseline CFS. Later Governance and Contestation work now owns actor dependence, veto structure, and endogenous gate formation (W.H.L. and Claude 2026g). Those tools can inform how a CFS parameter changes, but they should not be written retroactively into the baseline recurrence as though CFS itself explains the governance process.

> *Governance can change the parameters of a CFS trajectory without becoming another argument of the CFS recurrence itself.*

### 5.9.5 Observation and metric failure

CFS is only as informative as the measurements used to represent Ceiling and Floor. A bounded capability metric can make the Ceiling appear to stop moving. A coarse Floor measure can make assimilation look stagnant. A change in measurement scope can create an artificial gap or artificial convergence. Sparse observations can miss oscillation entirely.

And a proxy that initially provides useful discrimination can itself become saturated as the capability frontier advances. The updated frontier-model evidence in §5.8 provides a clear example: task-completion time horizon extended measurement beyond several bounded benchmarks, yet the task suite itself began approaching its reliable limit (METR, 2026; Barry, 2026).

Pachocki's (2026) "An Alien Mind" provides a contemporary frontier-lab formulation of the same measurement problem: capabilities that are easy to measure can improve faster than capabilities that are difficult to quantify, while increasing system capability can make the overall capability profile harder to characterize. This does not imply that the Ceiling is unknowable. It reinforces the distinction between movement in the underlying capability relevant to the realization object and movement in the proxy used to observe it. When the proxy ceases to discriminate meaningfully, the remedy is a documented bridge or a new measurement epoch, not an unmarked splice.

The measurement bottleneck relocated. That is not a failure of the underlying realization process. It is a failure of observation to remain well matched to the process being measured.

Apparent convergence also requires checks against changes in what is measured. A task’s remaining solution space can narrow as one instance approaches completion; a Go endgame is not evidence of learning across calendar time. An external gate or clock can change what is observed or admitted without identifying faster underlying adaptation. An aggregate series can combine populations with different gates and adjustment rates, concealing those differences behind a smooth trend. These cautions carry forward Series \#4’s methodological caveat (W.H.L. and Claude 2026b, §2.5). Alongside benchmark saturation, they require the task space, measurement window, gate state, population composition, and scale to be declared before interpreting a measured closure rate. Where these explanations cannot be separated, apparent narrowing does not identify the structural coupling parameter.

#### Measurement revision protocol

Proxy revision is legitimate only when the reason is documented independently of the desired CFS result - for example, saturation, construct drift, task-suite exhaustion, or a known change in what the metric measures. Where several plausible Ceiling proxies exist, choose one primary proxy based on the specified realization object, domain relevance, longitudinal interpretability, and resistance to known saturation; use alternatives as sensitivity checks rather than averaging them without an independently justified weighting rule.

When a proxy must change mid-trajectory, preserve an overlap or bridge period whenever possible and report the old and new measures side by side. Do not splice incomparable scales into one continuous *G<sub>t</sub>* or *S<sub>t</sub>* series merely to preserve continuity.

If no defensible bridge exists, close the earlier measurement segment and begin a new CFS application or measurement epoch. Earlier Slope estimates remain claims about the earlier operationalization; they should not be retrospectively recomputed on a later proxy unless the mapping between the two measures is independently established.

observed G<sub>t</sub> ↓ ⇏ genuine synchronization

observed S<sub>t</sub> ≈ 0 ⇏ genuine stagnation

Observation/Evidence therefore does not add another term to the recurrence. It constrains what can responsibly be inferred from the recurrence.

### 5.9.6 When not to use CFS

CFS should be used selectively. A strong application usually requires most of the following:

> 1\. a bounded domain and explicit realization object;
>
> 2\. an interpretable capability state C<sub>t</sub>;
>
> 3\. an interpretable realized or assimilation state F<sub>t</sub>;
>
> 4\. repeated observations over time using reasonably stable metrics;
>
> 5\. a meaningful capability-realization gap G<sub>t</sub>;
>
> 6\. a plausible coupling mechanism between Ceiling and Floor;
>
> 7\. evidence that thresholds, rates, delays, or gate structures matter analytically; and
>
> 8\. competing simpler models against which the CFS specification can be evaluated.

When these conditions are substantially absent, the model should not be rescued by adding parameters. If the Ceiling cannot be operationalized, CFS has no defensible capability state. If the Floor changes definition from one period to another, the gap may have no stable interpretation. If only one observation exists, structural coupling cannot be identified. If no plausible relation connects the selected Ceiling to the selected Floor, their subtraction may be numerically possible but analytically meaningless.

If the realization object itself changes, one longitudinal series may actually combine different processes. Different realization objects should ordinarily be treated as separate CFS applications unless a common scale and mapping are independently justified; segment indexing alone does not repair an object mismatch.

If the dominant mechanism is path foreclosure rather than differential movement within an available opportunity set, baseline CFS is incomplete by construction. And if the data cannot distinguish CFS from a simpler account, the simpler account should remain preferred.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Sidebar 5.C The Stop Rule</strong></p>
<p>Do not introduce a new variable, regime, scalar, or mechanism merely to make every realization problem fit CFS.</p>
<p>If Ceiling, Floor, longitudinal measurement, or plausible coupling cannot be specified without material ambiguity, stop rather than rescue the model.</p>
<p>The correct scientific verdict is: CFS not presently applicable.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

CFS earns its place in the Unified Gradual AGI framework precisely by remaining local. It gives a formal language for capability and realized assimilation moving on different clocks, but it does not replace the general realization architecture, decide which trajectories are desirable, explain governance processes, solve path foreclosure, or guarantee that its own observables remain valid. Those limits are not omissions to be repaired. They define the model.

## 5.10 Falsifiers, Open Questions, and Handoff

CFS is useful only if its claims can fail. The existence of a Ceiling-Floor gap is not itself evidence for the recurrence. A threshold-shaped trajectory is not by itself evidence for threshold gating. A fitted curve is not evidence for a particular synchronization-rate function merely because enough parameters can reproduce the observations.

### What would count against CFS?

> 1\. The recurrence should lose support if a constrained multi-period specification fails to predict the observed Floor trajectory better than simpler competing models. A one-period estimate of β cannot provide this test because it is algebraically tied to the observed Slope.
>
> 2\. Threshold gating should lose support if independently identified threshold crossings do not correspond to systematic changes in coupling or realized movement. An S-shaped adoption curve alone is insufficient.
>
> 3\. The heterogeneous-threshold extension should lose support if segment-level differences disappear once measurement, exposure, and realization-object differences are properly controlled.
>
> 4\. A gap-dependent synchronization rate should lose support if sufficiently dense longitudinal data show no systematic relation between the remaining gap and subsequent coupling, or if competing functional forms consistently perform better.
>
> 5\. The two-tier delay structure should lose support where supposedly capability-compressible and structurally persistent components cannot be empirically distinguished. If all observed delay responds to capability in the same way, the decomposition adds no explanatory value.
>
> 6\. A regime classification should lose support when stable measurement shows behavior inconsistent with the recurrence's own stability conditions. Regime labels should follow the dynamics, not rescue them.
>
> 7\. The entire CFS application should be abandoned if Ceiling, Floor, or their relation cannot be operationalized consistently over time. Numerical subtraction is not enough; the two states must remain analytically meaningful.

These are not all-or-nothing tests of the entire Unified Gradual AGI framework. CFS is a bounded submodel. Evidence may reject a threshold extension while leaving the minimal recurrence useful. A particular β(G<sub>t</sub>) form may fail while a different rate structure survives. One domain may reject CFS altogether while another remains well described by it. Falsification should occur at the level of the claim actually being tested.

What would count as positive evidence? Stronger support would require more than retrospective fit: a stable same-metric longitudinal panel in which a constrained CFS specification predicts held-out or future Floor movement better than plausible simpler alternatives, with thresholds, delays, or other mechanisms identified independently of the outcome series where possible. Replication across distinct segments or domains would strengthen claims of portability, but it would not make any parameter universal.

CFS also does not identify causal counterfactuals by itself. The recurrence describes an observed capability-realization relationship under the chosen operationalization; it does not tell us what the Floor would have done without the capability advance or under a different institutional path. Such claims require an external causal design - for example, a natural experiment, matched comparison, instrumental strategy, or another defensible source of counterfactual identification.

### What remains open

Several questions survive this chapter deliberately unresolved.

The first is the long-run residual and the limiting coupling rate. The available evidence does not identify *β<sub>∞</sub>*, and *β<sub>∞</sub>* alone does not determine whether a permanent residual remains. Under persistent positive Ceiling growth, any steady-state gap must satisfy *α* = *β*(*G<sup>\*</sup>*)*G<sup>\*</sup>*; if Ceiling growth later slows toward zero, different limiting-rate forms can imply different speeds of closure. The empirical problem is therefore to identify the joint long-run behavior of Ceiling growth, coupling, and the residual. Even if a persistent residual is eventually established, its meaning remains unidentified: technology limitation, standing human preference, institutional constraint, measurement boundary, or another relation missing from the specification.

The second open question is overtrust. The recurrence permits crossing beyond the contemporaneous Ceiling under the condition stated in §5.7; its oscillatory parameter regimes alone do not establish that crossing. Yet none of the four principal empirical domains has produced a clean, multi-period Regime 4 or 5 trace.

The third is endogenous gate oscillation. The original empirical work identified situations in which the threshold itself changes under contest among actors. Baseline CFS does not solve that mechanism.

The fourth is functional form. The displayed power-law representation of *β*(*G<sub>t</sub>*) is only an illustrative candidate satisfying the qualitative idea of gap-dependent coupling under the stated parameter conditions. It is not uniquely identified. Exponential, logistic, hyperbolic, or other monotonic forms remain viable until denser longitudinal evidence distinguishes among them.

The fifth is capability growth itself. The baseline approximation C<sub>t+1</sub> = C<sub>t</sub> + α treats Ceiling growth as locally constant. That assumption was introduced to expose synchronization dynamics, not to assert permanently linear capability growth. The 2026 mathematics shocks make the locally constant-growth approximation especially fragile during frontier jumps: the recurrence can still be used over a bounded interval, but a large observed capability discontinuity should not be smoothed into α merely to preserve a preferred regime classification.

The sixth is measurement survival. A proxy that works at one stage of a trajectory may fail later through saturation, scope drift, task-suite exhaustion, or changes in what the metric actually represents. The 2026 frontier-model update provides a direct example. Rapidly changing capability geometry can also force a new measurement epoch even when the underlying research question is unchanged; continuity of inquiry does not justify continuity of scale.

Finally, the empirical record remains sparse. None of the four original domains supplies a formal statistical fit of the complete recurrence. Calibration rests largely on longitudinal anchor points and mechanism-specific evidence rather than dense panels sufficient to discriminate among several nearby dynamical models.

### What Chapter 5 establishes

Within those limits, the chapter formulates a bounded dynamical interpretation of uneven realization, derives its conditional regimes, and examines mechanism-specific empirical contact. Capability and realized assimilation can move on different clocks. Their relation can be represented, in suitable domains, through a Ceiling, a Floor, and an observable Slope. The gap can evolve through continued capability growth and differential realization. Coupling can be threshold-gated. Different populations can cross different thresholds. The synchronization rate can change as the composition of the remaining gap changes. Continuous realization can coexist with discrete institutional gates. Some delays can be compressed by advancing capability while others remain structurally persistent over the relevant horizon. And a minimal recurrence can generate qualitatively different regimes rather than requiring those regimes to be imposed afterward.

None of these results makes CFS universal. CFS is one realization-dynamics submodel inside the broader architecture developed in Chapter 4. It does not define Potential, replace the general realization mapping, explain every gate, solve path foreclosure, choose a desirable trajectory, or guarantee that its observables remain valid.

> *CFS describes how a specified capability-realization relationship evolves when both sides can be meaningfully observed over time.*

### Handoff to Optimization

A dynamical model can tell us that trajectories differ. It can tell us that one trajectory closes a gap faster than another. It can reveal persistent residuals, delayed gates, unstable overshoot, or heterogeneous realization. But none of those observations determines what society should prefer.

A smaller gap can represent beneficial assimilation - or premature reliance. A slower Floor can reflect costly institutional inertia - or deliberate precaution. A persistent residual can represent unfinished adoption - or a boundary that actors intentionally preserve.

Once the question becomes whether a trajectory is good, desirable, safe, equitable, robust, or worth steering toward, dynamics alone no longer suffice. The problem has changed from description to choice.

> *CFS asks how a trajectory evolves.  
> Optimization asks which trajectory should be preferred.*

Chapter 6 begins there.

## Chapter References

References below include the principal theoretical lineage, Gradual AGI source papers that supply the inherited CFS framework and later interfaces, and the empirical sources cited directly in this chapter. Live 2026 updates used in §§5.4, 5.8, and 5.9 are included explicitly.

Anthropic. (2026e, August 10). Learning more about Claude's mathematical capabilities. [https://www.anthropic.com/research/riemann-zeta](https://www.anthropic.com/research/riemann-zeta)

Anthropic. (2026c, September 4). Formalizing Fermat's Last Theorem. [https://www.anthropic.com/research/formalizing-fermats-last-theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

Barro, R. J., & Sala-i-Martin, X. (1992). Convergence. *Journal of Political Economy*, 100(2), 223–251.

Barry, A. (2026, March 20). Impact of modelling assumptions on time horizon results. METR. [https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)

Bass, F. M. (1969). A new product growth for model consumer durables. *Management Science*, 15(5), 215–227.

Bresnahan, T. F., & Trajtenberg, M. (1995). General purpose technologies: “Engines of growth”? Journal of Econometrics, 65(1), 83–108. [https://doi.org/10.1016/0304-4076(94)01598-T](https://doi.org/10.1016/0304-4076(94)01598-T)

Castelvecchi, D. (2026a, June 12). Humans outperform AI at this highly rigorous mathematics test. Nature, 654, 847-848. [https://doi.org/10.1038/d41586-026-01888-9](https://doi.org/10.1038/d41586-026-01888-9)

Choi, S., Kang, H., Kim, N., & Kim, J. (2025b). How does artificial intelligence improve human decision-making? Evidence from the AI-powered Go program. Strategic Management Journal, 46(6), 1523–1554. [https://doi.org/10.1002/smj.3694](https://doi.org/10.1002/smj.3694)

David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. American Economic Review, 80(2), 355–361.

Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420–1443.

Griliches, Z. (1957). Hybrid corn: An exploration in the economics of technological change. *Econometrica*, 25(4), 501–522.

Imam, P. A., & Temple, J. R. W. (2026). Relative development and the intelligence divide: Human capital, technology diffusion, and AI. IMF Working Paper 2026/190. [https://doi.org/10.5089/9798229057349.001](https://doi.org/10.5089/9798229057349.001)

Insilico Medicine. (2026, July 7). Insilico initiates Phase III clinical trial for Rentosertib, its AI-empowered TNIK inhibitor for idiopathic pulmonary fibrosis. [https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr](https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr)

Korinek, A., Jones, C. I., Sacher, S., Cotter, T., & McCrory, P. (2026). Economic scenarios for transformative AI. The Anthropic Institute Working Paper No. 2026-02. [https://www-cdn.anthropic.com/files/4zrzovbb/website/cf58f84d46a4a76bf5a5b039ac695fba6b80041c.pdf](https://www-cdn.anthropic.com/files/4zrzovbb/website/cf58f84d46a4a76bf5a5b039ac695fba6b80041c.pdf)

Leiden Declaration on Artificial Intelligence and Mathematics. (2026, June 2). [https://doi.org/10.5281/zenodo.20302944](https://doi.org/10.5281/zenodo.20302944)

Massenkoff, M., Lyubich, E., McCrory, P., Appel, R., & Heller, R. (2026, March 24). Anthropic Economic Index report: Learning curves. Anthropic. [https://www.anthropic.com/research/economic-index-march-2026-report](https://www.anthropic.com/research/economic-index-march-2026-report)

METR. (2026, May 8). Task-completion time horizons of frontier AI models. [https://metr.org/time-horizons/](https://metr.org/time-horizons/)

National Highway Traffic Safety Administration. (2026, September 4). NHTSA opens investigation into Tesla Cybercab self-certification following Austin deployment. [https://www.nhtsa.gov/press-releases/investigation-tesla-cybercab-self-certification](https://www.nhtsa.gov/press-releases/investigation-tesla-cybercab-self-certification)

Nature Machine Intelligence. (2026, June 23). Solutions, challenges and rising tensions in AI and mathematics. Nature Machine Intelligence, 8, 857. [https://doi.org/10.1038/s42256-026-01269-x](https://doi.org/10.1038/s42256-026-01269-x)

Nelson, R. R., & Phelps, E. S. (1966). Investment in humans, technological diffusion, and economic growth. *American Economic Review*, 56(1/2), 69–75.

Nerlove, M. (1956). Estimates of the elasticities of supply of selected agricultural commodities. *Journal of Farm Economics*, 38(2), 496–509.

Ogburn, W. F. (1922). Social change with respect to culture and original nature. New York: B. W. Huebsch.

OpenAI. (2026l, August 1). Ten advances in mathematics and theoretical computer science. [https://openai.com/index/ten-advances-in-mathematics/](https://openai.com/index/ten-advances-in-mathematics/)

OpenAI. (2026j, September 6). Research acceleration: The view inside OpenAI. [https://openai.com/index/research-acceleration-view-inside-openai/](https://openai.com/index/research-acceleration-view-inside-openai/)

OpenAI. (2026d, September 8). On the Navier-Stokes Millennium Prize Problem. [https://openai.com/index/navier-stokes-solution/](https://openai.com/index/navier-stokes-solution/)

Pachocki, J. (2026, September 6). An alien mind. OpenAI. [https://openai.com/index/an-alien-mind/](https://openai.com/index/an-alien-mind/)

Perez, C. (2002). Technological revolutions and financial capital: The dynamics of bubbles and golden ages. Cheltenham: Edward Elgar.

Ren, F., Aliper, A., Chen, J., et al. (2025). A small-molecule TNIK inhibitor targets fibrosis in preclinical and clinical models. Nature Biotechnology, 43(1), 63–75. [https://doi.org/10.1038/s41587-024-02143-0](https://doi.org/10.1038/s41587-024-02143-0)

Reuters. (2026g, September 8). Slovenia clears Tesla’s FSD driver assistance ahead of EU vote. [https://www.reuters.com/business/slovenia-clears-teslas-fsd-driver-assistance-ahead-eu-vote-2026-09-08/](https://www.reuters.com/business/slovenia-clears-teslas-fsd-driver-assistance-ahead-eu-vote-2026-09-08/)

Rogers, E. M. (1962). Diffusion of innovations. New York: Free Press.

Shin, S., Kim, S., Choi, T., & Son, J. Y. (2026). Performance concentration and leadership transformation driven by AI diffusion: An empirical analysis of the global professional Go community. Journal of Intelligence and Information Systems, 32(2), 229–251. [https://doi.org/10.13088/jiis.2026.32.2.229](https://doi.org/10.13088/jiis.2026.32.2.229)

United Nations Economic Commission for Europe. (2026, June 24). UNECE adopts first-ever global rules allowing fully autonomous vehicles. [https://unece.org/sustainable-development/press/unece-adopts-first-ever-global-rules-allowing-fully-autonomous](https://unece.org/sustainable-development/press/unece-adopts-first-ever-global-rules-allowing-fully-autonomous)

W.H.L. & Claude (Opus 5). (2026g, August 3). Gradual AGI as Contestation: A Framework for Governance. Gradual AGI Series \#7. *Champaign Magazine*. [https://champaignmagazine.com/2026/08/03/gradual-agi-as-contestation-a-framework-for-governance/](https://champaignmagazine.com/2026/08/03/gradual-agi-as-contestation-a-framework-for-governance/)

W.H.L. & Claude (Sonnet 5). (2026b, July 4). Ceiling, Floor, and Slope: A Falsifiable Dynamical Model of Synchronization for Gradual AGI. Gradual AGI Series \#4. *Champaign Magazine*. [https://champaignmagazine.com/2026/07/04/ceiling-floor-and-slope-a-falsifiable-dynamical-model-of-synchronization-for-gradual-agi/](https://champaignmagazine.com/2026/07/04/ceiling-floor-and-slope-a-falsifiable-dynamical-model-of-synchronization-for-gradual-agi/)

W.H.L. & GPT-5.5. (2026n, June 29). Gradual AGI as Synchronization for Transformative Adoption. Gradual AGI Series \#3. *Champaign Magazine*. [https://champaignmagazine.com/2026/06/29/gradual-agi-as-synchronization-for-transformative-adoption/](https://champaignmagazine.com/2026/06/29/gradual-agi-as-synchronization-for-transformative-adoption/)

W.H.L., Claude Sonnet 5, & GPT-5.5. (2026j, July 22). Gradual AGI as Optimization: A Conceptual Framework. Gradual AGI Series \#5. *Champaign Magazine*. [https://champaignmagazine.com/2026/07/22/gradual-agi-as-optimization-a-conceptual-framework/](https://champaignmagazine.com/2026/07/22/gradual-agi-as-optimization-a-conceptual-framework/)

Weinreich, M. (2026). The crisis of AI-generated mathematics. arXiv:2608.02859. [https://arxiv.org/abs/2608.02859](https://arxiv.org/abs/2608.02859)
