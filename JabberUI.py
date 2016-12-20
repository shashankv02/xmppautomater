from Jabber import view
from PyQt4.QtGui import  *
import sys

app=QApplication(sys.argv)
JabberView = view.JabberView()
JabberView.show()
app.exec_()