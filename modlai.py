import numpy as np

def modlai(lai, ndvi_inf, ndvi_soil, K):
    lai = np.array(lai)
    return ndvi_inf + (ndvi_soil - ndvi_inf)*np.exp(-K*lai)

