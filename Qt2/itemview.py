import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


data = ['budapest', 'london', 'rome', 'paris', 'marokko', 'kenya']


class Model(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)

        for element in data:
            self.appendRow(QtGui.QStandardItem(element))


class TableView(QtGui.QTableView):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.model = Model()
        self.setSortingEnabled(True)
        self.setModel(self.model)
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selectionModel().selectionChanged.connect(self.get_selection)

    def get_selection(self):
        indexes = self.selectionModel().selectedIndexes()
        items = [str(index.data().toPyObject()) for index in indexes]

        print items


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(800, 100, 400, 800)
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
