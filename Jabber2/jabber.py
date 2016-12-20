from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtDeclarative import QDeclarativeView
import sys

app = QApplication(sys.argv)
view = QDeclarativeView()
view.setSource(QUrl('login.qml'))
view.show()
app.exec_()