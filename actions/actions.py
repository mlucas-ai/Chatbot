# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

client_app = 'aeeb153629c446a6a68c94b210d20e8f'
client_secret =  'ebec64e9a1064060b381f3c576d04387'




class ActionConnectSpotify(Action):

    def name(self) -> Text:
        return "action_hello_world" #

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_app,
            client_secret=client_secret
            )
        )

        results = sp.search(q='weezer', limit=20)
        for idx, track in enumerate(results['tracks']['items']):
            print(idx, track['name'])


        dispatcher.utter_message(text="Hello World!")

        return []

