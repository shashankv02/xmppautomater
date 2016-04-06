import threading
class UpdatetextBox():
    def __init__(self,tb):
        self.tb=tb
        threading.Thread(target=self.run,args=()).start()

    def run(self):
        while True:
            self.tb.setText(open('log.txt').read())

