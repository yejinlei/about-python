#coding:UTF-8

import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
hello = QtGui.QPushButton("Hello world!") #顶级窗体
hello.setGeometry(300, 300, 250, 150)    #窗体位置和大小
hello.setToolTip(u'我是顶级窗口')      #气泡提示
QtGui.QPushButton("yee", hello)         #控件
hello.setWindowTitle(u'Demo')          #标题
hello.show()
app.exec_()