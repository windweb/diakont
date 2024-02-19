import sys
from PyQt5.QtWidgets import QApplication
from code.example_widget import TestWidget  # Adjust the import path as necessary

def main():
    app = QApplication(sys.argv)
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
