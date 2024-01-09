#!/usr/bin/env python
"""
Convert luminance value to reflectance, which was written as intensity in the script, using curve fitting of look-up table (lut).

lut created by G. Aguilar, Oct. 2022

@authors: Ji Hyea Park

"""

import os
import csv
import numpy as np
from scipy.optimize import curve_fit

### LUT
path = os.path.join(os.path.dirname(__file__), 'lut.csv')

file = open(path, "r")
lut = list(csv.DictReader(file, delimiter=" "))
file.close()

Intensity_lut = [float(row["IntensityIn"]) for row in lut]
Luminance_lut = [float(row["Luminance"]) for row in lut]

### Find Intensity of Luminance
# luminance = a * intensity + b
def fit(x, a, b):
    return a * x + b

# lut fitting
params, covariance = curve_fit(fit, Intensity_lut, Luminance_lut)

def read_luminance(p, i):
    return p[0] * i + p[1]

def read_intensity(p, a, l):
    return (l + a - p[1]) / p[0]

def i_list(ls:list):
    return [read_intensity(params, 0, l) for l in ls]

###

I_PROBES_TW = np.linspace(0.1, 0.4, 6).round(2)
I_PROBES_TB = np.linspace(0.6, 0.9, 6).round(2)

I_PROBES_ZU = [0.93, 0.96]

INTENSITIES = I_PROBES_TW.tolist() + I_PROBES_TB.tolist() + I_PROBES_ZU

## SBC
# BG Bb Bw
l_sbc_bgs = [49.89,22.85,269.04]
i_sbc_bgs = i_list(l_sbc_bgs)

# Tb Tw
l_sbc_t5 = [89.42,89.76]
i_sbc_t5 = i_list(l_sbc_t5)

# Target intensities
l_sbc_ts = [
    26.73,
    33.54,
    42.79,
    50.18,
    57.55,
    71.07,
    122.6,
    130.1,
    151.8,
    193.5,
    218.4,
    246.3,
    251.68,
    272
]
i_sbc_ts = i_list(l_sbc_ts)

## WHITE
# BG 0 1 2 3 4 5 6 7
l_white_bgs = [
    49.79,
    33.09,
    289.30,
    21.39,
    246.87,
    19.96,
    250.92,
    23.96,
    332.03
]
i_white_bgs = i_list(l_white_bgs)

# Tb, Tw
l_white_t5 = [88.71,90.05]
i_white_t5 = i_list(l_white_t5)

l_white_ts = [
    27.22,
    33.56,
    42.91,
    50.47,
    56.84,
    71.33,
    122.15,
    128.55,
    153.55,
    190.65,
    217.25,
    246.70
]
i_white_ts = i_list(l_white_ts)

def get_int2(l, sbc=True):
    if sbc:
        target_index = INTENSITIES.index(l)
        i = i_sbc_ts[target_index]
    else:
        target_index = INTENSITIES.index(l)
        i = i_white_ts[target_index]

    return i

bgs = [i_sbc_bgs[0], i_white_bgs[0]]
bg = read_intensity(params, 0, 54.59)
