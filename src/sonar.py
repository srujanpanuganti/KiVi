import RPi.GPIO as gpio
import time
import cv2
import imutils
import numpy as np
import os
import statistics

#Define Pins

class Sonar():

	def init_spins(self):

		gpio.setmode(gpio.BOARD)
		gpio.setup(16, gpio.OUT)
		gpio.setup(18, gpio.IN)

	def distance(self):

	#Ensure output has novalue
		gpio.output(16, False)
		time.sleep(0.010)

	#Generate the trigger pulse
		gpio.output(16, True)
		time.sleep(0.00001)
		gpio.output(16,False)

	#Generate Echo time signal
		while gpio.input(18) ==0:
			pulse_start = time.time()

		while gpio.input(18) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

	# Convert time to Distance
		distance = pulse_duration*17150
		distance = round(distance, 2)

	# Clean up GPIO and return the distance
	#gpio.cleanup()


		return distance

#init_spins()
#while True:

	#dist = distance()
	#print(dist)

# if __name__ == 'main':
#
# 	main()
#
