import time
import json
from pypresence import Presence
from yandex_music.exceptions import UnauthorizedError
from yandex_music import Client

# НЕПРАВИЛЬНЫЙ КОД ЗАПИСИ КОНФИГА
#config = {}
#config['config'] = []
#config['config'].append({
#    "token": str(input('Введите свой токен Я.Музыки')),
#    "update_delay": 3,
#    "start_delay": 0,
#    "rpc_connect": 1163158250309566584
#})

#with open('config.txt', 'w') as outfile:
#    json.dump(config, outfile)

with open('config.json', 'r') as r:
    settings = json.load(r)
    token = settings['token']
    rpc_connect = settings['rpc_connect']
    start_delay = settings['start_delay']
    update_delay = settings['update_delay']

def get_track():
    root = Client(token=token).init()
    queues = root.queues_list()
    last_queue = root.queue(queues[0].id)
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    tid = last_track_id.track_id
    url = f"https://music.yandex.ru/track/{tid}"
    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    image_link=last_track.get_cover_url(size="200x200")
    duration_min = str((last_track.duration_ms // (1000 * 60)) % 60)
    duration_sec = str((last_track.duration_ms // 1000) % 60)
    return artists, title, url, image_link, duration_min, duration_sec

time.sleep(start_delay)
RPC = Presence(rpc_connect)
RPC.connect()

while True:
    try:
        track = get_track()
        RPC.update(buttons=[{"label": "Слушать", "url": track[2]}],
            state=f"Исполнитель: {track[0]}",
            details="" + track[1],
            large_image=track[3],
            large_text=track[1],
            small_image="ym_avatar",
            small_text=track[4] + ":" + track[5]
        )
    except(UnauthorizedError, UnicodeEncodeError):
        print('Упс...Вы указали неверный токен\nУкажите верный токен вручную в файле config.json', end="\n")
        break
    except:
        RPC.update(
            state="Yandex Music RPC by ShiftyX1",
            large_image="ym_avatar",
            large_text="Yandex Music",
            buttons=[{"label": "Repository", "url": "https://github.com/ShiftyX1"}],
        )
    time.sleep(update_delay)



