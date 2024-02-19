import sys
sys.path.append('code')

import pytest
from PyQt5 import QtCore, QtWidgets, QtGui   # Import QtGui for QMouseEvent
from example_form import Ui_ExampleForm
from enums.global_enums import GlobalErrorMessages


class TestExampleForm:
    @pytest.fixture
    def form(self, qtbot):
        self.widget = QtWidgets.QWidget()  # Use self to retain a reference
        ui = Ui_ExampleForm()
        ui.setupUi(self.widget)
        qtbot.addWidget(self.widget)
        return ui

    def test_initial_state(self, form):
        assert form.from_file_button.text() == GlobalErrorMessages.WRONG_LOAD_FROM_FILE.value  # "Load from file"
        assert form.to_file_button.text() == GlobalErrorMessages.WRONG_SAVE_TO_FILE.value  # "Save to file"
        # Add more assertions here to test initial states of UI components

    def test_button_clicks(self, form, qtbot):
        # Simulate button click and test the response
        qtbot.mouseClick(form.from_file_button, QtCore.Qt.LeftButton)

        # Add assertions to verify the expected outcome of clicking the button
