import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0 , 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.lap_button = QPushButton("Lap", self)
        self.lap_times_display = QTextEdit(self)
        self.timer = QTimer(self)
        self.lap_times = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My StopWatch")
        self.setWindowIcon(QIcon("assets/pixil-frame-1.png"))
        self.setGeometry(400, 150, 500, 400)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.lap_button)

        vbox.addLayout(hbox)

        # Add a QTextEdit to display lap times
        self.lap_times_display.setReadOnly(True)
        vbox.addWidget(self.lap_times_display)

        self.start_button.setObjectName("START")
        self.stop_button.setObjectName("STOP")
        self.reset_button.setObjectName("RESET")
        self.lap_button.setObjectName("LAP")

        self.setStyleSheet("""
            QPushButton, QLabel{
                           padding: 10px;
                           font-family: calibri;
                           }
            QPushButton{
                           font-size: 50px;
                           background-color: hsl(170, 14%, 75%)
                           
                           }
            QPushButton#START:hover{
                           background-color: hsl(122, 100%, 31%);
                           }
            QPushButton#STOP:hover{
                           background-color: hsl(0, 79%, 38%);
                           }
            QPushButton#RESET:hover{
                           background-color: grey;
                           }
            QPushButton#LAP:hover{
                           background-color: hsl(242, 57%, 63%);
                           }
            QLabel{
                           font-size: 120px;
                           background-color: hsl(170, 22%, 50%);
                           border-radius: 5px;
                           font-weight: bold;
                           }
            QTextEdit {
                           font-family: arial;
                           font-size: 20px;
                           background-color: hsl(186, 24%, 80%);
                           border-radius: 5px;
                           font-weight: bold;
                           padding: 10px;
                           }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.lap_button.clicked.connect(self.lap)

        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.lap_times = []
        self.lap_times_display.clear()

    def lap(self):
        lap_time = self.format_time(self.time)
        self.lap_times.append(lap_time)
        self.update_lap_times_display()

    def update_lap_times_display(self):
        self.lap_times_display.clear()
        for i, lap_time in enumerate(self.lap_times, 1):
            self.lap_times_display.append(f"Lap {i}: {lap_time}")

    def format_time(self, time):
        hours = time.hour()
        mins = time.minute()
        secs = time.second()
        milisec = time.msec() // 10 #three digits to two
        return f"{hours:02}:{mins:02}:{secs:02}.{milisec:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())