import sys
from PyQt4 import QtGui


ROOT_DIR = '/home/ford/Documents/dev'


class RepoModel(QtGui.QStandardItemModel):
    def __init__(self):
        super(RepoModel, self).__init__()
        self.appendRow(QtGui.QStandardItem('sdkfj'))
        self.appendRow(QtGui.QStandardItem('sdkfj'))
        self.appendRow(QtGui.QStandardItem('sdkfj'))
        self.appendRow(QtGui.QStandardItem('sdkfj'))




class RepoList(QtGui.QListView):
    def __init__(self):
        super(RepoList, self).__init__()
        self.setModel = RepoModel()


class MainLayout(QtGui.QVBoxLayout):
    def __init__(self):
        super(MainLayout, self).__init__()
        repolist = RepoList()
        self.addWidget(repolist)


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = MainLayout()
        self.setLayout(layout)
        self.show()


class MainSimple(QtGui.QWidget):
    def __init__(self):
        super(MainSimple, self).__init__()
        self.show()
        listview = QtGui.QListView()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(listview)
        # model = QtGui.QStandardItemModel()
        model = RepoModel()
        self.setLayout(layout)
        listview.setModel(model)
        model.appendRow(QtGui.QStandardItem('zdkfg'))



def main():
    app = QtGui.QApplication(sys.argv)
    mainwin2 = MainWindow()
    mainwin = MainSimple()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
