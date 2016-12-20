import paramiko
import logging
import string
import os
import random

#for each instance of Ssh, a random directory is created in $cwd to store certs.
class Ssh():
    def __init__(self,ip, username, password):
        self.ssh=paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username, password)
        randomdir = random.randint(1, 1000)
        self.downloaddir=os.path.join(os.getcwd(),str(randomdir))
        os.mkdir(self.downloaddir)

    def restartService(self,servicename='Cisco XCP XMPP Federation Connection Manager'):
        self.ssh.exec_command('controlcenter.sh '+servicename+' restart')
        logging.debug('command sent to ssh session')
        #stdout.channel.recv_exit_status()

    def download(self,filepath):
        sftp = self.ssh.open_sftp()
        tokens = filepath.split('/')
        filename = tokens[len(tokens)-1]
        try:
            sftp.get(filepath, self.downloaddir+'/'+filename)
            return self.downloaddir
        except:
            return 0
