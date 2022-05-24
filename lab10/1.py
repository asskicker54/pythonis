import requests
kemsu = '86.090851,55.352041'
home = '86.138312,55.347664'
ef = '2.294695,48.858717'
av = '159.057696,53.745054'
baikal = '107.673058,53.405332'
baikonur = '63.184111,46.198016'

def create_map_image(name, type, file_name, spn='0.01,0.01'):
    response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={name}8&spn={spn}&l={type}')
    with open(file_name, 'wb') as file:
        file.write(response.content)

create_map_image(kemsu, 'map', './res/maps/a.png')
create_map_image(home, 'map', './res/maps/b.png')
create_map_image(ef, 'sat', './res/maps/c.jpg')
create_map_image(av, 'sat', './res/maps/d.jpg')
create_map_image(baikal, 'sat', './res/maps/e.jpg')
create_map_image(baikonur, 'sat', './res/maps/f.jpg')