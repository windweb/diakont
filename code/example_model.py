from pathlib import Path
from typing import Any, Union, Tuple

from PyQt5.QtCore import QObject, Qt, QModelIndex

from jsonmodel import JsonModel, TreeItem, _translate
from packet_type import ScopeMethods, RequestTypes


class ExampleItem(TreeItem):
    def __init__(self, parent: QObject = None):
        super(ExampleItem, self).__init__(parent)


class Controls:
    @staticmethod
    def make_command(command_type: RequestTypes, name, method, arguments=None) -> Tuple[int, dict]:
        final_request = {"Type": command_type, "Name": name, "Method": method}
        if arguments is not None:
            final_request["Arguments"] = arguments
        return final_request

    def make_request(self, request):
        pass


class ExampleModel(JsonModel, Controls):
    item_type = ExampleItem
    context = "context"

    def __init__(self, parent: QObject = None):
        super(ExampleModel, self).__init__(parent)
        self.load(None)

    def load(self, document: Union[dict, list, tuple]):
        base_model = {
            "Values": [],
            "Times": 0,
            "Condition": "Equal",
            "Mode": "Cyclic",
            "Threshold": 0,
            "Trigger": "Cpu Debug",
            "PreTrigger": 0,
            "PostTrigger": 0,
        }
        dict_to_load = {}
        if isinstance(document, dict):
            dict_to_load = {
                "Values": document.get("Values", []),
                "Times": document.get("Times", 0),
                "Condition": document.get("Condition", "Equal"),
                "Mode": document.get("Mode", "Cyclic"),
                "Threshold": document.get("Threshold", 0),
                "Trigger": document.get("Trigger", ""),
                "PreTrigger": document.get("PreTrigger", 0),
                "PostTrigger": document.get("PostTrigger", 0),
            }
        elif isinstance(document, list):
            listed_dict = document[0]
            if isinstance(listed_dict, dict):
                dict_to_load = {
                    "Values": listed_dict.get("Values", []),
                    "Times": listed_dict.get("Times", 0),
                    "Condition": listed_dict.get("Condition", "Equal"),
                    "Mode": listed_dict.get("Mode", "Cyclic"),
                    "Threshold": listed_dict.get("Threshold", 0),
                    "Trigger": listed_dict.get("Trigger", ""),
                    "PreTrigger": listed_dict.get("PreTrigger", 0),
                    "PostTrigger": listed_dict.get("PostTrigger", 0),
                }
        else:
            dict_to_load = base_model
        super().load([dict_to_load])

    def data(self, index: QModelIndex, role: Qt.ItemDataRole) -> Any:
        """Override from QAbstractItemModel

        Return data from a json item according index and role

        """
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.DisplayRole:
            if role == Qt.DisplayRole:
                if index.column() == 0:
                    return _translate(self.context, item.key)

                if index.column() == 1:
                    return item.value

        elif role == Qt.EditRole:
            if index.column() == 1:
                return item.value

    def setData(self, index: QModelIndex, value: Any, role: Qt.ItemDataRole):
        item = index.internalPointer()
        if role == Qt.DisplayRole:
            if index.column() == 1:
                item.value = value
                self.dataChanged.emit(index, index, [])
                return True
        if role == Qt.EditRole:
            if index.column() == 1:
                item = index.internalPointer()
                item.value = value

                self.dataChanged.emit(index, index, [Qt.EditRole])

                return True

        return False

    def signals_list_index(self):
        root_index = self.index(0, 0)
        for j in range(self.rowCount(root_index)):
            idx = self.index(j, 0, root_index)
            if self.data(idx, Qt.DisplayRole) == "Values":
                return idx

    def set_trigger(self, get_data: bool = False):
        arguments = self.to_json()
        if get_data:
            method = ScopeMethods.REQUEST
        else:
            method = ScopeMethods.SETUP
        set_trigger_request = self.make_command(
            RequestTypes.SCOPE, "", method, arguments[0]
        )
        self.make_request(set_trigger_request)

    def reset_trigger(self):
        """
        Команда на сброс триггера в осциллографе
        AsyncConnector возвращает словарь с пустым значением
        :return:
        """
        reset_trigger_request = self.make_command(
            RequestTypes.SCOPE, "", ScopeMethods.RESET
        )
        self.make_request(reset_trigger_request)

    def get_data(self):
        set_data_request = self.make_command(
            RequestTypes.SCOPE, "", ScopeMethods.DOWNLOAD
        )
        self.make_request(set_data_request)

