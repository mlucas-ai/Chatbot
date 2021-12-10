from typing import Any, Optional, Text, Dict, List
import numpy as np
from rasa_sdk.types import DomainDict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_app = 'aeeb153629c446a6a68c94b210d20e8f'
client_secret = 'ebec64e9a1064060b381f3c576d04387'

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_app,
        client_secret=client_secret
    )
)


def get_song_by_artist(artist):
    limit = 10
    results = sp.search(q=artist, limit=limit)

    _valid = [
        t for t in results['tracks']['items']
        if t['artists'][0]['name'] in artist
    ]

    some_song = np.random.choice(_valid)
    song_name = some_song['name']
    song_artist = some_song['artists'][0]['name']

    return song_name, song_artist
