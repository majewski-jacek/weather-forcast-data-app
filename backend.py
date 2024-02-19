import requests

API_KEY = "5f3a52752e9c4c7b7c223f2d7ffed90d"


def get_data(place, forecast_days=2, kind="Temperature"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}" \
    f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    content = get_data(place="Tokyo", forecast_days=3, kind="Temperature")
    print(content)