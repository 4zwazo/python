from folium import Map, Marker, Popup
from geo import Geopoint

# get values
latitude = 18.6390
longitude = -74.1181

# Folium Map instance
mymap = Map(location = [latitude, longitude])

# create a geo point instance
geopoint = Geopoint(latitude=latitude, longitude=longitude)
popup = Popup(str(geopoint.get_weather()))
popup.add_to(geopoint)
geopoint.add_to(mymap)

# add a marker to the map
# jeremie = Marker(location = [latitude, longitude], popup = 'Jeremie')
# jeremie.add_to(mymap)

# save map instance
mymap.save('map.html')
