from PyQt4.QtCore import *
#! python3
from PyQt4.QtGui import *
import sys
import XmppApp4_ui
import threading
#import updatetextbox
#import ApplicationCore
import FedController
import Credentials
import advancedTab
import logging
import About
import os
import ctypes
import uploadCerts

logging.basicConfig(filename="log.txt",level=logging.INFO, format='%(threadName)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
#import ssh
#too much code creeped into mainthread again. need to refactor
class controller(QMainWindow,XmppApp4_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        logging.debug('Initialized')

        #workaround for taskbar icon  http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
        myappid = 'infy.cisco.xmppaspp.beta'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        #signals/slots
        self.cb_dns.toggled.connect(self.le_dns.clear)
        self.cb_dns.toggled.connect(self.le_dns.setEnabled)
        self.pb_start.clicked.connect(self.startfederation)
        self.cb_tls.currentIndexChanged.connect(self.advancedTabHandler)
        self.cb_copy.toggled.connect(self.copySlot)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionOpen_Log.triggered.connect(self.openLogFile)
        self.cb_cup.toggled.connect(self.credentialTabHandler)


        path = os.getcwd()

        #t1 =threading.Thread(target=self.logWatcher,args=())
        #t1.start()

        #print(logpath)
        #paths = [ logpath ]
        logpath = os.path.join(os.getcwd(), 'log.txt')
 #       file= QFile(logpath)
#        file.open()
  #      logfd = file.handle()
        #logfd = open(logpath, 'r')
   #     notifier = QSocketNotifier(logfd, QSocketNotifier.Read)
    #    notifier.activated.connect(self.logWatcher)
       # fs_watcher= QFileSystemWatcher()
       #fs_watcher.addPath(logpath)
        #fs_watcher.addPath(logpath)
        #fs_watcher.directoryChanged.connect(self.logWatcher)
        #fs_watcher.fileChanged.connect(self.logWatcher)

        #dev

        self.cb_copy.setChecked(True)

    def credentialTabHandler(self):
        if not self.cb_cup.isChecked():
            self.le_appid1.setReadOnly(True)
            self.le_apppw1.setReadOnly(True)
            self.le_platid1.setReadOnly(True)
            self.le_platpw1.setReadOnly(True)
            self.le_appid2.setReadOnly(True)
            self.le_apppw2.setReadOnly(True)
            self.le_platid2.setReadOnly(True)
            self.le_platpw2.setReadOnly(True)
        else:
            self.le_appid1.setReadOnly(False)
            self.le_apppw1.setReadOnly(False)
            self.le_platid1.setReadOnly(False)
            self.le_platpw1.setReadOnly(False)
            self.le_appid2.setReadOnly(False)
            self.le_apppw2.setReadOnly(False)
            self.le_platid2.setReadOnly(False)
            self.le_platpw2.setReadOnly(False)



    def openLogFile(self):   #this is slot for menu action open file
        os.startfile('log.txt')
        #logfd = open('log.txt', 'a')

    def showAbout(self):
        self.aboutBox = About.About()
        self.aboutBox.show()


    def logWatcher(self):
        print('in logwatcher')
        logpath = os.path.join(os.getcwd(), 'log.txt')
        f = open(logpath)
        self.te_log.append(f.readline())

    def copySlot(self):
        #only disabling here. copying happens in startFederation
        self.le_appid2.clear()
        if self.cb_copy.isChecked():
            self.le_appid2.setPlaceholderText('')
        else:
            self.le_appid2.setPlaceholderText('User Name')
        self.le_appid2.setReadOnly(True)

        self.le_apppw2.clear()
        if self.cb_copy.isChecked():
            self.le_apppw2.setPlaceholderText('')
        else:
            self.le_apppw2.setPlaceholderText('Password')
        self.le_apppw2.setReadOnly(True)

        self.le_platid2.clear()
        if self.cb_copy.isChecked():
            self.le_platid2.setPlaceholderText('')
        else:
            self.le_platid2.setPlaceholderText('User Name')
        self.le_platid2.setReadOnly(True)

        self.le_platpw2.clear()
        if self.cb_copy.isChecked():
            self.le_platpw2.setPlaceholderText('')
        else:
            self.le_platpw2.setPlaceholderText('Password')
        self.le_platpw2.setReadOnly(True)

    def advancedTabHandler(self,index):
        if index == 0:
            self.cb_certs.setCheckable(False)
            self.cb_sasl1.setCheckable(False)
            self.cb_sasl2.setCheckable(False)
        elif index == 1:
            self.cb_certs.setCheckable(True)
            self.cb_sasl1.setCheckable(False)
            self.cb_sasl2.setCheckable(False)
            self.cb_certs.setChecked(False)
        elif index == 2:
            self.cb_certs.setCheckable(True)
            self.cb_sasl1.setCheckable(True)
            self.cb_sasl2.setCheckable(True)
            self.cb_certs.setChecked(True)

    def startfederation(self):
       # logging.info('Starting')
        if self.validateFields() == 1:
            self.pb_start.setText('Working')
            logging.info('Validating Fields')
            #logging
            #textBoxUpdater = updatetextbox.UpdatetextBox(self.te_log)

            server1creds=''
            server2creds=''
            if self.cb_cup.isChecked():
                logging.debug('Found server 1 credentials')
                server1creds = Credentials.Credentials(self.le_appid1.text(),self.le_apppw1.text(),self.le_platid1.text(),self.le_platpw1.text())
                plat_tuple1 = server1creds._platid, server1creds._platpw

            if self.cb_copy.isChecked():
                logging.debug('Found server 2 credentials')
                server2creds = server1creds
            else:
                if self.cb_cup.isChecked():
                    logging.debug('Copying Server 2 credentials from server 1')
                    server2creds = Credentials.Credentials(self.le_appid2.text(), self.le_apppw2.text(), self.le_platid2.text(), self.le_platpw2.text())
                    plat_tuple2 = server2creds._platid, server2creds._platpw
            #self.log('server1creds')
            #self.log(server1creds._appid)
            #self.log(str(server1creds._apppw))
            # self.log('startfederation')
            hn1 = self.le_server1_hn.text()
            ip1 = self.le_server1_ip.text()
            dn1 = self.le_server1_dn.text()
            hn2 = self.le_server2_hn.text()
            ip2 = self.le_server2_ip.text()
            dn2 = self.le_server2_dn.text()
            dnsip = self.le_dns.text()
            dbsecret = self.le_dialback.text()  #needed since dbsecret is optional
            if not dbsecret:
                dbsecret='1234'
                logging.info("Using default dial back secret")
            self.advancedTab = advancedTab.AdvancedTab(dbsecret, self.cb_certs.isChecked(),self.cb_sasl1.isChecked(), self.cb_sasl2.isChecked())
            tlsoption=self.cb_tls.currentIndex()
            worker1 = FedController.WorkerThread(ip1,tlsoption,'r',hn1,dn1,dnsip,server1creds,self.advancedTab)
            worker2 = FedController.WorkerThread(ip2,tlsoption,'r',hn2,dn2,dnsip,server2creds,self.advancedTab)
            if self.cb_tls.currentIndex() == 1 or self.cb_tls.currentIndex() == 2:
                logging.info('inside if block tls enabled')
                worker1.downloadCerts()
                worker2.downloadCerts()
                dnldir1 = worker1.downloaddir
                dnldir2 = worker2.downloaddir
                logging.info("Server 1 certs downloaded to "+ str(dnldir1))
                logging.info('Server 2 certs downloaded to '+ str(dnldir2))


                uploader1 = uploadCerts.UploadCerts(ip1,'xmpp',plat_tuple1,dnldir2)
                uploader2 = uploadCerts.UploadCerts(ip2,'xmpp',plat_tuple2,dnldir1)


        else:
            pass
    def validateFields(self):
        if self.cb_dns.isChecked() and self.le_dns.text()=='':
            QMessageBox.warning(self, 'Required fields missing','DNS field cannot be empty when DNS config is selected')
            return 0

        elif self.cb_cup.isChecked() and (self.le_appid1.text()=='' or self.le_apppw1.text()==''):
            ret = QMessageBox.warning(self, 'Required fields missing', 'One or more field is empty')
            return 0

        else:
            return 1




app=QApplication(sys.argv)
controller=controller()
controller.show()
app.exec_()

