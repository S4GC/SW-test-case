
import numpy as np
import pyPLUTO as pp

for n in [1, 2]:

    print("\n==============================")
    print("OUTPUT:", n)
    print("==============================")

    D = pp.Load(path="./", nout=n)

    for name in [
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
    ]:

        if hasattr(D, name):

            a = np.asarray(getattr(D, name))

            print(
                f"{name:10s}",
                f"min={np.nanmin(a):.8e}",
                f"max={np.nanmax(a):.8e}",
                f"mean={np.nanmean(a):.8e}"
            )


for name in ["Bx1", "Bx2", "Bx3"]:

    if hasattr(D, name):

        a = np.asarray(getattr(D, name))

        print(
            f"{name:10s}",
            f"min={np.nanmin(a):.8e}",
            f"max={np.nanmax(a):.8e}",
            f"mean={np.nanmean(a):.8e}"
        )
