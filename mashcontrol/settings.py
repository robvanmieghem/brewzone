
#Run Flask application in Debug mode (reload the process on filechanges)
#This enables the Flask debugger but disables to ability to control the process externally (supervisor or PyDev debugger)
DEBUG = False


#One wire ids of the DS1820 sensors, put 'None' if not connected
from mashcontrol.sensors import DS1820

SENSORS = {
           'HLT': DS1820('28-00000481da8b'),
           'BOIL':DS1820('28-00000481da8b'),
           'MASHIN':None,
           'MASHOUT':DS1820('28-00000481da8b')
           }