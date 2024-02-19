from typing import Union

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox
from PyQt5.QtWidgets import QItemDelegate, QCheckBox, QLineEdit

_translate = QtCore.QCoreApplication.translate

from packet_type import ScopeConditions, ScopeModes

CONTEXT = "test_context"


class ItemDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(ItemDelegate, self).__init__(parent)

    def setEditorData(self, editor, index):
        if isinstance(editor, QCheckBox):
            checkState = bool(index.data())
            editor.setChecked(checkState)
            return
        if isinstance(editor, QLineEdit):
            value = index.model().data(index, Qt.EditRole)
            if value is None:
                value = "nan"
            editor.setText(str(value))
            return

        return super(ItemDelegate, self).setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if type(editor) == QCheckBox:
            check_state = editor.isChecked()
            model.setData(index, str(int(check_state)))
            return
        if type(editor) == QLineEdit:
            value = editor.text()
            model.setData(index, value, Qt.EditRole)

        return super(ItemDelegate, self).setModelData(editor, model, index)


class ExampleItemDelegate(ItemDelegate):
    def __init__(self, parent=None):
        super(ItemDelegate, self).__init__(parent)

    def setEditorData(self, editor, index):
        if index.model() and isinstance(editor, (QSpinBox, QDoubleSpinBox)):
            editor.setValue(index.model().data(index, Qt.EditRole))

        if index.model() and isinstance(editor, QComboBox):
            current_value = index.model().data(index, Qt.DisplayRole)
            obj_name = editor.objectName()
            if obj_name == "trigger_condition":
                text_to_set = self.__condition_to_index(current_value)
            elif obj_name == "trigger_mode":
                text_to_set = self.__mode_to_index(current_value)
            else:
                text_to_set = ""

            ind = editor.findText(text_to_set)
            if ind != -1:
                editor.setCurrentIndex(ind)

    def setModelData(self, editor, model, index):
        if isinstance(editor, (QSpinBox, QDoubleSpinBox)):
            editor.interpretText()
            value = editor.value()
            model.setData(index, value, Qt.EditRole)
        if index.model() and isinstance(editor, QComboBox):
            obj_name = editor.objectName()
            if obj_name == "trigger_condition":
                value_to_set = self.__index_to_condition(editor.currentText())
            elif obj_name == "trigger_mode":
                value_to_set = self.__index_to_mode(editor.currentText())
            else:
                value_to_set = None
            model.setData(index, value_to_set, Qt.EditRole)

    @staticmethod
    def __index_to_condition(index_value: str) -> str:
        index_to_condition = {
            _translate(CONTEXT, "< (less)"): ScopeConditions.LESS,
            _translate(CONTEXT, "> (great)"): ScopeConditions.GREAT,
            _translate(CONTEXT, "== (equal)"): ScopeConditions.EQUAL,
            _translate(CONTEXT, "<> (non equal)"): ScopeConditions.NON_EQUAL,
        }
        return index_to_condition[index_value].value

    @staticmethod
    def __condition_to_index(index_value: Union[str, ScopeConditions]) -> str:
        index_to_condition = {
            ScopeConditions.LESS: _translate(CONTEXT, "< (less)"),
            ScopeConditions.GREAT: _translate(CONTEXT, "> (great)"),
            ScopeConditions.EQUAL: _translate(CONTEXT, "== (equal)"),
            ScopeConditions.NON_EQUAL: _translate(CONTEXT, "<> (non equal)"),
        }
        return index_to_condition[index_value]

    @staticmethod
    def __index_to_mode(index_value: str) -> str:
        index_to_mode = {
            _translate(CONTEXT, "Force"): ScopeModes.FORCE,
            _translate(CONTEXT, "Once"): ScopeModes.ONCE,
            _translate(CONTEXT, "Cyclic"): ScopeModes.CYCLIC,
            _translate(CONTEXT, "Repeat"): ScopeModes.REPEAT,
        }
        return index_to_mode[index_value].value

    @staticmethod
    def __mode_to_index(mode: Union[str, ScopeModes]):
        index_to_mode = {
            ScopeModes.FORCE: _translate(CONTEXT, "Force"),
            ScopeModes.ONCE: _translate(CONTEXT, "Once"),
            ScopeModes.CYCLIC: _translate(CONTEXT, "Cyclic"),
            ScopeModes.REPEAT: _translate(CONTEXT, "Repeat"),
        }
        return index_to_mode[mode]
