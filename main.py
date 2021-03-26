success = False
error = 0
while success == False:
    try:
        success = True
        import sys
        import MainLayout
        from PyQt5 import QtWidgets
        from PyQt5.QtWidgets import QApplication


    except ImportError as e:
        # To print the error name and string:
        print(e.__class__.__name__,":", e)

        # Workshopping error handling for this, but it corrects itself.
        success = False
        error += 1
        if error >= 2:
            raise RuntimeError("Failed to fix all import errors")
        # This handles the error within the PyQT5 compliation
        # The entire exception reads as:
        # "cannot import name 'QtWebKitWidgets' from 'PyQt5' (/usr/lib/python3/dist-packages/PyQt5/__init__.py)"
        # but it should be sufficient to search for only: 
        # cannot import name 'QtWebKitWidgets' from 'PyQt5'
        if "cannot import name 'QtWebKitWidgets' from 'PyQt5'" in str(e):
            print("Trying to fix ")
            with open("MainLayout.py", "rt") as text_file:
                contents = text_file.read()
                contents = contents.replace('QtWebKitWidgets','QtWebEngineWidgets')
                contents = contents.replace('QWebView','QWebEngineView')
                text_file.close()
            with open("MainLayout.py", "wt") as text_file:
                text_file.write(contents)
                text_file.close()
            continue

class MainWindowUi(MainLayout.Ui_MainWindow):
# creates window with attributes of Qmainwindow
    def __init__(self, window):
        super(MainWindowUi, self).setupUi(window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUi(mainWindow) 
    mainWindow.showMaximized()
    sys.exit(app.exec_())

