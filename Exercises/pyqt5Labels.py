# PyQt5 Labels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LabelsIntro")
        self.setGeometry(250, 150, 800, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))

        label = QLabel("Hello", self) # self meaning the window
        label.setFont(QFont("Ariel", 48))
        label.setGeometry(0,0,800,100)
        label.setStyleSheet("color: #7a7a7a;"
                            "background-color: #8cffff;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
       
        # label.setAlignment(Qt.AlignRight) #label.setAlignment(flags)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignLeft)

        label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)


def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()