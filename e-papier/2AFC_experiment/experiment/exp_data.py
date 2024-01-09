#!/usr/bin/env python
"""
@authors: Guillermo Aguilar, Joris Vincent, Torsten Betz

originally from an example from HRL repository
modified by Ji Hyea Park for own project
"""

import csv
from datetime import datetime
from pathlib import Path

LANG = "en"
if LANG == "de":
    participant = (input("Bitte geben Sie Ihre Initialen ein (z.b.: DEMO): ") or "DEMO").upper()
if LANG == "en":
    participant = (input("Please enter participant initials (ex.: DEMO): ") or "DEMO").upper()

# Experiment path:
experiment_path = Path().absolute()

# Overall datapath
datapath = experiment_path.parent / "data"
datapath.mkdir(parents=True, exist_ok=True)  # create datapath + parents, if does not exist
print(f"Saving and loading data in {datapath}")

# Designs
designs_dir = datapath / "design" / participant
designs_dir.mkdir(parents=True, exist_ok=True)

# Results
results_dir = datapath / "results" / participant
results_dir.mkdir(parents=True, exist_ok=True)

# Current session (today's date)
session_id = datetime.today().strftime("%Y%m%d")

def design_filepath(block_id):
    """Construct filepath to design file for given block

    Will generally be in the form of "<designs_dir>/<participant>_<session_id>_<block_id>.design.csv"

    Parameters
    ----------
    block_id : str
        identifier-string for block

    Returns
    -------
    Path
        filepath to block design file
    """

    # Design filename for this block
    filename = f"{participant}_{session_id}_{block_id}.design.csv"

    # Full filepath design file
    return designs_dir / filename


def results_filepath(block_id):
    """Construct filepath to results file for given block

    Will generally be in the form of "<results_dir>/<participant>_<session_id>_<block_id>.results.csv"

    Parameters
    ----------
    block_id : str
        identifier-string for block

    Returns
    -------
    Path
        filepath to block results file
    """

    # Results filename for this block
    filename = f"{participant}_{session_id}_{block_id}.results.csv"

    # Full filepath resultsfile
    return results_dir / filename

### ^^^ From data_management.py ^^^ ###

def save_design(EXPS:list, block_id):
    target = open(design_filepath(block_id), 'w')
    writer = csv.writer(target)
    writer.writerow(['stim_name', 'target_bg', 'l_probe'])
    for d in EXPS:
        writer.writerow(d.values())
    target.close()
    return target

def save_result(RES:list, block_id):
    target = open(results_filepath(block_id), 'w')
    writer = csv.writer(target)
    writer.writerow(['stim_name', 'target_bg', 'l_probe', 'isBrighter', 'resp_time'])
    for d in RES:
        if type(d) == dict:
            writer.writerow(d.values())
    target.close()
    return target

def load_design(path):
    file = open(path, 'r')
    design = list(csv.DictReader(file))
    file.close()

    return design