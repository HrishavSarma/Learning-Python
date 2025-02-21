import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("WEATHER APP", self)
        self.city_input = QLineEdit(self)
        self.city_code_input = QLineEdit(self)
        self.get_weather_button = QPushButton("GET WEATHER", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.labelback = QLabel("", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Weather App")
        self.setGeometry(425,100, 500,500)
        self.setWindowIcon(QIcon("assets/weatherart.png"))
        self.labelback.setGeometry(0,0,500,500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_code_input)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_code_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.city_code_input.setObjectName("city_code_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.labelback.setObjectName("labelback")

        self.setStyleSheet("""
            QLabel, QPushButton{
                            font-family: roboto;
                           }
            QLabel#city_label{
                           font-family: roboto;
                           font-size: 20px;
                           font-weight: bold;
                           background-color: hsl(220, 17%, 60%);
                           padding: 10px;
                           }
            QLineEdit{
                           font-size: 20px;
                           color: black;
                           }
            QLineEdit#city_input::placeholder-text{
                           color: grey;
                           }
            QPushButton#get_weather_button{
                           font-size: 20px;
                           font-family: roboto;
                           background-color: hsl(220, 17%, 60%);
                           border: 3px solid;
                           border-color: white;
                           border-radius: 3px;
                           }
            QPushButton#get_weather_button:hover{
                           background-color: hsl(220, 30%, 75%);
                           border: 2px solid;
                           border-color: white;
                           }
            QPushButton#get_weather_button:pressed{
                           background-color: hsl(220, 17%, 40%);
                           border: 2px solid;
                           border-color: white;
                           }
            QLabel#temperature_label{
                           font-size: 50px;
                           }
            QLabel#emoji_label{
                           font-size: 100px;
                           font-family: Segoe UI emoji;
                           }
            QLabel#description_label{
                           font-size: 50px;
                           font-family: GoodDog Plain;
                           }
        """)

        self.city_code_input.setPlaceholderText("ENTER COUNTRY CODE")
        self.city_input.setPlaceholderText("ENTER CITY ZIPCODE")
        self.labelback.setStyleSheet("background-color: hsl(220, 17%, 35%)")
        self.labelback.lower()

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "abe2813e66b1a9127eec5d1327a02b23"
        city = self.city_input.text()
        city_code = self.city_code_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={city},{city_code}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request!:\nPlease check input")
                case 401:
                    self.display_error("UnAuthorised:\nInvalid API key")
                case 403:
                    self.display_error("Access Denied!:\nForbidden")
                case 404:
                    self.display_error("City not found!:\nPlease check input")
                case 500:
                    self.display_error("Internal Server Error:\nPlease check input")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server")
                case 503:
                    self.display_error("Service Unavailable:\nServer down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from server")
                case _:
                    self.display_error(f"HTTP Error occured:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\ncheck URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;"
                                             "color: red;")
        self.temperature_label.setText(message)

    def display_weather(self, data):
        print(data)
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        print(f"{temperature_c:.2f}°C")
        self.temperature_label.setText(f"{temperature_c:.2f}°C")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())