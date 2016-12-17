import sys
from functools import partial
from random import choice
from PyQt4 import QtGui
from PyQt4 import QtCore
import lsm


class Button(QtGui.QPushButton):
    def __init__(self, mini=False, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.setMinimumHeight(30)

        if mini:
            self.setMaximumWidth(45)
        else:
            self.setMinimumWidth(150)


class LogWidget(QtGui.QTextEdit):
    def __init__(self, *args, **kwargs):
        super(LogWidget, self).__init__(*args, **kwargs)
        self.setMaximumHeight(175)

    @property
    def history(self):
        return self.toPlainText() + '\n'

    @property
    def entry(self):
        pass

    @entry.setter
    def entry(self, text):
        # self.setText(self.history+'--> '+text)
        self.setText(self.history+text)
        self.moveCursor(QtGui.QTextCursor.End)

    @property
    def tab_entry(self):
        pass

    @tab_entry.setter
    def tab_entry(self, text):
        self.setText(self.history+'        '+text)
        self.moveCursor(QtGui.QTextCursor.End)

    @property
    def list_entry(self):
        pass

    @list_entry.setter
    def list_entry(self, entries):
        list_string = ', '.join(entries)
        self.tab_entry = list_string


class MainWindow(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.log = LogWidget()

        button_layout = QtGui.QVBoxLayout()
        button_new = Button(text='new')
        button_showselected = Button(text='show selected')
        button_layout.addWidget(button_new)
        button_layout.addWidget(button_showselected)
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addWidget(Button())
        button_layout.addStretch()
        button_layout.addWidget(Button())

        filter_layout = QtGui.QHBoxLayout()
        filterstring = QtGui.QLineEdit()
        button_clearfilter = Button(text='clr', mini=True)
        filter_layout.addWidget(filterstring)
        filter_layout.addWidget(button_clearfilter)

        table_layout = QtGui.QVBoxLayout()
        tableview = QtGui.QTableView()
        table_layout.addLayout(filter_layout)
        table_layout.addWidget(tableview)

        top_layout = QtGui.QHBoxLayout()
        top_layout.addLayout(button_layout)
        top_layout.addLayout(table_layout)

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.log)

        model = QtGui.QStandardItemModel()
        proxymodel = QtGui.QSortFilterProxyModel()
        proxymodel.setSourceModel(model)
        tableview.setModel(proxymodel)

        self.setGeometry(800, 80, 700, 950)
        self.setLayout(main_layout)
        self.show()
        self.populate_model(model)

        button_clearfilter.clicked.connect(filterstring.clear)
        button_new.clicked.connect(partial(self.create_new_item, model))
        button_showselected.clicked.connect(partial(self.list_selection,
                                            tableview=tableview))
        filterstring.textChanged.connect(partial(self.set_tableview_filter,
                                                proxymodel=proxymodel))
        tableview.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        tableview.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        tableview.setSortingEnabled(True)

        tableview.doubleClicked.connect(partial(self.show_item, tableview))
        button_showselected.clicked.connect(partial(self.show_item, tableview))

        tableview.verticalHeader().setVisible(False)
        tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        model.setHorizontalHeaderLabels(['item', 'length'])

    def populate_model(self, model):
        self.log.entry = 'populating model:'

        for index, data_item in enumerate(lsm.get_data()):
            row = [QtGui.QStandardItem(row_item) for row_item in data_item]
            model.appendRow(row)
            self.log.tab_entry = 'added item:'+data_item[0]

            if index == 7:
                break

    def create_new_item(self, model):
        self.log.entry = 'creating new item'
        newname = choice(lsm.db)

        for oldname in self.generate_model_items(model):
            if newname == oldname:
                self.log.tab_entry = 'item is duplicate: '+newname
                return

        row = [QtGui.QStandardItem(newname), QtGui.QStandardItem(str(len(newname)))]
        model.appendRow(row)
        self.log.tab_entry = 'added item: '+newname

    def set_tableview_filter(self, proxymodel):
        filter_text = self.sender().text()
        proxymodel.setFilterFixedString(filter_text)
        self.log.entry = 'filter set to: ' + filter_text

    def list_selection(self, tableview):
        self.log.entry = 'listing selection:'
        item_set = {str(index.model().index(index.row(), 0).data().toPyObject())
                            for index in tableview.selectedIndexes()}
        items = list(item_set)
        self.log.list_entry = items

        return items

    def show_item(self, tableview):
        item_list = self.list_selection(tableview=tableview)
        self.log.entry = 'showing items'
        self.log.list_entry = item_list

    def generate_model_items(self, model):
        for k in range(model.rowCount()):
            yield model.index(k, 0).data().toPyObject()


def main():
    app = QtGui.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
