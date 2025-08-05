from application import interface
from logic import recognition

import threading
import sys

ui = interface.Main_UI()

def start_recognition_thread():
        thread = threading.Thread(target=recognition.main, daemon=True)
        thread.start()

def print_to_widget(text):
    ui.text_app.appendPlainText(text)
    
def map_buttons():
    ui.start_button.clicked.connect(start_recognition_thread)