#!/usr/bin/env python
"""
@authors: G. Aguilar

originally from an example from HRL repository
modified by Ji Hyea Park for own project
"""

import data_management
import numpy as np
import pandas as pd
import random
from luminance2intensity import I_PROBES_TB, I_PROBES_TW

DEBUG = False

backgrounds=(0.0, 1.0)

if DEBUG:
    print('intensities Target in White: ', I_PROBES_TW)
    print('intensities Target in Black: ', I_PROBES_TB)
    print('backgrounds: ', backgrounds)

def generate_session(Nrepeats=1):
    """ 
    Generates design files for one session.
    We think of one session corresponding to several blocks of trials.
    You set up how many repeats you do per session with the argument
    Nrepeats
    """
    
    for i in range(Nrepeats):
        block = generate_block(i)
        block_id = f"2afc-{i}"

        # Save to file
        filepath = data_management.design_filepath(block_id)
        block.to_csv(filepath)


def generate_block(block_id):
    """ 
    Experimental design for one block of trials. 
    Here you define how many trials one block will contain, which
    will depend on the number of conditions you have. 
    """

    # path = f'../data/design/BASE/BASIS2/BASIS2_20231024_{block_id}.design.csv'
    path = f'../data/design/BASE/ZUSATZ/ZUSATZ-0.csv'
    
    if DEBUG:
        path = f'../data/design/BASE/SAMPLE2/SAMPLE2_20231024_{block_id}.design.csv'

    stimuli_design = data_management.load_design(path)
    
    random.shuffle(stimuli_design)

    # creates dataframe with all trials
    block = pd.DataFrame(
        stimuli_design,
        columns=['stim_name', 'target_bg', 'l_probe'],
        # stim_name, target_bg, l_probe
    )    
    
    print(block)

    # Shuffle trial order
    block = block.reindex(np.random.permutation(block.index))
    block.reset_index(drop=True, inplace=True)
    block.index.name = "trial"

    return block


if __name__ == "__main__":
    
    generate_session()
