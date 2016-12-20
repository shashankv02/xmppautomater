from PyQt4.QtGui import *
from PyQt4.QtCore import *
from . import jabberInstance
#import sys

class JabberView(QDialog):
    sig_sendMsg = pyqtSignal(str, str, name="sendMsg")
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Basic xmpp client")
        mainLayout = QVBoxLayout()
        self.te_chat = QTextEdit()
        self.te_chat.setReadOnly(True)
        self.le_msg = QLineEdit()
        pb_send = QPushButton('Send')
        msgbarLayout = QHBoxLayout()
        msgbarLayout.addWidget(self.le_msg)
        msgbarLayout.addWidget(pb_send)
        mainLayout.addWidget(self.te_chat)
        mainLayout.addLayout(msgbarLayout)
        self.setLayout(mainLayout)
        pb_send.clicked.connect(self.sendMsg)
        self.le_msg.setFocus()

        #Core jabber

        thread = QThread()
        self.jabber = jabberInstance.JabberInstance('user2@cisco.com','ccm-dod','cucm-65')
        self.jabber.moveToThread(thread)
        thread.start()
        thread.started.connect(self.jabber.init2)
        self.jabber.sig_msgRcvd.connect(self.handleRcvdMsg)


    def handleRcvdMsg(self,sender,msg):
        print('in handleRcvdMsg')
        self.te_chat.append(sender+':'+msg)

    def sendMsg(self):
        print('in sendMsg')
        msg=self.le_msg.text()
        if msg:
            #1.put message in text box
            #2.send it over network
            self.te_chat.append('Me:'+msg)
            self.le_msg.clear()
            self.sendMsgOverNetwork(msg)

    def sendMsgOverNetwork(self, msg):
        print('in sendMsgOverNetwork')
        jid = 'user2@cisco.com'
        self.jabber.send2('user1@cisco.com',msg)
        #self.jabber.send2(jid, msg)

