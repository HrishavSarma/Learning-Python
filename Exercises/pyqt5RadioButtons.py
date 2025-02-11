# PyQt5 RadioButtons
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(250, 150, 500, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.group1 = QButtonGroup(self)
        self.group2 = QButtonGroup(self)
        self.labelback = QLabel("", self)

        self.initUI()
    
    def initUI(self):
        self.radio1.setGeometry(10, 5, 480, 50)
        self.radio2.setGeometry(10, 60, 480, 50)
        self.radio3.setGeometry(10, 115, 480, 50)
        self.radio4.setGeometry(10, 170, 480, 50)
        self.radio5.setGeometry(10, 225, 480, 50)

        self.labelback.setStyleSheet("background-color: #4A5468")
        self.labelback.setGeometry(0,0,500,500)
        self.labelback.lower()

        self.setStyleSheet("QRadioButton{" # TO make all buttons have same stylesheet
                           "font-size: 30px;"
                           "font-family: arial;"
                           "font-weight: bold;"
                           "padding: 10px;"
                           "Background-color: grey;"
                           "}")
        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group2.addButton(self.radio4)
        self.group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()