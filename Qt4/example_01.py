import sys
from PyQt4 import QtGui


ROOT_DIR = '/home/ford/Documents/dev'


class RepoModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(RepoModel, self).__init__()
        self.appendRow(QtGui.QStandardItem('A'))
        self.appendRow(QtGui.QStandardItem('B'))
        self.appendRow(QtGui.QStandardItem('C'))
        self.appendRow(QtGui.QStandardItem('E'))


class RepoList(QtGui.QListView):
    def __init__(self):
        super(RepoList, self).__init__()
        model = RepoModel()
        self.setModel(model)


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
