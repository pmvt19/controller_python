import cv2
import numpy as np
import pygame 
from xbox_controller_clone import XboxController
import threading
import time


pygame.init()
joysticks = []

BAR_HEIGHT = 240

BAR_HEIGHT_JOY = 360

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

controller = XboxController(pygame)

FRAME_WIDTH = 480

base_frame = np.zeros((640, FRAME_WIDTH, 3))

trigger_marker = np.ones((BAR_HEIGHT, 40, 3)) * np.array([255, 0, 128])

joy_marker = np.ones((40, BAR_HEIGHT_JOY, 3)) * np.array([35, 148, 247])

while True:
    frame = base_frame.copy()

    controller.update_state()
    time.sleep(0.1)

    state = controller.get_contoller_state()

    if state[XboxController.XboxControls.A] == 1:
        frame[:120, :120, :] = [0, 255, 0]
    
    if state[XboxController.XboxControls.B] == 1:
        frame[:120, 120:240, :] = [0, 0, 255]

    if state[XboxController.XboxControls.X] == 1:
        frame[:120, 240:360, :] = [255, 0, 0]

    if state[XboxController.XboxControls.Y] == 1:
        frame[:120, 360:, :] = [0, 247, 255]
    # print(state[XboxController.XboxControls.RTRIGGER])
    
    r_val = BAR_HEIGHT - int((state[XboxController.XboxControls.RTRIGGER] + 1) * BAR_HEIGHT * 0.5)
    right_trigger_marker = np.zeros((BAR_HEIGHT, 40, 3)) + trigger_marker[:, :, :]
    right_trigger_marker[:r_val, :, :] = 0
    # print(r_val)
    frame[-(BAR_HEIGHT+1):-1, -40:, :] = right_trigger_marker


    l_val = BAR_HEIGHT - int((state[XboxController.XboxControls.LTRIGGER] + 1) * BAR_HEIGHT * 0.5)
    left_trigger_marker = np.zeros((BAR_HEIGHT, 40, 3)) + trigger_marker[:, :, :]
    left_trigger_marker[:l_val, :, :] = 0
    # print(l_val)
    frame[-(BAR_HEIGHT+1):-1, :40, :] = left_trigger_marker


    print(state)


    l_joy = int(state[XboxController.XboxControls.LTHUMBX] * BAR_HEIGHT_JOY)
    left_thumbx_marker = np.zeros((40, BAR_HEIGHT_JOY, 3)) + joy_marker[:, :, :]
    if l_joy > 0:
        left_thumbx_marker[:, :(BAR_HEIGHT_JOY//2), :] = 0 
        left_thumbx_marker[:, l_joy:] = 0 
    else:
        left_thumbx_marker[:, (BAR_HEIGHT_JOY//2):, :] = 0  
        left_thumbx_marker[:, :l_joy] = 0 

    

    lbound = (FRAME_WIDTH // 2) - (BAR_HEIGHT_JOY // 2)
    rbound = (FRAME_WIDTH // 2) + (BAR_HEIGHT_JOY // 2)
    # print(lbound, rbound)

    frame[250:290, lbound:rbound, :] = left_thumbx_marker
    


    cv2.imshow('frame', frame)



    if cv2.waitKey(1) == ord('q'):
        break 

