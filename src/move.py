# from numpy import interp
# from time import sleep
# import pigpio
# import math
# import os
# import signal
# import sys
#
# from .ui import UI
#
# class Motors:
#
#     def __init__(self):
#
#         ## Initializing the GPIO 12 as direction and 5 as PWM to DC Motor
#         # self.servo_pin = 17
#         self.motor_fL_PWM = 31
#         self.motor_fL_DIR = 12
#
#         self.motor_fR_PWM = 33a
#         self.motor_fR_DIR = 13
#
#         self.motor_rL_PWM = 35
#         self.motor_rL_DIR = 14
#
#         self.motor_rR_PWM = 37
#         self.motor_rR_DIR = 15
#
#         # self.MIN_DUTY = 1000
#         # self.MAX_DUTY = 2000
#         # self.CENTER_DUTY = 1500
#
#         self.pi = pigpio.pi()
#         self.speed_factor  = 3
#
#         if not self.pi.connected:
#            print('[ERROR] : pi not connected')
#            sys.stdout.flush()
#            exit()
#
#     def start_peripherals(self):
#
#         # self.pi.set_mode(self.servo_pin, pigpio.OUTPUT)
#         # self.pi.set_servo_pulsewidth(self.servo_pin, self.CENTER_DUTY)
#
#         self.pi.set_mode(self.motor_fL_PWM, pigpio.OUTPUT)
#         self.pi.set_mode(self.motor_fR_PWM, pigpio.OUTPUT)
#         self.pi.set_mode(self.motor_rL_PWM, pigpio.OUTPUT)
#         self.pi.set_mode(self.motor_rR_PWM, pigpio.OUTPUT)
#
#
#     def halt_dc_motro(self):
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#     def stop_peripherals(self):
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#         self.pi.stop()
#         os.system('sudo killall pigpiod')
#
#     def forward(self, input):
#
#         self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rR_DIR, 0)  ## initially 0
#
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))
#
#         sleep(input)
#         self.halt_dc_motro()
#
#         # self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#
#     def reverse(self, input):
#
#         self.pi.write(self.motor_fL_DIR, 1)  ## initially 0
#         self.pi.write(self.motor_fR_DIR, 1)  ## initially 0
#         self.pi.write(self.motor_rL_DIR, 1)  ## initially 0
#         self.pi.write(self.motor_rR_DIR, 1)  ## initially 0
#
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))
#
#         sleep(input)
#         self.halt_dc_motro()
#
#         # self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#     def right(self, input):
#
#         self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rR_DIR, 0)  ## initially 0
#
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#         sleep(input)
#         self.halt_dc_motro()
#
#         # self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#     def left(self, input):
#
#         self.pi.write(self.motor_fL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_fR_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rL_DIR, 0)  ## initially 0
#         self.pi.write(self.motor_rR_DIR, 0)  ## initially 0
#
#         self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_fR_PWM, int(255 / self.speed_factor))
#         self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         self.pi.set_PWM_dutycycle(self.motor_rR_PWM, int(255 / self.speed_factor))
#
#         sleep(input)
#         self.halt_dc_motro()
#
#         # self.pi.set_PWM_dutycycle(self.motor_fL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_fR_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rL_PWM, 0)
#         # self.pi.set_PWM_dutycycle(self.motor_rR_PWM, 0)
#
#
# class Move:
#
#     def __init__(self, motors: Motors, ui : UI):
#         self.motors = motors
#         # pass
#
#     def signal_handler(self, sig, frame):
#
#         print('[INFO] : You have pressed ctrl + c. exiting in motion!')
#         sys.stdout.flush()
#         # self.motion_status = False
#         self.motors.stop_peripherals()
#         # os.system('sudo killall pigpiod')
#         sys.exit()
#
#
#     def update(self):
#         pass
#         # Whatever we read in the Track.track, those imu values will be translated ot the motor commands
#
#
#     def train(self):
#         pass
#         # I'll write script to translate some information to motor commands
#
#
#     def key_input(self, event):
#         # init_pins()
#         print("Key: " ,event)
#         key_press = event
#         tf=1
#         if key_press.lower() == 'w':
#             self.motors.forward(tf)
#         elif key_press.lower() == 's':
#             self.motors.reverse(tf)
#         elif key_press.lower() == 'a':
#             self.motors.left(tf)
#         elif key_press.lower() == 'd':
#             self.motors.right(tf)
#         else:
#             print("Invalid")
#             #gameover()
#             #gpio.cleanup()
#
#
#
# front_end = UI()
# driver = Motors()
# motion = Move( driver, front_end)
#
# while True:
#     sleep(1)
#     # print('Distance:',distance(),"cm")
#     key_press = input('Select Driving mode:')
#     if key_press == 'p':
#         break
#     motion.key_input(key_press)

import RPi.GPIO as gpio
import time
import numpy as np
import math
import serial


class Motors:

	def init(self):
		gpio.setmode(gpio.BOARD)
		gpio.setup(31, gpio.OUT)
		gpio.setup(33, gpio.OUT)
		gpio.setup(35, gpio.OUT)
		gpio.setup(37, gpio.OUT)

		gpio.setup(7, gpio.IN, pull_up_down= gpio.PUD_UP)
		gpio.setup(12, gpio.IN, pull_up_down= gpio.PUD_UP)

	def gameover(self):
		gpio.output(31, False)
		gpio.output(33, False)
		gpio.output(35, False)
		gpio.output(37, False)

		#gpio.cleanup()



class Motion:

	def __init__(self, motors : Motors):

		self.motors = motors
		self.file1 = open("imu_drive.txt","a")
	#file1 = open("Encoder_data_3.txt","a")


	def forward(self, ticks):

		print('[INFO][Motion][forward]: inside forward ')

		self.motors.init()

		counterBR = np.uint64(0)
		counterFL = np.uint64(0)

		buttonBR = int(0)
		buttonFL = int(0)

		# Initialize pwm signal to control motor
		pwm1 = gpio.PWM(31,50)
		pwm2 = gpio.PWM(37,50)
		val = 80
		pwm1.start(val)
		pwm2.start(val)
		time.sleep(0.1)

		for i in range (0,10000000):
			print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
			#file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n"k)
			if int(gpio.input(12) != int(buttonBR)):
				buttonBR = int(gpio.input(12))
				counterBR += 1

			if int(gpio.input(7) != int(buttonFL)):
				buttonFL = int(gpio.input(7))
				counterFL = counterFL+1

			error = counterFL-counterBR
			counterBR += error
			if counterFL >= ticks:
				pwm1.stop()

			if counterBR >= ticks:
				pwm2.stop()


			if counterBR >=ticks and counterFL >= ticks :
				self.motors.gameover()
				print("Thanks for Playing")
				avg = float(counterBR+counterFL)/2

				dist = 100*avg/97
				dist = int(dist)
				self.file1.write(str(dist)+"\n")
				break

	def reverse(self,ticks):

		print('[INFO][Motion][reverse]: inside reverse ')

		self.motors.init()

		counterBR = np.uint64(0)
		counterFL = np.uint64(0)

		buttonBR = int(0)
		buttonFL = int(0)

		# Initialize pwm signal to control motor
		pwm1 = gpio.PWM(33,50)
		pwm2 = gpio.PWM(35,50)
		val = 60
		pwm1.start(val)
		pwm2.start(val)
		time.sleep(0.1)

		for i in range (0,10000000):
			print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
			#file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")

			if int(gpio.input(12) != int(buttonBR)):
				buttonBR = int(gpio.input(12))
				counterBR += 1

			if int(gpio.input(7) != int(buttonFL)):
				buttonFL = int(gpio.input(7))
				counterFL = counterFL+1

			error = counterFL-counterBR
			counterBR += error
			if counterFL >= ticks:
				pwm1.stop()

			if counterBR >= ticks:
				pwm2.stop()


			if counterBR >=ticks and counterFL >= ticks :
				self.motors.gameover()
				print("Thanks for Playing")
				#file1.close()
				break

	def left(self,rot):

		print('[INFO][Motion][left]: inside left ')

		self.motors.init()
		ticks= rot*5.85

		counterBR = np.uint64(0)
		counterFL = np.uint64(0)

		buttonBR = int(0)
		buttonFL = int(0)

		# Initialize pwm signal to control motor
		pwm1 = gpio.PWM(33,50)
		pwm2 = gpio.PWM(37,50)
		val = 95
	#	time.sleep(0.1)
		count =0
		flag = 0
		ser = serial.Serial('/dev/ttyUSB0', 9600)
		while True:
			if (ser.in_waiting >0):
				count +=1

				line = ser.readline()
				if count > 10:
					if flag ==0:
						pwm2.start(val)
						#time.sleep(0.01)
						pwm1.start(val)
						flag =1
					line = line.rstrip().lstrip()
					line = str(line)
					line = line.strip("'")
					line = line.strip("b'")

					line = line[2:9]
					angle = float(line)
					diff = 360 - angle
					print("Angle = ",angle,"counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
					#file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n")
					#angle = getimu()
					#diff = int(360-angle)
					if int(gpio.input(12) != int(buttonBR)):
						buttonBR = int(gpio.input(12))
						counterBR += 1

					if int(gpio.input(7) != int(buttonFL)):
						buttonFL = int(gpio.input(7))
						counterFL = counterFL+1

					error = counterFL-counterBR
					counterBR += error
					if  counterFL >= ticks or (diff>=rot-3 and diff<=rot+3) :
						pwm1.stop()

					if  counterBR >= ticks or (diff>=rot-3 and diff<=rot+3):
						pwm2.stop()


					if (counterBR >=ticks and counterFL >= ticks) or (diff>=rot-3 and diff<=rot+3):
						self.motors.gameover()
						avg = float(counterBR+counterFL)/2
						a = int(avg/0.25)
						self.file1.write(str(diff)+"\n")
						print("Thanks for Playing")
						#file1.close()
						break

	def right(self,rot):

		print('[INFO][Motion][right]: inside right ')

		self.motors.init()
		ticks= rot*5.85

		counterBR = np.uint64(0)
		counterFL = np.uint64(0)

		buttonBR = int(0)
		buttonFL = int(0)

		# Initialize pwm signal to control motor
		pwm1 = gpio.PWM(31,50)
		pwm2 = gpio.PWM(35,50)
		val = 95
	#	pwm1.start(val)
	#	pwm2.start(val)
		time.sleep(0.1)
		count =0
		flag =0
		ser = serial.Serial('/dev/ttyUSB0', 9600)
		while True:
			if (ser.in_waiting >0):
				count +=1

				line = ser.readline()
				if count > 10:


					if flag ==0:
						pwm1.start(val)
						pwm2.start(val)
						flag =1
					line = line.rstrip().lstrip()
					line = str(line)
					line = line.strip("'")
					line = line.strip("b'")
					line= line[2:9]
					diff = float(line)



					print("Angle = ",diff,"counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
					#print("counterBR = ",counterBR,"counterFL = ",counterFL,"BR state: ", gpio.input(12),"FL state: ", gpio.input(7))
					#file1.write(str(gpio.input(12))+str(gpio.input(7))+"\n"))
					#diff = getimu()
				#	diff = 360-angle
					if int(gpio.input(12) != int(buttonBR)):
						buttonBR = int(gpio.input(12))
						counterBR += 1

					if int(gpio.input(7) != int(buttonFL)):
						buttonFL = int(gpio.input(7))
						counterFL = counterFL+1

					error = counterFL-counterBR
					counterBR += error
					if counterFL >= ticks or diff >= rot:
						pwm1.stop()
						pwm2.stop()
					#if counterBR >= ticks or diff >= rot:
						#pwm2.stop()


					#if (counterBR >=ticks and counterFL >= ticks) or diff >= rot :
						#gameover()
						#print("Thanks for Playing")
						#file1.close()
						break

	def key_input(self,event):
		self.motors.init()
		print("Key: " ,event)
		key_press = event
	#	tf=1
		if key_press.lower() == 'w':
			x = input('Enter distance in Meters:')
			x = float(x)
			ticks= (1/(3.14*2*0.0325))*x*960
			self.forward(ticks)
		elif key_press.lower() == 's':
			x = input('Enter distance in Meters:')
			x = float(x)
			ticks= (1/(3.14*2*0.0325))*x*960
			self.reverse(ticks)
		elif key_press.lower() == 'a':
			x = input('Enter Angle in degrees:')
			x = int(x)
		#	ticks = int(ticks)
			self.left(x)
		elif key_press.lower() == 'd':
			x = input('Enter Angle in degrees:')
			x = float(x)
			#ticks= x*0.25
			self.right(x)
		else:
			print("Invalid")
			#gameover()
			#gpio.cleanup()

	def getimu(self):

		ser = serial.Serial('/dev/ttyUSB0',9600)
		count = 0
		while True:
			if(ser.in_waiting>0):
				count+=1
				# Read Serial Stream
				line = ser.readline()

				# Avoid first n-lines
				if count >10:

					# Strip serial stream of extra characters
					line = line.rstrip().lstrip()
					line = str(line)
					line = line.strip("'")
					line = line.strip("b'")

					line = float(line)
					return line


	## Edited for All_Together

	# def main():
	#
	#
	# 	while True:
	# #	forward(rev)
	# 		key_press = input("Select driving mode:")
	# 		if key_press =='p':
	# #		file1.close()
	# 			break
	# 		key_input(key_press)
