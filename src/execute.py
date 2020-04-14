from numpy import interp
from time import sleep
import pigpio
import math


import os
import signal
import sys

import numpy as np

class Track:

    def __init__(self):
        pass

    def signal_handler(self, sig, frame):

        print('[INFO] : You have pressed ctrl + c. exiting in tracker!')
        sys.stdout.flush()
        self.tracker_status = False
        # os.system('sudo killall pigpiod')
        sys.exit()

    def track(self, imu_lin_x, imu_lin_y, imu_ang_z):
        path = '/home/pi/roco_desk1/src/saved_models/path.npy'
        path_array = np.load(path)

        for i in path_array:

            imu_lin_x = i[0]
            imu_lin_y = i[1]
            imu_ang_z = i[2]

