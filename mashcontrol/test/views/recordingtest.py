import unittest
import tempfile, shutil, os
import mashcontrol.settings as settings
import mashcontrol.views.recording as recordingview


class RecordingTest(unittest.TestCase):


    def setUp(self):
        self.recordings_dir = tempfile.mkdtemp()
        settings.RECORDINGS_DIR = self.recordings_dir


    def tearDown(self):
        shutil.rmtree(self.recordings_dir)

    def Test_delete_recording_does_not_exist_correct_error(self):
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()