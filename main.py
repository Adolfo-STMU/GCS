from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import MainUi
import MainLayoutTest5
import Parameters
import MissionPlanner
from DigitalClockFile import DigitalClock
from PyQt5.QtCore import QTime, QTimer



class MainWindowUi(MainLayoutTest5.Ui_MainWindow):
            def __init__(self):
                super(MainWindowUi, self).__init__()
                size = app.desktop().availableGeometry()

            def setupUi(self, mainWindow):
                super(MainWindowUi, self).setupUi(mainWindow)

                #self.DigitalClock = DigitalClock(self.centralwidget)
                #self.DigitalClock.setGeometry(QtCore.QRect(110, 190, 200, 100))
            #def layoutswitch1 (self,):



#class MissionPlannerWindowUi(MissionPlanner.Ui_Mission_Planner):
#    def __init__(self):
#        super(MissionPlannerWindowUi, self).__init__()

#    def setupUi2(self, mainWindow2):
#        super(MissionPlannerWindowUi, self).setupUi(mainWindow2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi()
    ui.setupUi(mainWindow)
    mainWindow.showMaximized()

#    app2 = QtWidgets.QApplication(sys.argv)
#    mainWindow2 = QtWidgets.QMainWindow()
#    ui2 = MissionPlannerWindowUi()
#    ui2.setupUi2(mainWindow2)
#    mainWindow2.show()

    sys.exit(app.exec_())