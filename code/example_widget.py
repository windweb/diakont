import json
from pathlib import Path
from typing import Optional

from PyQt5.QtCore import (
    QModelIndex,
    Qt,
)
from PyQt5.QtWidgets import QWidget, QDataWidgetMapper, QTreeView, QFileDialog

from example_model import ExampleModel

from examplel_item_delegates import ExampleItemDelegate
from example_form import Ui_ExampleForm


class TestWidget(QWidget, Ui_ExampleForm):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)
        self.test_model: Optional[ExampleModel] = None
        self.setupUi(self)

        self.set_trigger_get_data_button.clicked.connect(
            lambda: self.set_trigger_button_clicked(get_data=True)
        )
        self.set_trigger_button.clicked.connect(
            lambda: self.set_trigger_button_clicked(get_data=False)
        )
        self.reset_trigger_button.clicked.connect(self.reset_trigger_button_clicked)
        self.get_data_button.clicked.connect(self.get_data_button_clicked)

        self.from_file_button.clicked.connect(self.restore_state_from_file)
        self.to_file_button.clicked.connect(self.save_state_to_file)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setOrientation(Qt.Vertical)

    def set_model(self, model: ExampleModel):
        self.test_model = model
        self.mapper.clearMapping()
        self.mapper.setItemDelegate(ExampleItemDelegate(self))
        self.mapper.setModel(model)
        self.mapper.addMapping(self.times, 1)
        self.mapper.addMapping(self.trigger_condition, 2)
        self.mapper.addMapping(self.trigger_mode, 3)
        self.mapper.addMapping(self.threshold_value, 4)
        self.mapper.addMapping(self.start_trigger_name, 5)
        self.mapper.addMapping(self.pretrigger_period_spinbox, 6)
        self.mapper.addMapping(self.posttrigger_period_spinbox, 7)
        index = self.mapper.model().index(0, 0)
        self.mapper.setRootIndex(index)
        self.mapper.setCurrentIndex(1)

    def set_trigger_button_clicked(self, get_data: bool = False) -> None:
        self.test_model.set_trigger(get_data)

    def reset_trigger_button_clicked(self):
        self.test_model.reset_trigger()

    def get_data_button_clicked(self):
        self.test_model.get_data()

    def save_state_to_file(self):
        file_path = QFileDialog.getSaveFileName(
            self,
            caption=self.tr("Select .json file to save" " widget state"),
            filter="*.json",
        )[0]
        if file_path:
            state = self.test_model.to_json()
            with open(file_path, "w") as file:
                json.dump(state, file, indent=4)

    def restore_state_from_file(self):
        file_path = QFileDialog.getOpenFileName(
            self,
            caption=self.tr("Select .json file to load " " widget state"),
            filter="*.json",
        )[0]
        if not file_path:
            return
        if Path(file_path).exists():
            with open(file_path, "r") as file:
                state_to_restore = json.load(file)

                # обновление модели
                self.test_model.load(state_to_restore)

                # обновление представления
                index = self.mapper.model().index(0, 0)
                self.mapper.setRootIndex(index)
                self.mapper.setCurrentIndex(1)



if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    model = ExampleModel()
    widget = TestWidget()

    widget.set_model(model)
    widget.show()

    view = QTreeView()
    view.setWindowTitle("Table")
    view.setModel(model)

    view.show()
    view.setAlternatingRowColors(True)
    view.resize(600, 400)

    sys.exit(app.exec_())
