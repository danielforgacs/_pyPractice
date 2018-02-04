import os
import sys
from PyQt4 import QtGui


ROOT_DIR = '/home/ford/Documents/dev'


class RepoModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(RepoModel, self).__init__()
        for item in os.listdir(ROOT_DIR):
            self.appendRow(QtGui.QStandardItem(item))


class RepoList(QtGui.QListView):
    def __init__(self):
        super(RepoList, self).__init__()
        model = RepoModel()
        self.setModel(model)
        selmodel = self.selectionModel()
        selmodel.selectionChanged.connect(self.selected)

    def selected(self, args):
        indexes = args.indexes()
        index = indexes[0]
        qtdata = index.data()
        data = qtdata.toPyObject()
        selected = str(data)
        print data


class MainLayout(QtGui.QVBoxLayout):
    def __init__(self):
        super(MainLayout, self).__init__()
        listview = RepoList()
        self.addWidget(listview)


class MainSimple(QtGui.QWidget):
    def __init__(self):
        super(MainSimple, self).__init__()
        self.show()
        layout = MainLayout()
        self.setLayout(layout)



def main():
    app = QtGui.QApplication(sys.argv)
    mainwin = MainSimple()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
