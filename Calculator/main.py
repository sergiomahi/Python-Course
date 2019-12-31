import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QLineEdit,
                             QVBoxLayout, QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() # This supper is related to QWidget

        self.init_ui()

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()

        button = QPushButton("Set Name")

        h = QHBoxLayout()

        h.addWidget(label)
        h.addWidget(name_input)
        
        v = QVBoxLayout()
        v.addLayout(h)

        v.addWidget(button)

        self.setLayout(v)
        self.setWindowTitle("Horizontal inside Vertical Layaout")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())