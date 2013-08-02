import settings
from flask_jigger.views import api_view

@api_view
def getState():
    def getSensorTemperature(name):
        sensor = settings.SENSORS[name]
        if sensor:
            return sensor.getCurrentTemp()
    
    mashheater = settings.HEATERS['MASH']
    
    return {'temperature':{
                         'hlt':getSensorTemperature('HLT'),
                         'mashin':getSensorTemperature('MASHIN'),
                         'mashout':getSensorTemperature('MASHOUT'),
                         'boil':getSensorTemperature('BOIL')
                         },
            'heaters':{
                       'mash':{
                               'watt':mashheater.watt,
                               'state':mashheater.state,
                               'frequency':mashheater.frequency,
                               'duty_cycle':mashheater.duty_cycle
                               }
                       }
            }
