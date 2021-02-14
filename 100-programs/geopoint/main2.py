from folium import Map, Marker, Popup
from geo import Geopoint

# get values
latitude = 18.6390
longitude = -74.1181

# Folium Map instance
mymap = Map(location = [latitude, longitude])

# house the content for the popup
popup_content = ""

# create a geo point instance
geopoint = Geopoint(latitude=latitude, longitude=longitude)

for weather in geopoint.get_weather():
    hr = '<hr style="margin: 1px;">'
    text = f'{weather[0][11:13]}h: {round(weather[1])}°F <img src="http://openweathermap.org/img/wn/{weather[3]}@2x.png" width="35">'
    popup_content += text + hr

print(popup_content)
popup = Popup(popup_content, max_width=300)
popup.add_to(geopoint)
geopoint.add_to(mymap)

# add a marker to the map
# jeremie = Marker(location = [latitude, longitude], popup = 'Jeremie')
# jeremie.add_to(mymap)

# save map instance
mymap.save('map.html')

print(geopoint.get_weather()[0][0][11:13])
