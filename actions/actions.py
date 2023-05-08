# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# E:\GitHub\FYPProjectDefault

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import random


class ActionHowToGreet(Action):

    def name(self) -> Text:
        return "action_how_to_greet"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        is_not_initial = tracker.get_slot("is_not_initial")  # default value: false

        if not is_not_initial:
            # First time: ask the user's name.
            dispatcher.utter_message(text="先生/女士你好，請問我應該怎麽稱呼你？")
            is_not_initial = True
        else:
            username = tracker.get_slot("username")
            dispatcher.utter_message(text="%s先生/女士，你好，很榮幸為你提供服務。".format(username))

        return [SlotSet("is_not_initial", is_not_initial)]


class ActionConnectDatabase(Action):

    def name(self) -> Text:
        return "action_connect_database"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Create
        engine = create_engine("mysql+pymysql://root:root@localhost:3306/fyp_project_default")

        try:
            connection = engine.connect()
            print("已成功連接數據庫")
            connection.close()
            dispatcher.utter_message(text="已成功連接數據庫")
        except OperationalError as e:
            print("連接數據庫失敗，請重試")
            print(e)
            dispatcher.utter_message(text="連接數據庫失敗，請重試")

        return []


class ActionFood(Action):

    def name(self) -> Text:
        return "action_ask_food"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        if last == "ask_food_cn" or last == "ask_food_jp" or last == "ask_food_kr" or last == "ask_food_sea":

            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r", errors='ignore') as f:
                lines = f.readlines()
                if len(lines) > 3:
                    random.shuffle(lines)
                    result = [lines[0].replace("\n", ""), lines[1].replace("\n", ""), lines[2].replace("\n", "")]
                f.close()
            dispatcher.utter_message(text="我推薦您去{}, {}或者{}".format(result[0], result[1], result[2]))
        else:
            dispatcher.utter_message(text="我認為你的輸入為{}, 但我想不到回答給你".format(last))
            return
        return []


class ActionVisit(Action):

    def name(self) -> Text:
        return "action_ask_visit"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        if last == "ask_visit_museums" or last == "ask_visit_outskirts" or last == "ask_visit_shopping":

            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r",
                      errors='ignore') as f:  ##example the same name as intent+ csv, like ask_visit_parks.csv
                lines = f.readlines()
                if len(lines) > 3:
                    random.shuffle(lines)
                    result = [lines[0].replace("\n", ""), lines[1].replace("\n", ""), lines[2].replace("\n", "")]
                f.close()
            dispatcher.utter_message(text="您可以嘗試去{}, {}或者{}".format(result[0], result[1], result[2]))

        else:
            dispatcher.utter_message(text="我認為你的輸入為{}, 但我想不到回答給你".format(last))
            return
        return []
