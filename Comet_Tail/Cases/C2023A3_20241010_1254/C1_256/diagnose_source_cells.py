
import numpy as np
import pyPLUTO as pp

D = pp.Load(path="./", nout=1)

# Physical parameters in CGS
Q = 1.0e29
Vn = 7.0e4
nu = 3.06e-6
mp = 1.67262192369e-24
mi = 18.0 * mp

L0 = 1.0e11
V0 = 4.0e7
T0 = 2.5e3
rho0 = 3.09411097591e-23
Rsoft = 1.2e9

Li = Vn / nu

# Coordinates
X, Y = np.meshgrid(D.x1, D.x2)

dx = X * L0
dy = Y * L0

r = np.sqrt(dx**2 + dy**2)
reff = np.sqrt(r**2 + Rsoft**2)

# Haser neutral density
nn = Q / (4.0*np.pi*Vn*reff**2)
nn *= np.exp(-r/Li)

# Mass source in normalized units
srho_cgs = mi * nu * nn
S = srho_cgs * T0 / rho0

# Last saved state
rho = np.asarray(D.rho)
P = np.asarray(D.prs)
C = np.asarray(D.tr1)

floor = P <= 1.01e-12

regions = {
    "LOWER LEFT": floor & (X < 0.3) & (Y < -0.6),
    "UPPER RIGHT": floor & (X > 1.5) & (Y > 0.5),
    "ALL FLOOR CELLS": floor,
    "WHOLE DOMAIN": np.ones_like(P, dtype=bool)
}

# Approximate output timestep from dbl.out
dt = 2.225228e-3

for name, mask in regions.items():

    values = S[mask]
    relative = (S / np.maximum(rho, 1.e-30))[mask]

    print("\n" + "="*45)
    print(name)
    print("="*45)

    if values.size == 0:
        print("No cells")
        continue

    print("Number of cells:", values.size)
    print("Source min:", np.min(values))
    print("Source max:", np.max(values))
    print("Source mean:", np.mean(values))

    print("Mean S/rho:", np.mean(relative))
    print("Maximum S/rho:", np.max(relative))

    print("Mean estimated dt*S/rho:", dt*np.mean(relative))
    print("Maximum estimated dt*S/rho:", dt*np.max(relative))

    print("Mean tracer:", np.mean(C[mask]))

print("\nMaximum source in domain:", np.max(S))
print("Maximum source at nucleus:", S[np.unravel_index(np.argmin(r), r.shape)])
