from threading import Thread
import time

class DS1820(Thread):
    """
     A class for getting the current temp of a DS18B20 (on Linux)
    """

    def __init__(self, sensorId):
        Thread.__init__(self)
        self.tempDir = '/sys/bus/w1/devices/'
        self.sensorId = sensorId
        self.currentTemp = None
        self.enabled = True

    def run(self):
        while True:
            if self.isEnabled():
                try:
                    f = open(self.tempDir + self.sensorId + "/w1_slave", 'r')
                except IOError:
                    self.currentTemp = None
                    print "Error reading " + self.tempDir + self.sensorId + "/w1_slave" ;
                    return;

                lines=f.readlines()
                f.close()
                crcLine=lines[0]
                tempLine=lines[1]
                result_list = tempLine.split("=")

                temp = float(result_list[-1])/1000 # temp in Celcius
                
                if crcLine.find("NO") > -1:
                    temp = None

                self.currentTemp = temp
                #print "Current: " + str(self.currentTemp) + " " + str(self.fileName)

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