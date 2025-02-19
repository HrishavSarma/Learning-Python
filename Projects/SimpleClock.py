# PyQt5 Simple Digital Clock
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Digital Clock")
        self.setGeometry(200, 300, 700, 100)
        self.setWindowIcon(QIcon("assets/pixil-frame-0.png"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 130px;"
                                      "color: hsl(144, 3%, 17%)")
        self.setStyleSheet("background-color: hsl(39, 20%, 49%)")

        font_id = QFontDatabase.addApplicationFont("E:\\fonts\\installed\\01 DigiGraphics.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        digigraphics = QFont(font_family, 150)
        self.time_label.setFont(digigraphics)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
