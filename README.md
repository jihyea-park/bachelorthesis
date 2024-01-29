# Vergleich zwischen E-Papier und Bildschirm als Anzeigeform der optischen Reizen

en) Comparison between E-Paper and Monitor as a Display Form for Visual Stimuli

## Description

The repository consists of scripts and data for experiments for bachelor thesis written in the department of [computational psychology](https://www.psyco.tu-berlin.de/) at Technische Universität Berlin. 2 alternative forced choice (2AFC) was implemented for experiments with e-paper and monitor, seperately. Most of them are based on example scripts of [HRL](https://github.com/computational-psychology/hrl) and [Stimupy](https://github.com/computational-psychology/stimupy). Tests and experiments were run on the environment with Debian OS.

### Experiment With E-Paper

Scripts and data sets for the experiment with e-paper. See [instruction for experimenter](#instruction-for-experimenter) before the experiment.

- experiment
    - imgs
        - Premade stimuli and background image files for the experiment with e-paper.
    - dp-setting.txt
        - Those commands might need to be run for pygame to function in debian OS.
    - exp_data.py
        - Import and export data for experiments, such as design and result.
    - exp_design.py
        - Export base designs in a certain order.
        - Initiate the experiment with random order of base designs.
    - exp_joystick.py
        - Control the experiment sequence with gamepad.
    - experiment.py
        - Main experiment script.
    - img_loader.py
        - *Load* image name and path, *Upload* image on the e-paper by making connection to e-paper server and *show* the image.
    - stimuli.py
        - Create and export stimuli image files. Note that created stimuli will be presented horizontally reversed on e-paper.
    - stimuli_helper.py
        - Helper tool for creating stimuli.
- data
    - design
        - Designs of experiments are saved here.
        - BASE: base designs of experiments.
    - results
        - Results of experiments are saved here.

### Experiment With Monitor

Scripts and data sets for the experiment with monitor. 
Experiment starts with 
´python run_experiment.py´

Mostly adapted from examples of [HRL](https://github.com/computational-psychology/hrl) or [Stimupy](https://github.com/computational-psychology/stimupy)
Scripts or contents without comment below are as-is or with very little changes adapted from HRL.

- experiment
    - data_management.py
    - design.py
        - Adapted from HRL example, generate experiment blocks with BASE designs in random order.
    - experiment_logic.py
    - luminanace2intensity.py
        - Read lut file, curve fit data from lut and convert luminance to intensity(reflectance).
    - lut.csv
    - run_experiment.py
    - stimuli.py
        - Generate stimuli with luminance values, by converting them to intensity(reflectance) values through luminance2intensity script.
    - stimuli_helper.py
        - Helper tool for generating stimuli.
    - text_displays.py
- data
    - design
        - Designs of experiments are saved here.
        - BASE: base designs of experiments.
    - results
        - Results of experiments are saved here.
- messungen
    - Luminance measurements results within calibration

### Evaluate Results

The first part of the psignifit implementation was done by [Dr. Guillermo Aguilar](https://www.psyco.tu-berlin.de/aguilar.html).

- evaluate.ipynb
    - Evaluate the result, plot psychometric function and confidence interval.

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

## Instruction for Experimenter

Following is the instruction for experimenters of experiment with E-Paper.

Before begin, make sure 1) e-paper and its server, 2) gamepad and the computer are connected.

1. In terminal:

This is to avoid error while running Pygame in Debian. 

```
sudo find / -name libstdc++.so.6>/dev/null
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
```

2. Make sure all [dependencies](#related) are installed in your environment. (e.g. use `conda activate ba-ji`)

3. Experiment starts in experiment folder with
`python experiment.py`

4. During the experiment, make sure the pygame window is selected.

5. Give a name of a test person. A test design will be generated, based on the BASE design.

6. **When the first instruction image is shown on e-paper**
    - Press **A** on the gamepad.
        - The base stimulus of SBC, both target squares with 0.5 reflectance, will be uploaded for the light control.
    - Control the light, so that two target squares are equi-luminant
    - Press **A** again to go back to the experiment instruction.

7. The test person starts 1. Block (SBC) with right trigger (RT)
    - 60 trials, a pause and another 60 trials

8. After the first block, **when the test person should take a rest and call the experimenter**
    - Press **B** on the gamepad.
        - The base stimulus of White, both target squares with 0.5 reflectance, will be uploaded for the light control.
    - Control the light, so that two target squares are equi-luminant
    - Press **B** again to go back to the experiment instruction.

9. The test person starts 2. Block (White) with RT
    - 60 trials, a pause and another 60 trials.

10. The experiment ends with Left Trigger (LT) by the test person.
    - With LT, results will be written and exported to data/results

### Troubleshoot & Notes about the Experiment with E-Paper

#### When the test person reports a problem, button does not work.
Check if pygame window is selected.

#### Test experiment with fewer trials
You can test the experiment with 1 or 5 repetitions (see exp_design.py)