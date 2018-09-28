# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 20:21:36 2018

@author: Gehaha
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    
    def Init_UI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('哈哈哈')
        
        formlayout = QFormLayout() #创建一个表单布局
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")
        
        formlayout.addRow(nameLabel,nameLineEdit)
        formlayout.addRow(introductionLabel,introductionLineEdit)
        self.setLayout(formlayout)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
    