from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather

class Geopoint:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def closest_parallel(self):
        return round(self.longitude)

    def get_city(self):
        zf = TimezoneFinder()
        return zf.timezone_at(lng=self.longitude, lat=self.latitude)

    def get_time(self):
        return datetime.now(timezone(self.get_city()))

    def get_weather(self):
        weather = Weather(apikey="d10353de4689668912054bc9dafd5439", \
                          lon=self.longitude, lat=self.latitude)
        return weather.next_12h_simplified()

haiti = Geopoint(longitude=-74.11, latitude=18.64)
print(haiti.get_city())
print(haiti.get_time())
print(haiti.get_weather())

# d10353de4689668912054bc9dafd5439
