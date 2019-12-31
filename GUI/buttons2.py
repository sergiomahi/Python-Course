import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, QLineEdit,
                             QVBoxLayout, QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() # This supper is related to QWidget

        self.init_ui()

    def init_ui(self):
        self.text_label = QLabel("There has been no name entered so I can't do anything yet.")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()

        self.button = QPushButton("Set name")

        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()

        h.addWidget(self.label)
        h.addWidget(self.name_input)
        
        v = QVBoxLayout()

        v.addWidget(self.text_label)
        v.addLayout(h)

        v.addWidget(self.button)

        self.setLayout(v)
        self.setWindowTitle("Nothing has been clicked.")

        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        our_string = "Hello {}".format(inputted_text)
        self.text_label.setText(our_string)
        self.setWindowTitle(inputter_text + "Window")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())