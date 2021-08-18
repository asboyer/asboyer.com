import spotipy
import json
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials

sys.path.append('/Users/baller/cs/websites/asboyer/secret/')
from api_keys import client_id, client_secret

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

bad_data = ['available_markets', 'album_type', 'album_group', 'type', 
            'external_urls', 'external_ids', 'tracks', 'copyrights',
            'label', 'release_date_precision', 'href', 'genres']

# TO DO:
# need to figure out how to do top current albums, and top tracks
# need to also write backend for top songs

def read_music_data_from_file(spec):
    with open(f'data/add_uris_music_{spec}.txt', 'r') as f:
        file_albums = f.readlines()
        albums = []
        for album in file_albums:
            album = album.strip('\n')
            new_album = album.split(" :: ")
            albums.append(new_album)
        return albums

def extract_uri(albums):
    uri_list = []
    for i in albums:
        uri_list.append(i[0].replace('spotify:album:', ''))
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

def build_database(uri_list):
    final = {}
    for uri in uri_list:
        print(uri)
        album_data = clean_result(sp.album(uri))
        final[album_data['name']] = album_data
    return final

def update_database(spec):
    with open(f'data/music_{spec}.json', 'r') as json_file: 
        data = json.load(json_file)
    data.update(build_database(
                extract_uri(
                read_music_data_from_file(spec)
                )
                )
                )
    with open(f'data/music_{spec}.json', 'w') as json_file: 
        json.dump(data, json_file, indent=4)

def data_base_clean():
    with open('data/music_all_time.json', 'r') as json_file:
        data = json.load(json_file)

    # data operation
    for album in data:
        data[album]['top_tracks'] = []
        del data[album]['top_traks']

    with open('data/music_all_time.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# update_database('all_time')
new_update()
