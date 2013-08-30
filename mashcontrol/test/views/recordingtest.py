import unittest
import tempfile, shutil
import mashcontrol.settings as settings
import mashcontrol.views.recording as recordingview


class RecordingTest(unittest.TestCase):


    def setUp(self):
        self.recordings_dir = tempfile.mkdtemp()
        settings.RECORDINGS_DIR = self.recordings_dir


    def tearDown(self):
        shutil.rmtree(self.recordings_dir)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()