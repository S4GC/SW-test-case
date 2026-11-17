
import numpy as np
import pyPLUTO as pp

for n in [0, 1]:

    print("\n" + "=" * 45)
    print(f" C1 - OUTPUT {n}")
    print("=" * 45)

    D = pp.Load(path="./", nout=n)

    variables = [
        "rho",
        "vx1",
        "vx2",
        "vx3",
        "bx1",
        "bx2",
        "bx3",
        "prs",
        "psi_glm",
        "tr1"
    ]

    for name in variables:

        if not hasattr(D, name):
            continue

        a = np.asarray(getattr(D, name))
        finite = a[np.isfinite(a)]

        if finite.size == 0:
            print(f"{name}: no hay valores finitos")
            continue

        print(
            f"{name:10s} "
            f"min={finite.min():.8e} "
            f"max={finite.max():.8e} "
            f"mean={finite.mean():.8e} "
            f"NaN={np.isnan(a).sum()}"
        )

        if name == "prs":
            negative = np.count_nonzero(
                np.isfinite(a) & (a <= 0)
            )
            print(f"  Celdas con presión <= 0: {negative}")




# --------------------------------------------------
# Localización de celdas con presión en el piso
# --------------------------------------------------

P = np.asarray(D.prs)

floor = 1.01e-12
mask = np.isfinite(P) & (P <= floor)

print("\nCELDAS CON PRESION EN EL PISO")
print("Cantidad:", np.count_nonzero(mask))
print("Porcentaje:", 100*np.mean(mask), "%")

if np.any(mask):

    indices = np.argwhere(mask)

    for idx in indices[:15]:

        j, i = idx[-2], idx[-1]

        print(
            f"j={j}, i={i}, "
            f"rho={D.rho[j,i]:.6e}, "
            f"prs={P[j,i]:.6e}, "
            f"vx1={D.vx1[j,i]:.6e}, "
            f"vx2={D.vx2[j,i]:.6e}, "
            f"tr1={D.tr1[j,i]:.6e}"
        )



P = np.asarray(D.prs)

idx = np.unravel_index(np.nanargmin(P), P.shape)
j, i = idx[-2], idx[-1]

print("\nCELDA DE PRESION MINIMA")
print("Indice:", idx)
print("x1:", D.x1[i])
print("x2:", D.x2[j])
print("rho:", D.rho[j,i])
print("vx1:", D.vx1[j,i])
print("vx2:", D.vx2[j,i])
print("tr1:", D.tr1[j,i])




# Distribución espacial de las celdas con presión mínima

P = np.asarray(D.prs)
mask = np.isfinite(P) & (P <= 1.01e-12)

j_idx, i_idx = np.where(mask)

print("\nDISTRIBUCION ESPACIAL DEL PISO DE PRESION")
print("Celdas afectadas:", len(i_idx))

if len(i_idx) > 0:

    print("i mínimo y máximo:", i_idx.min(), i_idx.max())
    print("j mínimo y máximo:", j_idx.min(), j_idx.max())

    print("\nCantidad de celdas afectadas por fila:")

    for j in range(P.shape[0]):
        count = np.count_nonzero(mask[j, :])

        if count > 0:
            print(
                f"j={j:3d}, "
                f"y={D.x2[j]: .6f}, "
                f"celdas={count:3d}"
            )

    print("\nCantidad de celdas afectadas por columna:")

    for i in range(P.shape[1]):
        count = np.count_nonzero(mask[:, i])

        if count > 0:
            print(
                f"i={i:3d}, "
                f"x={D.x1[i]: .6f}, "
                f"celdas={count:3d}"
            )




# --------------------------------------------------
# Diagnostic of kinetic and magnetic energy
# --------------------------------------------------

rho = np.asarray(D.rho)

vx1 = np.asarray(D.vx1)
vx2 = np.asarray(D.vx2)
vx3 = np.asarray(D.vx3)

bx1 = np.asarray(D.bx1)
bx2 = np.asarray(D.bx2)
bx3 = np.asarray(D.bx3)

P = np.asarray(D.prs)
C = np.asarray(D.tr1)

# Energy densities in code units
ekin = 0.5 * rho * (vx1**2 + vx2**2 + vx3**2)
emag = 0.5 * (bx1**2 + bx2**2 + bx3**2)

bmag = np.sqrt(bx1**2 + bx2**2 + bx3**2)

# Coordinates
X, Y = np.meshgrid(D.x1, D.x2)

floor = P <= 1.01e-12

regions = {
    "Lower-left": (
        (X < 0.3) & (Y < -0.6)
    ),
    "Upper-right": (
        (X > 1.5) & (Y > 0.5)
    ),
    "Whole domain": np.ones_like(P, dtype=bool)
}

for name, region in regions.items():

    print("\n", "=" * 40)
    print(name)
    print("=" * 40)

    for field_name, field in [
        ("rho", rho),
        ("pressure", P),
        ("kinetic energy", ekin),
        ("magnetic energy", emag),
        ("magnetic field", bmag),
        ("tracer", C)
    ]:

        a = field[region]
        a = a[np.isfinite(a)]

        if a.size:
            print(
                f"{field_name:18s}",
                f"min={a.min():.6e}",
                f"max={a.max():.6e}",
                f"mean={a.mean():.6e}"
            )

    print(
        "Pressure-floor cells:",
        np.count_nonzero(floor & region)
    )
