# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker, FormValidationAction
from typing import Any, Optional, Text, Dict, List
import spotify_api as spot


class ActionGetMusic(Action):

    def name(self) -> Text:
        return "action_give_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        artist = tracker.get_slot('artist_slot')

        song_name, song_artist = spot.get_song_by_artist(artist)

        dispatcher.utter_message(text='Here is %s by %s' % (
            song_name,
            song_artist
        ))

        return []
