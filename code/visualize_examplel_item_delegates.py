import sys
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant

class MyModel(QAbstractTableModel):
    def rowCount(self, parent=QModelIndex()): return 3
    def columnCount(self, parent=QModelIndex()): return 3
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return "Row %s, Column %s" % (index.row() + 1, index.column() + 1)
        return QVariant()

app = QApplication(sys.argv)
table_view = QTableView()
model = MyModel()
table_view.setModel(model)

# Assuming you have setup ExampleItemDelegate correctly
item_delegate = ExampleItemDelegate()
table_view.setItemDelegateForColumn(0, item_delegate)  # Set delegate to the first column for demonstration

table_view.show()
sys.exit(app.exec_())
