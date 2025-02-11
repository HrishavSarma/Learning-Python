# PyQt5 CSS Styles
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))

        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    def initUI(self):
        central_widgets = QWidget()
        self.setCentralWidget(central_widgets)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widgets.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet(""" 
            QPushButton{
                            font-size: 30px;
                            font-family: arial;
                            padding: 15px 75px;
                            margin: 25px;
                            border: 3px solid;
                            border-radius: 15px;
                            color: hsl(0, 0%, 0%)
                        }
            QPushButton#button1{
                           background-color: hsl(0, 100%, 68%);
                        }
            QPushButton#button2{
                           background-color: hsl(134, 100%, 68%);
                        }
            QPushButton#button3{
                           background-color: hsl(217, 100%, 68%);
                        }
            QPushButton#button1:hover{
                           background-color: hsl(0, 100%, 78%);
                           border: None;
                           color: hsl(0, 0%, 20%)
                        }
            QPushButton#button2:hover{
                           background-color: hsl(134, 100%, 78%);
                           border: None;
                           color: hsl(0, 0%, 20%)
                        }
            QPushButton#button3:hover{
                           background-color: hsl(217, 100%, 78%);
                           border: None;
                           color: hsl(0, 0%, 20%)
                        }
        """)

def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()