import sys
from PyQt5 import QtWidgets



class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainwin = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
