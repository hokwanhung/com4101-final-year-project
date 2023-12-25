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

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.events import ConversationPaused, SessionStarted
from rasa_sdk.forms import FormAction
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from datetime import datetime, timedelta
import random
import uuid

#
# Sentiment nlu
#
class FeedbackForm(FormAction):

    def name(self) -> Text:
        return "Feedback_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "feedback": [self.from_text()]
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[EventType]:
        conversation_id = uuid.uuid4()
        conversation_byte = bytes.fromhex(conversation_id.hex.replace('-', ''))

        dispatcher.utter_message("再次感謝您使用我們的聊天機器人客戶服務~期待您的再次光臨~")
        dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")
        return [SlotSet("conversation_id", conversation_byte)]


class ActionEndConversation(Action):
    # To simulate how the conversation would end (rasa does not have relevant functionalities).
    def name(self) -> Text:
        return "action_end_conversation"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Pause conversation for 30 seconds
        dispatcher.utter_message(
            text="很感謝您使用這次的客戶服務，本次客戶服務將會於現在結束😄😄。如果需要再次使用這個服務，請等候30秒后重新刷新。")
        dispatcher.utter_message(text="期待您下一次再度光臨。")
        return [ConversationPaused(), SessionStarted(datetime.now() + timedelta(seconds=30))]


#
# General nlu
#
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


#
# Hotel Registration
#
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


#
# Ask Hotel Relevant Information
#

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
