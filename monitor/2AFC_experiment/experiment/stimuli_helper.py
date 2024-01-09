#!/usr/bin/env python
"""
Create stimulus of two-sided simultaneous brightness contrast display with central targets

@authors: Lynn Schmittwilken, Marianne Maertens, Joris Vincent

modified by Ji Hyea Park for own project.
"""

from stimupy.stimuli.sbcs import basic
from stimupy.utils import resolution, stack_dicts

def two_sided_edit(
    visual_size=None,
    ppd=None,
    shape=None,
    target_size=None,
    Br=0.0,
    Bl=1.0,
    Tr=0.5, 
    Tl=0.5,
):
    """
    Two-sided simultaneous contrast display with central targets
    
    adjusted by Ji Hyea Park for own project

    Parameters
    ----------
    visual_size : Sequence[Number, Number], Number, or None (default)
        visual size [height, width] of grating, in degrees
    ppd : Sequence[Number, Number], Number, or None (default)
        pixels per degree [vertical, horizontal]
    shape : Sequence[Number, Number], Number, or None (default)
        shape [height, width] of grating, in pixels
    target_size : float or (float, float)
        size of the target in degree visual angle (height, width)
    intensity_background : Sequence[Number, Number]
        intensity values for backgrounds
    intensity_target : float
        intensity value for target

    Returns
    -------
    dict[str, Any]
        dict with the stimulus (key: "img"),
        mask with integer index for the target (key: "target_mask"),
        and additional keys containing stimulus parameters

    References
    ----------
    Chevreul, M. (1855).
        The principle of harmony and contrast of colors.
    """
    if target_size is None:
        raise ValueError("two_sided() missing argument 'target_size' which is not 'None'")

    # Resolve resolution
    shape, visual_size, ppd = resolution.resolve(shape=shape, visual_size=visual_size, ppd=ppd)

    # left
    stim_l = basic(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        intensity_background=Bl,
        intensity_target=Tl,
    )

    # right
    stim_r = basic(
        visual_size=(visual_size[0], visual_size[1] / 2),
        ppd=ppd,
        target_size=target_size,
        intensity_background=Br,
        intensity_target=Tr,
    )

    stim = stack_dicts(stim_l, stim_r)
    del stim["intensity_background"]
    del stim["target_position"]
    stim["intensity_backgrounds"] = (Bl, Br)
    stim["target_positions"] = (stim_l["target_position"], stim_r["target_position"])
    stim["shape"] = shape
    stim["visual_size"] = visual_size
    
    return stim
