from numpy import interp
from time import sleep
import pigpio
import math
import os
import signal
import sys

from ui import UI

class Motors:

    def __init__(self):

        ## Initializing the GPIO 12 as direction and 5 as PWM to DC Motor
        # self.servo_pin = 17
        self.motor_fL_PWM = 31
        self.motor_fL_DIR = 12

        self.motor_fR_PWM = 33
        self.motor_fR_DIR = 13

        self.motor_rL_PWM = 35
        self.motor_rL_DIR = 14

        self.motor_rR_PWM = 37
        self.motor_rR_DIR = 15

        # self.MIN_DUTY = 1000
        # self.MAX_DUTY = 2000
        # self.CENTER_DUTY = 1500

        self.pi = pigpio.pi()
        self.speed_factor  = 3


        if not self.pi.connected:
           print('[ERROR] : pi not connected')
           sys.stdout.flush()
           exit()

    def start_peripherals(self):

        # self.pi.set_mode(self.servo_pin, pigpio.OUTPUT)
        # self.pi.set_servo_pulsewidth(self.servo_pin, self.CENTER_DUTY)

        self.pi.set_mode(self.motor_fL_PWM, pigpio.OUTPUT)
        self.pi.set_mode(self.motor_fR_PWM, pigpio.OUTPUT)
        self.pi.set_mode(self.motor_rL_PWM, pigpio.OUTPUT)
        self.pi.set_mode(self.motor_rR_PWM, pigpio.OUTPUT)


    def halt_dc_motro(self):
        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

    def stop_peripherals(self):
        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

        self.pi.stop()
        os.system('sudo killall pigpiod')

    def forward(self, input):

        self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rR_DIR, 0)  ## initially 0

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))

        sleep(input)

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

    def reverse(self, input):

        self.pi.write(self.motor_fL_DIR, 1)  ## initially 0
        self.pi.write(self.motor_fR_DIR, 1)  ## initially 0
        self.pi.write(self.motor_rL_DIR, 1)  ## initially 0
        self.pi.write(self.motor_rR_DIR, 1)  ## initially 0

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))

        sleep(input)

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

    def right(self, input):

        self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rR_DIR, 0)  ## initially 0

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

        sleep(input)

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)

    def left(self, input):

        self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
        self.pi.write(self.motor_rR_DIR, 0)  ## initially 0

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))

        sleep(input)

        self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
        self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)


class Move:

    def __init__(self, motors: Motors, ui : UI):
        pass

    def update(self):
        pass
        # Whatever we read in the Track.track, those imu values will be translated ot the motor commands


    def train(self):
        pass
        # I'll write script to translate some information to motor commands




