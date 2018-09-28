# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 20:43:34 2018

@author: Gehaha
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp,QMenu
import sys
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def InitUI(self):
        self.statusBar().showMessage('准备就绪')
        
        self.setGeometry(300,300,400,300)
        self.setWindowTitle("哈哈哈")
        
        exitAct = QAction(QIcon('111.png'),'退出(&E)',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        
        saveMenu = QMenu('保存方式(&S)',self)
        saveAct = QAction(QIcon('111.png'),'保存...',self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('saveas.png'),'另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)
        
        newAct = QAction(QIcon('new.png'),'新建(&N)',self)
        newAct.setShortcut('ctrl + N')
        
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&E)')
        fileMenu.addAction(exitAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())