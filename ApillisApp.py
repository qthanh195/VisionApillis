from PySide6.QtWidgets import QApplication
from frontpage import MySideBar
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MySideBar()
    widget.show()
    sys.exit(app.exec())
