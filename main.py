import sys
from PyQt5.QtWidgets import *
from GUI import Ui_MainWindow
from time import sleep

# proxyChange.py dosyasını import ettik
from proxyChange import *

class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ip   = ""
        self.port = ""
        self.link = "http://aargin.com/"

    def siteyeGit_A(self):
        # Proxyyi siteden çektik, ip ve portu aldık
        # 1 https://gimmeproxy.com/api/getProxy
        # 2 https://api.getproxylist.com/proxy
        proxyCek = requests.get("https://api.getproxylist.com/proxy")
        self.ip,self.port = proxyCek.json()['ip'], str(proxyCek.json()['port'])

        self.ui.lblIp.setText("IP : "+self.ip)
        self.ui.lblPort.setText("PORT : "+self.port)
        self.ui.lblApiSite.setText("API : https://api.getproxylist.com/proxy")

        proxyAyarla(self.ip,self.port,self.link)

    def siteyeGit_M(self):
        proxyAyarla(self.ip,self.port,self.link)

    def getIp(self, ip):
        self.ip = ip
    
    def getPort(self, port):
        self.port = port
    
    def getLink1(self, link):
        self.link = link
    
    def getLink2(self, link):
        self.link = link

if __name__ == '__main__':
    app = QApplication([])
    pencere = Pencere()
    pencere.show()
    app.exec_()