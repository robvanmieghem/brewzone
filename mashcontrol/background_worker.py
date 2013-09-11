from threading import Thread
import time
import settings

class BackgroundWorker(Thread):
    '''
    In order to prevent multiple worker threads, only one background thread is started
    It instructs the recorder and sensors to update and times the PIControllers
    '''

    def __init__(self, recorder):
        self.recorder = recorder
        Thread.__init__(self)
        self.daemon = True
    
    def _updateSensors(self):
        self._updateSensor('HLT')
        self._updateSensor('MASHIN')
        self._updateSensor('MASHOUT')
        self._updateSensor('BOIL')

    def _updateSensor(self,name):
        sensor = settings.SENSORS[name]
        if sensor:
            sensor.update()
    
    def _regulateMashHeater(self):
        mashController = settings.HEATCONTROLLERS['mash']
        if not mashController.running:
            return
        
        inTemp = settings.SENSORS['MASHOUT'].getCurrentTemp()
        outTemp = settings.SENSORS['MASHIN'].getCurrentTemp()
        newDutyCycle = mashController.get_control_value(inTemp, outTemp)
        
        mashHeater = settings.HEATERS['mash']
        mashHeater.change_duty_cycle(newDutyCycle)
    
    def run(self):
        while True:
            self._updateSensors()
            self.recorder.update()
            self._regulateMashHeater()

            time.sleep(1)