# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests as rq
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReqApi(Action):
    def name(self) -> Text:
        return "action_req_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = tracker.get_slot("id")
        t = rq.get(f"https://api.opendota.com/api/players/{id}")
        if 'profile' in t.json().keys():
            dispatcher.utter_message(text=f"Ok,I understand. Your ID is {id}. You can ask me further")
        else:
            dispatcher.utter_message(text=f"Your id is invalid")
        return []
