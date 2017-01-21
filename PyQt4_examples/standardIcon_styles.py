import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Widget(QWidget):
    def __init__(self, parent= None):
        super(Widget, self).__init__()


        btn_folder = QPushButton("Folder")
        btn_folder.setIcon(self.style().standardIcon(QStyle.SP_DirIcon))

        btn_one = QPushButton("Play")
        btn_one.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        btn_two = QPushButton("Stop")
        btn_two.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))

        btn_three = QPushButton("Pause")
        btn_three.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        layout = QHBoxLayout()
        layout.addWidget(btn_folder)
        layout.addWidget(btn_one)
        layout.addWidget(btn_two)
        layout.addWidget(btn_three)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Widget()
    dialog.show()

    app.exec_()
