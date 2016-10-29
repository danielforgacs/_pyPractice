import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


db = [{key: value} for key, value in enumerate(list('abcd'))]
# db = list('abcde')


# class View(QtGui.QTableView):
class View(QtGui.QListView):
    def __init__(self):
        super(View, self).__init__(parent=None)
        model = QtGui.QStandardItemModel()

        for item in db:
            row = QtGui.QStandardItem(str(list(item.keys())[0]))
            model.appendRow(row)

        self.setModel(model)


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        layout = QtGui.QGridLayout()

        view = View()
        layout.addWidget(view)
        self.setLayout(layout)

        self.show()


app = QtGui.QApplication([])
win = Window()

sys.exit(app.exec_())