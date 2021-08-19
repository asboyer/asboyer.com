import sys
import music_backend

def update_music(spec):
    music_backend.update_database(spec)

def update_tracks():
    music_backend.update_songs_database()

if __name__ == "__main__":
    try:
        spec = sys.argv[1]
    except IndexError:
        specs = ['all_time', 'current']

    if type(spec) == str:
        if spec == 'songs' or spec == 'tracks':
            music_backend.update_songs_database()
        else:
            update_music(spec)
    elif type(spec) == list:
        for spec in specs:
            update_music(spec)
        music_backend.update_songs_database()
    else:
        print('invalid arg')