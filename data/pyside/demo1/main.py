import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
hello = QtGui.QPushButton("Hello world!")
hello.show()
app.exec_()