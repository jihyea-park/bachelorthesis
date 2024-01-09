#!/usr/bin/env python
"""
Create and export stimuli for e-paper

@authors: Ji Hyea Park
"""

import stimupy
from stimupy.utils import resolution, export
import os
import stimuli_helper as stimhelper
import numpy as np

PPD = 34

epaper_shape = (1200, 1600)
epaper_size = resolution.visual_size_from_shape_ppd(shape=epaper_shape, ppd=PPD)

w = 1.0
b = 0.0
t = 0.5

# %% SBC
def sbcs(target_bg:str, l_probe:float):

    # target_bg: W or B
    # L: B, R: W
    # Tw Pb
    # Pw Tb
    Br = w
    Bl = b
    Tr = 0.0
    Tl = 0.0
    # Br, Bl, Tr, Tl

    if target_bg.lower() == 'b':
        Tr = l_probe
        Tl = t

    if target_bg.lower() == 'w':
        Tr = t
        Tl = l_probe

    return stimhelper.two_sided_edit(
        visual_size=epaper_size, 
        target_size=resolution.visual_size_from_shape_ppd(shape=(300,300), ppd=PPD),
        ppd=PPD,
        Br=Br,
        Bl=Bl,
        Tr=Tr,
        Tl=Tl
        )

# %% WHITE'S
def whites(target_bg:str, l_probe:float):
    
    # target_bg: W or B
    # Pb Tw
    # Tb Pw
    Br = 0.0
    Bl = 0.0
    Tr = 0.0
    Tl = 0.0

    if target_bg.lower() == 'w':
        Br = w
        Tr = t
        Bl = b
        Tl = l_probe

    if target_bg.lower() == 'b':
        Br = w
        Tr = l_probe
        Bl = b
        Tl = t

    return stimupy.stimuli.whites.white(
        visual_size=epaper_size,
        ppd=PPD, 
        n_bars = 8,
        intensity_bars= (Br, Bl),
        target_indices = (2, 5),
        intensity_target = (Tr, Tl),
        target_heights = resolution.visual_angle_from_length_ppd(400, PPD)
    )

# %% export stimuli
def export_stimuli(stim_name:str, target_bg:str, l_probe:float):
    stim_name = stim_name.lower()
    target_bg = target_bg.upper()
    # Name scheme: <stim_name>_<target_bg>_P<l_probe>
    img_name = '%s_%s_P%s' % (stim_name, target_bg, round(l_probe, 2))
    img_path = os.path.join(os.path.dirname(__file__), 'imgs/%s/%s' % (stim_name, img_name))

    print(img_path)

    if stim_name == 'sbcs':
        export.array_to_image(sbcs(target_bg, l_probe)["img"], img_path)
        print('new sbc exported!')
    elif stim_name == 'whites':
        export.array_to_image(whites(target_bg, l_probe)["img"], img_path)
        print('new white exported!')  
    

# %% export stims
STIMS = ('sbcs', 'whites')
BGS = ('w', 'b')
L_PROBES_TW = np.linspace(0.1, 0.4, 6).round(2)
L_PROBES_TB = np.linspace(0.6, 0.9, 6).round(2)
L_PROBES_ZU_W = [0.53, 0.56]
L_PROBES_ZU_S = [0.93, 0.96]

LUMINANCES = [L_PROBES_TW.tolist(), L_PROBES_TB.tolist()]

# for bg_id in np.arange(0, len(BGS)):
#     for l in LUMINANCES[bg_id]:
#         export_stimuli('sbcs', BGS[bg_id], round(l, 2))

# for bg_id in np.arange(0, len(BGS)):
#     for l in LUMINANCES[bg_id]:
#         export_stimuli('whites', BGS[bg_id], round(l, 2))

# for l in L_PROBES_ZU_S:
#     export_stimuli('sbcs', 'b', l)

# for l in L_PROBES_ZU_W:
#     export_stimuli('whites', 'b', l)