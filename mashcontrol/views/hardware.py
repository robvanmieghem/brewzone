import settings
from flask_jigger.views import api_view, status
from flask import request, abort

recorder = None

@api_view
def getState():
    def getSensorTemperature(name):
        sensor = settings.SENSORS[name]
        if sensor:
            return sensor.getCurrentTemp()
    
    mashheater = settings.HEATERS['mash']
    mashpump = settings.PUMPS['mash']
    
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
                       },
            'pumps':{
                     'mash':{
                             'state':mashpump.state
                             }
                     },
            'recorder':{
                        'recording':recorder.recording
                        }
            }

@api_view
def setPumpState(pumpIdentifier):
    pump = settings.PUMPS[pumpIdentifier]
    desiredState = request.get_json()['state']
    if (desiredState != pump.state):
        if (desiredState == 'ON'):
            pump.start()
        elif (desiredState == 'OFF'):
            pump.stop()
        else:
            abort(status.HTTP_400_BAD_REQUEST)

@api_view
def setRecorderState():
    request_data = request.get_json()
    desiredState = request_data['recording']
    if (desiredState != recorder.recording):
        if (desiredState):
            start = request_data['start']
            recorder.start(start)
        else:
            recorder.stop()
            

@api_view
def setHeaterState(heaterIdentifier):
    heater = settings.HEATERS[heaterIdentifier]
    newState = request.get_json();
    
    duty_cycle = float(newState['duty_cycle'])
    if (duty_cycle != heater.duty_cycle):
        heater.change_duty_cycle(duty_cycle)
    
    frequency = float(newState['frequency'])
    if (frequency != heater.frequency):
        heater.change_frequency(frequency)
        
    desiredState = newState['state']
    if (desiredState != heater.state):
        if (desiredState == 'ON'):
            heater.start()
        elif (desiredState == 'OFF'):
            heater.stop()
        else:
            abort(status.HTTP_400_BAD_REQUEST)
