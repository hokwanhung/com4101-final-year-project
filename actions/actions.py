# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHowToGreet(Action):

    def name(self) -> Text:
        return "action_how_to_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        is_not_initial = tracker.get_slot("is_not_initial")  # default value: false

        if not is_not_initial:
            # First time: ask the user's name.
            dispatcher.utter_message(text="先生/女士你好，請問我應該怎麽稱呼你？")
            is_not_initial = True
        else:
            user_name = tracker.get_slot("user_name")
            dispatcher.utter_message(text="%s先生/女士，你好，很榮幸為你提供服務。".format(user_name))

        return [SlotSet("is_not_initial", is_not_initial)]
