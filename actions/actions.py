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
from rasa_sdk.forms import FormAction, FormValidationAction
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from datetime import datetime, timedelta
import random
import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
import numpy as np


#
# Sentiment nlu
#

class FeedbackForm(FormAction):

    def name(self) -> Text:
        # Returns the name of the form.
        return "Feedback_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        # Returns the list of slots that are required to be filled.
        return ["feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        # Maps the slot names to their values using a disctionary.
        return {
            "feedback": self.from_text()
        }

    def submit(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[EventType]:
        # Call when the form is submitted.

        # Store the conversation in uuid and its relative byte form.
        conversation_id = uuid.uuid4()
        conversation_byte = bytes.fromhex(conversation_id.hex.replace('-', ''))

        # Send back the uuid to users.
        dispatcher.utter_message("再次感謝您使用我們的聊天機器人客戶服務~期待您的再次光臨~")
        dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")

        # Initialize to Firebase
        json_path = os.path.join(os.path.dirname(__file__), "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred,
                                      {
                                          'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        key = conversation_byte
        data = {
            "feedback": tracker.get_slot("feedback"),
            "overall_sentiment": ""
        }

        # Add the new key-value pair to Firebase
        ref.child(key).set(data)

        # Set the uuid to slot.
        return [SlotSet("conversation_id", conversation_byte)]


class ActionSubmitFeedback(Action):
    def name(self) -> Text:
        return "action_submit_feedback"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        feedback = tracker.get_slot("feedback")
        if feedback is not None:
            dispatcher.utter_message(f"我們已收到您的反饋：\n{feedback}")
        else:
            dispatcher.utter_message("抱歉，系統似乎出了點故障。感謝您的反饋。")

        return []

class ActionEndConversation(Action):
    # To simulate how the conversation would end (rasa does not have relevant functionalities).
    def name(self) -> Text:
        return "action_end_conversation"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Initialize to Firebase
        json_path = os.path.join(os.path.dirname(__file__), "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        # Get the slot of conversation_byte
        conversation_byte = tracker.get_slot("conversation_id")
        if conversation_byte is None:
            # Store the conversation in uuid and its relative byte form.
            conversation_id = uuid.uuid4()
            conversation_byte = bytes.fromhex(conversation_id.hex.replace('-', ''))

            # Send back the uuid to users.
            dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")

        #
        # Continue its original flow
        #
        sentiment_list = tracker.slots.get("sentiment_list", [])
        timestamps = list(range(1, len(sentiment_list) + 1))

        # Calculate weights using exponential decay function
        weights = np.exp((np.array(timestamps) - max(timestamps)) / -10)

        # Calculate weighted sum of data
        weighted_sum = sum([sentiment_list[i] * weights[i] for i in range(len(sentiment_list))])

        # Calculate total weight
        total_weight = sum(weights)

        # Calculate weighted average
        weighted_average = weighted_sum / total_weight

        #
        # Save the record to Firebase
        #
        # Initialize to Firebase
        json_path = os.path.join(os.path.dirname(__file__), "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred,
                                      {
                                          'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        # Add the new key-value pair to Firebase
        ref.child(conversation_byte).update({
            "overall_sentiment": weighted_average
        })

        # Send goodbye messages to user.
        dispatcher.utter_message(
            text="很感謝您使用這次的客戶服務，本次客戶服務將會於現在結束😄😄。如果需要再次使用這個服務，請等候30秒后重新刷新。")
        dispatcher.utter_message(text="期待您下一次再度光臨。")

        # No need to store uuid in slot as it starts a new conversation afterwards.
        return [ConversationPaused(), SessionStarted(datetime.now() + timedelta(seconds=30))]


class ActionAppendSentimentList(Action):
    def name(self) -> Text:
        return "action_append_sentiment_list"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        # Get the current value of the "sentiment_list" slot
        sentiment_list = tracker.slots.get("sentiment_list", [])

        # Get the latest user message
        latest_message = tracker.latest_message

        # Get the "sentiment" entity
        sentiment_entity = next((e for e in latest_message['entities'] if e['entity'] == 'sentiment'), None)

        if sentiment_entity:
            # If the "sentiment" entity exists, get its value and confidence
            sentiment_value = sentiment_entity['value']
            sentiment_confidence = sentiment_entity['confidence_entity']

            # Do something with the "sentiment" value and confidence
            if sentiment_value == "pos":
                sentiment_value = 1
            elif sentiment_value == "neu":
                sentiment_value = 0
            elif sentiment_value == "neg":
                sentiment_value = -1
            else:
                sentiment_value = None

            # Append sentiment_value into the sentiment_list
            sentiment_list.append(sentiment_value)

            # For example, send a message to the user with the detected sentiment
            print(f"The sentiment of your message is {sentiment_value} with a confidence of {sentiment_confidence}.")
        else:
            sentiment_list.append(None)

            # If the "sentiment" entity does not exist, send a default message
            print("Sorry, I could not detect the sentiment of your message.")

        return [SlotSet("sentiment_list", sentiment_list)]

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


class ActionBuy(Action):

    def name(self) -> Text:
        return "action_ask_buy"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        if last == "ask_buy_groceries" or last == "ask_buy_clothing":

            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r",
                      errors='ignore') as f:  ##example the same name as intent+ csv, like ask_visit_parks.csv
                lines = f.readlines()
                if len(lines) > 3:
                    random.shuffle(lines)
                    result = [lines[0].replace("\n", ""), lines[1].replace("\n", ""), lines[2].replace("\n", "")]
                f.close()
            dispatcher.utter_message(
                text="您可以嘗試去這些地方購物, 比如說,{}, {}或者{}".format(result[0], result[1], result[2]))

        else:
            dispatcher.utter_message(text="我認為你的輸入為{}, 但我想不到回答給你".format(last))

        return []
