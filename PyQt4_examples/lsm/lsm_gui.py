import sys
from functools import partial
from random import choice
import lsm
from PyQt4 import QtGui


class Button(QtGui.QPushButton):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setMinimumWidth(150)
        self.setMinimumHeight(30)


class MainWindow(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        button_layout = QtGui.QVBoxLayout()
        btn_new = Button(text='new')
        button_layout.addWidget(btn_new)
        btn_delete = Button(text='delete')
        button_layout.addWidget(btn_delete)
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addStretch()
        button_layout.addWidget(Button())

        filter_layout = QtGui.QHBoxLayout()
        filter_line = QtGui.QLineEdit()
        btn_filter_clear = QtGui.QPushButton('clr')
        btn_filter_clear.setMaximumWidth(30)
        filter_layout.addWidget(filter_line)
        filter_layout.addWidget(btn_filter_clear)

        table_layout = QtGui.QVBoxLayout()
        table = QtGui.QTableView()
        table_layout.addLayout(filter_layout)
        table_layout.addWidget(table)

        top_layout = QtGui.QHBoxLayout()
        top_layout.addLayout(button_layout)
        top_layout.addLayout(table_layout)

        log = QtGui.QTextEdit()
        log.setMaximumHeight(50)

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(QtGui.QLineEdit())
        main_layout.addWidget(log)

        model = QtGui.QStandardItemModel()
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setSourceModel(model)
        table.setModel(proxy)

        self.setGeometry(800, 80, 700, 900)
        self.setLayout(main_layout)
        self.show()
        self.populate_model(model)

        btn_new.clicked.connect(partial(self.create_item, model))
        filter_line.textChanged.connect(partial(self.set_table_filter, proxy))
        btn_filter_clear.clicked.connect(filter_line.clear)
        btn_delete.clicked.connect(partial(self.get_selection, table))

    def populate_model(self, model):
        for index, data_item in enumerate(lsm.get_data()):
            row = [QtGui.QStandardItem(row_item)
                        for row_item in data_item]
            model.appendRow(row)

    def create_item(self, model):
        item_name = choice(lsm.db)
        row = [QtGui.QStandardItem(item_name), QtGui.QStandardItem(str(len(item_name)))]
        model.appendRow(row)

    def set_table_filter(self, modelproxy):
        filter_text = self.sender().text()
        modelproxy.setFilterFixedString(filter_text)

    def get_selection(self, table):
        model = table.selectedIndexes()[0].model().sourceModel()
        # items = [str(index.data().toPyObject()) for index in table.selectedIndexes()]
        # print table.selectedIndexes()[0].model().sourceModel()
        items2 = [str(model.index(index.row(), 0).data().toPyObject())
                    for index in table.selectedIndexes()]
        # print items
        print items2


def main():
    app = QtGui.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
