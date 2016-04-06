from selenium import webdriver
from selenium.webdriver.support.ui import Select
import threading
import os
import logging
import ssh

#this class can be generalized for other cert purposes. purpose field doednt do anything right now
class UploadCerts():
    def __init__(self,ip, purpose, plat_tuple,fromdir):
        thread = threading.Thread(target=self.run,args=(ip, purpose, plat_tuple,fromdir))
        thread.start()

    def run(self, ip, purpose, plat_tuple,fromdir):
        browser = webdriver.Firefox()
        browser.get('http://'+ip+'/cmplatform/certificateUpload.do')
        un = browser.find_element_by_name('j_username')
        un.send_keys(plat_tuple[0])
        pw = browser.find_element_by_name('j_password')
        pw.send_keys(plat_tuple[1])
        login_btn = browser.find_element_by_css_selector('button.cuesLoginButton:nth-child(1)')
        login_btn.click()
        dropdown_list = Select(browser.find_element_by_xpath("id('NAME')"))
       # dropdown_list.click()
        if purpose == 'xmpp':
            dropdown_list.select_by_value('cup-xmpp-trust')
       # browse_btn = browser.find_element_by_css_selector('#FILE')
       # browse_btn.send_keys('test.txt')
        file =browser.find_element_by_id('FILE')
        full_path = os.path.join(fromdir,'cup-xmpp-s2s.der')
        full_path_EC = os.path.join(fromdir,'cup-xmpp-s2s-ECDSA.der')
        logging.info('Upload dir is '+full_path)
        file.send_keys(full_path)
       # browser.execute_script('document.getElementById("FILE").setAttribute("value", "C:\\cup-xmpp-s2s.der")')
        submit_btn = browser.find_element_by_css_selector('input.cuesButton:nth-child(1)')
        submit_btn.click()
        logging.info('Upload dir is ' + full_path_EC)
        file2 = browser.find_element_by_id('FILE')
        #time.sleep(7)
        try:
            file2.send_keys(full_path_EC)
            upload2 = browser.find_element_by_css_selector('input.cuesButton:nth-child(1)')
            upload2.click()
        except:
            logging.exception('')
        browser.close()

        logging.info("Restarting XCP Router")
        myssh = ssh.Ssh(ip)
        myssh.restartService('Cisco XCP Router')
        logging.info('Done')




