
class PumpSimulation(object):
    
    def __init__(self, pin):
        '''
        Constructor
        '''
        self.pin = pin
        self.state = 'OFF'
        
    def start(self):
        self.state = 'ON'
        
    def stop(self):
        self.state = 'OFF'
        