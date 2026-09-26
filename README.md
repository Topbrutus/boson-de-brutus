# Boson de Brutus

> **Correction status (v2.0.1):** Frozen V1 remains unchanged. The 576480... chain is an intermediate NEO/cadence calculation, not the final Boson mass candidate. A final V2 mass formula is not locked until the documented 4/7 branch is reconnected explicitly.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22927791.svg)](https://doi.org/10.5281/zenodo.22927791)

Dépôt de recherche consacré à la **Constante / formule Brutus**, figée le **2026-09-19**.

## Créateur / auteur

**Gabriel St-Pierre (Topbrutus)** — créateur de la formule candidate Brutus V1 et auteur du dossier de recherche.

## Archive officielle

- **Zenodo record :** https://zenodo.org/records/22927791
- **DOI version v0.1.0 :** https://doi.org/10.5281/zenodo.22927791
- **Concept DOI :** https://doi.org/10.5281/zenodo.22927790

## Statut

**CANDIDAT — VALIDATION PHYSIQUE NON ÉTABLIE**

Ce dépôt ne revendique pas la découverte d'une nouvelle loi physique ni une détermination théorique du boson de Higgs. Il conserve une relation numérique figée, sa reproductibilité, ses comparaisons externes, ses limites et les tests capables de la réfuter.

## Formule figée

```text
((300000000 - 299792458) / 300000000)
× (1 / (3×10^18))
× (1 - π/100)
```

Résultat numérique :

```text
2.2335763974987408 × 10^-22
```

Unité proposée par **Gabriel St-Pierre (Topbrutus)** : **g**.

> L'unité « g » est une hypothèse d'interprétation. Elle n'est pas dérivée dimensionnellement de la formule telle qu'elle est écrite.

Si l'on accepte provisoirement cette unité, la masse équivalente vaut environ **125.294447051 GeV/c²**.

## Règle de gel

La relation ci-dessus est considérée comme **FROZEN V1**. Aucun coefficient, constante ou facteur ne doit être modifié après coup pour améliorer l'accord avec une mesure.

## Philosophie

1. Figer avant de comparer.
2. Reproduire par code.
3. Séparer calcul, unité proposée et interprétation physique.
4. Comparer à plusieurs références, pas seulement à celle qui paraît la plus favorable.
5. Définir des tests hors échantillon.
6. Publier aussi les échecs.

## Structure

- `FORMULE-FIGEE-2026-09-19.md` — spécification canonique.
- `calculs/reproduce.py` — reproduction numérique.
- `calculs/RESULTATS.md` — conversions et comparaisons.
- `docs/HISTOIRE-ORIGINE.md` — chronologie de découverte.
- `docs/PROTOCOLE-FALSIFICATION.md` — règles de test.
- `docs/STATUT-ET-LIMITES.md` — ce qui est établi et ce qui ne l'est pas.
- `references/REFERENCES.md` — sources externes.

## Principe

**Une proximité numérique est une observation. Elle n'est pas, à elle seule, une explication physique.**

---

# V2 reconstruction status

The previously published v2.0.0 release incorrectly promoted the high-precision NEO/cadence value

[
576480.0999991384128720100332329305696089792266297631159ldots
]

as if it were the final Boson V2 mass candidate.

That interpretation is withdrawn.

The value above remains a reproducible **intermediate mathematical quantity** from the 240.1 Hz / 1 fs chain. It is not assigned a mass unit here.

The small frozen Brutus relation, evaluated at high precision without changing its formula, is

[
oxed{
2.233576397498740792411442896327489490267550118723876865300357561047027907489616401334082266253205148830761002425428929ldots	imes10^{-22}
}
]

If, and only if, the same historical project convention of grams is provisionally applied, the equivalent mass is

[
oxed{
125.2944470513553891726729240992025119613201616521227042175770269524274426944ldots mathrm{GeV}/c^2
}
]

using exact SI values of (e) and (c).

The structural (4/7) branch is preserved separately. No final V2 mass formula is declared until the exact documented map

[
	ext{4/7 branch} ightarrow 	ext{small Boson output}
]

is recovered and tested.

Files:
- `V2/CORRECTION-v2.0.1.md`
- `calculs/reproduce_mass_high_precision.py`
- `calculs/reproduce_v2.py` — retained as an intermediate-chain reproducer only
- `test_reproduce_v2.py`

**CALCULATION ≠ PHYSICAL VALIDATION.**
