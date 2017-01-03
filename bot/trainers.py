import datetime
import json
import io
from bson import ObjectId
from chatterbot.trainers import Trainer
import config
from os import path
import pytest


def handle_training_error(error_type, data=None, type=None):
    if not data and type:
        error = {
            "status": "failure",
            "response": {
                "time": datetime.datetime.now(),
                "message": config.ERROR_MESSAGES[error_type],
            }
        }
        return error
    else:
        error = {
            "status": "failure",
            "response": {
                "time": datetime.datetime.now(),
                "message": config.ERROR_MESSAGES[error_type].format(data, type),
            }
        }
        return error


def json_file_reader(file):
    with io.open(file, encoding='utf-8') as file_data:
        data = json.load(file_data)
    return data

a = json_file_reader(file="/Downloads/pepperoni-app-kit/node_modules/react-native-mock/package.json")
print(a['_npmUser']['name'])


class JSONTrainer(Trainer):
    """
    Allows a chat bot to trained a json data passed through where
    the json represents a conversation.
    """
    def __init__(self, storage, **kwargs):
        super().__init__(storage, **kwargs)

    def train(self, conversation):
        """
        Train bot based on provided json data
        :param conversation:
        :return:
        """
        if path.isfile(conversation):
            data = json_file_reader(conversation)
            if data:
                statement = data["statement"]
                response = data["response"]
                parameters = data["parameters"]
                if isinstance(list, response):
                    statement == self.get_or_create(te)
                    logic_adapter

        else:
            try:
                json.loads(conversation)
            except ValueError as error:
                raise Exception("{0}".format(error))
            else:
                analyze_json(conversation)


class BotTrainer(Trainer):
    def __init__(self, storage=None, **kwargs):
        super(BotTrainer, self).__init__(storage, **kwargs)

    def init_training(self, data):
        for_service = data["for_service"]
        using = data["using"]
        file_or_url = data["data"]
        if not isinstance(for_service, ObjectId):
            handle_training_error(error_type="INVALID_TYPE", data=for_service, type=ObjectId)
        else:
            pass

