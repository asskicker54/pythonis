from geocoder import *

result = ''
northern_latitude = 90
cities = input().split(',')

for city in cities:
    temp_northern_latitude = get_coordinates(get_json(city))[1]
    if temp_northern_latitude < northern_latitude:
        result = city
        northern_latitude = temp_northern_latitude

print('Южнее всех', result)