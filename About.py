import About_ui
from PyQt4.QtGui import *

class About(QDialog,About_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

