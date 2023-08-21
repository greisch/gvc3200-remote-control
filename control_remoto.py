import sys
from PyQt6 import QtWidgets,QtGui,QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebEngineWidgets import *

## Las cosas secretas las guardo en un archivo passwd fuera del sistema de versiones....
from passwd import url_login

import threading
import time


def thread_function(name):
    #logging.info("Thread %s: starting", name)
    time.sleep(2)
    #logging.info("Thread %s: finishing", name)


#if __name__ == "__main__":
#   format = "%(asctime)s: %(message)s"
#    logging.basicConfig(format=format, level=logging.INFO,
#                        datefmt="%H:%M:%S")
#    logging.info("Main    : before creating thread")
#    x = threading.Thread(target=thread_function, args=(1,))
#    logging.info("Main    : before running thread")
#    x.start()
#   logging.info("Main    : wait for the thread to finish")
#    # x.join()
#    logging.info("Main    : all done")



class MyQWebEngineView(QWebEngineView):
    def __init__(self):
        super().__init__()


    def loadFinished(self,  a0):
        super().loadFinished(a0)
        print("llamaron a finished")
        self.title = "juancho"

#sys.stdout.writelines("hola")


def threadme(qtw : QWebEngineView):
    time.sleep(3)
    #w.load(QtCore.QUrl("http://www.fenf.edu.uy/bugs"))
    #w.showNormal()
    time.sleep(5)
    w.setWindowTitle("hola!!!!!")
    #w.load(QtCore.QUrl("https://www.fenf.edu.uy/bugs/show_bug.cgi?id=7798"))
    #w.showNormal()

    
    


if __name__ == "__main__":
    url_base = 'http://192.168.10.129/'
    url = 'control/video.html?ver=1.0.3.69'
    url2= 'control/video.html'
    app=QtWidgets.QApplication(sys.argv)
    #windows = QMainWindow()
    #windows.setWindowTitle("JUANCHO PAMZA")
    w=MyQWebEngineView()
    w.setWindowTitle("GVC3200 Remote Control")
    w.load(QtCore.QUrl(url_base + url_login) )
    w.showNormal()
    x = threading.Thread(target=threadme, args=(w,))
    x.start()

    #w.showMaximized()
    sys.exit(app.exec())


