import sys
import logging
import dns.resolver
import dns.update
import dns.zone

class Federation():                 #legacy naming :(
    def __init__(self):
        logging.debug("initializing DNS Class")
        #self.resolver = dns.resolver.Resolver()
        #self.resolver.nameservers = ['10.77.137.19']   #for testing

    def ResolveDns(self):
        try:
            query=self.resolver.query(self.lineedit_resolve_host.text(), 'A')
        except:
            print('try again')
        for answer in query:
            self.textbox.append(str(answer))
            print(answer)
       # query = dns.resolver.query('gmail.com', 'MX')
        #for data in query:
         #   self.textbox.append("test "+str(data.exchange))
          #  print('Host', data.exchange, 'has preference', data.preference)


    def UpdateDnsA(self,host,ip,domain,type,dnsip):
        logging.debug('UpdateDnsA: '+host+' '+ip+' '+domain+' '+dnsip)
        update = dns.update.Update(domain)
        update.replace(host, 3600, type, ip)
        try:
            logging.debug('UpdateDnsA: writing to dns server')
            response = dns.query.tcp(update, dnsip)
        except:
            logging.info('Writing A record failed')
            logging.exception('')
        #self.lineedit_resolve_host.setText(host+'.test.com')
        #self.lineedit_srv.setText('test.com')

    def UpdateDnsSrv(self,port,host,domain,dnsip):
        update=dns.update.Update(domain)
        update.add('_xmpp-server._tcp',3600,'SRV','0 0 5269 '+host)
        try:
            logging.debug('UpdateDnsSrv: writing to dns server')
            response = dns.query.tcp(update, dnsip)
        except:
            logging.info('Writing SRV failed')
            logging.exception('')


    def GetSrvRecords(self):
        domain='_xmpp-server._tcp.'+self.lineedit_srv.text()
        print(domain)
        queryresult = self.resolver.query(domain, 'SRV')
       #for answers in queryresult:
        #    print(answers)
        #except:
         #   print("couldn't find srv")




