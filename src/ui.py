from gpiozero import LED, Button

class UI:

    def __init__(self):

        self.train_switch   =    Button(13) #
        self.execute_switch =    Button(26)  #   new user button
        self.dev_push_button =   Button(19)   #   returning_user button

        # self.led_1 =       LED(16)    #
        # self.led_2 =       LED(20)    #
        # self.led_3 =       LED(21)    #
        # self.add_user_button =      Button(26)  #   new user button
