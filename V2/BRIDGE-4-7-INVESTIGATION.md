# Investigation — raccord historique 4/7 → petit Boson

Date: 2026-09-25  
Status: OPEN / evidence ledger

## Goal

Recover the historical, explicit mathematical map from the NEO/Genesis 4/7 branch to the small Brutus/Boson output without inventing a relation after the fact.

## Evidence recovered

### NEO-10 / Genesis kernel

From the 2026-09-09 Scalpel report:

[
K_1=x=rac47=0.571428571428ldots
]

[
K_2=y=rac{343}{390}=0.879487179487ldots
]

[
K_3=z=rac3{13}=0.230769230769ldots
]

[
K_4=C=x+y+z=rac{4591}{2730}=1.681684981684ldots
]

[
K_5=G=1,203,930,quad
K_6=D=2730,quad
K_7=Q=441=21^2.
]

Also:

[
G	imes C=2,024,631.
]

The 2026-09-14 conversation also contained a candidate chain

[
0.23	o0.46	o0.92	o1.84.
]

This was discussed as a NEO-family sequence, but no archived formula currently connects it to the frozen Brutus mass candidate.

### Frozen Brutus V1 lineage

The documented small-output chain is

[
B=rac{300000000-299792458}{300000000}
=rac{207542}{300000000}
=0.000691806666ldots
]

then

[
M_{m prepi}
=
rac{B}{3	imes10^{18}}
=
2.30602222222222222222ldots	imes10^{-22},
]

then

[
M_{m V1}
=
M_{m prepi}
left(1-rac{pi}{100}ight)
]

which gives

[
2.23357639749874079241144289632748949026755ldots	imes10^{-22}.
]

## Numerical coincidence worth recording, not promoting

Rescaling the pre-(pi) value by (10^{21}) gives

[
0.23060222222222222222ldots
]

which is close to the NEO-10 value

[
K_3=rac3{13}=0.23076923076923076923ldots
]

but they are not equal.

Exact difference:

[
rac3{13}-rac{103771}{450000}
=
rac{977}{5850000}
approx1.67008547008547	imes10^{-4}.
]

Relative difference versus (3/13):

[
approx7.237037037	imes10^{-4}
=
0.07237037%.
]

This is recorded as a numerical proximity only.

## Falsification checks performed

### Hypothesis A — replace the pre-(pi) coefficient by exactly 3/13

This would be an undocumented substitution.

Under the historical provisional gram convention it would produce approximately

[
125.3851887768628 {m GeV}/c^2,
]

which is farther from the previously used Higgs comparison values than Frozen V1.

**Status: REJECTED as a V2 derivation.**

### Hypothesis B — replace the pre-(pi) coefficient by 0.23 exactly

This would produce approximately

[
124.9672381476066 {m GeV}/c^2.
]

Again this is not historically documented and does not improve the comparison.

**Status: REJECTED as a V2 derivation.**

### Hypothesis C — directly use 4/7 as the pre-(pi) coefficient

This gives a completely different scale, about

[
310.4776103046 {m GeV}/c^2
]

under the same provisional mass convention.

**Status: REJECTED.**

## Current conclusion

No archived source currently establishes

[
rac47
longrightarrow
	ext{Frozen Brutus small-output formula}
]

as an explicit derivation.

The following are therefore kept separate:

1. **NEO-10 / Genesis structural constants**;
2. **Frozen Brutus V1 mass candidate**;
3. **240.1 / 2401 / NEO cadence intermediate**.

A final Boson V2 must not be locked until an explicit historical map is recovered or a genuinely new prospective formula is preregistered before comparison.

## Integrity rule

[
oxed{	ext{NUMERICAL PROXIMITY}
eq	ext{DERIVATION}}
]
