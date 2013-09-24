from flask import Flask, url_for, redirect
import settings, background_worker
from mashcontrol.views import hardware, recording
from recorder import Recorder

application = Flask(__name__)


@application.route('/')
def index():
    return redirect(url_for('static',filename='index.html'))

recorder = Recorder()
worker = background_worker.BackgroundWorker(recorder)

if __name__ == '__main__':
    worker.start()
    hardware.recorder = recorder
    application.add_url_rule('/hardware', 'hardware', hardware.getState)
    application.add_url_rule('/hardware/pi', 'pihardware', hardware.getPiState)
    application.add_url_rule('/hardware/pumps/<pumpIdentifier>','setPumpState',hardware.setPumpState, methods=['PUT'])
    application.add_url_rule('/hardware/heaters/<heaterIdentifier>','setHeaterState',hardware.setHeaterState, methods=['PUT'])
    application.add_url_rule('/hardware/recorder','setRecorderState', hardware.setRecorderState, methods=['PUT'])
    application.add_url_rule('/recordings', 'recordinglist', recording.get_recording_list)
    application.add_url_rule('/recordings/<recording_id>','recordingdetail', recording.recording_details, methods=['GET'])
    application.add_url_rule('/recordings/<recording_id>','deleterecording',recording.delete_recording, methods=['DELETE'])
    
    application.debug = settings.DEBUG
    application.testing = True
    application.run("0.0.0.0", port = settings.PORT)