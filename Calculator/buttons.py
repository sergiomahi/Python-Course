import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QLineEdit,
                             QVBoxLayout, QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() # This supper is related to QWidget

        self.init_ui()
        self.counter = 0

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()

        self.button = QPushButton("Clicked")
        self.button.released.connect(self.releasedButton)
        self.button.clicked.connect(self.clickedButton)

        h = QHBoxLayout()

        h.addWidget(label)
        h.addWidget(name_input)
        
        v = QVBoxLayout()
        v.addLayout(h)

        v.addWidget(self.button)

        self.setLayout(v)
        self.setWindowTitle("Horizontal inside Vertical Layaout")

        self.show()

    def clickedButton(self):
        print("This button has been clicked")

    def releasedButton(self):
        print("This button has been released")
        self.counter += 1
        self.button.setText("Clicked: {}".format(self.counter))
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())