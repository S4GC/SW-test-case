
#ifndef COMET_SOURCE_H
#define COMET_SOURCE_H

#include <math.h>
#include "comet_parameters.h"

/* Mathematical constant */

#define COMET_PI 3.14159265358979323846

typedef struct {

    double srho;
    double unx;
    double uny;
    double energy;

} CometSourceTerms;


/* ==========================================================
   Evaluate neutral coma and mass-loading source.

   Input coordinates: PLUTO code units.

   Returned source: PLUTO code units.

   ========================================================== */

static inline CometSourceTerms
EvaluateCometSource(double x1, double x2)
{
    CometSourceTerms S;

    double dx, dy;
    double r, reff;

    double nn;
    double srho_cgs;

    double unx_cgs, uny_cgs;

    /* Coordinates relative to nucleus */

    dx = (x1 - COMET_X0_CODE) * COMET_L0_CGS;
    dy = (x2 - COMET_Y0_CODE) * COMET_L0_CGS;

    r = sqrt(dx*dx + dy*dy);

    reff = sqrt(
        r*r +
        COMET_RSOFT_CGS*COMET_RSOFT_CGS
    );

    /* Neutral density: Haser-type approximation */

    nn = COMET_Q_MOL_S /
         (4.0 * COMET_PI *
          COMET_VN_CGS * reff * reff);

    nn *= exp(-r / COMET_LI_CGS);

    /* Ionization mass source in CGS */

    srho_cgs =
        COMET_MI_CGS *
        COMET_NU_ION *
        nn;

    /* Convert mass source to code units */

    S.srho = srho_cgs *
             COMET_T0_S /
             COMET_RHO0_CGS;

    /* Neutral radial velocity in code units */

    unx_cgs = COMET_VN_CGS * dx / reff;
    uny_cgs = COMET_VN_CGS * dy / reff;

    S.unx = unx_cgs / COMET_V0_CGS;
    S.uny = uny_cgs / COMET_V0_CGS;

    /* Total energy source */

    S.energy = S.srho *
        (
            COMET_EINT_CODE +
            0.5 * (
                S.unx*S.unx +
                S.uny*S.uny
            )
        );

    return S;
}

#endif