import adafruit_bno055
import time
from busio import I2C
from board import SDA, SCL

i2c = I2C(SCL, SDA)


sensor = adafruit_bno055.BNO055(i2c)


print("Calibration Status is : ",sensor.calibrated)

print("Calibration Status is : ",sensor.calibration_status)

'''
while True:
    print("Temperature: {} degrees C".format(sensor.temperature))
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Quaternion: {}".format(sensor.quaternion))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print("Gravity (m/s^2): {}".format(sensor.gravity))
    print()
 
    time.sleep(1)
'''
