from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import MainUi
import MainLayout
import ParametersWidget

from PyQt5.QtCore import QTime, QTimer



class MainWindowUi(MainLayout.Ui_MainWindow):
            def __init__(self):
                super(MainWindowUi, self).__init__()
                size = app.desktop().availableGeometry()

            def setupUi(self, mainWindow):
                super(MainWindowUi, self).setupUi(mainWindow)



class ParametersWidgetUi(ParametersWidget.Ui_ParametersWidget):
    def __init__(self):
       super(ParametersWidgetUi, self).__init__()

    def setupUi2(self, mainWindow2):
        super(ParametersWidgetUi, self).setupUi(mainWindow2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi()
    ui.setupUi(mainWindow)
    mainWindow.showMaximized()


    #app2 = QtWidgets.QDockWidget()
    #mainWindow2 = QtWidgets.QDockWidget()
    #ui2 = ParametersWidgetUi()
    #ui2.setupUi2(mainWindow2)
    #mainWindow2.show()

    sys.exit(app.exec_())