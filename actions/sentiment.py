# set this before running function
# set PYTHONPATH=E:\GitHub\FYPProjectDefault\actions;%PYTHONPATH%
# replace E:\GitHub\FYPProjectDefault\actions; with your project directory
# echo %PYTHONPATH%

from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
from rasa_sdk import Action, Tracker

from nltk.classify import NaiveBayesClassifier
import os
import pickle
from typing import Any, Optional, Text, Dict

SENTIMENT_MODEL_FILE_NAME = "sentiment_classifier.pkl"


class SentimentAnalyzer(Component):
    """A custom sentiment analysis component"""
    name = "sentiment"
    provides = ["entities"]
    requires = ["tokens"]
    defaults = {}
    language_list = ["zh"]
    print('initialised the class')

    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Load the sentiment polarity labels from the text
           file, retrieve training tokens and after formatting
           data train the classifier."""

        with open(os.getcwd() + '\\actions\\labels.txt', 'r') as f:
            labels = f.read().splitlines()

        training_data = training_data.training_examples  # list of Message objects
        tokens = []
        for t in training_data:
            if not "text" in t.data:
                continue
            try:
                tokens.append(list(map(lambda x: x, t.data['text'])))
            except TypeError:
                continue
        processed_tokens = [self.preprocessing(t) for t in tokens]
        labeled_data = [(t, x) for t, x in zip(processed_tokens, labels)]
        self.clf = NaiveBayesClassifier.train(labeled_data)

    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"entity": "sentiment",
                  "confidence_entity": confidence,
                  "value": value,
                  "extractor": "sentiment_extractor (sentiment)"}

        return entity

    def preprocessing(self, tokens):
        """Create bag-of-words representation of the training examples."""

        return ({word: True for word in tokens})

    def process(self, message, **kwargs):
        """Retrieve the tokens of the new message, pass it to the classifier
            and append prediction results to the message class."""

        if not self.clf:
            # component is either not trained or didn't
            # receive enough training data
            entity = None
        else:
            print("waiww" + str(message.data))
            if "action_name" in message.data:
                tokens = message.data['action_name']
            elif "text" in message.data:
                tokens = message.data['text']
            elif "intent" in message.data:
                tokens = message.data['intent']

            tb = self.preprocessing(tokens)
            pred = self.clf.prob_classify(tb)

            sentiment = pred.max()
            confidence = pred.prob(sentiment)
            entity = self.convert_to_rasa(sentiment, confidence)

            message.set("entities", [entity], add_to_output=True)

    def persist(self, file_name, model_dir):
        """Persist this model into the passed directory."""
        classifier_file = os.path.join(model_dir, SENTIMENT_MODEL_FILE_NAME)

        with open(classifier_file, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        return {"classifier_file": SENTIMENT_MODEL_FILE_NAME}

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,
             model_metadata=None,
             cached_component=None,
             **kwargs):
        file_name = meta.get("classifier_file")
        classifier_file = os.path.join(model_dir, file_name)
        with open(classifier_file, 'rb') as f:
            return pickle.load(f)
