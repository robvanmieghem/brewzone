import datetime
import os
import settings

class Recorder(object):


    def __init__(self):
        self.recording = False
       
    def start(self):
        now = datetime.datetime.today().replace(microsecond=0).isoformat()
        
        self.recording_dir = os.path.join(settings.RECORDINGS_DIR,now)
        os.mkdir(self.recording_dir)
        self.recording = True
        
        
    def stop(self):
        self.recording = False
        
    def update(self):
        if not self.recording:
            return
        