

class BaseSensor(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.currentTemp = None

    def getReading(self):
        return None

    def update(self):
        self.currentTemp = self.getReading()

    def getCurrentTemp(self):
        return self.currentTemp

    
        