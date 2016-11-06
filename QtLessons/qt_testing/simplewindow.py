"""
limme alone pylint docstring...
"""

import sys
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QtWidgets.QMainWindow):
    """
    class docsting for pylint...
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(600, 400)


def main():
    app = QtWidgets.QApplication([])
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
