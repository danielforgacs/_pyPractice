import sys
from PyQt5 import QtWidgets


class MainWin(QtWidgets.QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.show()


def main():
    app = QtWidgets.QApplication([])
    mainwin = MainWin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()