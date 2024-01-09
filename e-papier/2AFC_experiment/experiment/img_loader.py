#!/usr/bin/env python
"""
Show stimulus on the e-paper display

@authors: Ji Hyea Park

"""

from vss_python_api import ApiDeclarations

def upload(img_name:str, img:str):
    vss_api_instance = ApiDeclarations('http://localhost:8081/', '3e9d8e459f5d0aae', 'xsijYfFpMew5Zk+9OHsAAe6QWPCOYOKqkcoE9DDV83M')
    uuid = '38002200-0351-3430-3939-313800000000'

    fr= {'image': (img_name, open(img, 'rb'), 'image/png', {'Expires': '0'})}

    vss_api_instance.set_http(uuid, fr)

    print(f'{img_name} uploaded!')

def show_blank():
    #img_name, img = load_image('blank')
    #upload(img_name, img)
    img_name, img = load_image('g_blank')
    upload(img_name, img)
    img_name, img = load_image('w_blank')
    upload(img_name, img)

def load_image(status:str):
    img_name = '%s.png' % (status)
    img = './imgs/%s' % (img_name)
    
    return img_name, img

def load_stimuli(exp:dict):
    stim_name = exp['stim_name']
    bg = exp['target_bg']
    refl = exp['l_probe']

    # Name scheme: <stim_name>_<target_bg>_P<l_probe>.png
    img_name = '%s_%s_P%s.png' % (stim_name.lower(), bg.upper(), refl)
    img = './imgs/%s/%s' % (stim_name, img_name)

    print('loaded %s' % img_name)

    return img_name, img

def control_stim(stim_name:str):
    img_name = '%s_T0.5.png' % (stim_name.lower())
    img = './%ss/%s' % (stim_name, img_name)
    upload(img_name, img)

def set_display(exp:dict, status:str):
    if status == 'experiment':
        img_name, img = load_stimuli(exp)
        upload(img_name, img)
    else:
        img_name, img = load_image(status)
        upload(img_name, img)
    return exp
