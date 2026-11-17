
#ifndef COMET_PARAMETERS_H
#define COMET_PARAMETERS_H

/* ==========================================================
   C/2023 A3 - 10 October 2024, 12:54 UTC
   Physical parameters and normalization
   ========================================================== */

/* Cometary gas production */

#define COMET_Q_MOL_S       1.0e29

/* Neutral gas */

#define COMET_VN_CGS        7.0e4
#define COMET_NU_ION        3.06e-6

/* Water ion mass */

#define COMET_MP_CGS        1.67262192369e-24
#define COMET_MI_CGS        (18.0 * COMET_MP_CGS)

/* PLUTO normalization */

#define COMET_L0_CGS        1.0e11
#define COMET_V0_CGS        4.0e7
#define COMET_T0_S          2.5e3

#define COMET_RHO0_CGS      3.09411097591e-23

/* Neutral coma regularization */

#define COMET_RSOFT_CGS     1.2e9

/* Nucleus position in code coordinates */

#define COMET_X0_CODE       0.0
#define COMET_Y0_CODE       0.0

/* Neutral internal energy in code units */

#define COMET_EINT_CODE     0.0

/* Derived quantities */

#define COMET_LI_CGS \
    (COMET_VN_CGS / COMET_NU_ION)

#define COMET_RSOFT_CODE \
    (COMET_RSOFT_CGS / COMET_L0_CGS)

#endif
