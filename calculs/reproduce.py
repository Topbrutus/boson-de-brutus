import math

C_ROUND = 300_000_000
C_EXACT = 299_792_458
SCALE = 3e18

value = (
    ((C_ROUND - C_EXACT) / C_ROUND)
    * (1 / SCALE)
    * (1 - math.pi / 100)
)

print(f"Brutus V1 = {value:.16e}")
assert value == 2.2335763974987408e-22

# Interprétation conditionnelle seulement :
# si value est exprimée en grammes.
E_CHARGE = 1.602176634e-19  # C, exact in SI
C = 299_792_458             # m/s, exact in SI
kg_per_GeV_c2 = (1e9 * E_CHARGE) / (C * C)
candidate_GeV = (value * 1e-3) / kg_per_GeV_c2

print(f"If unit=g: {candidate_GeV:.12f} GeV/c^2")
