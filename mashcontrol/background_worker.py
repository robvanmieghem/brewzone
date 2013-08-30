from threading import Thread
import time
import settings

class BackgroundWorker(Thread):
    '''
    In order to prevent multiple threads, only one thread is started
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
        
    def run(self):
        while True:
            self._updateSensors()
            self.recorder.update()

            time.sleep(1)