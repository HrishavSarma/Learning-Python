# PyQt5 CheckBoxes
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(250, 150, 800, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))

        self.checkbox = QCheckBox("Do you like food?", self)

        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: times new roman;")
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.check_changed)

    def check_changed(self, state):
        #print(state)
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like foood")


def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()