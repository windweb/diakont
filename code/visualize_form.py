import sys
from PyQt5 import QtWidgets
from example_form import Ui_ExampleForm

class ExampleFormWindow(QtWidgets.QWidget, Ui_ExampleForm):
    def __init__(self, *args, **kwargs):
        super(ExampleFormWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleFormWindow()
    mainWin.show()
    sys.exit(app.exec_())
