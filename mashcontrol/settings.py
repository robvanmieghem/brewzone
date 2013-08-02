
#Run Flask application in Debug mode (reload the process on filechanges)
#This enables the Flask debugger but disables to ability to control the process externally (supervisor or PyDev debugger)
DEBUG = False


#One wire ids of the DS1820 sensors, put 'None' if not connected
#from mashcontrol.sensors import DS1820
# 
# SENSORS = {
#            'HLT': DS1820('28-00000481da8b'),
#            'BOIL':DS1820('28-00000481da8b'),
#            'MASHIN':DS1820('28-00000481a5f0'),
#            'MASHOUT':DS1820('28-0000048158b6')
#            }

from mashcontrol.sensors import Simulator
SENSORS = {
            'HLT': Simulator(),
            'BOIL':Simulator(),
            'MASHIN':None,
            'MASHOUT':Simulator()
            }


#from mashcontrol.regulators import heater
#HEATERS = {
#           'MASH': heater.Heater(15)
#           }

from mashcontrol.regulators import heatersimulation
HEATERS = {
           'MASH': heatersimulation.HeaterSimulation(15, 2500)
           }