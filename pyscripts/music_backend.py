import spotipy
import json
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials

sys.path.append('../secret/')
from api_keys import client_id, client_secret

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

bad_data = ['available_markets', 'album_type', 'album_group', 'type', 
            'external_urls', 'external_ids', 'tracks', 'copyrights',
            'label', 'release_date_precision', 'href', 'genres', 'is_local', 'disc_number']

# TO DO:
# need to write js for top albums, top tracks
    # figure out how to loop though the list of top tracks in jquery
    
# loop through albums and find top tracks, set up top tracks
    # maybe pass top tracks as string arg in original text file


############################################################################

def read_music_data_from_file(spec):
    with open(f'../data/add/add_uris_music_{spec}.txt', 'r') as f:
        file_albums = f.readlines()
        albums = []
        for album in file_albums:
            new_album = album.strip('\n')
            albums.append(new_album)
    f = open(f'../data/add/add_uris_music_{spec}.txt', 'w+')
    f.close()
    return albums

def extract_uri(albums):
    uri_list = []
    for i in albums:
        uri_list.append(i)
    return uri_list

def clean_result(result):
    for data_key in list(result):
        if data_key in bad_data:
            del result[data_key]
    artist_list = []
    for artist in result['artists']:
        artist_list.append(artist['name'])
    artists_string = ''
    for i in range(len(artist_list)):
        if i == len(artist_list) - 1:
            artists_string += artist_list[i]
        else:
            artists_string += f'{artist_list[i]}, '
    result['artists'] = artists_string
    best_image_url = ''
    for image in result['images']:
        if image['height'] == 640:
            best_image_url = image['url']
    del result['images']
    result['image'] = best_image_url
    result['top_tracks'] = []

    return result

def bring_album_from_all_to_current():
    with open(f'../data/add/bring_album_from_all_time_to_current.txt', 'r') as f:
        file_albums = f.readlines()
        albums = []
        for album in file_albums:
            new_album = album.strip('\n')
            albums.append(new_album)
    f = open(f'../data/add/bring_album_from_all_time_to_current.txt', 'w+')
    f.close()  

    uri_list = extract_uri(albums)

    names = []

    for uri in uri_list:
        print(uri)
        album_data = clean_result(sp.album(uri))
        names.append(album_data['name'])

    with open(f'../data/favorites/music/music_current.json', 'r') as json_file: 
        current_data = json.load(json_file)

    with open(f'../data/favorites/music/music_all_time.json', 'r') as json_file: 
        all_time_data = json.load(json_file)

    for name in names:
        current_data[name] = all_time_data[name]

    with open(f'../data/favorites/music/music_current.json', 'w') as json_file: 
        json.dump(current_data, json_file, indent=4)

def build_database(uri_list):
    final = {}
    for uri in uri_list:
        print(uri)
        album_data = clean_result(sp.album(uri))
        final[album_data['name']] = album_data
    return final

def update_database(spec):
    with open(f'../data/favorites/music/music_{spec}.json', 'r') as json_file: 
        data = json.load(json_file)
    data.update(build_database(
                extract_uri(
                read_music_data_from_file(spec)
                )
                )
                )
    with open(f'../data/favorites/music/music_{spec}.json', 'w') as json_file: 
        json.dump(data, json_file, indent=4)

def clean_song(result):
    # need to figure out what sp.track actually returns
    for data_key in list(result):
        if data_key in bad_data:
            del result[data_key]
    artist_list = []
    for artist in result['artists']:
        artist_list.append(artist['name'])
    artists_string = ''
    for i in range(len(artist_list)):
        if i == len(artist_list) - 1:
            artists_string += artist_list[i]
        else:
            artists_string += f'{artist_list[i]}, '
    result['artists'] = artists_string
    best_image_url = ''
    for image in result['album']['images']:
        if image['height'] == 640:
            best_image_url = image['url']
    result['image'] = best_image_url
    del result['album']
    return result

def build_songs_database(uri_list):
    final = {}
    for uri in uri_list:
        print(uri)
        song_data = clean_song(sp.track(uri))
        final[song_data['name']] = song_data
    return final

def update_songs_database():
    with open(f'../data/favorites/music/music_current_songs.json', 'r') as json_file:
        data = json.load(json_file)

    data.update(build_songs_database(
                extract_uri(
                read_music_data_from_file('current_songs')
                )
                )
                )

    with open(f'../data/favorites/music/music_current_songs.json', 'w') as json_file: 
        json.dump(data, json_file, indent=4)

############################################################################

# misc function
def data_base_clean():
    with open('../data/favorites/music/music_all_time.json', 'r') as json_file:
        data = json.load(json_file)

    # data operation
    for album in data:
        del data[album]['genres']

    with open('../data/favorites/music/music_all_time.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    data_base_clean()
# update_database('all_time')
# new_update()
