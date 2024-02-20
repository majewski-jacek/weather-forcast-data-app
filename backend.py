import requests
from streamlit import secrets
import os

API_KEY = secrets["WEATHER_API_KEY"]


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}" \
    f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"][:8 * forecast_days] 
    return filtered_data


if __name__ == "__main__":
    content = get_data(place="Tokyo", forecast_days=3)
    print(content)