from selenium import webdriver
#import threading
#from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver():
    def __init__(self,ip,hn,tlsoption,mode,creds,advancedTab):
        #thread=threading.Thread(target=self.run,args=(ip,tlsoption,mode))
        if mode=='debug':
           browser = webdriver.Firefox()
        else:
            browser = webdriver.Firefox()
        browser.implicitly_wait(10)
        #browser.get('http://'+ip)
        browser.get('http://'+ip+'/cupadmin/xmppFederationSettingsEdit.do')
        #adminlink = browser.find_element_by_css_selector('body > div:nth-child(2) > ul:nth-child(3) > li:nth-child(1) > a:nth-child(1)')
        #adminlink.click()
        userid = browser.find_element_by_css_selector('.content > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)')
       # userid_=browser.find_element_by_class_name()
        userid.send_keys(creds._appid)
        pw = browser.find_element_by_css_selector('.content > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)')
        pw.send_keys(creds._apppw)
        pw.submit()
        #presencetab = browser.find_element_by_css_selector('#udm > li:nth-child(2) > h3:nth-child(1) > a:nth-child(1)')
        #presencetab.click()
        #inter_domain_fed = browser.find_element_by_css_selector('#udm > li:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)')
        #inter_domain_fed.click()
        #xmpp_fed = browser.find_element_by_css_selector('#udm > li:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
        #xmpp_fed.click()
        #settings = browser.find_element_by_css_selector('#udm > li:nth-child(2) > ul:nth-child(2) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
        #settings.click()
        dropdown = browser.find_element_by_css_selector('#ENABLEXMPPNODE')
        dropdown.click()
        xmppnode = browser.find_element_by_css_selector('#ENABLEXMPPNODE > option:nth-child(2)')
        xmppnode.click()
        tlsdropdown = browser.find_element_by_css_selector('#TKSECURITYMODE')
        tlsdropdown.click()
        if tlsoption==0:
            try:
                notls = browser.find_element_by_css_selector('#TKSECURITYMODE > option:nth-child(1)')
                notls.click()
                try:
                    modalalert = browser.switch_to.active_element
                    modalalert.accept()
                except:
                    pass
            except:
                pass

        elif tlsoption==1:
            try:
                tlsoptional=browser.find_element_by_css_selector('#TKSECURITYMODE > option:nth-child(2)')
                tlsoptional.click()
                try:
                    modalalert=browser.switch_to.active_element
                    modalalert.accept()
                except:
                    pass
            except:
                pass

        elif tlsoption==2:
            try:
                tlsrequired=browser.find_element_by_css_selector('#TKSECURITYMODE > option:nth-child(3)')
                tlsrequired.click()
                try:
                    modalalert = browser.switch_to.active_element
                    modalalert.accept()
                except:
                    pass
            except:
                pass

        #try:
         #   alert = browser.switch_to.alert()
            #alert.accept()
        #except: pass

        if advancedTab.clientcert==1:
            cc=browser.find_element_by_css_selector('#CLIENTSIDECERTREQ')
            print(str(cc.is_selected()))
            if cc.is_selected() != 1:
                self.wait=WebDriverWait(browser,4)
                cc_= self.wait.until(EC.element_to_be_clickable(By.ID,'#CLIENTSIDECERTREQ'))
                print("clicking cc")
                cc_.click()

        if advancedTab.sasl_in==1:
            _sasl_in=browser.find_element_by_css_selector('#ENABLESASLEXTERNALINCOMING')
            #print _sasl_in.is_selected()
            if _sasl_in.is_selected() != 1:
                _sasl_in_ = self.wait.until(EC.element_to_be_clickable(By.ID, '#CLIENTSIDECERTREQ'))
                print("clicking _sasl_in")
                _sasl_in_.click()

        if advancedTab.sasl_out==1:
            _sasl_out=browser.find_element_by_css_selector('#ENABLESASLEXTERNALOUTGOING')
          #  print _sasl_out.is_selected()
            if _sasl_out.is_selected() != 1:
                _sasl_out_ = self.wait.until(EC.element_to_be_clickable(By.ID, '#CLIENTSIDECERTREQ'))
                print("clicking _sasl_out")
                _sasl_out_.click()
        dialback = browser.find_element_by_css_selector('#DIALBACKSECRET')
        dialback.clear()
        try:
            dbalert = browser.switch_to.active_element()
            dbalert.accept()
        except:
            pass
        dialback.send_keys(advancedTab.dbsecret)
        print('sending dialback '+advancedTab.dbsecret)
        dialbackconfirm = browser.find_element_by_css_selector('#DIALBACKSECRETCONFIRM')
        dialbackconfirm.clear()
        try:
            dbconfirmalert = browser.switch_to.active_element()
            dbconfirmalert.accept()
        except:
            pass
        dialbackconfirm.send_keys(advancedTab.dbsecret)
        save = browser.find_element_by_css_selector('.cuesButton')
        save.click()
        print('tlsoption is '+str(tlsoption))
       # if tlsoption == 1 or tlsoption == 2:
        #    self.exchangeCerts(browser,ip,hn,creds)
        browser.close()

    #delete the cod below
    def exchangeCerts(self,browser,ip,hn,creds):
        #url = 'http://'+ip+'/cmplatform/certificateFindList.do'
        url =  'http://'+ip+'/cmplatform/'
        print(url)
        browser.get(url)
        #Login
        un = browser.find_element_by_css_selector('.content > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)')
        un.send_keys(creds._platid)
        pw = browser.find_element_by_css_selector('.content > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)')
        pw.send_keys(creds._platpw)
        login = browser.find_element_by_css_selector('button.cuesLoginButton:nth-child(1)')
        login.click()
        security_btn = browser.find_element_by_css_selector('#SecurityButton')
        security_btn.click()
        certmgmt = browser.find_element_by_css_selector('#security > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
        certmgmt.click()
        findbtn = browser.find_element_by_css_selector('#filterRow0 > td:nth-child(7) > input:nth-child(1)')
        findbtn.click()
        cert = browser.find_elements_by_link_text(hn)
        for elements in cert:
            print(elements)
