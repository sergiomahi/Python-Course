import sys
from  PyQt5.QtWidgets import *
from  PyQt5.QtGui     import *
from  PyQt5.QtCore    import *

class Button():
    def __init__(self, text, results):
        real_text = str(text)
        self.b = QPushButton(real_text)
        self.text = real_text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        print("Clicked {}".format(v) )


class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.createApp()

    def createApp(self):
        # Create grid.
        grid = QGridLayout()

        results = QLineEdit()
        grid.addWidget(results, 0, 0, 1, 4)

        buttons = ["AC", "C", "CE", "/", 
                    7, 8, 9, "*",
                    4, 5, 6, "-",
                    1, 2, 3, "+",
                    0, ".", "=" ]


        row = 1
        col = 0

        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            

            b_object = Button(button, results)
            if button == 0:
                grid.addWidget(b_object.b, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(b_object.b, row, col, 1, 1)

            col += 1

       

        self.setLayout(grid)
        self.show()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Application()

    sys.exit(app.exec_())
