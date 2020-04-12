from multiprocessing import Manager
from multiprocessing import Process, Value

from ui import UI

import time
import os
import sys
import signal
os.system('sudo modprobe bcm2835-v4l2')
os.system('sudo pigpiod')
from move import Motors
from move import Move
from execute import Track
from train import Train


if __name__ == "__main__":

    ui = UI()
    train_sw = ui.train_switch
    run_sw = ui.execute_switch
    dev_pb = ui.dev_push_button

    motors = Motors()
    motors.start_peripherals()

    print('[INFO]:[main] : peripherals attached')

    while True:

        developer_mode = False
        st_time = time.time()
        while (dev_pb.is_held):
            e_time = time.time()
            # print((e_time-st_time))
            if (e_time-st_time) >= 8:
                developer_mode = True
                print('[INFO]:[main] : Entering developer mode')
                sys.stdout.flush()
            else:
                developer_mode = False

        if developer_mode == True:
            sys.exit()


        while train_sw and not run_sw:
            print("[INFO]:[main] : now training: ")

            with Manager() as manager:

                record = Value('i',0)
                imu_lin_x = Value('i',0)
                imu_lin_y = Value('i',0)
                imu_ang_z = Value('i',0)

                motion = Move(motors, ui)

                print('[INFO]:[main] : motion initialized')
                sys.stdout.flush()

                # imu_lin_x = 0
                # imu_lin_y = 0
                # imu_ang_z = 0

                trainer = Train()

                process_imu = Process(target=trainer.record,args= (imu_lin_x, imu_lin_y, imu_ang_z))
                process_move = Process(target=motion.train,args= (imu_lin_x, imu_lin_y, imu_ang_z))

                process_imu.start()
                process_move.start()

                process_imu.join()
                process_move.join()


        while run_sw and not train_sw:
            print("[INFO]:[main] : now executing: ")

            with Manager() as manager:

                motion = Move(motors, ui)

                print('[INFO]:[main] : motion initialized')
                sys.stdout.flush()

                imu_lin_x = Value('i',0)
                imu_lin_y = Value('i',0)
                imu_ang_z = Value('i',0)

                tracker = Track()

                process_imu = Process(target=tracker.track,args= (imu_lin_x, imu_lin_y, imu_ang_z))
                process_move = Process(target=motion.update,args= (imu_lin_x, imu_lin_y, imu_ang_z))
                process_pid = Process(target=motion.update,args= (imu_lin_x, imu_lin_y, imu_ang_z))

                process_imu.start()
                process_move.start()
                process_pid.start()

                process_imu.join()
                process_move.join()
                process_pid.join()

