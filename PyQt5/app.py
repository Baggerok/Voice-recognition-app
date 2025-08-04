from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import recognition
from PyQt5.QtCore import pyqtSignal, QObject
import threading

def recognition_thread():
    recognition.main()

def start_recognition():
    thread = threading.Thread(target=recognition_thread, daemon=True)
    thread.start()

def window ():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1280,720)
    win.setWindowTitle("My app")

    central_widget = QWidget()
    layout = QVBoxLayout()
    central_widget.setLayout(layout)
    win.setCentralWidget(central_widget)

    start_button = QtWidgets.QPushButton("Start recognition")
    layout.addWidget(start_button)

    start_button.clicked.connect(start_recognition)

    win.show()
    sys.exit(app.exec_())

window()