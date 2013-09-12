import datetime, time
import os
import settings

class Recorder(object):


    def __init__(self):
        self.recording = False
       
    def start(self, start_time):
        now = time.time()
        self.start_time = start_time
        
        self.recording_dir = os.path.join(settings.RECORDINGS_DIR,start_time)
        os.makedirs(self.recording_dir)
        self.recording = True
        
        
        
    def stop(self):
        self.recording = False
        
    def update(self):
        if not self.recording:
            return
        