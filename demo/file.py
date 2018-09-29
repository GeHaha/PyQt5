# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:19:21 2018

@author: Gehaha
"""

from PyQt5.QtWidgets import QDialog,QWidget ,QApplication ,QPushButton ,QColorDialog,QFontDialog,QTextEdit,QFileDialog
from PyQt5.QtPrintSupport import QPageSetupDialog,QPrintDialog,QPrinter

import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.printer = QPrinter()
        
    def initUI(self):
        self.setGeometry(300,300,500,300)
        self.setWindowTitle("哈哈哈")
        
        self.tx = QTextEdit(self)
        self.tx.setGeometry(20,20,300,270)
        
        self.bt1 = QPushButton("打开文件",self)
        self.bt1.move(350,20)
        
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        
        self.bt3 = QPushButton("选择颜色",self)
        self.bt3.move(350,120)
        
        self.bt4 = QPushButton("打开多个文件",self)
        self.bt4.move(350,220)
        
        self.bt5 = QPushButton("保存文件",self)
        self.bt5.move(350,270)
        
        self.bt6 = QPushButton("打印文档",self)
        self.bt6.move(350,320)
        
        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)
        self.bt4.clicked.connect(self.openfiles)
        self.bt5.clicked.connect(self.savefile)
        self.bt6.clicked.connect(self.printdialog)
        
        
        self.show()
        
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self,"打开文件",'./')
        if fname[0]:
            with open(fname[0],'r',encoding = 'utf-8',errors = 'ignore') as f:
                self.tx.setText(f.read())
                
    def choicefont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)
            
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)
            
    def openfiles(self):
        fnames = QFileDialog.getOpenFileNames(self,'打开多个文件','./')
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname,'r',encoding = 'utf-8',errors = 'ignore') as f:
                    f.write(self.tx.toPlainText())
                    
    def savefile(self):
        fileName = QFileDialog.getSaveFileName(self,'保存文件','./')
        if fileName[0]:
            with open(fileName[0],'w',encoding = 'utf-8',errors  = 'ignore') as f:
                f.write(self.tx.toPlainText())
#最后我们使用write函数将QTextEdit的内容保存在文件中。获取的QTextEdit的内容可以使用这个函数toPlainText()。效果如下：
                              
    
    def printdialog(self):
        printdialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printdialog.exec_():
            self.tx.print(self.printer)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        