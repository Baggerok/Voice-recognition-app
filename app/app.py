"""
import app.interface as interface


if __name__ == "__main__":
    import sys
    app = interface.QtWidgets.QApplication(sys.argv)
    MainWindow = interface.QtWidgets.QMainWindow()
    ui = interface.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
