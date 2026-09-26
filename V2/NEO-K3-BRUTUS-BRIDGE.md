# NEO K3 ↔ Brutus pre-π bridge — exact post-hoc identity

Date: 2026-09-25  
Status: **EXACT ARITHMETIC / POST-HOC / NOT A HISTORICAL DERIVATION**

## 1. Recovered NEO doubling chain

The older NEO discussion included the sequence remembered approximately as

[
0.23	o0.46	o0.92	o1.84.
]

The exact NEO-10 value

[
K_3=rac3{13}
]

generates that sequence by repeated doubling:

[
oxed{
rac3{13}
	o
rac6{13}
	o
rac{12}{13}
	o
rac{24}{13}
}
]

with decimal expansions

[
0.230769230769ldots
	o
0.461538461538ldots
	o
0.923076923076ldots
	o
1.846153846153ldots
]

This recovers the mathematical structure of the old “0.23 / double / double” discussion.

## 2. Brutus pre-π coefficient at the same decimal scale

Frozen V1 begins from

[
Delta c
=
300000000-299792458
=
207542.
]

Before the factor (1-pi/100),

[
M_{m prepi}
=
rac{207542}{300000000}
rac1{3	imes10^{18}}.
]

Multiplying by (10^{21}) gives the dimensionless coefficient

[
P_B
=
10^{21}M_{m prepi}
=
rac{207542}{900000}
=
rac{103771}{450000}
]

or

[
oxed{
P_B=0.230602222222222222ldots
}
]

Thus

[
oxed{
M_{m prepi}
=
0.230602222222ldots	imes10^{-21}
=
2.306022222222ldots	imes10^{-22}.
}
]

## 3. Exact Genesis rewrite of the Brutus coefficient

The previously recovered exact identity

[
207542=(7	imes13-9)(7^4+10	imes13)
]

gives

[
oxed{
P_B
=
rac{(7	imes13-9)(7^4+10	imes13)}
{9	imes10^5}.
}
]

This equality is exact.

## 4. Exact difference from NEO K3

The two nearby values are

[
K_3=rac3{13}=0.230769230769ldots
]

and

[
P_B=rac{103771}{450000}=0.230602222222ldots
]

Their exact difference is

[
oxed{
K_3-P_B
=
rac{977}{5850000}
}
]

or

[
0.000167008547008547ldots
]

The relative difference with respect to (K_3) is

[
oxed{
rac{K_3-P_B}{K_3}
=
rac{977}{1350000}
=
0.000723703703703ldots
}
]

which is

[
oxed{
0.0723703703703ldots%
}.
]

The residual numerator itself admits the exact rewrite

[
oxed{
977
=
3	imes7^3-(13-9)	imes13
}
]

and therefore

[
K_3-P_B
=
rac{
(9-7),[3	imes7^3-(13-9)	imes13]
}{
13	imes9	imes10^5
}.
]

Again, this was found after both values were known.

## 5. Interpretation

What is now established:

1. the old 0.23→0.46→0.92→1.84 sequence is exactly the repeated-doubling chain of (3/13);
2. the Brutus pre-(pi) value, when written at the same (10^{-21}) scale, is exactly (0.2306022222ldots);
3. the difference between these quantities is exactly computable and small;
4. the Brutus coefficient can itself be written using Genesis integers (7,9,10,13,2401).

What is **not** established:

- that (3/13) generated the Brutus formula historically;
- that the small residual has physical significance;
- that the numerical proximity is evidence of a particle model;
- that (4/7) is part of Frozen V1.

## 6. Scientific rule

This relation is useful as a candidate bridge for a future **prospective** test, but it cannot retroactively count as a prediction.

[
oxed{
	ext{EXACT POST-HOC IDENTITY}

eq
	ext{PRIOR PREDICTION}
}
]
