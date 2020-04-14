from numpy import interp
from time import sleep
import pigpio
import math


import os
import signal
import sys

import numpy as np

class Train:

    def __init__(self):
        pass

    def signal_handler(self, sig, frame):

        print('[INFO] : You have pressed ctrl + c. exiting in tracker!')
        sys.stdout.flush()
        self.trainer_status = False
        # os.system('sudo killall pigpiod')
        sys.exit()


    def record(self, imu_lin_x, imu_lin_y, imu_ang_z, record):

        empty_array = np.empty(shape=(0,3), dtype=np.float64)

        while record:

            new_array = np.array([imu_lin_x, imu_lin_y, imu_ang_z])
            empty_array = np.concatenate(empty_array, new_array)

        np.save('/home/pi/roco_desk1/src/saved_models/path.npy' , empty_array )
