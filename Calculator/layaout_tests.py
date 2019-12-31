import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout, 
                             QVBoxLayout, QPushButton, QLabel)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__() # This supper is related to QWidget

        self.init_ui()

    def init_ui(self):
        label = QLabel("Hi there, I'm a label")

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        horizontal = QHBoxLayout()

        horizontal.addStretch(1) # So we can change our window size
        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()

        vertical.addStretch(1)
        vertical.addWidget(label)
        vertical.addLayout(horizontal)

        self.setLayout(vertical)
        self.setWindowTitle("Horizontal inside Vertical Layaout")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    sys.exit(app.exec_())