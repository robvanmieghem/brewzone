from base_sensor import BaseSensor
import random

class Simulator(BaseSensor):
    '''
    Simulates a temperature sensor with a random value between 60.0 and 61.0
    '''


    def __init__(self):
        BaseSensor.__init__(self)
        
    
    def getReading(self):
        return 60.0 + random.random()