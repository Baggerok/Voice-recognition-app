from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.resize(622, 528)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 621, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(490, 10, 111, 41))
        self.start_button.setObjectName("start_button")

        self.modes_label = QtWidgets.QLabel(self.centralwidget)
        self.modes_label.setGeometry(QtCore.QRect(10, 20, 61, 31))
        self.modes_label.setObjectName("modes_label")
        self.modes_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.modes_label_2.setGeometry(QtCore.QRect(60, 20, 281, 31))

        font = QtGui.QFont()
        font.setUnderline(False)

        self.modes_label_2.setFont(font)
        self.modes_label_2.setObjectName("modes_label_2")

        self.vertical_line = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line.setGeometry(QtCore.QRect(460, 0, 21, 61))
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")

        self.text_app = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_app.setGeometry(QtCore.QRect(10, 80, 331, 381))
        self.text_app.setAutoFillBackground(True)
        self.text_app.setObjectName("text_app")
        self.text_app.setReadOnly(True)
        self.text_app.setPlainText("")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start recognition"))
        self.modes_label.setText(_translate("MainWindow", "Modes:"))
        self.modes_label_2.setText(_translate("MainWindow", "Default, gaming, speech typing"))