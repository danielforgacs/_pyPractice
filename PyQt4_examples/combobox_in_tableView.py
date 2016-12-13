import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(3)
        self.setCentralWidget(self.table)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']
        combo_box_options = ["Option 1","Option 2","Option 3"]

        self.table.setRowCount(4)

        for index in range(4):
            item1 = QtGui.QTableWidgetItem(data1[index])
            self.table.setItem(index,0,item1)
            item2 = QtGui.QTableWidgetItem(data2[index])
            self.table.setItem(index,1,item2)
            combo = QtGui.QComboBox()
            for t in combo_box_options:
                combo.addItem(t)
            self.table.setCellWidget(index,2,combo)

def main():
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
