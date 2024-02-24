import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium
key="8ac5345a4c48451085e49b9479b19521"

number = input("Enter phone number with country code:")

ch_num=phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(ch_num,"en")
print(location)

from phonenumbers import carrier
service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(map_location)
map_location.save("mylocation.html")