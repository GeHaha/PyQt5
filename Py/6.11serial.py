import sys
import serial
import serial.tools.list_ports
import time   
from PyQt5 import QtCore, QtGui, QtWidgets

import binascill





class csCMSerial:											# class Coffee Machine Serial
	receiveBuffer_bA = bytearray(0)					# 接收数据缓存区,长度初始为0
	send_prompt_msg = '123'										# 发送数据提示信息
	recv_prompt_msg = '321'										# 接收数据提示信息
    
    
	# 初始化
	def __init__(self):
		self.__ser = serial.Serial()
		
        
	#获取COM号列表  
	def portlist(self):
		Com_List=[]
		port_list = list(serial.tools.list_ports.comports())
		for port in port_list:
			Com_List.append(port[0])
		return Com_List
	
    
	# 串口是否打开
	def SerialisOpen(self):
		return self.__ser.isOpen()
	
    
	# 打开串口
	def openSerialPort(self, baudrate, portname):
		self.__ser.baudrate = baudrate
		self.__ser.port = portname
		if not self.__ser.isOpen():
			self.__ser.open()


    # 关闭串口
	def closeSerialPort(self):
		self.__ser.close()
	
    
    # 获取时间
	def getTimeStamp(self):
		localTime = time.localtime()
		Hour = localTime[3]
		Minu = localTime[4]
		Secd = localTime[5]
		strHour = str(Hour)
		strMinu = str(Minu)
		strSecd = str(Secd)
		if(Hour < 10):
			strHour = '0' + str(Hour)
		if(Minu < 10):
			strMinu = '0' + str(Minu)
		if(Secd < 10):
			strSecd = '0' + str(Secd)

		return (strHour + ':' + strMinu + ':' + strSecd)
	
    
    # 整数转换为十六进制字符串
	def intToHexStr(self, num):
		hexStr = hex(num)
		if(num < 0x10):
			return '0x0' + hexStr[2:]
		else:
			return hexStr
	
    
    # 字节数组转换为十六进制字符串
	def byteArrayToHexStr(self, ba):
		hexStr = ' '
		for i in ba:
			hexStr = hexStr + self.intToHexStr(i) + ' '
		return hexStr
	
    # 产生提示信息,结果保存在prompt_msg中
	def generatePromptMsg(self, sendFlag, ba):
		if sendFlag:
			print(self.byteArrayToHexStr(ba))
		else:
			self.recv_prompt_msg = self.getTimeStamp() + ' Recv:' + self.byteArrayToHexStr(ba) + attached

	# 构建数据帧
	def buildDataFrame(self, cmd_name):
		for i in range(dataFillLen):
			ba[i] = cmd_name[i]
		return ba                    # 返回构建的字节数组
		
	# 检查获取新数据,需被定时调用
	# 从接收数据缓存区中解析出一帧数据
	# Buffer有数据但在500ms内都未能解析出数据(cmd_code allways == 0x00)
	# 从Flag == True开始计时
	# 则调用resetInputBuffer清数据接收缓存区
	# 避免了接收数据出错之后阻塞的情况
	def checkNewData_And_getOneDataFrame(self):
		length = self.__ser.in_waiting
		if length > 0:
			flag = True
			return self.receiveBuffer_bA, flag
		else:
			flag = False
			return self.receiveBuffer_bA, flag

	# 清空接收数据缓存区和串口接收数据缓存区
	def resetInputBuffer(self):
		self.receiveBuffer_bA = bytearray(0)
		#self.__ser.reset_input_buffer()

	# 解析获取的数据帧,此部分代码先支持桌上型机器
	def parseDataFrame(self, dataFrame):
		attachedStr = '[ ]'
		attachedStr = '[接受的数据:' + dataFrame + ']'
		self.generatePromptMsg(False, dataFrame, attachedStr)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.my_serial = csCMSerial(); 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 31, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 41, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 51, 31))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 110, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 150, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 190, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 70, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 250, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 250, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 180, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 230, 61, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 150, 61, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(430, 150, 61, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 10, 341, 121))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 321, 91))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 139, 161, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 141, 111))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 180, 61, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 230, 61, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
       
    
        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.open_serial)
        self.pushButton_3.clicked.connect(self.my_serial.closeSerialPort)
        self.pushButton_5 .clicked.connect(self.send_serial)
        self.pushButton_4.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_6.clicked.connect(self.lineEdit.clear)
        self.pushButton_5.clicked.connect(self.lineEdit.show)
        self.lineEdit_2.selectionChanged.connect(self.pushButton_5.showMenu)
#        self.pushButton_3.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">串口</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">波特率</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">校验位</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">数据位</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">停止位</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "6"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "7"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "NONE"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "EVEN"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ODD"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "MARK"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "SPACE"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "14400"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "19200"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "56000"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "57600"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "128000"))
        self.pushButton_2.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_3.setText(_translate("MainWindow", "关闭串口"))
        self.pushButton_4.setText(_translate("MainWindow", "清除发送"))
        self.pushButton_5.setText(_translate("MainWindow", "发送"))
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkBox_2.setText(_translate("MainWindow", "Hex发送"))
        self.groupBox.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_2.setTitle(_translate("MainWindow", "发送区"))
        self.pushButton_6.setText(_translate("MainWindow", "清除接收"))
        self.pushButton_7.setText(_translate("MainWindow", "停止发送"))
     
    def open_serial(self):
        self.my_serial.openSerialPort(9600,'com2')
    def send_serial(self):
        self.my_serial.generatePromptMsg(1,1)
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
