#!/usr/bin/env python
"""
Design and initiate experiment.

@authors: Ji Hyea Park
"""

import random
import numpy as np
from exp_data import save_design, load_design

STIMS = ('sbcs', 'whites')
BGS = ('w', 'b')

L_PROBES_TW = np.linspace(0.1, 0.4, 6).round(2)
L_PROBES_TB = np.linspace(0.6, 0.9, 6).round(2)

LUMINANCES = [L_PROBES_TW.tolist(), L_PROBES_TB.tolist()]

### Stim design for 2AFC
### stim_name, (l_target), p_target, l_probe

### PATHS
sample = f'../data/design/BASE/SAMPLE2/SAMPLE2_20231024_' # 1 wdh
basistest = f'../data/design/BASE/BASIS-TEST/BASIS-TEST_20231023_' # 5 wdh
basis = f'../data/design/BASE/BASIS2/BASIS2_20231024_' # 10 wdh
zusatz = f'../data/design/BASE/ZUSATZ/ZUSATZ-' # 10 wdh

def create_design(STIMS, BGS, LUMINANCES, wdh):
    designs = []

    for block_id in np.arange(0, len(STIMS)):
        for i in np.arange(0, wdh):
            for bg_id in np.arange(0, len(BGS)):
                for luminance in LUMINANCES[bg_id]:
                    designs.append({
                        'stim_name': STIMS[block_id],
                        'target_bg': BGS[bg_id],
                        'l_probe': round(luminance, 2)
                    })
        save_design(designs, block_id)
        print('id: %s len: %s' % (block_id, len(designs)))
        designs = []

def make_block(DESIGN, block_id):
    # make block with designs in random order
    random.shuffle(DESIGN)
    save_design(DESIGN, block_id)
    return DESIGN

def init(test=False):
    # create and return designs and empty results
    designs = []
    results = [[dict], [dict]]

    if test:
        for block_id in np.arange(0, len(STIMS)):
            BASIS_path = sample + f'{block_id}.design.csv'
            BASIS = load_design(BASIS_path)
            designs.append(make_block(BASIS, block_id))
    else:
        for block_id in np.arange(0, len(STIMS)):
            BASIS_path = basis + f'{block_id}.design.csv'
            BASIS = load_design(BASIS_path)
            designs.append(make_block(BASIS, block_id))

    return designs, results

def init_zusatz(both=True):
    designs = []
    results = [[dict], [dict]]

    if not both:
        block_id = 1
        path = zusatz + f'{block_id}.csv'
        stem = load_design(path)
        designs.append(make_block(stem, block_id))

    if both:
        for block_id in np.arange(0, len(STIMS)):
            path = zusatz + f'{block_id}.csv'
            stem = load_design(path)
            designs.append(make_block(stem, block_id))

    return designs, results


# create_design(STIMS, BGS, LUMINANCES, 10) # BASIS
# create_design(STIMS, BGS, LUMINANCES, 1) # SAMPLE
# create_design(STIMS, BGS, LUMINANCES, 5) # BASIS-TEST

# L_PROBES_ZU_W = [0.53, 0.56]
# L_PROBES_ZU_S = [0.93, 0.96]
# create_design(['sbcs'], ['b'], [L_PROBES_ZU_S], 10) # ZU-SBCS
# create_design(['whites'], ['b'], [L_PROBES_ZU_W], 10) # ZU-WHITES