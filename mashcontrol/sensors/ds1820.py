from base_sensor import BaseSensor

class DS1820(BaseSensor):
    """
     A class for getting the current temp of a DS18B20 (on Linux)
    """

    def __init__(self, sensorId):
        BaseSensor.__init__(self)
        self.tempDir = '/sys/bus/w1/devices/'
        self.sensorId = sensorId


    def getReading(self):
        try:
            f = open(self.tempDir + self.sensorId + "/w1_slave", 'r')
        except IOError:
            self.currentTemp = None
            #print "Error reading " + self.tempDir + self.sensorId + "/w1_slave" ;
            return None;

        lines=f.readlines()
        f.close()
        crcLine=lines[0]
        tempLine=lines[1]
        result_list = tempLine.split("=")

        temp = float(result_list[-1])/1000 # temp in Celcius
                
        if crcLine.find("NO") > -1:
            temp = None

        return temp
