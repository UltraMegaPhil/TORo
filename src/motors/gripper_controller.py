#!/usr/bin/python

from dc_motor_controller import DCMotorController

class GripperController(DCMotorController):

    def __init__(self, motorHat, motorNum):
        DCMotorController.__init__(self, motorHat, motorNum, 225)
        
    def openGripper(self):
        self.run(1.0)
        
    def closeGripper(self):
        self.run(-1.0)
        

