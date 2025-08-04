from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

def window ():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1280,720)
    win.setWindowTitle("My app")

    win.show()
    sys.exit(app.exec_())

window()