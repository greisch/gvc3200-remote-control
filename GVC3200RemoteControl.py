#!/bin/python3

'''
### Este programa permite mover la camara PTZ del GrandStream GVC3200
### Osea es un control remoto

# File: GVC3200RemoteControl
# Licencia: Beer-Ware Licence
# Author: Guillermo Reisch <greisch@fenf.edu.uy>

/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * Guillermo Reisch <greisch@fenf.edu.uy> wrote this file.  As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return.   Guillermo Reisch
 * ----------------------------------------------------------------------------
 */
 '''


import sys
from PyQt6 import QtWidgets,QtGui,QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtCore import QUrl
from hashlib import sha256

## Las cosas secretas las guardo en un archivo passwd fuera del sistema de versiones....
import secret

import threading
import time



class GVC3200RemoteControl(QWebEngineView):
    realm = None
    logued = False

    def __init__(self, *args, **kwargs):
        super(GVC3200RemoteControl,  self).__init__(*args, **kwargs)
        self.loadProgress.connect(self.onLoadProgress)
        self.setWindowTitle("GVC3200 Remote Control")
        #start real proccess
        self.load_realm()
    
    def onEnterMouse(self):
        super().onEnterMouse()
        self.setWindowTitle("ME ENTRO!")
        # Por alguna razon esto no funciona...
        ...
  
    def onLoadProgress(self,  porcentage):
        #self.page().runJavaScript('alert("Pika");')
        if porcentage == 100:
            if self.realm == None:
                # In page Realm!
                self.page().toPlainText(self.set_realm)
            elif self.logued == False:
                # In page of Login...!
                self.page().toPlainText(self.check_login_ok)
    
    def check_login_ok(self, response):
        if response.partition('\n')[0] == "Response=Success":
            self.logued = True
            self.load(QUrl(secret.servidor + "/control/video.html?ver=1.0.3.69"))
        else:
            raise Exception("Not logued! Contraseña incorrecta!")
    
    def load_realm(self):
        url = secret.servidor + "/manager?action=loginrealm&time=" + str(round(time.time()))
        self.load(QUrl(url))
    
    def set_realm(self,  value):
        self.realm = value
        # Real is set! Now start Login Proccess!
        self.login()
    
    def login(self):
        if self.realm == None:
            raise Exception("realm is not set! call load_realm() firts")
        username = secret.usuario
        password = secret.contrasenia
        A1 =  username + ":" + self.realm  + ":" + password
        sha = sha256(A1.encode('utf8'))
        url = secret.servidor + "/manager?action=login&Username=" + username + "&Secret=" + sha.hexdigest() + "&t=sha"
        self.load(QUrl(url))


#def threadme(qtw : QWebEngineView):
#    #w.load(QtCore.QUrl("http://www.fenf.edu.uy/bugs"))
#    #w.showNormal()
#    time.sleep(2)
#    #qtw.setWindowTitle("hola!!!!!")
#
#    time.sleep(3)
#    #qtw.load(QUrl("file://"))
#    time.sleep(3)
#    #qtw.page().runJavaScript('alert(document.cookie);')
#    #w.load(QtCore.QUrl("https://www.fenf.edu.uy/bugs/show_bug.cgi?id=7798"))
#    #w.showNormal()



if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=GVC3200RemoteControl()
    #w.showMaximized()
    w.showNormal()
    w.resize(800, 600)
    
    #x = threading.Thread(target=threadme, args=(w,))
    #x.start()

    sys.exit(app.exec())


