import sys
sys.path.append('code')

import pytest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from example_widget import TestWidget
from example_model import ExampleModel
from example_form import Ui_ExampleForm
from PyQt5.QtTest import QTest
import time


@pytest.fixture
def setup_ui(qtbot):
    app = QApplication([])
    ui1 = TestWidget()
    ui2 = TestWidget()
    qtbot.addWidget(ui1)
    qtbot.addWidget(ui2)
    ui1.show()  # Ensure UI is visible for interaction
    ui2.show()
    return ui1, ui2, qtbot


def test_ui_element_interactions(setup_ui):
    ui1, ui2, qtbot = setup_ui

    # Simulate text input in ui1 and verify update in ui2
    QTest.keyClicks(ui1.some_text_input, 'Test Input')
    qtbot.wait(100)  # Wait for the UI to update
    assert ui2.some_display_element.text() == 'Test Input'

    # Simulate button click and verify action performed
    QTest.mouseClick(ui1.some_button, Qt.LeftButton)
    qtbot.wait(100)  # Wait for action to complete
    # Assert some expected outcome, e.g., a dialog opens, or data changes


def test_data_binding_validation(setup_ui):
    ui1, ui2, _ = setup_ui
    # Directly modify the data model and verify UI updates
    ui1.model.some_data_attribute = 'New Value'
    assert ui1.some_ui_element.text() == 'New Value'
    assert ui2.some_ui_element.text() == 'New Value'


def test_error_handling(setup_ui):
    ui1, _, qtbot = setup_ui
    # Trigger an error condition, e.g., invalid file format
    QTest.mouseClick(ui1.load_button, Qt.LeftButton)
    qtbot.waitUntil(lambda: ui1.error_dialog.isVisible(), timeout=1000)
    assert ui1.error_dialog.text() == "Expected error message"


def test_performance(setup_ui):
    ui1, _, qtbot = setup_ui
    start_time = time.time()
    # Perform an action expected to be intensive
    QTest.mouseClick(ui1.load_large_dataset_button, Qt.LeftButton)
    qtbot.waitUntil(lambda: not ui1.loading_indicator.isVisible(), timeout=10000)
    end_time = time.time()
    assert end_time - start_time < 5  # Example: Assert it completes within 5 seconds
