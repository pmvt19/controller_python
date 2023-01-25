import pygame 

pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

# for al the connected joysticks
# print(pygame.joystick.get_count())
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print ("Detected joystick "),joysticks[-1].get_name(),"'"

while keepPlaying:
    clock.tick(60)
    for event in pygame.event.get():
        
        event_id = event.type

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print ("A Has Been Pressed")
            elif event.button == 1:
                print ("B Has Been Pressed")
            elif event.button == 2:
                print ("X Has Been Pressed")
            elif event.button == 3:
                print ("Y Has Been Pressed")
            elif event.button == 4:
                print ("LB Has Been Pressed")
            elif event.button == 5:
                print ("RB Has Been Pressed")
            elif event.button == 6:
                print ("Back Has Been Pressed")
            elif event.button == 7:
                print ("Start Has Been Pressed")
            elif event.button == 8:
                print ("Left Thumb Has Been Pressed")
            elif event.button == 9:
                print ("Right Thumb Been Pressed")
            else:
                print ("TESTING", event.button)
        
        # if event.type == pygame.JOYAXISMOTION:
        #     if event.axis == 0:
        #         print("LJ Has Been Pressed Axis 0:", event.value) 
        #     elif event.axis == 1:
        #         print("LJ Has Been Pressed Axis 1:", event.value)  
        #     elif event.axis == 2: 
        #         print("RJ Has Been Pressed Axis 2:", event.value)   
        #     elif event.axis == 3:
        #         print("RJ Has Been Pressed Axis 3:", event.value) 
        #     elif event.axis == 4: 
        #         print("LT Has Been Pressed:", event.value)
        #     elif event.axis == 5: 
        #         print("RT Has Been Pressed:", event.value)

        if event.type == pygame.JOYHATMOTION:
            print(event.value)

        # print(event.type, pygame.event.event_name(event.type)) 

