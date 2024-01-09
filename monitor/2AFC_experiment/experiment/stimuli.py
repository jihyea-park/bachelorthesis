#!/usr/bin/env python
"""
Create stimuli for experiments with certain luminance values in a certain size.

@authors Ji Hyea Park
"""

import stimupy
import luminance2intensity as L2I
import stimuli_helper as stimhelp
import numpy as np

# size: degree, visual angle
# ppd: pixel per degree here 34
# shape: px 

def calculate_visual_angle(object_size):
    '''
    object_size in meter
    '''
    va = 2 * np.rad2deg(np.arctan(object_size/2))
    return va

# visual size in meter weicht von echter Größe ab, wegen der Kurven (CRT)
visual_size_in_meter = (0.28, 0.37) # 0.20, 0.26
target_size_in_meter = (0.07, 0.07)
target_height_in_meter = 0.28/3

visual_size_ = tuple(calculate_visual_angle(i) for i in visual_size_in_meter)
target_size_ = tuple(calculate_visual_angle(i) for i in target_size_in_meter)
target_height_ = calculate_visual_angle(target_height_in_meter)

W = 1.0
B = 0.0
T = 0.5
PPD = 34

def sbcs(target_bg:str, l_probe:float):

    # Left: b, Right: w

    Bl = L2I.i_sbc_bgs[1]
    Br = L2I.i_sbc_bgs[2]

    Tl = 0.0
    Tr = 0.0

    if target_bg.lower() == 'b':
        Tr = L2I.get_int2(l_probe)
        Tl = L2I.i_sbc_t5[0]
    elif target_bg.lower() == 'w':
        Tr = L2I.i_sbc_t5[1]
        Tl = L2I.get_int2(l_probe)

    print(f'Bl: {Bl}, Tl: {Tl}, Br: {Br}, Tr: {Tr}')

    return stimhelp.two_sided_edit(
        visual_size=visual_size_, 
        target_size=target_size_,
        ppd=PPD,
        Br=Br,
        Bl=Bl,
        Tr=Tr,
        Tl=Tl,
        )

# %% WHITES
def whites(target_bg:str, l_probe:float):
    # L: Tb, R: Tw

    # target_bg: W or B
    # Pb Tw
    # Tb Pw
    bars = L2I.i_white_bgs[1:]
    Tr = 0.0
    Tl = 0.0

    if target_bg.lower() == 'w':
        Tr = L2I.i_white_t5[1]
        Tl = L2I.get_int2(l_probe, sbc=False)
    if target_bg.lower() == 'b':
        Tr = L2I.get_int2(l_probe, sbc=False)
        Tl = L2I.i_white_t5[0]

    print(f'bars: {bars}, Tl: {Tl}, Tr: {Tr}')

    return stimupy.stimuli.whites.white(
        visual_size=visual_size_,
        ppd=PPD, 
        n_bars = 8,
        intensity_bars= bars,
        target_indices = (2, 5),
        intensity_target = (Tl, Tr),
        target_heights = target_height_
    )