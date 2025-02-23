from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from frontpage import MySideBar
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MySideBar()
    widget.setWindowTitle("Vision System")
    widget.setWindowIcon(QIcon("logo.png"))  # Thêm logo vào thanh tiêu đề
    widget.showMaximized()
    sys.exit(app.exec())
