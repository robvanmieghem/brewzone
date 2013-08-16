import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Heater():
    '''
    classdocs
    '''

    def __init__(self, pin, watt=None):
        self.watt = watt
        self.pin = pin
        self.frequency = 0.5 #frequency of 2 seconds
        self.duty_cycle = 10.0 #duty cycle of 10% 
        self.state = 'OFF'
        
    def start(self):
        print 'Starting pwm on pin %s with a duty cycle of %s' % (self.pin, self.duty_cycle)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(self.duty_cycle)
        self.state = 'ON'
    
    def stop(self):
        print 'Stopping pwm on pin %s' % (self.pin)
        self.pwm.stop()
        self.state = 'OFF'
        #GPIO.cleanup()
        
    def change_duty_cycle(self, dc):
        '''
        where 0.0 <= dc <= 100.0
        '''
        print 'Adjusting duty cycle to %s' % dc
        self.duty_cycle = dc
        self.pwm.ChangeDutyCycle(dc)   
    
    def change_frequency(self, freq):
        '''
        freq is the new frequency in Hz
        '''
        print 'Adjusting frequency to %s' % freq
        self.frequency = freq
        self.pwm.ChangeFrequency(freq)
