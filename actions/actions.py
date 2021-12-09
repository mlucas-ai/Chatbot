# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
import numpy as np
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


# This is a simple example for a custom action which utters "Hello World!"
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionGetMusic(Action):

    def name(self) -> Text:
        return "action_give_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        limit = 10rs
        artist = tracker.get_slot('artist')
        results = sp.search(q=artist, limit=limit)

        # sort by artist, only keep <artist>

        some_song = results['tracks']['items'][0]
        song_name = some_song['name']
        song_artist = some_song['artists'][0]['name']

        dispatcher.utter_message(text='Here is %s from %s' % (
            song_name,
            song_artist
        ))

        return []


class ActionTest(Action):

    def name(self) -> Text:
        return "action_test"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text='Here is some test')

        return []
