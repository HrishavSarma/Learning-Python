import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout,
                             QDesktopWidget)
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
        self.location_label = QLabel(self)
        self.labelback = QLabel("", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Weather App")
        self.setWindowIcon(QIcon("assets/weatherart.png"))


        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.city_label)
        self.vbox.addWidget(self.city_code_input)
        self.vbox.addWidget(self.city_input)
        self.vbox.addWidget(self.get_weather_button)
        self.vbox.addWidget(self.temperature_label)
        self.vbox.addWidget(self.emoji_label)
        self.vbox.addWidget(self.location_label)
        self.vbox.addWidget(self.description_label)

        self.temperature_label.hide()
        self.emoji_label.hide()
        self.location_label.hide()
        self.description_label.hide()

        self.setLayout(self.vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_code_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.location_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.city_code_input.setObjectName("city_code_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.location_label.setObjectName("location_label")
        self.labelback.setObjectName("labelback")

        self.setStyleSheet("""
            QLabel, QPushButton{
                            font-family: poppins;
                           }
            QLabel#city_label{
                           font-family: montserrat;
                           font-size: 24px;
                           font-weight: bold;
                           color: hsl(207, 90%, 54%);
                           background-color: hsl(205, 87%, 94%);
                           padding: 10px;
                           border-radius: 10px;
                           }
            QLineEdit{
                           font-family: open sans;
                           font-size: 18px;
                           color: hsl(0, 0%, 13%);
                           background-color: hsl(0, 0%, 100%);
                           border: 2px solid hsl(207, 89%, 86%);
                           border-radius: 5px;
                           padding: 5px;
                           }
            QLineEdit#city_input::placeholder-text{
                           color: hsl(0, 0%, 46%);
                           }
            QPushButton#get_weather_button{
                           font-size: 20px;
                           font-family: montserrat;
                           font-weight: bold;
                           color: hsl(0, 0%, 100%);
                           background-color: hsl(207, 90%, 54%);
                           border: 2px solid hsl(207, 90%, 54%);
                           border-radius: 10px;
                           padding: 10px;
                           }
            QPushButton#get_weather_button:hover{
                           background-color: hsl(210, 79%, 46%);
                           border-color: hsl(210, 79%, 46%);
                           }
            QPushButton#get_weather_button:pressed{
                           background-color: hsl(216, 85%, 34%);
                           border-color: hsl(216, 85%, 34%);
                           }
            QLabel#temperature_label{
                           font-family: poppins;
                           font-size: 50px;
                           color: hsl(0, 0%, 13%);
                           }
            QLabel#location_label{
                           font-size: 30px;
                           font-family: montserrat;
                           color: hsl(207, 90%, 54%);
                           }
            QLabel#emoji_label{
                           font-size: 100px;
                           font-family: Segoe UI emoji;
                           border-radius: 20px;
                           padding: 10px;
                           }
            QLabel#description_label{
                           font-family: nunito sans;
                           font-size: 24px;
                           color: hsl(0, 0%, 46%);
                           }
        """)

        self.city_code_input.setPlaceholderText("ENTER COUNTRY CODE")
        self.city_input.setPlaceholderText("ENTER CITY ZIPCODE")
        self.labelback.setStyleSheet("background-color: hsl(205, 87%, 94%)")
        self.labelback.lower()

        self.get_weather_button.clicked.connect(self.get_weather)

        self.resizeEvent(None)

        self.resize(500,200)
        self.center_window()

    def center_window(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        center_point = screen_geometry.center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def resizeEvent(self, event):
        self.labelback.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

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

        self.temperature_label.show()
        self.emoji_label.hide()
        self.location_label.hide()
        self.description_label.hide()

        self.temperature_label.setStyleSheet("font-size: 30px;"
                                             "color: hsl(0, 100%, 66%);")
        self.temperature_label.setText(message)
        
        self.vbox.update()
                
        self.resize(500,200)

        self.center_window()

    def display_weather(self, data):
        print(data)
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15

        weather_description = data["weather"][0]["description"]

        location = data["name"]

        weather_id = data["weather"][0]["id"]

        self.temperature_label.setStyleSheet(
            "color: hsl(0, 0%, 13%);"
            "font-size: 50px;"
        )

        self.temperature_label.setText(f"{temperature_c:.2f}°C")
        self.location_label.setText(f"{location}")
        self.description_label.setText(weather_description.capitalize())
        self.emoji_label.setText(self.show_emoji(weather_id))

        self.temperature_label.show()
        self.emoji_label.show()
        self.location_label.show()
        self.description_label.show()

        self.resize(500,500)

        self.center_window()

    @staticmethod
    def show_emoji(weather_id):
        if 200 <= weather_id <= 232:  # Thunderstorm
            if weather_id == 200:
                return "🌩"  # Thunderstorm with light rain
            elif weather_id == 201:
                return "⛈"  # Thunderstorm with rain
            elif weather_id == 202:
                return "🌧⛈"  # Thunderstorm with heavy rain
            elif 210 <= weather_id <= 212:
                return "🌩"  # Light/Heavy Thunderstorm
            elif weather_id == 221:
                return "🌩"  # Ragged Thunderstorm
            elif 230 <= weather_id <= 232:
                return "⛈🌧"  # Thunderstorm with drizzle
            else:
                return "⛈"  # Default Thunderstorm

        elif 300 <= weather_id <= 321:  # Drizzle
            if weather_id == 300:
                return "🌦"  # Light intensity drizzle
            elif weather_id == 301:
                return "🌧"  # Drizzle
            elif weather_id == 302:
                return "🌧🌧"  # Heavy intensity drizzle
            elif 310 <= weather_id <= 314:
                return "🌧"  # Drizzle rain
            elif weather_id == 321:
                return "🌧"  # Shower drizzle
            else:
                return "🌧"  # Default Drizzle

        elif 500 <= weather_id <= 531:  # Rain
            if weather_id == 500:
                return "🌦"  # Light rain
            elif weather_id == 501:
                return "🌧"  # Moderate rain
            elif 502 <= weather_id <= 504:
                return "🌧🌧"  # Heavy/Extreme rain
            elif weather_id == 511:
                return "🌨"  # Freezing rain
            elif 520 <= weather_id <= 531:
                return "🌧"  # Shower rain
            else:
                return "🌧"  # Default Rain

        elif 600 <= weather_id <= 622:  # Snow
            if weather_id == 600:
                return "🌨"  # Light snow
            elif weather_id == 601:
                return "❄️"  # Snow
            elif weather_id == 602:
                return "❄️❄️"  # Heavy snow
            elif 611 <= weather_id <= 613:
                return "🌨"  # Sleet
            elif 615 <= weather_id <= 616:
                return "🌨🌧"  # Rain and snow
            elif 620 <= weather_id <= 622:
                return "🌨"  # Shower snow
            else:
                return "❄️"  # Default Snow

        elif 701 <= weather_id <= 781:  # Atmosphere (Mist, Smoke, Haze, etc.)
            if weather_id == 701:
                return "🌫"  # Mist
            elif weather_id == 711:
                return "💨"  # Smoke
            elif weather_id == 721:
                return "🌫"  # Haze
            elif weather_id == 731:
                return "🌪"  # Sand/Dust whirls
            elif weather_id == 741:
                return "🌁"  # Fog
            elif weather_id == 751:
                return "🏜"  # Sand
            elif weather_id == 761:
                return "🌪"  # Dust
            elif weather_id == 762:
                return "🌋"  # Volcanic ash
            elif weather_id == 771:
                return "💨"  # Squalls
            elif weather_id == 781:
                return "🌪"  # Tornado
            else:
                return "🌫"  # Default Atmosphere

        elif weather_id == 800:  # Clear
            return "☀️"  # Clear sky

        elif 801 <= weather_id <= 804:  # Clouds
            if weather_id == 801:
                return "🌤"  # Few clouds
            elif weather_id == 802:
                return "⛅️"  # Scattered clouds
            elif weather_id == 803:
                return "🌥"  # Broken clouds
            elif weather_id == 804:
                return "☁️"  # Overcast clouds
            else:
                return "☁️"  # Default Clouds

        else:
            return ":("  # Unknown weather

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())