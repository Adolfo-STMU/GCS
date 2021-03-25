import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import MainLayout


class MainWindowUi(MainLayout.Ui_MainWindow):
    # creates window with attributes of Qmainwindow
    def __init__(self, window):
        super(MainWindowUi, self).setupUi(window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi(mainWindow)
    # for var in dir(ui):
    #    print(var)
    mainWindow.showMaximized()
    #for var in dir(mainWindow):
    #    print(var)
    sys.exit(app.exec_())
