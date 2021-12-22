from math import log2, log
from .fisher_exact import test1t as fisher_exact


def MI(O11, O12, O21, O22, E11, E12, E21, E22):
    return log2(O11 / E11)


def Xsq(O11, O12, O21, O22, E11, E12, E21, E22):
    val = (O11 - E11)**2 / E11 + (O12 - E12)**2 / E12 + (O21 - E21)**2 / E21 + (O22 - E22)**2 / E22
    if O11 < E11:
        val = -val
    return val


def Gsq(O11, O12, O21, O22, E11, E12, E21, E22):
    val = 2 * (GsqT(O11, E11) + GsqT(O12, E12) + GsqT(O21, E21) + GsqT(O22, E22))
    if O11 < E11:
        val = -val
    return val


def Dice(O11, O12, O21, O22, E11, E12, E21, E22):
    return 2 * O11 / (O11 + O12 + O11 + O21)


def DeltaP21(O11, O12, O21, O22, E11, E12, E21, E22):
    return O11 / (O11 + O12) - O21 / (O21 + O22)


def DeltaP12(O11, O12, O21, O22, E11, E12, E21, E22):
    return O11 / (O11 + O21) - O12 / (O12 + O22)


def FisherExact(O11, O12, O21, O22, E11, E12, E21, E22):
    pval = fisher_exact(O11, O12, O21, O22)
    if O11 < E11: 
        pval *= -1
    return pval


def FisherAttract(O11, O12, O21, O22, E11, E12, E21, E22):
    pval = fisher_exact(O11, O12, O21, O22)
    fisher_attract = -log(pval)
    if O11 < E11:
        fisher_attract = -fisher_attract
    return fisher_attract


# Helpers for association measures
def GsqT(O, E):
    if O == 0: return 0
    return O * log(O/E)


def additive_smooth(O11, O12, O21, O22, alpha=0.1):
    O11 += alpha
    O12 += alpha
    O21 += alpha
    O22 += alpha
    N = O11 + O21 + O12 + O22
    R1 = O11 + O12
    C1 = O11 + O21
    R2 = N - R1
    C2 = N - C1
    return O11, O12, O21, O22, R1*C1/N, R1*C2/N, R2*C1/N, R2*C2/N
