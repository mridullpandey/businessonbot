# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
import random,requests,json
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def get_details(pins):
    url = f"https://api.postalpincode.in/pincode/{pins}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_txt=json.loads(response.text.encode('utf8'))
    return {"city": response_txt[0]['PostOffice'][0]['Circle'],"state":response_txt[0]['PostOffice'][0]['State'],"country":response_txt[0]['PostOffice'][0]['Country']}
# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence
 
class ActionPlayRPS(Action):
   
    def name(self) -> Text:
        return "action_get_details"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_choice = tracker.get_slot("choice")
        pin=tracker.get_slot("pincode")
        comp_choice=get_details(pin)
        xxx=comp_choice[f"{user_choice}".lower()]
        dispatcher.utter_message(text=f"your {user_choice} is  {xxx}")
        return []
