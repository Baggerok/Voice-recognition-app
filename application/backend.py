from application import interface
from logic.input import Mode_handler
from logic import recognition

import threading
import sys

ui = interface.Main_UI()

def print_to_widget(text):
    ui.text_app.appendPlainText(text)

moder = Mode_handler(print_to_widget)

def recognition_thread():
        if not recognition.stop_recognition:
            thread = threading.Thread(target=recognition.main, args=(moder,), daemon=True)
            thread.start()
            ui.start_button.setText("Shutdown recog")
        else:
            recognition.stop_recognition = True

def map_buttons():
    ui.start_button.clicked.connect(recognition_thread)