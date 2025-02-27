import streamlit as st
import requests
from datetime import datetime, timedelta

# Function to show emoji based on weather ID
def show_emoji(weather_id):
    if 200 <= weather_id <= 232:  # Thunderstorm
        return "⛈️"
    elif 300 <= weather_id <= 321:  # Drizzle
        return "🌧️"
    elif 500 <= weather_id <= 531:  # Rain
        return "🌧️🌧️"
    elif 600 <= weather_id <= 622:  # Snow
        return "❄️"
    elif weather_id == 800:  # Clear
        return "☀️"
    elif 801 <= weather_id <= 804:  # Clouds
        return "☁️"
    elif 701 <= weather_id <= 781:  # Atmosphere (Mist, Smoke, Haze, etc.)
        return "🌫️"
    else:
        return ":("

# Set page title and icon
st.set_page_config(page_title="Weather App", page_icon="🌤️")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: hsl(207, 90%, 54%);
        color: white;
        font-size: 20px;
        font-family: 'Roboto', sans-serif;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: hsl(210, 79%, 46%);
    }
    .stTextInput>div>div>input {
        font-size: 18px;
        font-family: 'Open Sans', sans-serif;
    }
    .stMarkdown h1 {
        font-family: 'Montserrat', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: hsl(207, 90%, 54%);
        background-color: hsl(205, 87%, 94%);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1>WEATHER APP</h1>", unsafe_allow_html=True)

# Input fields
city = st.text_input("ENTER CITY ZIPCODE", placeholder="e.g., 10001")
country_code = st.text_input("ENTER COUNTRY CODE", placeholder="e.g., US")

# Button to fetch weather
if st.button("GET WEATHER"):
    if not city or not country_code:
        st.error("Please enter both city ZIP code and country code.")
    else:
        api_key = "abe2813e66b1a9127eec5d1327a02b23"  # Replace with your OpenWeatherMap API key
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={city},{country_code}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                # Extract weather data
                temperature_k = data["main"]["temp"]
                temperature_c = temperature_k - 273.15
                weather_description = data["weather"][0]["description"]
                location = data["name"]
                weather_id = data["weather"][0]["id"]
                timezone_offset = data["timezone"]

                # Display weather information
                st.success(f"Weather data fetched successfully for {location}!")
                st.write(f"**Temperature:** {temperature_c:.2f}°C")
                st.write(f"**Weather Description:** {weather_description.capitalize()}")
                st.write(f"**Emoji:** {show_emoji(weather_id)}")  # Call the function here

                # Display local time
                local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)
                st.write(f"**Local Time:** {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

            else:
                st.error(f"Error: {data.get('message', 'Unknown error')}")

        except requests.exceptions.HTTPError as http_error:
            st.error(f"HTTP Error: {http_error}")
        except requests.exceptions.ConnectionError:
            st.error("Connection Error: Check your internet connection.")
        except requests.exceptions.Timeout:
            st.error("Timeout Error: The request timed out.")
        except requests.exceptions.RequestException as req_error:
            st.error(f"Request Error: {req_error}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")