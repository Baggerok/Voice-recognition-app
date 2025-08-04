from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import recognition

def window ():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1280,720)
    win.setWindowTitle("My app")

    start_button = QtWidgets.QPushButton(win)
    start_button.setText("Start recognition")
    start_button.clicked.connect(recognition.main)


    win.show()
    sys.exit(app.exec_())

window()