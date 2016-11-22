import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


data = ['budapest', 'london', 'rome', 'paris']


class Model(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)

        for element in data:
            self.appendRow(QtGui.QStandardItem(element))


class TableView(QtGui.QTableView):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.model = Model()
        self.setModel(self.model)
        # self.QAbstractItemView.NoEditTriggers()
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(50, 100, 400, 800)
        self.table = TableView(self)
        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.table)


def main():
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
