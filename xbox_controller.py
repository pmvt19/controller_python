import pygame 

class XboxController:
    

    # Indices
    # self.LTHUMBX = 0
    # self.LTHUMBY = 1
    # self.RTHUMBX = 2
    # self.RTHUMBY = 3
    # self.LTRIGGER = 4
    # self.RTRIGGER = 5
    # self.A = 6
    # self.B = 7
    # self.X = 8
    # self.Y = 9
    # self.LBUMPER = 10
    # self.RBUMPER = 11
    # self.LJOY = 12
    # self.RJOY = 13
    # self.BACK = 14
    # self.START = 15
    # self.XBOX = 16
    # self.DPAD = 17

    class XboxControls():
        LTHUMBX = 0
        LTHUMBY = 1
        RTHUMBX = 2
        RTHUMBY = 3
        LTRIGGER = 4
        RTRIGGER = 5
        A = 6
        B = 7
        X = 8
        Y = 9
        LBUMPER = 10
        RBUMPER = 11
        LJOY = 12
        RJOY = 13
        BACK = 14
        START = 15
        XBOX = 16
        DPAD = 17

    class PyGameAxis():
        LTHUMBX = 0
        LTHUMBY = 1
        RTHUMBX = 2
        RTHUMBY = 3
        RTRIGGER = 4
        LTRIGGER = 5

    class PyGameButtons():
        A = 0
        B = 1
        X = 2
        Y = 3
        LBUMPER = 4
        RBUMPER = 5
        BACK = 6
        START = 7
        XBOX = 8
        LJOY = 9
        RJOY = 10

    # AXISCONTROLMAP = {PyGameAxis.LTHUMBX: XboxControls.LTHUMBX,
    #                 PyGameAxis.LTHUMBY: XboxControls.LTHUMBY,
    #                 PyGameAxis.RTHUMBX: XboxControls.RTHUMBX,
    #                 PyGameAxis.RTHUMBY: XboxControls.RTHUMBY}

    AXISCONTROLMAP = {PyGameAxis.LTHUMBX: XboxControls.LTHUMBX,
                    PyGameAxis.LTHUMBY: XboxControls.LTHUMBY,
                    PyGameAxis.RTHUMBX: XboxControls.RTHUMBX,
                    PyGameAxis.RTHUMBY: XboxControls.RTHUMBY, 
                    PyGameAxis.RTRIGGER: XboxControls.RTRIGGER,
                    PyGameAxis.LTRIGGER: XboxControls.LTRIGGER}

    # TRIGGERCONTROLMAP = {PyGameAxis.RTRIGGER: XboxControls.RTRIGGER,
    #                     PyGameAxis.LTRIGGER: XboxControls.LTRIGGER}

    BUTTONCONTROLMAP = {PyGameButtons.A: XboxControls.A,
                        PyGameButtons.B: XboxControls.B,
                        PyGameButtons.X: XboxControls.X,
                        PyGameButtons.Y: XboxControls.Y,
                        PyGameButtons.LBUMPER: XboxControls.LBUMPER,
                        PyGameButtons.RBUMPER: XboxControls.RBUMPER,
                        PyGameButtons.BACK: XboxControls.BACK,
                        PyGameButtons.START: XboxControls.START,
                        PyGameButtons.XBOX: XboxControls.XBOX,
                        PyGameButtons.LJOY: XboxControls.LJOY,
                        PyGameButtons.RJOY: XboxControls.RJOY}
    def __init__(self, my_game):

        self.game = my_game

        # LTHUMBX, LTHUMBY, RTHUMBX, RTHUMBY, LTRIGGER, RTRIGGER, A, B, X, Y, LBUMPER, RBUMPER, LJOY, RJOY, BACK, START, XBOX, DPAD
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (0, 0)]



    def get_contoller_state(self):
        return self.state 


    def update_state(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                pressed_button = event.button 
                state_ind = self.BUTTONCONTROLMAP[pressed_button]
                self.state[state_ind] = 1 
            
            if event.type == pygame.JOYBUTTONUP:
                pressed_button = event.button 
                state_ind = self.BUTTONCONTROLMAP[pressed_button]
                self.state[state_ind] = 0

            if event.type == pygame.JOYHATMOTION:
                self.state[self.XboxControls.DPAD] = event.value

            if event.type == pygame.JOYAXISMOTION:
                moved_axis = event.axis
                state_ind = self.AXISCONTROLMAP[moved_axis]
                self.state[state_ind] = event.value 
        return 