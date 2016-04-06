import paramiko
import logging
import string
import os
import random

#for each instance of Ssh, a random directory is in cwd created to store certs.
class Ssh():
    def __init__(self,ip,username='cisco',password='root'):
        self.ssh=paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip,username='root',password='cisco')
        randomdir = random.randint(1, 1000)
        self.downloaddir=os.path.join(os.getcwd(),str(randomdir))
        os.mkdir(self.downloaddir)

    def restartService(self,servicename='Cisco XCP XMPP Federation Connection Manager'):
        self.ssh.exec_command('controlcenter.sh '+servicename+' restart')
        logging.debug('command sent to ssh session')
        #stdout.channel.recv_exit_status()

    def setDomain(self,domain):
        #need to give admin credentials for this method
        pass

    def download(self,filepath):
        sftp = self.ssh.open_sftp()
        tokens = filepath.split('/')
        filename = tokens[len(tokens)-1]
        try:
            sftp.get(filepath, self.downloaddir+'/'+filename)
            return self.downloaddir
        except:
            return 0
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('10.77.46.90', username='admin',password='ccm-dod')
#stdin,stdout,stderr=ssh.exec_command('controlcenter.sh list')
#print(stdout.readlines())

#sftp = ssh.open_sftp()
#cwd = os.getcwd()

#sftp = paramiko.SFTPClient()
#filepath = '/usr/local/sip/.security/xmpp/certs/cup-xmpp.der'

#sftp.get(filepath,cwd+'\\cup-xmpp2.der')