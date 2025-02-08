# PyQt5 introduction
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon

# Normally LayoutManager cannot be added to mainwindow object,
# we create generic widgets add layout manager to widget and add widget to mainwindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(250, 150, 800, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget() # Generic widget
        self.setCentralWidget(central_widget) # Self is the mwindow

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#4", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: #ba2d2d")
        label2.setStyleSheet("background-color: #375938")
        label3.setStyleSheet("background-color: #7ecfcb")
        label4.setStyleSheet("background-color: #8a3285")
        label5.setStyleSheet("background-color: #8f8022")

        vbox = QVBoxLayout() # create a layout manager
        hbox = QHBoxLayout()
        grid = QGridLayout()

        vbox.addWidget(label1,0,1)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)
        grid.addWidget(label4,1,0)
        grid.addWidget(label5,1,2)

        central_widget.setLayout(vbox)

def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()