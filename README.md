# On Gradual AGI

[![Calculation tests](https://github.com/champaignmagazine/on-gradual-agi/actions/workflows/tests.yml/badge.svg)](https://github.com/champaignmagazine/on-gradual-agi/actions/workflows/tests.yml)

**W.H.L.**, with GPT-6.1 Sol and Claude Opus 5.5 · *Champaign Magazine* · First Edition, 2026

*On Gradual AGI* treats artificial general intelligence as a gradual, ongoing transformation rather than a single arrival. It sets out the Multi-Plateau Framework and the Unified Gradual AGI Model. The book follows how capability becomes realized change through availability, exposure and domain conditions, and how optimization, governance, participation, evidence and feedback shape that path. Every claim carries an explicit status, and the book states what would count against it.

> **First Edition, version 1.0** (October 18, 2026). Digital edition: PDF and online. The print edition is in production.

## Read

- **Online:** <https://champaignmagazine.github.io/on-gradual-agi/>, searchable, with chapter navigation
- **PDF:** [On_Gradual_AGI_v1.0.pdf](https://github.com/champaignmagazine/on-gradual-agi/releases/download/v1.0/On_Gradual_AGI_v1.0.pdf) (direct download)
- **All formats:** [latest release](https://github.com/champaignmagazine/on-gradual-agi/releases/latest), with the complete PDF, the Word master and the full-resolution Figure 12.1

## Contents

| Part | Chapters |
| --- | --- |
| Front matter | Copyright and License · Preface · Contributors and AI Collaboration · About the Author · Notation Quick Reference · Reader Guide |
| I. Orientation | 1 AGI and the Meaning of Gradual Transformation · 2 AGI-Inclusive Humanity |
| II. Architecture | 3 A Multi-Plateau Framework of the Unified Gradual AGI Model · 4 From Potential to Realization · 5 Synchronization: Ceiling, Floor, and Slope · 6 Optimization: Choosing Among Trajectories |
| III. Mediation | 7 Governance: Contesting Realization · 8 Participation: Subjects, Acts, and Consequences · 9 Participation: What Survives Empirical Contact · 10 Observation, Evidence, and Epistemic Discipline · 11 Feedback, Recursion, and Ongoing Transformation |
| IV. Integration | 12 The Unified Gradual AGI Model · Glossary · Full Notation Guide · Claims and Status Register · Revision Record · Unified References |

## Verify your download

Each release includes `SHA256SUMS.txt`, listing the SHA-256 checksum of every file. Download it into the same folder as the book files, then run:

- **macOS:** `shasum -a 256 -c SHA256SUMS.txt`
- **Linux:** `sha256sum -c SHA256SUMS.txt`
- **Windows (PowerShell):** `Get-FileHash On_Gradual_AGI_v1.0.pdf -Algorithm SHA256`, then compare the result with the line for that file in `SHA256SUMS.txt`

On macOS and Linux, each file you downloaded should report `OK`; files you didn't download are reported as missing, which is fine. GitHub also shows each file's checksum on the release page.

## Cite

GitHub's **"Cite this repository"** button (from [`CITATION.cff`](CITATION.cff)) gives APA and BibTeX. In short:

> W.H.L. (2026). *On Gradual AGI* (First Edition, Version 1.0). Champaign Magazine. https://github.com/champaignmagazine/on-gradual-agi

## Code

[`code/`](code/) reproduces the book's calculations: the Chapter 5 synchronization recurrence, regimes and threshold results; the Chapter 6 selection rules; and the Chapter 9 Frame One counts and rate-ratio interval. Each is checked against the values printed in the book. Run `python -m gradual_agi` from `code/`; no dependencies are needed. To install it as a package instead, run `pip install ./code` from the repository root. The tests run automatically on every change (badge above).

## Versions and corrections

- **1.0.x:** corrections that change no claim (typos, citations, dates, links)
- **1.x:** updated facts or a changed claim status
- **2.0:** a new edition, for any change to the architecture itself

Changes after v1.0 are listed in [`REVISIONS.md`](REVISIONS.md) and in the book's Revision Record. To report an error, please [open an issue](https://github.com/champaignmagazine/on-gradual-agi/issues).

## Repository layout

```
docs/          the book as Markdown, one page per chapter (source of the online edition)
docs/media/    figures; Figure 12.1 is also provided at full resolution
mkdocs.yml     online-edition configuration (MkDocs Material)
.github/       workflow that publishes the online edition to GitHub Pages
tools/         scripts that regenerate docs/ from the Word master
code/          Python reference implementations of the Chapter 5, 6 and 9 calculations, with tests
CITATION.cff   citation metadata
REVISIONS.md   post-publication revision record
LICENSE        Creative Commons Attribution 4.0 International
```

The Word master is the authoritative text. The Markdown here is generated from it for each release, so corrections should be reported as issues rather than made directly to `docs/`.

## License

The book's content is licensed under [CC BY 4.0](LICENSE), except where separately credited or otherwise indicated. Third-party material remains subject to its own rights and notices. Attribution: *W.H.L. On Gradual AGI. First Edition. Champaign Magazine, 2026. Licensed under CC BY 4.0.*

The code in `code/` and `tools/` is released under the MIT License ([code/LICENSE](code/LICENSE), [tools/LICENSE](tools/LICENSE)).

The AI systems credited in the book contributed under W.H.L.'s direction. No copyright is claimed on their behalf; see *Contributors and AI Collaboration*.
