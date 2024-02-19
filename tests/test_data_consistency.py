import sys
sys.path.append('code')


from example_widget import TestWidget
import pytest
from PyQt5.QtWidgets import QApplication


@pytest.fixture
def app(qtbot):
    try:
        test_app = QApplication()
        widget = TestWidget()
        qtbot.addWidget(widget)
        return widget
    except Exception as e:
        print(f"Error setting up the app: {e}")
        raise


def test_add_operation_consistency(app, qtbot):
    # Simulate typing a value into an input field
    qtbot.keyClicks(app.inputField, "test value")
    # Simulate clicking the add button
    qtbot.mouseClick(app.addButton, Qt.LeftButton)
    # Verify the expected outcome, e.g., the value appears in a list widget
    assert "test value" in [app.listWidget.item(i).text() for i in range(app.listWidget.count())]