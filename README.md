# Boson de Brutus

> **Current development line: V2 high-precision candidate.** The original V1 remains frozen and unchanged.

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

# V2 — High-Precision Candidate Relation

V2 does **not** replace Frozen V1. It is a separate derivation built from the later high-precision 240.1/femtosecond residual chain.

The exact rational chain is:

[
f_{m abs}
=
rac{240.1}{1-240.1	imes10^{-15}}
=
rac{2401000000000000000}{9999999999997599}
]

[
NEO_{m exact}
=
2401 f_{m abs}
=
rac{5764801000000000000000}{9999999999997599}
]

and the internal V2 candidate is

[
oxed{
B_{m V2}
=
NEO_{m exact}-10^{-6}
=
rac{5764800999990000000000002401}
{9999999999997599000000}
}
]

with decimal expansion beginning

[
576480.09999913841287201003323293056960897922662976311591231380612413ldots
]

The structural (4/7) branch is preserved exactly rather than truncated:

[
rac47,NEO_{m exact}
=
rac{3294172000000000000000}{9999999999997599}
]

and

[
rac47,B_{m V2}
=
rac{5764800999990000000000002401}
{17499999999995798250000}.
]

These (4/7) values are arithmetic transforms only. No physical equivalence is claimed from them.

Files:
- `V2/BOSON-BRUTUS-V2-HAUTE-PRECISION.md`
- `calculs/reproduce_v2.py`
- `test_reproduce_v2.py`

V2 status remains:

**CANDIDAT — VALIDATION PHYSIQUE NON ÉTABLIE**
