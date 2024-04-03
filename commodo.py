# Creating a QSpinBox widget for maximum length
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.max_length_spinbox = QSpinBox()
        self.setCentralWidget(self.max_length_spinbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
