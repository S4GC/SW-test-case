
import numpy as np
import pyPLUTO as pp

D = pp.Load(path="./", nout=1)

# Primitive variables
rho = np.asarray(D.rho)
P = np.asarray(D.prs)

vx1 = np.asarray(D.vx1)
vx2 = np.asarray(D.vx2)
vx3 = np.asarray(D.vx3)

# Magnetic field: note uppercase B
bx1 = np.asarray(D.Bx1)
bx2 = np.asarray(D.Bx2)
bx3 = np.asarray(D.Bx3)

tracer = np.asarray(D.tr1)

# Energy densities
ekin = 0.5 * rho * (vx1**2 + vx2**2 + vx3**2)
emag = 0.5 * (bx1**2 + bx2**2 + bx3**2)

bmag = np.sqrt(bx1**2 + bx2**2 + bx3**2)

# Plasma beta
beta = P / np.maximum(emag, 1.e-30)

# Coordinates
X, Y = np.meshgrid(D.x1, D.x2)

# Pressure floor mask
floor = P <= 1.01e-12

regions = {
    "LOWER LEFT": (X < 0.3) & (Y < -0.6),
    "UPPER RIGHT": (X > 1.5) & (Y > 0.5),
    "WHOLE DOMAIN": np.ones_like(P, dtype=bool)
}

fields = {
    "Density": rho,
    "Pressure": P,
    "Kinetic energy": ekin,
    "Magnetic energy": emag,
    "Magnetic field": bmag,
    "Plasma beta": beta,
    "Tracer": tracer
}

for name, region in regions.items():

    print("\n" + "=" * 45)
    print(name)
    print("=" * 45)

    for field_name, field in fields.items():

        values = field[region]
        values = values[np.isfinite(values)]

        if values.size:
            print(
                f"{field_name:18s} "
                f"min={values.min():.6e} "
                f"max={values.max():.6e} "
                f"mean={values.mean():.6e}"
            )

    # Statistics specifically for pressure-floor cells
    local_floor = region & floor

    print(
        "Pressure-floor cells:",
        np.count_nonzero(local_floor)
    )

    if np.any(local_floor):
        print("Mean rho in floor cells:", np.mean(rho[local_floor]))
        print("Mean B in floor cells:", np.mean(bmag[local_floor]))
        print("Mean kinetic energy in floor cells:", np.mean(ekin[local_floor]))
        print("Mean magnetic energy in floor cells:", np.mean(emag[local_floor]))
