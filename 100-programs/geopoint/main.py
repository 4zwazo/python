from folium import Map
from geo import Geopoint

latitude = 18.6390
longitude = 74.1181

antipode_latitude = latitude * -1
antipode_longitude = 0

if longitude <= 0:
    antipode_longitude = longitude * 180
elif longitude == 0:
    antipode_longitude = 180

print(antipode_longitude)
location = [antipode_latitude, antipode_longitude]

jmap = Map(location)
jmap.save(str('antipode.html'))

long = 90.9
lat = 13.9

mypoint = Geopoint(long, lat)
print(mypoint.closest_parallel())
