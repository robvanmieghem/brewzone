import settings
from flask_jigger.views import api_view, status
from flask import request, abort
import datetime, os

@api_view
def get_recording_list():
    recordings_list = []
    
    directories = os.listdir(settings.RECORDINGS_DIR)
    directories.sort(reverse=True)
    for directory in directories:
        recordings_list.append({'start':directory})
    
    return recordings_list