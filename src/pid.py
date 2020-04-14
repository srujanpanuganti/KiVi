import time
import sys
import signal

class PID:
    def __init__(self, kp = 1, ki = 0, kd = 0):
        self.kp = kp
        self.kd = kd
        self.ki = ki

    def initialize(self):
        # initialize the current and previous time
        self.currTime = time.time()
        self.prevTime = self.currTime

        # initialize the previous error
        self.prevError = 0

        # initialize the term result variables
        self.cP = 0
        self.cI = 0
        self.cD = 0



    def update(self, error, sleep=0.2):
        # pause for a bit
        time.sleep(sleep)

        # grab the current time and calculate delta time
        self.currTime = time.time()
        deltaTime = self.currTime - self.prevTime

        # delta error
        deltaError = error - self.prevError

        # proportional term
        self.cP = error

        # integral term
        self.cI += error * deltaTime

        # derivative term and prevent divide by zero
        self.cD = (deltaError / deltaTime) if deltaTime > 0 else 0

        # save previous time and error for the next update
        self.prevtime = self.currTime
        self.prevError = error

        # sum the terms and return
        return sum([
            self.kp * self.cP,
            self.ki * self.cI,
            self.kd * self.cD])




class PID_controller:

    def signal_handler(self, sig, frame):
        print('You have pressed ctrl + c. existing!')
        sys.exit()


    def pid_process(self, output, p, i, d, objCoord, centerCoord):
        # signal trap to handle keyboard interrupt
        signal.signal(signal.SIGINT, self.signal_handler)

        # create a PID and initialize it
        p = PID(p.value, i.value, d.value)
        p.initialize()

        # loop indefinitely
        while True:
            # calculate the error
            error = centerCoord.value - objCoord.value

            # update the value
            output.value = p.update(error)
