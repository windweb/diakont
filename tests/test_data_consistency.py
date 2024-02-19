"""
Проверка согласованности данных
Этот тест гарантирует, что изменения в одном виджете отражаются в другом, проверяя синхронизацию данных.
"""
import sys
sys.path.append('code')

import pytest
from PyQt5.QtWidgets import QApplication
from example_widget import TestWidget
from example_model import ExampleModel

@pytest.fixture(scope='module')
def setup_test_environment(qtbot):
    app = QApplication([])
    model = ExampleModel()
    widget1 = TestWidget()
    widget1.set_model(model)
    widget2 = TestWidget()
    widget2.set_model(model)
    qtbot.addWidget(widget1)
    qtbot.addWidget(widget2)
    return widget1, widget2, model

def test_data_consistency(setup_test_environment):
    widget1, widget2, model = setup_test_environment
    # Simulate data change in widget1
    model.setData(model.index(0, 0), 'New Value', Qt.EditRole)
    # Assert that widget2 reflects the change
    assert widget1.mapper.mappedWidgetAt(0).text() == 'New Value'
    assert widget2.mapper.mappedWidgetAt(0).text() == 'New Value'

# """
# Этот тест проверяет функциональность сохранения в файл и загрузки из файла,
# обеспечивая сохранение состояния в разных сессиях.
# """
#
# tmpdir = sys.path
# def test_save_and_load(setup_test_environment, tmpdir):
#     widget1, _, model = setup_test_environment
#     # Simulate data change
#     model.setData(model.index(0, 0), 'Test Save', Qt.EditRole)
#     # Save current state to a temporary file
#     tmp_file = tmpdir.join("example.json")
#     widget1.save_state_to_file(str(tmp_file))
#     # Reset model to initial state
#     model.load(None)
#     # Load state from file
#     widget1.restore_state_from_file(str(tmp_file))
#     # Verify that the state has been restored
#     assert model.data(model.index(0, 0), Qt.DisplayRole) == 'Test Save'

# from example_widget import TestWidget
# import pytest
# from PyQt5.QtWidgets import QApplication
#
#
# @pytest.fixture
# def app(qtbot):
#     try:
#         test_app = QApplication()
#         widget = TestWidget()
#         qtbot.addWidget(widget)
#         return widget
#     except Exception as e:
#         print(f"Error setting up the app: {e}")
#         raise
#
#
# def test_add_operation_consistency(app, qtbot):
#     # Simulate typing a value into an input field
#     qtbot.keyClicks(app.inputField, "test value")
#     # Simulate clicking the add button
#     qtbot.mouseClick(app.addButton, Qt.LeftButton)
#     # Verify the expected outcome, e.g., the value appears in a list widget
#     assert "test value" in [app.listWidget.item(i).text() for i in range(app.listWidget.count())]