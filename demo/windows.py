# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:25:58 2018

@author: Gehaha
"""

import sys
from PyQt5.QtWidgets import QApplication ,QWidget,QPushButton,QMessageBox,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from random import randint

class Example(QWidget):
    def __init__(self):
#子类继承父类的时候，我们继承了父类的方法。子类中含有__init__时，不会自动调用父类__init__,
#如需使用父类__init__中的变量，则需要在子类__init__中显示调用（super().__init__()）
        
        super().__init__()
        self.initUI()
        self.num = randint(1,100)
        
    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('学点编程')
        self.setWindowIcon(QIcon('111.ico'))
        
        self.bt1 = QPushButton('我猜',self)
        self.bt1.setGeometry(115,150,70,30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>') #富文本格式，鼠标停留在按钮上就会出现
        self.bt1.clicked.connect(self.showMessage)
        
        self.text = QLineEdit("在这里输入数字",self)
        self.text.selectAll() #将默认数字全选
        self.text.setFocus() #让焦点置于文本框中
        self.text.setGeometry(80,50,150,30)
                
        self.show()
        
    def showMessage(self):
        
        guessnumber = int(self.text.text())
        print(self.num)     
    
        if guessnumber > self.num:
            QMessageBox.about(self, '看结果','猜大了!') # QMessageBox.about弹出一个对话框
            self.text.setFocus()        
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果','猜小了!')
            self.text.setFocus()       
        else:
            QMessageBox.about(self, '看结果','答对了!进入下一轮!')
            self.num = randint(1,100)
            self.text.clear() # 将文本栏里面的内容删除，同时重新生成一个随机数
            self.text.setFocus()    
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()
                
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()  
    sys.exit(app.exec_())
    
