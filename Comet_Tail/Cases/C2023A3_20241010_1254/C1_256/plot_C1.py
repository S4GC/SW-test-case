
import numpy as np
import matplotlib.pyplot as plt
import pyPLUTO as pp

# Load last saved C1 state
D = pp.Load(path="./", nout=1)

x1 = np.asarray(D.x1)
x2 = np.asarray(D.x2)

P = np.asarray(D.prs)
C = np.asarray(D.tr1)
rho = np.asarray(D.rho)

# Identify pressure-floor cells
pressure_floor = 1.0e-12
mask = P <= 1.01 * pressure_floor

# Avoid log10(0)
logP = np.log10(np.maximum(P, pressure_floor))

fig, ax = plt.subplots(1, 3, figsize=(17, 5))

# Pressure
im0 = ax[0].pcolormesh(
    x1, x2, logP,
    shading="auto",
    cmap="magma"
)
ax[0].set_title("log10(Pressure)")
fig.colorbar(im0, ax=ax[0])

# Pressure floor
im1 = ax[1].pcolormesh(
    x1, x2, mask.astype(float),
    shading="auto",
    cmap="gray_r",
    vmin=0, vmax=1
)
ax[1].set_title("Pressure floor cells")
fig.colorbar(im1, ax=ax[1])

# Cometary tracer
im2 = ax[2].pcolormesh(
    x1, x2, C,
    shading="auto",
    cmap="viridis",
    vmin=0, vmax=1
)
ax[2].set_title("Cometary tracer")
fig.colorbar(im2, ax=ax[2])

for a in ax:
    a.set_xlabel("X1")
    a.set_ylabel("X2")
    a.set_aspect("equal")

fig.suptitle("C1 - Haser mass loading, t = 10.30872")
fig.tight_layout()

fig.savefig("C1_pressure_diagnostics.png", dpi=200)
plt.show()

print("Pressure-floor cells:", np.count_nonzero(mask))
print("Affected percentage:", 100*np.mean(mask))
