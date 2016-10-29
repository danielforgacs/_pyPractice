import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QListView
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem

# Add some textual items
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]
## Create a Qt application
app = QApplication(sys.argv)

# Our main window will be a QListView
list_ = QListView()
list_.setWindowTitle('Example List_')
list_.setMinimumSize(600, 400)
model = QStandardItemModel(list_)

for food in foods:
    item = QStandardItem(food)
    item.setCheckable(True)
    model.appendRow(item)

list_.setModel(model)
list_.show()
app.exec_()