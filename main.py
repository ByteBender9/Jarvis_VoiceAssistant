import os
import eel
import subprocess
import threading
import time

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call(['bash', 'device.sh'])  # Ensure this script has executable permission
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    # Launch Chrome in app mode using a thread
    def open_chrome():
        time.sleep(2)
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        url = "http://localhost:8000/index.html"
        os.system(f'"{chrome_path}" --app="{url}" &')

    threading.Thread(target=open_chrome).start()

    eel.start('index.html', mode=None, host='localhost', port=8000, block=True)
