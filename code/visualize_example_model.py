import json
import sys
from PyQt5.QtWidgets import QTreeView, QApplication, QHeaderView
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QObject, Qt, QFileInfo
# from jsonmodel import JsonModel
from example_model import JsonModel


if __name__ == "__main__":
    app = QApplication(sys.argv)  # No changes needed here for PyQt5
    view = QTreeView()
    model = JsonModel()

    view.setModel(model)

    # Adjust the path to your 'example.json' file if necessary
    json_path = QFileInfo(__file__).absoluteDir().filePath("example_widget.json")

    with open(json_path) as file:
        document = json.load(file)
        model.load(document)

    view.show()
    view.header().setSectionResizeMode(QHeaderView.Stretch)  # PyQt5 uses the same method here
    view.setAlternatingRowColors(True)
    view.resize(500, 300)
    sys.exit(app.exec_())
