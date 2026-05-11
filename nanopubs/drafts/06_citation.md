# 06 — CiTO Citation

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Description:** *"Declare citations between papers or other works, using Citation Typing Ontology"*

## Field-by-field draft

### Identifier for the citing creative work (text input, required)

URI of the Outcome published in step 05. Pull from `nanopubs/PUBLISHED.md`.

```
<replace-with-published-Outcome-URI-from-step-05>
```

### List citations (repeatable group, required ≥1)

#### Citation 1 — back to the original paper (Soroye 2020)

##### Citation Type (dropdown)

- [x] **`confirms`**

(Outcome verdict is Validated, which maps to CiTO `confirms`. The substrate extension at HEALPix nside=128 confirms the same TEI mechanism Soroye et al. proposed.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.1126/science.aax8591
```

#### Citation 2 — extends the canonical nside=64 sibling chain

##### Citation Type (dropdown)

- [x] **`extends`**

(This Study is a methodological substrate extension of the canonical Iberian *Bombus* replication, refitting the GLMM at a finer resolution. Both substrates' Outcomes report consistent substrate-robustness.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.5281/zenodo.20113777
```

(Concept DOI of `weatherxbiodiversity-projection`. Or, once published, paste the canonical nside=64 sibling Outcome URI directly.)

#### Citation 3 — extends the methodological substrate-sensitivity sibling chain

##### Citation Type (dropdown)

- [x] **`extends`**

(The substrate-sensitivity sibling chain documents the projection-time grid-coupling diagnostic and the recommended reporting protocol that this Outcome's per-species ranking is filtered against.)

##### DOI or other URL of the cited work (text input)

```
https://doi.org/10.5281/zenodo.20113786
```

(Concept DOI of `weatherxbiodiversity-substrate-sensitivity`.)

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 06.

This completes the six-step FORRT chain. Optional next layers:

- **Research Software** (`drafts/07_research_software.md`) — if the repo *produces* a reusable software artefact.
- **Research Synthesis** (`drafts/08_synthesis.md`) — if this chain is one of several testing facets of a shared property.
