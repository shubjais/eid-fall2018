# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TemperatureQT_shubham.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT
import sys
import time
import datetime

def button_clicked():
    humidity,temperature = (0,0)
    humidity,temperature = Adafruit_DHT.read_retry(22,4)
    if(temperature == None):
        self.label_4.setText("Error: Sensor not Connected")
        return
    temp_string = '{0:.2f}'.format(temperature)
    self.lineEdit.setText(self._translate("TemperatureQT",temp_string))
    humidity_string = '{0:.2f}'.format(humidity)
    self.lineEdit_2.setText(self._translate("TemperatureQT",humidity_string))
    now = datetime.datetime.now().time()
    time_string = str(now)
    self.lineEdit_3.setText(self._translate("TemperatureQT",time_string))
    
class Ui_TemperatureQT(object):
    def setupUi(self, TemperatureQT):
        TemperatureQT.setObjectName("TemperatureQT")
        TemperatureQT.resize(591, 505)
        TemperatureQT.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(TemperatureQT)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 61, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 190, 82, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 140, 113, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 239, 211, 61))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        TemperatureQT.setCentralWidget(self.centralwidget)

        self.retranslateUi(TemperatureQT)
        QtCore.QMetaObject.connectSlotsByName(TemperatureQT)

    def retranslateUi(self, TemperatureQT):
        _translate = QtCore.QCoreApplication.translate
        TemperatureQT.setWindowTitle(_translate("TemperatureQT", "TemperatureQT"))
        self.label.setText(_translate("TemperatureQT", "Temperature"))
        self.label_2.setText(_translate("TemperatureQT", "Humidity"))
        self.label_3.setText(_translate("TemperatureQT", "Time"))
        self.pushButton.setText(_translate("TemperatureQT", "Fetch Data"))
        self.pushButton.clicked.connect(button_clicked)
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    TemperatureQT = QtWidgets.QMainWindow()
    ui = Ui_TemperatureQT()
    ui.setupUi(TemperatureQT)
    TemperatureQT.show()
    sys.exit(app.exec_())

