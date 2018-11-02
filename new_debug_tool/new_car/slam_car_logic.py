# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:16:50 2018

@author: Gehaha
""" 
import sys
from Ui import Ui_MainWindow
import binascii
import threading
import stopThreading

import socket
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget


#逻辑部分
class SignalLogic(QtWidgets.QMainWindow,Ui_MainWindow):
 
    def __init__(self):  #析构函数，实例化后默认加载
        super(SignalLogic,self).__init__()  #超级加载
        self.setupUi(self)
        self.udp_scoket = None
        self.address = None
        self.sever_th = None
        self.client_th = None
        self.client_socket_list = list()
        
      
        self.link = False # 用于标记是否开启连接
        
        
        self.Connect_Button.clicked.connect(self.udp_client_start)
        self.Disconnect_Button.clicked.connect(self.udp_close)
        self.Start_Button.clicked.connect(self.udp_send)
        
        self.connect()
    
    def connect(self):       
       # 控件的信号
        self.signal_write_msg.connect(self.write_msg)
    
    def write_msg(self,msg):
        #signal_write_msg会触发这个函数
        self.Recv_textEdit.insertPlainText(msg)
        self.Recv_textEdit.moveCursor(QtGui.QTextCursor.End)
    
                      
    def udp_server_start(self):
        """
        开启服务端的方法
        """
        port = int(self.Port_lineEdit.text())
        self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        try:
            address = (str(self.IP_lineEdit.text()),int(self.Port_lineEdit.text()))
        except Exception as ret:
            msg = '请检查端口号'
            self.signal_write_msg.emit(msg)
        else:
            self.sever_th = threading.Thread(target=self.udp_server_concurrency) 
            self.sever_th.start() 
            msg = 'UDP服务端正在监听端口:{}\n'.format(port) 
            self.signal_write_msg.emit(msg) 
        
    def udp_client_concurrency(self,address):
        """
        创建一个线程持续监听udp通信   
        """
        while True:
            recv_msg  = self.udp_socket.recvfrom(1024)
            if recv_msg:                  
                msg = recv_msg.decode('utf-8')
                msg = '来自IP:{}端口:{}:\n{}\n'.format(address[0], address[1], msg)
                self.signal_write_msg.emit(msg)  
            else:
                self.udp_scoket.close()
                self.reset()
                msg = '从服务器断开连接\n'
                self.signal_write_msg.emit(msg)
                break
  
            
    def udp_client_start(self):
            
        self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
        try:
           address = (str(self.IP_lineEdit.text()),int(self.Port_lineEdit.text()))         
        except Exception as ret:
            msg = '请检查目标IP，目标端口\n'
            self.signal_write_msg.emit(msg)           
        else:
            msg = 'UDP客户端已启动\n'
            self.signal_write_msg.emit(msg)
            
            """
                msg ='请检查目标IP,目标端口\n'
                self.signal_write_msg.emit(msg)               
                self.client_th = threading.Thread(target=self.udp_client_concurrency) 
                self.client_th.start()
                msg = 'UDP客户端已连接IP:%s端口：%s\n' % address
                print(3)
                self.signal_write_msg.emit(msg)
                msg = ''
             
                print(1)
                self.client_th = threading.Thread(target=self.udp_client_concurrency) 
                self.client_th.start() 
                print(2)
                msg = 'UDP客户端已连接IP:%s端口：%s\n' % address
                print(3)
                self.signal_write_msg.emit(msg)
            """
    def udp_close(self):
        """
        关闭网络连接
        """                 
        self.udp_socket.close()
        try:
            stopThreading.stop_thread(self.sever_th)
        except Exception:
            pass
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass
        self.show_status_label.setText("断开成功")
    
                                
    
    def udp_send(self):
        """
        用于发送消息
        """
        if self.link is False:
            self.show_status_label.setText("请连接服务器")
        else:
           try:
               send_msg = (hex(self.Hight_Edit.toPlainText().encode('utf-8')))
               self.udp_scoket.sendto(send_msg,self.address)
               msg = 'UDP客户端已发送\n'
               self.signal_write_msg.emit(msg)
           except Exception as ret:
                msg = '发送失败\n'
                self.signal_write_msg.emit(msg)
    def stop(self):
        pass
    
    def head(self):
        pass
    
    def back(self):
        pass
        
    def left(self):
        pass
    
    def right(self):
        pass
#程序调用界面                
#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv) #外部参数列表
    MainWindow = QtWidgets.QMainWindow()  # 
    ui = SignalLogic()  
    ui.show() 
    sys.exit(app.exec_())  #退出中使用的消息循环，结束消息循环时就退出程序


