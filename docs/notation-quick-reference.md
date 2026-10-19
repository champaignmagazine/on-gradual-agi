# Notation Quick Reference

This reference introduces the notation most useful for reading across chapters. The Full Notation Guide in Part IV explains additional symbols, local assumptions, and distinctions between similar letters. Symbols are defined in context; the equations here are representations, not claims that the whole framework is one numerical model.

## Realization — Chapter 4

$$R_{g}(t) = \mu_{t}\left( P(t),Av(t),{Ex}_{g}(t),Z_{d}(t) \right).$$

| Symbol          | Read as                                   |
|-----------------|-------------------------------------------|
| $R_{g}(t)$    | Realized state for group $g$ at time $t$. |
| $P(t)$        | Potential or capability.                  |
| $Av(t)$       | Availability.                             |
| ${Ex}_{g}(t)$ | Group-specific Exposure.                  |
| $Z_{d}(t)$    | Domain-specific realization conditions.   |
| $\mu_{t}$     | The structured realization relation.      |

The mapping has four arguments. It is not a sum or a fixed sequence. Optimization, governance, Participation, evidence, and feedback affect the architecture without becoming fifth arguments. Realization does not establish benefit.

Exposure comprises Reach, Susceptibility, and Recourse:

$${Ex}_{g}(t) = \left( {Rh}_{g}(t),{Su}_{g}(t),{Rc}_{g}(t) \right).$$

These components remain distinct. Chapter 7 names and symbolizes Susceptibility without measuring or calibrating it; a nominal appeal channel does not establish effective Recourse.

## Synchronization — Chapter 5

| Symbol                         | Read as                                                                                      |
|--------------------------------|----------------------------------------------------------------------------------------------|
| $C_{t},\ F_{t}$              | CFS Ceiling and Floor within a specified domain.                                             |
| $G_{t} = C_{t} - F_{t}$      | Their gap.                                                                                   |
| $S_{t} = \Delta F_{t}/G_{t}$ | Observed Slope: the fraction of the current gap closed in one period; undefined at zero gap. |
| $\alpha,\ \beta$             | Ceiling growth and gap-closure parameter in the baseline recurrence.                         |

$$G_{t + 1} = \alpha + (1 - \beta)G_{t}.$$

In this baseline, Ceiling grows by $\alpha$ per period and Floor moves by $\beta G_{t}$. Under this one-period baseline, $S_{t} = \beta$ algebraically; that equality does not independently validate structural coupling. CFS is a bounded submodel: its Ceiling is not general Potential, and its Floor is not general Realization. The Full Notation Guide explains the regime boundaries, delay, and extensions.

## Optimization — Chapter 6

| Symbol                                              | Read as                                                                      |
|-----------------------------------------------------|------------------------------------------------------------------------------|
| $\Gamma\mathcal{\in T}$                           | A candidate trajectory within the candidate trajectory space.                |
| $J_{i}\mathcal{:T \rightarrow}\mathbb{R}^{k}$     | Evaluator $i$’s multidimensional objective mapping.                          |
| $\sigma_{i}:\mathbb{R}^{k}\mathbb{\rightarrow R}$ | A local scalarization, where justified.                                      |
| $Z_{j}(t) \leq \Psi_{j}(t)$                       | A local Absorption Capacity constraint; $\Psi_{j}(t)$ is the capacity bound. |

A trajectory includes intermediate states and changes to future options. No universal scalar objective is assumed. The local $Z_{j}(t)$ constraint is distinct from Chapter 4’s domain conditions $Z_{d}(t)$. Evaluation does not itself confer authority to decide.

## Participation — Chapters 8–9

| Abbreviation or symbol                            | Read as                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| RO → FP → AD                                      | Realization Orientation, Foreclosure Position, Actor Dependence: the reading order of the Relational Grammar. |
| $\Pi_{r}\left\lbrack t_{0},t_{1} \right\rbrack$ | A Participatory Configuration for realization object $r$ over an interval, in Chapter 9.                      |
| $C_{r},\ C_{rj}$                                | Participatory Consequence; observed consequence class $j$.                                                    |
| $\mathcal{l}$                                   | Evidentiary linkage grade.                                                                                    |

The Grammar’s reading order is not a causal or temporal sequence. Chapter 9’s partial pathway is

$$\Pi_{r} \rightarrow C_{r} \rightarrow X\prime_{r} \rightarrow R\prime_{g},$$

where $X\prime_{r}$ is one of the mapping’s existing realization conditions, as changed through a consequence, and $R\prime_{g}$ is the subsequent changed realized state. Every arrow may fail: $\Pi_{r} \nRightarrow C_{r}$ and $C_{r} \nRightarrow \Delta R_{g}$. Participatory Consequence $C_{r}$ is distinct from CFS Ceiling $C_{t}$.

## Evidence and return paths — Chapters 10–11

| Symbol                             | Read as                                           |
|------------------------------------|---------------------------------------------------|
| ${St}_{t},\ {Ob}_{t},\ {Rp}_{t}$ | Underlying State, Observation, Representation.    |
| $\Omega_{t},\ \rho_{t}$          | Observation process and representation procedure. |

$${Ob}_{t} = \Omega_{t}\left( {St}_{t} \right),\quad\quad{Rp}_{t} = \rho_{t}\left( {Ob}_{t} \right).$$

The five-term separation is Underlying State ≠ Observation ≠ Representation ≠ Inference ≠ Claim Status. For example, ${St}_{t} \neq {Ob}_{t}$: an underlying state is not identical to its observation. The upright ${St}_{t}$ is not Slope $S_{t}$ or the standing institution ${St}_{g}(t)$ within Recourse (Chapter 7; see the Full Notation Guide). Representation ${Rp}_{t}$ is not realized state $R_{g}(t)$. Chapter 11’s return-path representation reads: realization → consequence or observation → response → changed conditions → subsequent realization. Evidence must establish that an earlier outcome altered a later realization condition; a recorded sequence alone establishes neither feedback nor recursion.

**Reading relations.** $\neq$ marks non-identity. $\nRightarrow$ means “does not entail”; it does not mean that a pathway is impossible. The displayed arrows mark a mapping type in $J_{i}$ and $\sigma_{i}$, a reading order in RO → FP → AD, a partial transition in Chapter 9’s pathway, or Chapter 11’s proposed return path. These roles differ; an arrow does not automatically denote an identified causal effect.

**Indices.** $t$ marks time or an observation period; $g$ a group; $d$ a domain. Other indices are local: $i$ indexes an evaluator or actor in Optimization, while $j$ indexes an actor or domain in Chapter 6’s Absorption Capacity constraint and a consequence class in Chapter 9. Matching letters in different expressions do not establish matching objects.
