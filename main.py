from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import test4
from DigitalClockFile import DigitalClock
from PyQt5.QtCore import QTime, QTimer



class transformedUI(test4.Ui_Dialog):
            def __init__(self):
                super(transformedUI, self).__init__()

            def setupUi(self, mainWindow):
                super(transformedUI, self).setupUi(mainWindow)
                self.DigitalClock = DigitalClock(self.centralwidget)
                self.DigitalClock.setGeometry(QtCore.QRect(110, 190, 200, 100))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = transformedUI()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())