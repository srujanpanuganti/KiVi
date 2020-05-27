# from multiprocessing import Manager
# from multiprocessing import Process, Value
#
# from .ui import UI
#
# import time
# import os
# import sys
# import signal
# os.system('sudo modprobe bcm2835-v4l2')
# os.system('sudo pigpiod')
# from .move import Motors
# from .move import Move
# from .execute import Track
# from .train import Train
#
#
# if __name__ == "__main__":
#
#     ui = UI()
#     train_sw = ui.train_switch
#     run_sw = ui.execute_switch
#     dev_pb = ui.dev_push_button
#
#     motors = Motors()
#     motors.start_peripherals()
#
#     print('[INFO]:[main] : peripherals attached')
#
#     while True:
#
#         developer_mode = False
#         st_time = time.time()
#         while (dev_pb.is_held):
#             e_time = time.time()
#             # print((e_time-st_time))
#             if (e_time-st_time) >= 8:
#                 developer_mode = True
#                 print('[INFO]:[main] : Entering developer mode')
#                 sys.stdout.flush()
#             else:
#                 developer_mode = False
#
#         if developer_mode == True:
#             sys.exit()
#
#
#         while train_sw and not run_sw:
#             print("[INFO]:[main] : now training: ")
#
#             with Manager() as manager:
#
#                 record = Value('i',0)
#                 imu_lin_x = Value('d',0)
#                 imu_lin_y = Value('d',0)
#                 imu_ang_z = Value('d',0)
#
#                 motion = Move(motors, ui)
#
#                 print('[INFO]:[main] : motion initialized')
#                 sys.stdout.flush()
#
#                 # imu_lin_x = 0
#                 # imu_lin_y = 0
#                 # imu_ang_z = 0
#
#                 trainer = Train()
#
#                 process_imu = Process(target=trainer.record,args= (imu_lin_x, imu_lin_y, imu_ang_z))
#                 process_move = Process(target=motion.train,args= (imu_lin_x, imu_lin_y, imu_ang_z))
#
#                 process_imu.start()
#                 process_move.start()
#
#                 process_imu.join()
#                 process_move.join()
#
#
#         while run_sw and not train_sw:
#             print("[INFO]:[main] : now executing: ")
#
#             with Manager() as manager:
#
#                 motion = Move(motors, ui)
#
#                 print('[INFO]:[main] : motion initialized')
#                 sys.stdout.flush()
#
#                 imu_lin_x = Value('d',0)
#                 imu_lin_y = Value('d',0)
#                 imu_ang_z = Value('d',0)
#
#                 tracker = Track()
#
#                 process_imu = Process(target=tracker.track,args= (imu_lin_x, imu_lin_y, imu_ang_z))
#                 process_move = Process(target=motion.update,args= (imu_lin_x, imu_lin_y, imu_ang_z))
#                 process_pid = Process(target=motion.update,args= (imu_lin_x, imu_lin_y, imu_ang_z))
#
#                 process_imu.start()
#                 process_move.start()
#                 process_pid.start()
#
#                 process_imu.join()
#                 process_move.join()
#                 process_pid.join()
#



import time
import os
import sys
# import cv2
# import gripper
# from .sonar import Sonar
import imutils
from move import Motors
from move import Motion
# import IMU as imu
import RPi.GPIO as gpio
# from picamera.array import PiRGBArray
# from picamera import PiCamera


#trig= 16
#echo = 18

# mygripper = gripper.gripper()
# drive.init_pins()
#sodar.init_spins()
#gpio.setmode(gpio.BOARD)
#gpio.setup(trig, gpio.OUT)
#gpio.setup(echo, gpio.IN)
# camera = PiCamera()
# camera.resolution = (640,480)
# camera.framerate = 60
# rawCapture = PiRGBArray(camera , size = (640,480))
# time.sleep(0.1)

# define HSV mask for Blu
# lower_B = (160, 25 , 0)
# upper_B = (180,255,255)
# def distance():
#
#     trig= 16
#     echo = 18
#
#     #Ensure output has novalue
#     gpio.output(trig, False)
#     time.sleep(0.010)
#     gpio.setmode(gpio.BOARD)
#     gpio.setup(trig, gpio.OUT)
#     gpio.setup(echo, gpio.IN)
#
#     #Generate the trigger pulse
#     gpio.output(trig, True)
#     time.sleep(0.00001)
#     gpio.output(trig,False)
#
#     #Generate Echo time signal
#     while gpio.input(echo) ==0:
#         pulse_start = time.time()
#
#     while gpio.input(echo) == 1:
#         pulse_end = time.time()
#
#     pulse_duration = pulse_end - pulse_start
#
#     # Convert time to Distance
#     distance = pulse_duration*17150
#     distance = round(distance, 2)
#
#     # Clean up GPIO and return the distance
#     #gpio.cleanup()
#
#     return distance

# mygripper.grip(7)
# time.sleep(1)



motors = Motors()
move = Motion(motors)

# motors.init()

# for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=False):
#     img = frame.array
#     time.sleep(0.1)
#     img=cv2.flip(img,0)
#     img=cv2.flip(img,1)
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv , lower_B, upper_B)
#     cnt = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#     cnt = imutils.grab_contours(cnt)
#
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     coord = (50,50)
#     fontscale = 0.5
#     color =(255,255,255)
#     thickness = 1
#
#     if len(cnt)>0:
#         cn = max(cnt, key= cv2.contourArea)
#         ((x,y),radius) = cv2.minEnclosingCircle(cn)
#
#         M = cv2.moments(cn)
#         if(M["m00"] > 0):
#             x = int(M["m10"] / M["m00"])
#             y = int(M["m01"] / M["m00"])
#         contoured= cv2.circle(img, (x,y), int(radius) ,(0,0,255),3)
#         contoured= cv2.circle(contoured, (x,y), 1,(0,0,255),2)
#         cv2.putText(contoured,'('+str(x)+','+str(y)+')',coord,font,fontscale,color,thickness,cv2.LINE_AA)
#         c=cv2.line(contoured,(320,200),(320,280),(0,0,0),1)
#         c=cv2.line(c,(280,240),(360,240),(0,0,0),1)
#         cv2.imshow("cont",c)
#         key = cv2.waitKey(1) & 0xFF
#     else:
#         contoured = img
#         cv2.imshow(contoured)
#
#         cv2.waitKey(0)
#     rawCapture.truncate(0)
#


while True:

    print('[INFO][main]: inside while ')
    move.forward(500)

    print('[INFO][main]: After forward ')

    # if x>=345:
    #     angle = (x-320)*0.061
    #     imu.right(angle)
    #
    # elif x<=295:
    #     angle = (320-x)*0.061
    #     imu.left(angle)
    # elif 305<x  and x<335:
    #     continue
        #
        # objectReahced= False
        # while not objectReahced:
        #     imu.forward(0.1)
        #     print('Gettinf dius5t')
        #     dist = distance()
        #     print(dist)
        #     if dist<= 10:
        #         objectReahced= True
        # mygripper.grip(4)


        # While objecReached:
            # Go Forward 10 cms
            # Check the distance to the object 10  less than 10 cm/ 7 cms, You check the distance using UltraSonic

            # Then make objecReached = True
        # Now Pickup the object by activating the Grippers

#    if x>=320:
#        angle = (x-320)*0.061
#        imu.right(angle)

#    else:
#        angle = (320-x)*0.061
#        imu.left(angle)
#     if key == ord("q"):
#         break

    time.sleep(5)

    move.reverse(500)
    print('[INFO][main]: After reverse ')

    time.sleep(5)

    move.left(50)   ## We basically give the angle how much it should turn
    print('[INFO][main]: After left ')

    time.sleep(5)

    move.right(10)  ## We basically give the angle how much it should turn#
    # print('[INFO][main]: After right ')

    time.sleep(5)


    break


motors.gameover()
gpio.cleanup()
