#!/usr/bin/python

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class DCMotorController:
    
    def __init__(self, motorHat, motorNum, maxSpeed):
        self.motorHat = motorHat
        self.motorNum = motorNum
        self.motor = motorHat.getMotor(motorNum)
        self.maxSpeed = maxSpeed
        
    def stop(self):
        self.motor.run(Adafruit_MotorHAT.RELEASE)

    def run(self, percentage):
        percentage = self.clamp(-1.0, percentage, 1.0)
        motorVal = int(percentage * self.maxSpeed)
        if(motorVal == 0):
            self.stop()
        else:
            motorDir = Adafruit_MotorHAT.FORWARD if (motorVal > 0) else Adafruit_MotorHAT.BACKWARD
            self.motor.run(motorDir)
            self.motor.setSpeed(abs(motorVal))

    def clamp(self, minimum, x, maximum):
        return max(minimum, min(x, maximum))
