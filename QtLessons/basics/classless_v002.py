import sys
from PySide import QtGui
from PySide import QtCore

def on_click():
    print 'CLK'

class Button(QtGui.QPushButton):
    def __init__(self, label=None):
        super(Button, self).__init__(text=label)

app = QtGui.QApplication([])
mainwindow = QtGui.QWidget()
layout = QtGui.QGridLayout()
button1 = Button('bla')
button2 = Button('alb')
# style = QtGui.QStyle()
# button.clicked.connect(on_click)
layout.addWidget(button1)
layout.addWidget(button2)
mainwindow.setLayout(layout)
mainwindow.resize(800, 400)
mainwindow.style()
mainwindow.show()
sys.exit(app.exec_())