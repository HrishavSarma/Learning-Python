# PyQt5 Images
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap # Class QPixmap used for handling images, provides functionality for loading manipulating displaying images

# We will load images to a QPixmap object and then add this object to a label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI window")
        self.setGeometry(450, 150, 500, 500)
        self.setWindowIcon(QIcon("stuffs/VictorPFP.png"))

        label = QLabel(self) # self refers to the window object. Window is the parent widget. Label is one of its child widgets
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("stuffs/VictorPFP.png")
        label.setPixmap(pixmap) # We set pixmap object to label

        label.setScaledContents(True) # To scale the image to dimensions

        label.setGeometry((self.width()-label.width()) // 2, # // -> integer division, rounds to the nearest integer
                          (self.height()-label.height()) // 2,
                          label.width(),
                          label.height())

def main(): # boiler plate code
    app = QApplication(sys.argv) # this is for line arguments we might give a []: empty list
    window = MainWindow() # default behaviour of window is to hide it
    window.show()
    sys.exit(app.exec_()) # sys.exit() ensures clean exit, app.exec_() waits for user inputs and other inputs

if __name__ == "__main__":
    main()