import spotipy
import json
import sys
from spotipy.oauth2 import SpotifyClientCredentials
sys.path.append('secret')
from api_keys import client_id, client_secret

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.search(album="ye", type="album")
