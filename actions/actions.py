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
from rasa_sdk.events import ConversationPaused, SessionStarted, UserUtteranceReverted
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import WebDriverException


#
# Sentiment nlu
#

# class FeedbackForm(FormAction):
#
#     def name(self) -> Text:
#         # Returns the name of the form.
#         return "feedback_form"
#
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         # Returns the list of slots that are required to be filled.
#         return ["feedback"]
#
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         # Maps the slot names to their values using a dictionary.
#         return {
#             "feedback": self.from_text()
#         }
#
#     def validate(
#             self,
#             dispatcher: "CollectingDispatcher",
#             tracker: "Tracker",
#             domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         print("復核信息中")
#         feedback = tracker.get_slot("feedback")
#         print(feedback)
#
#         if feedback is None:
#             dispatcher.utter_message("抱歉，系統似乎出了點故障。感謝您的反饋。")
#             return {"feedback": None}
#         else:
#             dispatcher.utter_message(f"我們已收到您的反饋：\n{feedback}")
#
#         return {"feedback": feedback}
#
#     def submit(
#             self,
#             dispatcher: "CollectingDispatcher",
#             tracker: "Tracker",
#             domain: "DomainDict",
#     ) -> List[EventType]:
#         # Call when the form is submitted.
#
#         # Store the conversation in uuid and its relative byte form.
#         conversation_id = uuid.uuid4()
#
#         # Send back the uuid to users.
#         dispatcher.utter_message("再次感謝您使用我們的聊天機器人客戶服務~期待您的再次光臨~")
#         dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")
#
#         # Initialize to Firebase
#         json_path = os.path.join(os.path.dirname(__file__), "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
#         cred = credentials.Certificate(json_path)
#         firebase_admin.initialize_app(cred,
#                                       {
#                                           'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})
#
#         # Get a database reference to the "users" node
#         ref = db.reference("users")
#
#         key = str(conversation_id)
#         data = {
#             "feedback": tracker.get_slot("feedback"),
#             "overall_sentiment": ""
#         }
#
#         # Add the new key-value pair to Firebase
#         ref.child(key).set(data)
#
#         # Set the uuid to slot.
#         return [SlotSet("conversation_id", str(conversation_id))]
#
#
class ActionValidateFeedback(Action):
    def name(self) -> Text:
        return "action_validate_feedback"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        feedback = tracker.latest_message["text"]
        print(f"feedback: {tracker.latest_message}")

        if feedback is not None:
            dispatcher.utter_message(f"我們已收到您的反饋：\n{feedback}")
        else:
            dispatcher.utter_message("抱歉，系統似乎出了點故障。感謝您的反饋。")

        # Store the conversation in uuid and its relative byte form.
        conversation_id = uuid.uuid4()

        # Send back the uuid to users.
        dispatcher.utter_message("再次感謝您使用我們的聊天機器人客戶服務~期待您的再次光臨~")
        dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")

        #
        # Continue its original flow
        #
        sentiment_list = tracker.get_slot("sentiment_list")
        timestamps = list(range(1, len(sentiment_list) + 1))

        # Calculate weights using exponential decay function
        weights = np.exp((np.array(timestamps) - max(timestamps)) / -10)

        # Calculate weighted sum of data if the value is not -999
        weighted_sum = sum(
            [sentiment_list[i] * weights[i] for i in range(len(sentiment_list)) if sentiment_list[i] != -999])

        # Calculate total weight
        total_weight = sum(weights)

        # Calculate weighted average
        weighted_average = weighted_sum / total_weight

        # Get a Firebase Instance (if not exist, then create one)
        try:
            firebase_admin.get_app()
        except ValueError:
            json_path = os.path.join(os.path.dirname(__file__),
                                     "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
            cred = credentials.Certificate(json_path)
            firebase_admin.initialize_app(cred,
                                          {
                                              'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        key = str(conversation_id)
        data = {
            "feedback": feedback,
            "overall_sentiment": weighted_average
        }

        # Add the new key-value pair to Firebase
        ref.child(key).set(data)

        # Send goodbye messages to user.
        dispatcher.utter_message(
            text="很感謝您使用這次的客戶服務，本次客戶服務將會於現在結束😄😄。如果需要再次使用這個服務，請等候30秒后重新刷新。")
        dispatcher.utter_message(text="期待您下一次再度光臨。")

        # No need to store uuid in slot as it starts a new conversation afterwards.
        return [ConversationPaused(), SessionStarted(datetime.now() + timedelta(seconds=30))]


class ActionEndConversation(Action):
    # To simulate how the conversation would end (rasa does not have relevant functionalities).
    def name(self) -> Text:
        return "action_end_conversation"

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get a Firebase Instance (if not exist, then create one)
        try:
            firebase_admin.get_app()
        except ValueError:
            json_path = os.path.join(os.path.dirname(__file__),
                                     "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
            cred = credentials.Certificate(json_path)
            firebase_admin.initialize_app(cred,
                                          {
                                              'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        # Get the slot of conversation_byte
        # conversation_id = tracker.get_slot("conversation_id")
        # if conversation_id is None:
        # Store the conversation in uuid and its relative byte form.
        conversation_id = uuid.uuid4()

        # Send back the uuid to users.
        dispatcher.utter_message(f"聊天記錄號碼：{conversation_id}")

        #
        # Continue its original flow
        #
        sentiment_list = tracker.get_slot("sentiment_list")
        timestamps = list(range(1, len(sentiment_list) + 1))

        # Calculate weights using exponential decay function
        weights = np.exp((np.array(timestamps) - max(timestamps)) / -10)

        # Calculate weighted sum of data if the value is not -999
        weighted_sum = sum(
            [sentiment_list[i] * weights[i] for i in range(len(sentiment_list)) if sentiment_list[i] != -999])

        # Calculate total weight
        total_weight = sum(weights)

        # Calculate weighted average
        weighted_average = weighted_sum / total_weight

        #
        # Save the record to Firebase
        #
        # Get a Firebase Instance (if not exist, then create one)
        try:
            firebase_admin.get_app()
        except ValueError:
            json_path = os.path.join(os.path.dirname(__file__),
                                     "fypprojectdefault-firebase-adminsdk-em0ra-cc7419a6b6.json")
            cred = credentials.Certificate(json_path)
            firebase_admin.initialize_app(cred,
                                          {
                                              'databaseURL': "https://fypprojectdefault-default-rtdb.asia-southeast1.firebasedatabase.app"})

        # Get a database reference to the "users" node
        ref = db.reference("users")

        # Add the new key-value pair to Firebase
        ref.child(str(conversation_id)).update({
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
        sentiment_list = tracker.get_slot("sentiment_list")
        print(sentiment_list)

        # Initialize the sentiment_list if there is not a sentiment_list beforehand.
        if sentiment_list is None:
            sentiment_list = []

        # Get the latest user message
        latest_message = tracker.latest_message

        # Get the "sentiment" entity

        sentiment_entity = next((e for e in latest_message['entities'] if e['entity'] == 'sentiment'), None)

        # print(sentiment_entity)
        # It seems the value can be gotten:
        # e.g. {'entity': 'sentiment', 'confidence_entity': 0.53994163996895, 'value': 'neg',
        # 'extractor': 'sentiment_extractor (sentiment)'}

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
            else:  # if the value is None
                sentiment_value = -999

            # Append sentiment_value into the sentiment_list
            sentiment_list.append(sentiment_value)

            # For example, send a message to the user with the detected sentiment
            print(
                f"The sentiment of your message is {sentiment_value} ({sentiment_value}) with a confidence of {sentiment_confidence}.")
            print(sentiment_list)
        else:
            sentiment_list.append(-999)

            # If the "sentiment" entity does not exist, send a default message
            print("Sorry, I could not detect the sentiment of your message.")

        return [SlotSet("sentiment_list", sentiment_list)]


#
# Hotel Registration
#
# class HotelInfoForm(FormAction):
#
#     def name(self) -> Text:
#         return "Hotel_Info_form"
#
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["room_type, special_view, room_capacity, price"]
#
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "room_type": self.from_text(),
#             "special_view": self.from_text(),
#             "room_capacity": self.from_text(),
#             "price": self.from_text()
#         }
#
#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: "DomainDict",
#     ) -> List[EventType]:
#         # Submit the form
#         dispatcher.utter_message()
#         return[]

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
# Go to the directory: venv/Lib/site-packages/rasa/core/channels/console.py
# Change the default value of DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS to more than 10, in my case I changed it to 30 it worked.
#

class ActionFood(Action):

    def name(self) -> Text:
        return "action_ask_food"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        print(last)
        if last == "ask_food_cn" or last == "ask_food_jp" or last == "ask_food_kr" or last == "ask_food_sea":

            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r", errors='ignore', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    random.shuffle(lines)
                    results = [lines[0].replace("\n", ""), lines[1].replace("\n", "")]
                    dispatcher.utter_message(
                        text="我推薦您去{}或者{}，貴客您可以參考下面兩個網址：".format(results[0], results[1]))
                    print(results)
                f.close()

            # New Flow
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            urls = []

            try:
                for result in results:
                    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
                    driver.get("https://www.google.com/")

                    cookie_button = driver.find_element(By.ID, "L2AGLb")
                    cookie_button.click()

                    search_box = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.ID, "APjFqb"))
                    )
                    search_box.send_keys(f"{result} openrice")
                    search_panel = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']")
                    search_button = search_panel.find_element(By.XPATH, ".//center//input[@name='btnK']")
                    search_button.click()

                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='yuRUbf']"))
                    )
                    url_panel = driver.find_element(By.XPATH, "//div[@class='yuRUbf']")
                    url_element = url_panel.find_element(By.CSS_SELECTOR, "a")
                    url = url_element.get_attribute("href")

                    urls.append(url)

                    driver.close()

                # Must dispatch messages at last
                print(urls)
                dispatcher.utter_message(urls[0])
                dispatcher.utter_message(urls[1])
            except WebDriverException:
                dispatcher.utter_message("很抱歉，網址未能正確顯示，請貴客您稍後再試🥺🥺。")
        else:
            dispatcher.utter_message(
                text=f"很抱歉，貴客您的輸入為{last}, 但是基於未知原因，未能正確反饋信息給您。請見諒🥺🥺🥺🥺。")

        return []


class ActionVisit(Action):

    def name(self) -> Text:
        return "action_ask_visit"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        print(last)
        if last == "ask_visit_museums" or last == "ask_visit_outskirts" or last == "ask_visit_shopping":

            # example the same name as intent+ csv, like ask_visit_parks.csv
            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r", errors='ignore', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    random.shuffle(lines)
                    results = [lines[0].replace("\n", ""), lines[1].replace("\n", "")]
                    dispatcher.utter_message(
                        text="您可以嘗試去{}或者{}，貴客您可以參考下面兩個網址：".format(results[0], results[1]))
                    print(results)
                f.close()

            # New Flow
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            urls = []
            try:
                for result in results:
                    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
                    driver.get("https://www.google.com/")

                    cookie_button = driver.find_element(By.ID, "L2AGLb")
                    cookie_button.click()

                    search_box = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.ID, "APjFqb"))
                    )
                    search_box.send_keys(f"{result} hk")
                    search_panel = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']")
                    search_button = search_panel.find_element(By.XPATH, ".//center//input[@name='btnK']")
                    search_button.click()

                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='yuRUbf']"))
                    )
                    url_panel = driver.find_element(By.XPATH, "//div[@class='yuRUbf']")
                    url_element = url_panel.find_element(By.CSS_SELECTOR, "a")
                    url = url_element.get_attribute("href")

                    urls.append(url)
                    driver.close()

                print(urls)
                dispatcher.utter_message(urls[0])
                dispatcher.utter_message(urls[1])

            except WebDriverException:
                dispatcher.utter_message("很抱歉，網址未能正確顯示，請貴客您稍後再試🥺🥺。")
        else:
            dispatcher.utter_message(
                text=f"很抱歉，貴客您的輸入為{last}, 但是基於未知原因，未能正確反饋信息給您。請見諒🥺🥺🥺🥺。")

        return []


class ActionBuy(Action):

    def name(self) -> Text:
        return "action_ask_buy"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last = tracker.get_intent_of_latest_message()
        print(last)
        if last == "ask_buy_groceries" or last == "ask_buy_clothing":

            with open(os.getcwd() + "\\csv\\" + last + ".csv", "r", errors='ignore', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    random.shuffle(lines)
                    results = [lines[0].replace("\n", ""), lines[1].replace("\n", "")]
                    dispatcher.utter_message(
                        text="您可以嘗試去這些地方購物, 比如說,{}或者{}，貴客您可以參考下面兩個網址：".format(results[0], results[1]))
                f.close()
                print(results)

            # New Flow
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            urls = []

            try:
                driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
                for result in results:
                    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
                    driver.get("https://www.google.com/")

                    cookie_button = driver.find_element(By.ID, "L2AGLb")
                    cookie_button.click()

                    search_box = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.ID, "APjFqb"))
                    )
                    search_box.send_keys(f"{result} hk")
                    search_panel = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']")
                    search_button = search_panel.find_element(By.XPATH, ".//center//input[@name='btnK']")
                    search_button.click()

                    WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='yuRUbf']"))
                    )
                    url_panel = driver.find_element(By.XPATH, "//div[@class='yuRUbf']")
                    url_element = url_panel.find_element(By.CSS_SELECTOR, "a")
                    url = url_element.get_attribute("href")

                    urls.append(url)
                    driver.close()

                print(urls)
                dispatcher.utter_message(urls[0])
                dispatcher.utter_message(urls[1])
            except WebDriverException:
                dispatcher.utter_message("很抱歉，網址未能正確顯示，請貴客您稍後再試🥺🥺。")
        else:
            dispatcher.utter_message(
                text=f"很抱歉，貴客您的輸入為{last}, 但是基於未知原因，未能正確反饋信息給您。請見諒🥺🥺🥺🥺。")

        return []

# class ActionOutOfScope(Action):
#     def name(self) -> Text:
#         return "action_out_of_scope"
#
#     def run(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # tell the user they are being passed to a customer service agent
#         dispatcher.utter_message(text="不好意思，我不太明白您的意思。麻煩貴客您重組後跟我説一下🥺🥺。")
#
#         # assume there's a function to call customer service
#         # pass the tracker so that the agent has a record of the conversation between the user
#         # and the bot for context
#
#         # pause the tracker so that the bot stops responding to user input
#         return [ConversationPaused(), UserUtteranceReverted()]
