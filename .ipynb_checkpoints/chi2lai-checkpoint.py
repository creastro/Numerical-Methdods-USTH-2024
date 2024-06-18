import numpy as np
from modlai import modlai


def chi2lai(params, lai_exp, ndvi_exp):
    ndvi_inf, ndvi_soil, K = params

    if len(lai_exp) != len(ndvi_exp):
        raise ValueError('LAI and NDVI are not in the same dimension')
    return np.sum((ndvi_exp - modlai(lai_exp,ndvi_inf,ndvi_soil,K))**2)