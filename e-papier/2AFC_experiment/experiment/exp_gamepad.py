#!/usr/bin/env python
"""
Make an experiment sequence, run by gamepad.

@authors: Ji Hyea Park
"""

import pygame
from img_loader import set_display, show_blank, control_stim
from sys import exit

WHITE = (255, 255, 255)
BLACK = (0,0,0)

def export_value(exp:dict, res:list, brighter:str, resp_time):
    exp['isBrighter'] = brighter
    exp['resp_time'] = resp_time
    res.append(exp)
    return '%s_%s_P%s: %s side is brighter' % (exp['stim_name'], exp['target_bg'], exp['l_probe'], exp['isBrighter'])

def set_message(font, msg:str):
    text_surface = font.render(msg, True, BLACK, None)
    return text_surface

def exp_control(exp_designs:list, results:list):
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Experiment')
    running = True
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    count = 0
    block_change = False
    status = 'start'
    brighter = ''

    msg = 'welcome!'

    block_id = 0
    exp_id = 0
    block = exp_designs[block_id]
    exp_design = block[exp_id]
    
    stim_control = False

    font = pygame.font.Font(None, 32)
    
    set_display(exp_design, status)
    start_time = None
    pygame.event.clear()
    
    while running:
        '''
        Key references
            a: 0 (down)
            b: 1 (right)
            x: 2 (left)
            y: 3 (up)

            left_trigger: 4 (space)
            right_trigger: 5 (enter)
        '''
        for event in pygame.event.get():

            event = pygame.event.wait()

            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")
            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 5:
                    if status == 'experiment':
                        brighter = 'RIGHT'
                        end_time = pygame.time.get_ticks()
                        resp_time = (end_time - start_time) / 1000
                        msg = str(count) + '. ' + export_value(exp_design, results[block_id], brighter, resp_time)
                        print(msg)
                        if count > len(block)-1: 
                            if not block_change:
                                status = 'pause'
                                print('pause')
                            else:
                                status = 'exit'
                                print('exit')
                        else:
                            if count == len(block)//2:
                                status = 'half'
                                print('half')
                            count += 1
                            if exp_id < len(block)-1:
                                exp_id += 1
                                exp_design = block[exp_id]
                                msg = 'Change stimuli: %s_%s_P%s' % (exp_design['stim_name'], exp_design['target_bg'], exp_design['l_probe'])
                                print(msg)
                    elif status == 'half':
                        status = 'experiment'
                    elif status == 'start':
                            msg = 'Start experiment: %s_%s_P%s' % (exp_design['stim_name'], exp_design['target_bg'], exp_design['l_probe'])
                            print(msg)
                            status = 'experiment'
                            count += 1
                    elif status == 'pause':
                            block_id += 1
                            exp_id = 0
                            block = exp_designs[block_id]
                            exp_design = block[exp_id]
                            msg = 'switch stimuli type and start experiment: %s_%s_P%s' % (exp_design['stim_name'], exp_design['target_bg'], exp_design['l_probe'])
                            print(msg)
                            block_change = True
                            count = 1
                            status = 'experiment'
                if event.button == 4:
                    print('left')
                    if status == 'experiment':
                        brighter = 'LEFT'
                        end_time = pygame.time.get_ticks()
                        resp_time = (end_time - start_time) / 1000
                        msg = str(count) + '. ' + export_value(exp_design, results[block_id], brighter, resp_time)
                        print(msg)
                        if count > len(block)-1: 
                            if not block_change:
                                status = 'pause'
                                print('pause')
                            else:
                                status = 'exit'
                                print('exit')
                        else:
                            if count == len(block)//2:
                                status = 'half'
                                print('half')
                            count += 1
                            if exp_id < len(block)-1:
                                exp_id += 1
                                exp_design = block[exp_id]
                                msg = 'Change stimuli: %s_%s_P%s' % (exp_design['stim_name'], exp_design['target_bg'], exp_design['l_probe'])
                                print(msg)
                    elif status == 'pause':
                        block_id += 1
                        exp_id = 0
                        block = exp_designs[block_id]
                        exp_design = block[exp_id]
                        msg = 'switch stimuli type and start experiment: %s_%s_P%s' % (exp_design['stim_name'], exp_design['target_bg'], exp_design['l_probe'])
                        print(msg)
                        block_change = True
                        count = 1
                        status = 'experiment'
                    elif status == 'exit':
                        status = 'thanks'
                        running = False
                        for joy in joysticks:
                            joy.quit()
                if event.button == 0:
                    # button a
                    print('A')
                    stim_control = not stim_control
                    show_blank()
                    control_stim('sbc')
                if event.button == 1:
                    # button b
                    print('B')
                    stim_control = not stim_control
                    show_blank()
                    control_stim('white')

                screen.fill(WHITE)
                status_surface = set_message(font, status)
                screen.blit(status_surface, (100, 100))

                text_surface = set_message(font, msg)
                screen.blit(text_surface, (100, 300))

                if not stim_control:
                    show_blank()
                    set_display(exp_design, status)
                    start_time = pygame.time.get_ticks()

    pygame.quit()

    return results
