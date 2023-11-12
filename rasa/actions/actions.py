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
<<<<<<< HEAD
        

        id = tracker.get_slot("id")
        t = rq.get(f"https://api.opendota.com/api/players/{id}")
        dispatcher.utter_message(text=str(t.json()))
        return []
=======
        id = 1174043788
        t = rq.get(f"https://api.opendota.com/api/players/{id}")
        dispatcher.utter_message(text=str(t.json()))
        return []
>>>>>>> 7dddb1172a30d4b20639ff68729a1b39b865074e
