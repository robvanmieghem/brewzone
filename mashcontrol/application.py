from flask import Flask, url_for, redirect
import settings
from mashcontrol.views import hardware

application = Flask(__name__)


@application.route('/')
def index():
    return redirect(url_for('static',filename='index.html'))

def startSensors():
    startSensor('HLT')
    startSensor('MASHIN')
    startSensor('MASHOUT')
    startSensor('BOIL')

def startSensor(name):
    sensor = settings.SENSORS[name]
    if sensor:
        sensor.start()

if __name__ == '__main__':
    startSensors()
    application.add_url_rule('/hardware', 'hardware', hardware.getState)
    
    application.debug = settings.DEBUG
    application.testing = True
    application.run("0.0.0.0")