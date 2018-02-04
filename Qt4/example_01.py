import sys
from PyQt4 import QtGui



class MainWindow(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    mainwin = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
