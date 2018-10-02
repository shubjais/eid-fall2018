# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TemperatureQT3.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT             #importing this to get the Adafruit DHT22 libraries
import sys
import time
import datetime                 #importing this to get date and time of button push
import matplotlib.pyplot as pt1 #importing this to plot temperature and humidity graph
import matplotlib.pyplot as pt2


class Ui_TemperatureQT(object):
    count = 1                   #variable to keep count of button presses and therefore keep track of no of temp and humdidity records
    total_temp =0
    total_humidity = 0
    avg_temp = 0
    avg_humidity = 0
    all_temp = [];              #creating an empty array so that data can be appended to it for graph plotting
    all_humidity = [];
    humidity,temperature=(0,0)
    def setupUi(self, TemperatureQT):
        TemperatureQT.setObjectName("TemperatureQT")
        TemperatureQT.resize(591, 367)
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
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 82, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 132, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 211, 61))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 180, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 231, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 30, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 80, 101, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 20, 113, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 70, 113, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 130, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 130, 81, 31))
        self.label_8.setObjectName("label_8")
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
        self.pushButton_2.setText(_translate("TemperatureQT", "Plot"))
        self.label_5.setText(_translate("TemperatureQT", "Error Message displayed below:"))
        self.label_6.setText(_translate("TemperatureQT", "Avg Temp"))
        self.label_7.setText(_translate("TemperatureQT", "Avg Humidity"))
        self.label_8.setText(_translate("TemperatureQT", "Temp Unit"))
        self.comboBox.addItem("Celsius")
        self.comboBox.addItem("Farhenite")
        self.pushButton.clicked.connect(self.button_clicked)             #button_clicked function will be called whenever 'Fetch Data' button is pressed
        self.pushButton_2.clicked.connect(self.plot_clicked)             #plot_clicked function will be called whenever 'Plot' button is clicked
        
    def button_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        self.humidity,self.temperature = Adafruit_DHT.read_retry(22,4)
        text = str(self.comboBox.currentText())
        self.label_4.setText(_translate("TemperatureQT",""))
        if(self.temperature == None):
            self.label_4.setText(_translate("TemperatureQT","Error: Sensor not Connected"))     #if sensor is not connected show an error message
            return
        humidity_string = '{0:.2f}'.format(self.humidity)           #convert temp data to string so that it can be populated in line edit
        self.lineEdit_2.setText(_translate("TemperatureQT",humidity_string))
        now = datetime.datetime.now().time()
        time_string = str(now)                                      #convert time data to string
        self.lineEdit_3.setText(_translate("TemperatureQT",time_string))
        self.total_temp = self.total_temp + self.temperature
        self.total_humidity = self.total_humidity + self.humidity
        self.avg_temp = self.total_temp / self.count
        self.avg_humidity = self.total_humidity / self.count
        self.count = self.count + 1
        avg_temp_string = '{0:.2f}'.format(self.avg_temp)              #convert avg temp data to string
        avg_humidity_string = '{0:.2f}'.format(self.avg_humidity)        #conver avg humidity data to string
        self.lineEdit_4.setText(_translate("TemperatureQT", avg_temp_string)) 
        self.lineEdit_5.setText(_translate("TemperatureQT", avg_humidity_string))
        self.all_temp.append(self.temperature)                          #Append temperature data in array
        self.all_humidity.append(self.humidity)                         #Append humidity data in array
        if (text == "Farhenite"):
            Far_temperature = self.temperature
            Far_temperature = Far_temperature * 9/5.0 + 32
            temp_string1 = '{0:.2f}'.format(Far_temperature)           #convert temp data to string so that it can be populated in line edit
            self.lineEdit.setText(_translate("TemperatureQT",temp_string1))
        else:
            temp_string = '{0:.2f}'.format(self.temperature)           #convert temp data to string so that it can be populated in line edit
            self.lineEdit.setText(_translate("TemperatureQT",temp_string))
        
    
    def plot_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        if(self.temperature == None):
            self.label_4.setText(_translate("TemperatureQT","Error: Sensor not Connected"))
            return
        if(len(self.all_temp)<10):                                      #show plot only in data collected points collected is more than 10
            self.label_4.setText(_translate("TemperatureQT","Error: Data not sufficient"))
            return
        i = range(0,len(self.all_temp))
        pt1.plot(i,self.all_temp)                         #plot temp data
        pt2.plot(i,self.all_humidity)                     #plot humidity data
        pt1.show()                                        #show temperature graph
        pt2.show()                                        #show humidity graph
        
        
        
        
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    TemperatureQT = QtWidgets.QMainWindow()
    ui = Ui_TemperatureQT()
    ui.setupUi(TemperatureQT)
    TemperatureQT.show()
    sys.exit(app.exec_())


