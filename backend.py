import requests

API_KEY = "5f3a52752e9c4c7b7c223f2d7ffed90d"


def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}" \
    f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    content = get_data("Tokyo")
    print(content)