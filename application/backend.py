from application import interface
from logic.input import Mode_handler
from logic import recognition

import threading
import sys

recognizer = recognition.Recognizer()
moder = Mode_handler()
ui = interface.Main_UI()

thread = None

def recognition_thread():
    global thread

    if not recognizer.stop_recognition and (thread is None or not thread.is_alive()):
        thread = threading.Thread(target=recognizer.recog_loop, args=(moder,), daemon=True)
        thread.start()

        ui.start_button.setText("Shutdown recog")
        print("Recognition started")
    else:
        recognizer.stop_recognition = True
        if thread != None:
            thread.join()

        ui.start_button.setText("Start recog")
        print("Recognition ended")
        recognizer.stop_recognition = False

def map_buttons():
    ui.start_button.clicked.connect(recognition_thread)