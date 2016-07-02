import sys
from PySide import QtGui
from PySide import QtCore


class Selector(QtGui.QDialog):
    def __init__(self, text):
        super(Selector, self).__init__()
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        label = QtGui.QLabel(text)
        self.textlabel = QtGui.QLineEdit(self, displayText='qqq')
        btn_ok = QtGui.QPushButton('ok', self)
        btn_ok.clicked.connect(self.accept)
        items = 'abcdefg'.split()
        itemlist = QtGui.QListView()
        model = QtGui.QStandardItemModel(itemlist)
        item = QtGui.QStandardItem()
        item.setText('Item text')
        textual_item = QtGui.QStandardItem('Item text')
        model.appendRow(item)
        itemlist.setModel(model)
        layout.addWidget(label)
        layout.addWidget(self.textlabel)
        layout.addWidget(itemlist)
        layout.addWidget(btn_ok)

class MainWin(QtGui.QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        layout = QtGui.QVBoxLayout()
        self.resize(50, 50)
        self.label = QtGui.QLabel('akjsfg', self)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.changebutton = QtGui.QPushButton('change')
        self.changebutton.clicked.connect(self.change_label)
        layout.addWidget(self.changebutton)

    def change_label(self):
        selector = Selector(self.label.text())
        selector.exec_()
        self.label.setText(selector.textlabel.text())


app = QtGui.QApplication([])
window = MainWin()
window.show()
sys.exit(app.exec_())