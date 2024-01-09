# Vergleich zwischen E-Papier und Bildschirm als Anzeigeform der optischen Reizen

en) Comparison between E-Paper and Monitor as a Display Form for Visual Stimuli

## Description

The repository consists of scripts and data for experiments for bachelor thesis written in the department of [computational psychology](https://www.psyco.tu-berlin.de/) at Technische Universität Berlin. 2 alternative forced choice (2AFC) was implemented for experiments with e-paper and monitor, seperately. Most of them are based on example scripts of [HRL](https://github.com/computational-psychology/hrl) and [Stimupy](https://github.com/computational-psychology/stimupy). Tests and experiments were run on the environment with Debian OS.

### Experiment With E-Paper

Scripts and data sets for the experiment with e-paper. 
Experiment starts with 
´python experiment.py´

- experiment:
    - imgs: 
        Premade stimuli and background image files for the experiment with e-paper.
    - dp-setting.txt:
        Those commands might need to be run for pygame to function in debian OS.
    - exp_data.py:
        Import and export data for experiments, such as design and result.
    - exp_design.py:
        Export base designs in a certain order.
        Initiate the experiment with random order of base designs.
    - exp_joystick.py
        Control the experiment sequence with gamepad.
    - experiment.py
        Main experiment script.
    - img_loader.py
        Load image, make connection to e-paper server, upload and show image on the e-paper.
    - stimuli.py
        Create and export stimuli image files.
    - stimuli_helper.py
        Helper tool for creating stimuli.
- data
    - design: 
        Designs of experiments are saved here.
        - BASE: base designs of experiments.
    - results:
        Results of experiments are saved here.

### Experiment With Monitor

Scripts and data sets for the experiment with e-paper. 
Experiment starts with 
´python run_experiment.py´

Mostly adapted from examples of [HRL](https://github.com/computational-psychology/hrl) or [Stimupy](https://github.com/computational-psychology/stimupy)
Scripts or contents without comment below are as-is or with very little changes adapted from HRL.

- experiment: 
    - data_management.py
    - design.py
        Adapted from HRL example, generate experiment blocks with BASE designs in random order.
    - experiment_logic.py
    - luminanace2intensity.py
        Read lut file, curve fit data from lut and convert luminance to intensity(reflectance).
    - lut.csv
    - run_experiment.py
    - stimuli.py
        Generate stimuli with luminance values, by converting them to intensity(reflectance) values through luminance2intensity script.
    - stimuli_helper.py
        Helper tool for generating stimuli.
    - text_displays.py
- data
    - design
        Designs of experiments are saved here.
        - BASE: base designs of experiments.
    - results
        Results of experiments are saved here.
- messungen
    Luminance measurements results within calibration

### Evaluate Results

The first part of the psignifit implementation was done by [Dr. Guillermo Aguilar](https://www.psyco.tu-berlin.de/aguilar.html).

- evaluate.ipynb
    - evaluate the result, plot psychometric function and confidence interval.

## Authors

- [@Ji Hyea Park](https://github.com/jihyea-park)

## Acknowledgements

- [Dr. Guillermo Aguilar](https://www.psyco.tu-berlin.de/aguilar.html)
- [Computational Psychology at TU Berlin](https://www.psyco.tu-berlin.de/)

## Related

- [HRL: High Resolution Luminance](https://github.com/computational-psychology/hrl)
- [Stimupy](https://github.com/computational-psychology/stimupy)
- [Psignifit](https://github.com/wichmann-lab/python-psignifit)
- [Python Visionect Software Suite API library](https://github.com/visionect/libpyvss)
- [Pygame](https://www.pygame.org/)