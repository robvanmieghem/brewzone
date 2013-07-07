import settings
from flask_jigger.views import api_view

@api_view
def getState():
    def getSensorTemperature(name):
        sensor = settings.SENSORS[name]
        if sensor:
            return sensor.getCurrentTemp()
    
    return {'temperature':{
                         'hlt':getSensorTemperature('HLT'),
                         'mashin':getSensorTemperature('MASHIN'),
                         'mashout':getSensorTemperature('HLT'),
                         'boil':getSensorTemperature('MASHOUT')
                         }
            }