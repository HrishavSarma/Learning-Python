# PyQt5 Buttons
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))
        self.button = QPushButton("CLICK ME!", self)
        self.label1 = QLabel("HELLO!", self)
        self.label2 = QLabel("", self) #BACKGROUND
        self.initUI()

    def initUI(self):
        # Without self we declare a local variable
        # self.button = QPushButton("CLICK ME!", self) # local button object
          # with self. the button belongs to the main window 
                                        # self refers to the window
                                        # we put this in the constructor
          # when we create variable or object within a class we should do so in the constructor
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;"
                             "font-weight: bold;"
                             "background-color: #98e3cb;"
                             "color: #54233f;")
        self.button.clicked.connect(self.on_click) # (slot) -> slot is an action the widget is going to take when signal occurs

        self.label1.setGeometry(150,310,200, 50)
        self.label1.setStyleSheet("font-size: 30px;"
                             "font-weight: bold;"
                             "font-style: italic;"
                             "background-color: #9192b5;"
                             "color: #f5f5f5;")
        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        
        #BACKGROUND
        self.label2.setStyleSheet("background-color: #4A5468")
        self.label2.setGeometry(0,0,500,500)
        self.label2.lower()

        # self.grid = QGridLayout()
        # self.grid.addWidget(self.label2,2,2)
        # # central_widget.setLayout(self.grid)

    def on_click(self):
        print("Button Clicked")
        self.button.setText("CLICKED!")

        self.button.setStyleSheet("font-size: 30px;"
                             "font-weight: bold;"
                             "background-color: red;"
                             "color: black;")
        self.button.setDisabled(True)
        self.label1.setText("GOODBYE")
        self.label1.setStyleSheet("font-size: 30px;"
                             "font-weight: bold;"
                             "font-style: italic;"
                             "background-color: black;"
                             "color: #f5f5f5;")
        
        # To make the application quit after 1 second
        QTimer.singleShot(3000, QApplication.quit)
        


def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()