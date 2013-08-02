from threading import Thread
import time


class BaseSensor(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.currentTemp = None
        self.enabled = True


    def getReading(self):
        return None

    def run(self):
        while True:
            if self.isEnabled():
                self.currentTemp = self.getReading()

            time.sleep(1)

    #returns the current temp for the probe
    def getCurrentTemp(self):
        return self.currentTemp

    #setter to enable this probe
    def setEnabled(self, enabled):
        self.enabled = enabled
    #getter       
    def isEnabled(self):
        return self.enabled
    
        