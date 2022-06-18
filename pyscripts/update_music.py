import sys
import music_backend

def update_music(spec):
    if spec == 'all':
        specs = ['all_time', 'current', 'to_listen']
        for spc in specs:
            music_backend.update_database(spc)
    else:
        music_backend.update_database(spec)

def update_tracks():
    music_backend.update_songs_database()

def import_from_all_time():
    music_backend.bring_album_from_all_to_current()

if __name__ == "__main__":
    try:
        spec = sys.argv[1]
        if spec == 'all':
            spec = ['all_time', 'current']
    except IndexError:
        spec = []
    if type(spec) == str:
        if spec == 'songs' or spec == 'tracks':
            music_backend.update_songs_database()
        else:
            update_music(spec)
    if type(spec) == list:
        for sp in spec:
            update_music(sp)
        music_backend.update_songs_database()
    else:
        print('invalid arg')