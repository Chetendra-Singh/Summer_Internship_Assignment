# to get more details from weather API

import requests
data={
  "coord":{"lon": 75.8167,"lat": 26.9167},
  "weather":[{"id": 804,"main": "Clouds","description": "overcast clouds","icon": "04d"}],
  "base": "stations",
  "main":{"temp": 304.09,"feels_like": 311.09,"temp_min": 304.09,"temp_max": 304.09,
    "pressure": 1000,"humidity": 73,"sea_level": 1000,"grnd_level": 952},
  "visibility": 10000,
  "wind": {"speed": 5.65,"deg": 293,"gust": 5.59},
  "clouds": {"all": 99},
  "dt": 1750658079,
  "sys": {"country": "IN","sunrise": 1750637032,"sunset": 1750686832},
  "timezone": 19800,
  "id": 1269515,
  "name": "Jaipur",
  "cod": 200
}

def weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2727330fa4ab320ebf57ec164e28c1ae"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity=data["main"]["humidity"]
        feels_like=data["main"]["feels_like"]
        lon=data["coord"]["lon"]
        lat=data["coord"]["lat"]
        descr=data["weather"][0]["description"]
        press=data["main"]["pressure"]
        sea_lvl=data["main"]["sea_level"]
        wind_spd=data["wind"]["speed"]
        sunrise=data["sys"]["sunrise"]
        sunset=data["sys"]["sunset"]

        print(f"temperature in {city}:{(temperature-273.15):.2f}")
        print(f"humidity in {city}:{humidity}")
        print(f"it feels like:{(feels_like-273.15):.2f}")
        print(f"coordinates of {city}:{"Longitude",lon},{"Latitude",lat}")
        print(f"Weather Description:{descr}")
        print(f"Pressure:{press}")
        print(f"Sea Level:{sea_lvl}")
        print(f"Wind Speed:{wind_spd}")
        print(f"Sunrise:{sunrise}")
        print(f"Sunset:{sunset}")




    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data:{e}")


# call
city = input("enter city name:")
weather(city)


