# import sys
# import json
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget
# from PyQt5.QtCore import QFileInfo, QAbstractItemModel, QModelIndex, Qt
# from example_model import JsonModel
# from example_widget import TestWidget
# from PyQt5.QtWidgets import QHeaderView

import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QHeaderView
from PyQt5.QtCore import QFileInfo, QAbstractItemModel, QModelIndex, Qt
from example_model import JsonModel
from example_widget import TestWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Example Application")

        # Создаем модель и загружаем данные
        self.model = JsonModel()
        json_path = QFileInfo(__file__).absoluteDir().filePath("example.json")
        with open(json_path) as file:
            document = json.load(file)
            self.model.load(document)

        # Создаем виджет для отображения данных модели
        self.view = QTreeView()
        self.view.setModel(self.model)
        self.view.header().setSectionResizeMode(QHeaderView.Stretch)
        self.view.setAlternatingRowColors(True)

        # Создаем пользовательский виджет для взаимодействия с данными
        self.test_widget = TestWidget()
        self.test_widget.set_model(self.model)

        # Устанавливаем макет для главного окна
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(self.test_widget)

        # Устанавливаем центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()