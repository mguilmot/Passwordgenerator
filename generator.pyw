import sys, string, random
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

''' To make the icon work in the taskbar in Win7+, ctype is needed'''
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class runApplication(Ui_MainWindow):
    def __init__(self):
        self._translate = QtCore.QCoreApplication.translate
        self.run()
        self.Quit()

    def run(self):
        self.app=QApplication(sys.argv)
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.buttonactions()
        self.window.show()
        self.Quit()

    def buttonactions(self):
        self.ui.pushButtonGenerate.clicked.connect(lambda: self.generate(self.ui.textLength.text()))

    def generate(self,length):   
        def genpwd(length=8,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+"#$%&@!?"):
            '''
            Generates a password. Takes 2 variables:
                length : the length of the generated password
                chars : the characters from which the password is constructed
            '''
            return "".join((char for amount in range(length) for char in chars[random.randint(0,len(chars)-1)]))
        try:
            self.length=int(length)
            self.wrong=False
        except:
            self.length=8
            self.wrong=True
        self.pwd=genpwd(length=self.length)
        if self.wrong == True:
            self.pwd+=" (only input integers!)"
        self.ui.textGenerated.setText(self._translate("MainWindow", self.pwd))

    def Quit(self):
        sys.exit(self.app.exec_())

if __name__=="__main__":
    runApplication()