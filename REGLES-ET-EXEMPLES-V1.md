# Règles et exemples — Boson de Brutus V1

**STATUT** = complément documentaire  
**FORMULE DE RÉFÉRENCE** = `FORMULE-FIGEE-2026-09-19.md`  
**EFFET SUR V1** = aucun changement  
**VALIDATION_PHYSIQUE** = NON ÉTABLIE

Ce document ajoute seulement des règles d’utilisation et des exemples de reproduction autour de la formule V1 déjà figée.

## Formule V1 de référence

[
left(
rac{300000000-299792458}{300000000}
ight)
	imes
left(
rac{1}{3	imes10^{18}}
ight)
	imes
left(
1-rac{pi}{100}
ight)
]

Valeur numérique reproduite :

[
oxed{2.2335763974987408	imes10^{-22}}
]

---

## Règles supplémentaires

### Règle 1 — V1 reste figée

Les valeurs suivantes appartiennent à la V1 et ne sont pas modifiées :

- `300000000`
- `299792458`
- `3 × 10^18`
- `pi`
- `100`

La formule V1 n’est pas corrigée après coup.

### Règle 2 — Aucun ajustement pour améliorer le résultat

Après calcul, aucun coefficient ne doit être déplacé, remplacé ou arrondi volontairement pour rapprocher le résultat d’une valeur connue.

On applique la formule telle qu’elle est, puis on observe le résultat.

### Règle 3 — Même calcul, mêmes étapes

Une reproduction de V1 doit conserver les trois termes :

[
T_1=
rac{300000000-299792458}{300000000}
]

[
T_2=
rac{1}{3	imes10^{18}}
]

[
T_3=
1-rac{pi}{100}
]

puis :

[
R=T_1	imes T_2	imes T_3
]

### Règle 4 — Résultat numérique et interprétation physique restent séparés

Le calcul numérique est reproductible.

L’unité `g` reste une unité proposée dans V1 et non dérivée par analyse dimensionnelle.

L’interprétation comme masse candidate du boson de Higgs reste une hypothèse de recherche.

La validation physique demeure **NON ÉTABLIE**.

### Règle 5 — Toute variante devient une nouvelle version

Si un coefficient, une règle, une constante, une unité ou une structure de calcul change, ce n’est plus la V1.

La variante doit recevoir un nouveau numéro ou un nouveau nom et ne doit jamais remplacer silencieusement la formule figée.

### Règle 6 — Les échecs sont conservés

Un test qui ne fonctionne pas ou une comparaison qui ne correspond pas ne doit pas être supprimé uniquement parce qu’il est défavorable.

Les résultats positifs et négatifs doivent pouvoir être comparés.

---

## Exemples de reproduction

### Exemple 1 — Premier terme

[
T_1=
rac{300000000-299792458}{300000000}
]

[
T_1approx0.0006918066666666666
]

### Exemple 2 — Deuxième terme

[
T_2=
rac{1}{3	imes10^{18}}
]

[
T_2approx3.3333333333333334	imes10^{-19}
]

### Exemple 3 — Troisième terme

[
T_3=
1-rac{pi}{100}
]

[
T_3approx0.968584073464102
]

### Exemple 4 — Résultat complet

[
R=
0.0006918066666666666
	imes
3.3333333333333334	imes10^{-19}
	imes
0.968584073464102
]

[
oxed{R=2.2335763974987408	imes10^{-22}}
]

---

## Exemple minimal en Python

```python
import math

c_hypothetique = 300000000
c_reel = 299792458
facteur_espace = 3 * 10**18

terme_1 = (c_hypothetique - c_reel) / c_hypothetique
terme_2 = 1 / facteur_espace
terme_3 = 1 - (math.pi / 100)

resultat = terme_1 * terme_2 * terme_3

print(resultat)
```

Résultat attendu :

```text
2.2335763974987408e-22
```

---

## Règle de lecture

**On ne cherche pas à faire fonctionner la formule. On applique la formule telle qu’elle est, puis on regarde si elle fonctionne.**

Ce fichier complète la V1 sans modifier `FORMULE-FIGEE-2026-09-19.md`.
