import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=86.073238,55.359502&l=map&z=11&'
'pt=86.060298,55.344411,pmwts1~' 
'86.125416,55.388704,pmwts2~' 
'86.071911,55.375898,pmwts3~' 
'86.094458,55.348816,pmwts4') 
with open('./res/7.png', 'wb') as file:
        file.write(response.content)