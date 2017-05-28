#!/usr/bin/python

from gripper_controller import GripperController
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time

                ####################
                # TEST HARNESS APP #
                ####################
                
motorHatAddress = 0x60     
motorHat = Adafruit_MotorHAT(addr=motorHatAddress)
gripper = GripperController(motorHat, 4)

print("OPENING....")
gripper.openGripper()
time.sleep(2)

print("CLOSING...")
gripper.closeGripper()
time.sleep(2)

gripper.stop()

