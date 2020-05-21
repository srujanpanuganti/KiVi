# import adafruit_bno055
# import time
# from busio import I2C
# from board import SDA, SCL
#
# i2c = I2C(SCL, SDA)
#
#
# '''
# i2c tutorial : https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
# adafruit_bno055 installation : https://circuitpython.readthedocs.io/projects/bno055/en/latest/index.html
# adafruit_bno055 usage : https://github.com/adafruit/Adafruit_CircuitPython_BNO055
# webGL to see the 3D movement corresponding to imu values : https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/webgl-example
# '''
#
# sensor = adafruit_bno055.BNO055(i2c)
#
# while True:
#
#     if sensor.calibration_status:
#
#         print("Calibration Status is : ",sensor.calibrated)
#         print("Calibration Status is : ",sensor.calibration_status)
#         print("Temperature: {} degrees C".format(sensor.temperature))
#         print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
#         print("Magnetometer (microteslas): {}".format(sensor.magnetic))
#         print("Gyroscope (rad/sec): {}".format(sensor.gyro))
#         print("Euler angle: {}".format(sensor.euler))
#         print("Quaternion: {}".format(sensor.quaternion))
#         print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
#         print("Gravity (m/s^2): {}".format(sensor.gravity))
#
#         time.sleep(1)
