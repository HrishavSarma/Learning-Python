# PyQt5 LineEdits
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(250, 150, 500, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))

        self.line_edit1 = QLineEdit(self)
        self.button = QPushButton("SUBMIT", self)
        self.initUI()

    def initUI(self):
        self.line_edit1.setGeometry(10,10, 250,40)
        self.button.setGeometry(265, 10, 100, 40)

        self.line_edit1.setStyleSheet("font-size: 30px;"
                                      "font-family: arial;"
                                      "font-weight: bold")
        self.button.setStyleSheet("font-size: 20px;"
                                  "font-family: times new roman;"
                                  "font-weight: bold;"
                                  "background-color: red;"
                                  "color: black;")
        
        self.line_edit1.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.when_submit_clicked)
        
    def when_submit_clicked(self):
        print("Submitted")
        text = self.line_edit1.text()
        print(f"Hello {text}")

def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()