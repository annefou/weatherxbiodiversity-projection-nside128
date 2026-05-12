# Published FORRT nanopub chain — this repository

This is the URI registry for the **HEALPix nside=128 substrate extension chain** — a methodological replication of Soroye et al. 2020 ([10.1126/science.aax8591](https://doi.org/10.1126/science.aax8591)) at the native pixelisation of DestinE Climate DT IFS-NEMO standard. The chain confirms the TEI mechanism is substrate-robust on Iberian *Bombus* at this finer grid: **Outcome = Validated**, CiTO citation `confirms` Soroye 2020 + `extends` the canonical nside=64 sibling.

For the **full three-chain constellation view** — including the canonical nside=64 sibling and the methodological substrate-sensitivity diagnostic, with a graph of how all 18 nanopubs interlink — see [the constellation chapter in `weatherxbiodiversity-substrate-sensitivity`](https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/nanopubs/published).

## Chain graph

```{mermaid}
graph TB
    Soroye(["Soroye et al. 2020<br/>10.1126/science.aax8591"]):::paper
    Quote(["01 — Quote<br/>RAErLL…<br/>shared with sibling"]):::shared
    AIDA(["02 — AIDA: TEI_delta positive<br/>RAgb6p…<br/>shared with sibling"]):::shared
    Claim(["03 — Claim: statistical significance<br/>RAh7NY…<br/>shared with sibling"]):::shared
    Study(["04 — Study: nside=128 refit<br/>RAsGeFqq…"]):::nside128
    Outcome(["05 — Outcome: Validated<br/>RAa4QR41…"]):::nside128
    CiTO(["06 — CiTO: confirms + extends<br/>RAhw9m0B…"]):::nside128
    RS(["07 — Research Software<br/>RA-GY81…"]):::nside128

    Soroye --> Quote --> AIDA --> Claim
    Claim --> Study --> Outcome --> CiTO
    Claim -.-> RS

    classDef paper fill:#fff3b0,stroke:#7a5901,stroke-width:2px,color:#000
    classDef shared fill:#e8e8e8,stroke:#444,color:#000
    classDef nside128 fill:#d6f5d6,stroke:#1a9850,color:#000
```

The Quote, AIDA, and Claim nanopubs are **shared with the canonical nside=64 sibling chain** — same upstream paper, same atomic finding (the TEI_delta coefficient is positive and credibly above zero on Iberian *Bombus*); the two chains diverge at step 04 (Study), where each provides substrate-specific evidence for the same claim.

## URI registry

### Chain (six required steps)

| Step | Template | URI |
|---|---|---|
| 01 | Quote-with-comment — *shared with nside=64 sibling* | <https://w3id.org/sciencelive/np/RAErLL_QSe3e0pKBxHkUHH5v49F66fFVuS2OmYMJz02OY> |
| 02 | AIDA Sentence — *shared with nside=64 sibling* | <https://w3id.org/sciencelive/np/RAgb6pxwyANh-jpPdiY3H5k-fGWGgCmN72UrV_zAJcSMI> |
| 03 | FORRT Claim — *shared with nside=64 sibling* | <https://w3id.org/sciencelive/np/RAh7NYjme8dajwxnoBfbOjsd1L76LQfN-pMEajIwiRDJE> |
| 04 | Replication Study — HEALPix nside=128 refit | <https://w3id.org/sciencelive/np/RAsGeFqqv4iQqrFNyjQwpSqKQYYk8JqGEjpCCJf1FtAM4> |
| 05 | Replication Outcome — **Validated** | <https://w3id.org/sciencelive/np/RAa4QR41Hot9zxujcrCyTo82Ij7oaw_6z8zk8NxDqoJFM> |
| 06 | CiTO Citation — `confirms` + `extends` | <https://w3id.org/sciencelive/np/RAhw9m0BEj0-9hXrTtJ2NHG5rMr-ZBf_mdBQTQRk6u3n4> |

### Optional layer

| Step | Template | URI |
|---|---|---|
| 07 | Research Software | <https://w3id.org/sciencelive/np/RA-GY814xxcpEsUWozEJKHGG39bDV8gkbor7OhX8QpVPE> |

(A Research Synthesis nanopub is not published from this chain — see the methodological sibling `weatherxbiodiversity-substrate-sensitivity` for the cross-chain synthesis.)

## Sibling chains

- **`weatherxbiodiversity-projection`** — canonical Iberian *Bombus* replication at CEA + HEALPix nside=64. [Zenodo](https://doi.org/10.5281/zenodo.20113777) · [Jupyter Book](https://annefou.github.io/weatherxbiodiversity-projection/)
- **`weatherxbiodiversity-substrate-sensitivity`** — methodological diagnostic + cross-chain Research Synthesis. [Zenodo](https://doi.org/10.5281/zenodo.20113786) · [Jupyter Book](https://annefou.github.io/weatherxbiodiversity-substrate-sensitivity/)

## How to view a nanopub

Open any URI directly in your browser. The Science Live viewer renders the four named graphs (Head, Assertion, Provenance, PublicationInfo). If a direct link doesn't resolve, wrap the URI:

```
https://platform.sciencelive4all.org/np/?uri=<full-URI>
```

Nanopubs are immutable once published. To correct a published nanopub, publish a retraction or supersession (see `docs/programmatic-nanopubs.md`).
