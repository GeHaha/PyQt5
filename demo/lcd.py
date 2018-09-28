# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:53:12 2018

@author: Gehaha
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget ,QLCDNumber ,QDial,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        
    def initUi(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)  #拨动的小部件
        
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("哈哈哈")
        
        lcd.setGeometry(100,50,150,60)
        dial.setGeometry(120,120,100,100)
        
        dial.valueChanged.connect(lcd.display)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    