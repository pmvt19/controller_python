import pygame 
from xbox_controller_clone import XboxController
import threading
import time 

pygame.init()
joysticks = []

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

controller = XboxController(pygame)

# print(controller.get_contoller_state())
# controller.update_state()
# print(controller.get_contoller_state())

t1 = threading.Thread(target=controller.continuous_update_state)
# t1.start()

while True:
    controller.update_state()
    
    print(controller.get_contoller_state())
    time.sleep(0.5)




t1.join()