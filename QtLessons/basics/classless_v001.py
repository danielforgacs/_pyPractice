import sys
from PySide import QtGui

app = QtGui.QApplication([])
window = QtGui.QMainWindow()
layout = QtGui.QGridLayout()
table = QtGui.QTableWidget(4, 5)
headers = 'a b c d'.split()
table.Header
layout.addWidget(table)
window.resize(1200, 800)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())