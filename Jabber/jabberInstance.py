import sleekxmpp
import logging
from PyQt4.QtCore import QObject, pyqtSignal

class JabberInstance(sleekxmpp.ClientXMPP, QObject):
    sig_msgRcvd = pyqtSignal(str, str, name='msgReceived')
    def __init__(self, jid, password, host, port='5222'):

        QObject.__init__(self)
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.register_plugin('xep_0030')  # Enable service discovery
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.handleRcvdMessage)
        self.host=host
        print('server in constructor is '+self.host)
        self.port=port
        self.jid=jid
        self.password=password
        self.dummy()
        #self.init2()


    def dummy(self):
        print('dummy '+self.host)

    def init2(self):
        print('server value in init '+self.host)
        print('in init')

        print('init 2')
        if self.host:
            con = self.connect(address=(self.host, self.port))
            self.stream = sleekxmpp.XMLStream(host=self.host,port='5222')
            print('con 2')
            if con:
                #logging.info('Connected')
                # self.send_message(mto='user2@cisco.com',mbody='Hey')
                print('Connected')
                self.process()
            else:
                print('con coulnt be established')
        else:
            con = self.connect()
            logging.info('Connecting through service discovery')
            print('Connecting through service discovery')




    def start(self, event):
        print('in start')
        self.send_presence()
        try:
            self.get_roster()
            logging.info('Got roster')
            print('Got roster')
            logging.info(self.client_roster)
            print(self.client_roster)

        except:
            logging.info('')

    def handleRcvdMessage(self, msg):
        sender = msg['from']
        tokens = str(sender).split('@')
        sendername = tokens[0]
        print("Received messaged from network. emiting signal")
        self.sig_msgRcvd.emit(sendername, msg['body'])


    def send2(self, jid, msg):
        print('in send2')
        self.send_message(mto=jid,mbody=msg,mtype='chat')
        #self.send_message(

        # self.stream.send(msg)
        #self.process(block=True)
       # self.disconnect(wait=True)




