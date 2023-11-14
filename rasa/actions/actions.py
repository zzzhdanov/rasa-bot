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
        
        quantity = int(tracker.latest_message["entities"][-1]["value"])

        dispatcher.utter_message(text=Player(id).get_teammates(quantity))


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
        
        quantity = int(tracker.latest_message["entities"][-1]["value"])

        dispatcher.utter_message(text=Player(id).get_heroes(quantity))

        return []

# class ActionGetTeammates(Action):
#     def name(self) -> Text:
#         return "action_test_syn"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
#         field = tracker.latest_message["entities"]

#         dispatcher.utter_message(text=str(field))


#         return []

# class ActionFallback(Action):
#     def name(self) -> Text:
#         return "action_fallback"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         dispatcher.utter_message(text="sorry, can you please repharse your question and try again?")
#         return []



# class ActionTestEnt(Action):
#     def name(self) -> Text:
#         return "action_test_ent"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         quantity = tracker.latest_message["entities"][-1]["value"]
        
#         dispatcher.utter_message(text=f"This is your last \n{quantity} matches!")

#         return []



