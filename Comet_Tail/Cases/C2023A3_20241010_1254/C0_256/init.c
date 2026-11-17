
#include "pluto.h"
#include "comet_parameters.h"

/* ==========================================================
   C/2023 A3 - Solar wind initial conditions
   Date: 2024-10-10 12:54 UTC

   Model:
   2D Cartesian MHD, GLM divergence cleaning

   ========================================================== */

/* ----------------------------------------------------------
   Initial conditions
   ---------------------------------------------------------- */

void Init(double *v, double x1, double x2, double x3)
{
    /* Solar wind density */

    v[RHO] = RHO_SW;

    /* Relative velocity in comet reference frame */

    v[VX1] = VX_SW;
    v[VX2] = VY_SW;
    v[VX3] = VZ_SW;

    /* Thermal pressure */

    v[PRS] = PRS_SW;

    /* Parker magnetic field in local coordinates */

    #if PHYSICS == MHD

    v[BX1] = BX_SW;
    v[BX2] = BY_SW;
    v[BX3] = BZ_SW;

    #ifdef GLM_MHD
    v[PSI_GLM] = 0.0;
    #endif

    #endif

    /* Initially no cometary plasma */

    v[TRC] = TRC_SW;
}

/* ----------------------------------------------------------
   Additional domain initialization
   ---------------------------------------------------------- */

void InitDomain(Data *d, Grid *grid)
{
}

/* ----------------------------------------------------------
   Analysis
   ---------------------------------------------------------- */

void Analysis(const Data *d, Grid *grid)
{
}

/* ----------------------------------------------------------
   User-defined boundary conditions
   ---------------------------------------------------------- */

void UserDefBoundary(
    const Data *d,
    RBox *box,
    int side,
    Grid *grid
)
{
    int i, j, k;

    /*
       Solar wind enters through the left boundary.
    */

    if (side == X1_BEG) {

        /*
           DIV_CLEANING uses cell-centered magnetic fields.
        */

        if (box->vpos == CENTER) {

            BOX_LOOP(box, k, j, i) {

                /* Density */

                d->Vc[RHO][k][j][i] = RHO_SW;

                /* Velocity */

                d->Vc[VX1][k][j][i] = VX_SW;
                d->Vc[VX2][k][j][i] = VY_SW;
                d->Vc[VX3][k][j][i] = VZ_SW;

                /* Pressure */

                d->Vc[PRS][k][j][i] = PRS_SW;

                #if PHYSICS == MHD

                /* Magnetic field */

                d->Vc[BX1][k][j][i] = BX_SW;
                d->Vc[BX2][k][j][i] = BY_SW;
                d->Vc[BX3][k][j][i] = BZ_SW;

                #ifdef GLM_MHD
                d->Vc[PSI_GLM][k][j][i] = 0.0;
                #endif

                #endif

                /* Passive tracer */

                d->Vc[TRC][k][j][i] = TRC_SW;
            }
        }
    }
}
