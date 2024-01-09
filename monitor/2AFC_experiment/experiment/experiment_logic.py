#!/usr/bin/env python
"""
@authors: G. Aguilar

originally from an example from HRL repository
modified by Ji Hyea Park for own project
"""

import numpy as np
import stimuli
import sys
import time

def display_stim(ihrl, stim_name, target_bg, l_probe):
    """Display stimulus for current trial""" 
    
    if stim_name == 'sbcs':
        stimulus = stimuli.sbcs(
            target_bg=target_bg,
            l_probe=l_probe
        )

    if stim_name == 'whites':
        stimulus = stimuli.whites(
            target_bg=target_bg,
            l_probe=l_probe
        )
    
    # Convert the stimulus image(matrix) to an OpenGL texture
    stim_texture = ihrl.graphics.newTexture(stimulus['img'])
    
    # Determine position: we want the stimulus around the center
    # center = (1080//2, 1920//2)
    center = (768 // 2, 1024 // 2)
    pos = (center[1] - (stim_texture.wdth // 2), center[0] - (stim_texture.hght // 2))

    # Create a display: draw texture on the frame buffer
    stim_texture.draw(pos=pos, sz=(stim_texture.wdth, stim_texture.hght))
                 
    # Draw textures on the frame buffer
    # draw_fixation_cross(ihrl)
                       
    # Display: flip the frame buffer
    ihrl.graphics.flip()  # flips the frame buffer to show everything

    return


def draw_fixation_cross(ihrl):
    
    # draws fixation cross in the middle

    fix = ihrl.graphics.newTexture(np.ones((5, 5))*0.0)
    fix.draw(( 1024 // 2, 768 // 2))
    
    
def display_fixation_cross(ihrl):
    
    ihrl.graphics.flip(clr=True)
    draw_fixation_cross(ihrl)
    ihrl.graphics.flip()
      
    return 

        
def run_trial(ihrl, stim_name, target_bg, l_probe, **kwargs):
    """ Function that runs sequence of events during one trial"""
    
    # Fixation cross
    display_fixation_cross(ihrl)
    
    # sleeps for 250 ms # using system time (inaccurate)
    time.sleep(0.25)
    
    # Display stimuli 
    display_stim(
        ihrl,
        stim_name, 
        target_bg, 
        l_probe    
    )
    
    # Wait for answer
    btn, t1 = ihrl.inputs.readButton(btns=['Left', 'Right', 'Escape', 'Space'])
    
    # Raise SystemExit Exception
    if (btn == "Escape") or (btn=='Space'): sys.exit("Participant terminated experiment.")


    # end trial
    return {"response": btn, 'resp.time': t1}
