from geocoder import *

geocode = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

for address in geocode:
    print(address, get_administartive_area(get_json(address)), sep=': ')