import settings
from flask_jigger.views import api_view, status
from flask import request, abort
import os, shutil

#TODO: check with the abspath and commonprefix if no directory traversal is going on

@api_view
def get_recording_list():
    recordings_list = []
    
    directories = os.listdir(settings.RECORDINGS_DIR)
    directories.sort(reverse=True)
    for directory in directories:
        recordings_list.append({'start':directory})
    
    return recordings_list

@api_view
def delete_recording(recording_id):
    
    shutil.rmtree(os.path.join(settings.RECORDINGS_DIR, recording_id))

@api_view
def recording_details(recording_id):
    return {'start':recording_id}