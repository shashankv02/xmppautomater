import sleekxmpp
import sys


if sys.version_info < (3,0):
    sys.setdefaultencoding('utf8')


class EchoBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid,password)

        #XMPP spec requires clients to broadcast its presence and retreive its roster
        #once it conects and a establishes a session with XMPP Server. Until this is done
        # server may not deliver or send messages or presence notifications to client.
        # So do these two tasks once sessiosn is started
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.message)  #when <message /> stanza is receieved

        #event handler start accepts a single paramter which typically is a stanza
        #that caused the event. In this case event wil be a empty dictionary

        #send_presence and get_roster are lib methods
        #send_presence() with no args sens simplest stanza <presence />

    def start(self, event):
        print('in start')
        self.send_presenece()
        try:
            self.get_roster()   #will send a IQ stanza requesting roster to server and waits for response
                            #roster dats received is stores in self.client_roster            except:
            print(self.client_roster)
        except:
            print('excpetion in get')


    def message(self, msg):
        #msg.reply("Received:\n%s" % msg['body']).send()  #reply handles setting to  JID
            print("recvd msg")
            print(msg)


##USAGE:
#jabber = EchoBot('USERNAME', 'PASSWORD')
#jabber.register_plugin('xep_0030')
#jabber.register_plugin('xep_0199')

#con = jabber.connect(address=('HOSTNAME','5222'))
#if con:
 #   print('connected')
    #jabber.process(block=True)
  #  jabber.send_message(mto='USERNAME', mbody='hello')
  #  jabber.process(block=True)
  #  jabber.disconnect(wait=True)

#else:
 #   print('Unable to connect')
