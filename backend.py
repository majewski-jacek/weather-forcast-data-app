import requests

API_KEY = "5f3a52752e9c4c7b7c223f2d7ffed90d"


def get_data(place, forecast_days=2):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}" \
    f"&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]    
    return filtered_data


if __name__ == "__main__":
    content = get_data(place="Tokyo", forecast_days=3)
    print(content)