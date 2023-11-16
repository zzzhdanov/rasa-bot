from .parse import Player

import requests as rq

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionFetchId(Action):
    def name(self) -> Text:
        return "action_fetch_id"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        id = str(tracker.get_slot("id"))
        
        try:
            player = Player(id)
            nickname = player.get_nickname()
            dispatcher.utter_message(text=f"Your profile has been found! Hello, {nickname}!")
            return []
            
        except ValueError:
            dispatcher.utter_message(text="We couldn't find your profile! Please check that the entered ID is correct")
            return [SlotSet("id", None)]



class ActionBriefInfo(Action):
    def name(self) -> Text:
        return "action_brief_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = str(tracker.get_slot("id"))

        if id == "None":
            dispatcher.utter_message(text="Player ID is not defined. Please indicate your ID")
            return []
        
        dispatcher.utter_message(text=Player(id).get_brief_info())

        return []



class ActionGetTeammates(Action):
    def name(self) -> Text:
        return "action_get_teammates"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = str(tracker.get_slot("id"))
        if id == "None":
            dispatcher.utter_message(text="Player ID is not defined. Please indicate your ID")
            return []
        
        quantity, sort_field = (3, "wrate")
        entities = tracker.latest_message["entities"]

        for ent in entities:
            if ent["entity"]=="quantity":
                quantity = int(ent["value"])
            if ent["entity"]=="sort_field":
                sort_field = ent["value"]


        dispatcher.utter_message(text=Player(id).get_teammates(quantity, sort_field))


        return []


class ActionGetMatches(Action):
    def name(self) -> Text:
        return "action_get_matches"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = str(tracker.get_slot("id"))
        if id == "None":
            dispatcher.utter_message(text="Player ID is not defined. Please indicate your ID")
            return []
        
        quantity = int(tracker.latest_message["entities"][-1]["value"])

        dispatcher.utter_message(text=Player(id).get_matches(quantity))

        return []


class ActionGetHeroes(Action):
    def name(self) -> Text:
        return "action_get_heroes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = str(tracker.get_slot("id"))
        if id == "None":
            dispatcher.utter_message(text="Player ID is not defined. Please indicate your ID")
            return []
        
        quantity, sort_field = (3, "wrate")
        entities = tracker.latest_message["entities"]

        for ent in entities:
            if ent["entity"]=="quantity":
                quantity = int(ent["value"])
            if ent["entity"]=="sort_field":
                sort_field = ent["value"]

        dispatcher.utter_message(text=Player(id).get_heroes(quantity, sort_field))

        return []



