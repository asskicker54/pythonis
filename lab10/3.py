from geocoder import *

json = get_json('Москва, Красная площадь, 1')
print('Адрес:', get_text_address(json))
print('Координаты:', get_coordinates(json))