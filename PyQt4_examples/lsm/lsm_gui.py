import sys
from functools import partial
from random import choice
import lsm
from PyQt4 import QtGui
from PyQt4 import QtCore


class Button(QtGui.QPushButton):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setMinimumWidth(150)
        self.setMinimumHeight(30)


class NewDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.button_ok = QtGui.QPushButton('Ok', self)
        self.button_ok.clicked.connect(self.accept)
        self.button_cancel = QtGui.QPushButton('Cancel', self)
        self.button_cancel.clicked.connect(self.reject)
        self.button_ok.setMinimumHeight(30)
        self.button_cancel.setMinimumHeight(30)
        # self.burrowsname_widget = BurrowsNameWidget(parent=self)
        # self.valid_name = self.burrowsname_widget.valid_name
        layout = QtGui.QGridLayout(self)
        layout.addWidget(QtGui.QLineEdit(), 0, 0)
        # layout.addWidget(self.burrowsname_widget, 0, 0)
        layout.addWidget(self.button_ok, 1, 0)
        layout.addWidget(self.button_cancel, 2, 0)
        self.setWindowTitle('Name Judge')



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

        btn_filter_clear.clicked.connect(filter_line.clear)
        btn_new.clicked.connect(partial(self.create_item, model))
        btn_delete.clicked.connect(partial(self.get_selection, table))

        filter_line.textChanged.connect(partial(self.set_table_filter, proxy))

        table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        table.setSortingEnabled(True)

        table.doubleClicked.connect(self.show_item)

    def populate_model(self, model):
        for index, data_item in enumerate(lsm.get_data()):
            row = [QtGui.QStandardItem(row_item) for row_item in data_item]
            model.appendRow(row)

    def create_item(self, model):
        new_dialog = NewDialog()
        # new_dialog.addWidget(Button('ok'))

        if new_dialog.exec_() is QtGui.QDialog.Accepted:
            print 'accepted'



        # item_name = choice(lsm.db)
        # row = [QtGui.QStandardItem(item_name), QtGui.QStandardItem(str(len(item_name)))]
        # model.appendRow(row)

    def set_table_filter(self, modelproxy):
        filter_text = self.sender().text()
        modelproxy.setFilterFixedString(filter_text)

    def get_selection(self, table):
        items = {str(index.model().index(index.row(), 0).data().toPyObject())
                            for index in table.selectedIndexes()}

        return list(items)

    def show_item(self):
        table = self.sender()
        items = self.get_selection(table=table)
        print items


def main():
    app = QtGui.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
