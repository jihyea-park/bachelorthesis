#!/usr/bin/env python
"""
Run two alternative forced choice experiment with e-paper and a gamepad.

@authors Ji Hyea Park

"""

from exp_gamepad import exp_control
import exp_data
import exp_design
import numpy as np

EXPS, RES = exp_design.init()
# EXPS, RES = exp_design.init_zusatz()
RES = exp_control(EXPS, RES)
print(RES)

for block_id in np.arange(0, len(RES)):
    exp_data.save_result(RES[block_id], block_id)
