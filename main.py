from application import backend

from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    #setup services
    MainApp = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    backend.ui.setupUi(MainWindow)
    backend.map_buttons()

    #show window
    MainWindow.show()
    MainApp.exec_()
