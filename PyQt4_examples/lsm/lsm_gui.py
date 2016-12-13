import sys
from functools import partial
import lsm
from PyQt4 import QtGui


class Button(QtGui.QPushButton):
    def __init__(self, text='-', parent=None):
        super(Button, self).__init__(text=text, parent=parent)
        self.setMinimumWidth(150)
        self.setMinimumHeight(30)


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        main_layout = QtGui.QVBoxLayout()
        button_layout = QtGui.QVBoxLayout()
        btn_new = Button(text='new')
        filter_layout = QtGui.QHBoxLayout()
        filter_line = QtGui.QLineEdit()
        filter_layout.addWidget(filter_line)
        filter_layout.addWidget(QtGui.QPushButton('clr'))
        button_layout.addWidget(btn_new)
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addStretch()
        button_layout.addWidget(Button())
        table_layout = QtGui.QVBoxLayout()
        table_layout.addLayout(filter_layout)
        top_layout = QtGui.QHBoxLayout()
        top_layout.addLayout(button_layout)
        table = QtGui.QTableView()
        table_layout.addWidget(table)
        top_layout.addLayout(table_layout)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(QtGui.QLineEdit())
        log = QtGui.QTextEdit()
        log.setMaximumHeight(50)
        main_layout.addWidget(log)
        model = QtGui.QStandardItemModel()
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setSourceModel(model)
        table.setModel(proxy)
        btn_new.clicked.connect(partial(self.create_item, model))
        filter_line.textChanged.connect(partial(self.set_table_filter, proxy))
        self.populate_model(model)
        self.setGeometry(100, 100, 700, 800)
        self.setLayout(main_layout)
        self.show()

    def populate_model(self, model):
        for index, item in enumerate(lsm.get_data()):
            qt_item = QtGui.QStandardItem
            row = [qt_item(item), qt_item(str(index))]
            model.appendRow(row)

    def create_item(self, model):
        row = [QtGui.QStandardItem('hehe'), QtGui.QStandardItem('str(index)')]
        model.appendRow(row)

    def set_table_filter(self, modelproxy):
        print self.sender().text()
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
