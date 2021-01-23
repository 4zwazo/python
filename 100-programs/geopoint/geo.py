class Geopoint:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def closest_parallel(self):
        return round(self.longitude)