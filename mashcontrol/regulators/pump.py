import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Pump(object):
    
    def __init__(self, pin):
        '''
        Constructor
        '''
        self.pin = pin
        self.state = 'OFF'
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        
    def start(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = 'ON'
        
    def stop(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = 'OFF'
        