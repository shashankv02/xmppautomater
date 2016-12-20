import threading
import CupConfig
import logging
import ApplicationCore
import ssh
import uploadCerts

PORT = 5269

class WorkerThread():
    def __init__(self,ip1,tlsoption,mode,hn1,dn1,dnsip, creds,advancedTab):
        self.ip = ip1
        self.tlsoption = tlsoption
        self.mode=mode
        self.hn=hn1
        self.dn=dn1
        self.dnsip=dnsip
        self.creds=creds
        self.advancedTab=advancedTab

        self.core  = ApplicationCore.Federation()
        if self.creds:
            logging.info('Credential given. Creating driver for cup config. ')
            thread = threading.Thread(target=self.run,args=())
            thread.start()
        else:
            logging.info('No credential given. Not doing cup config')

        if dnsip:
            logging.info("DNS ip given. Updating DNS")
            self.updateDns()

        #if tlsoption == 1 or tlsoption ==2:
         #   if self.downloadCerts() == 1:
            # pass
          #       self.uploadCerts()

    def updateDns(self):
        logging.info('Contacting DNS. Updating A record')
        self.core.UpdateDnsA(self.hn, self.ip, self.dn, 'A', self.dnsip)
        logging.info('Contacting DNS. Updating SRV record')
        self.core.UpdateDnsSrv(PORT, self.hn, self.dn, self.dnsip)


    def downloadCerts(self):
       # if tlsoption == 1 or tlsoption == 2:
        logging.info('Downloading certs from '+self.ip)
        myssh = ssh.Ssh(self.ip)
        try:
            self.downloaddir = myssh.download('/usr/local/sip/.security/xmpp-s2s/certs/cup-xmpp-s2s.der')
            logging.info('Downloaded certs to '+self.downloaddir)
            myssh.download('/usr/local/sip/.security/xmpp-s2s-ECDSA/certs/cup-xmpp-s2s-ECDSA.der')
        except:
            logging.info('Certificate download failed')
            return 0
        logging.info('Downloaded certificates')
        return 1


    def uploadCerts(self):
        logging.info("Starting upload certs")
        plat_tuple = self.creds._platid, self.creds._platpw
        uploadCerts.UploadCerts(self.ip,'xmpp',plat_tuple,self.downloaddir)

    def run(self):
        logging.debug('Running driver thread')
        CupConfig.Driver(self.ip, self.hn, self.tlsoption, self.mode, self.creds, self.advancedTab)


