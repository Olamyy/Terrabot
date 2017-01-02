import datetime
from bson import ObjectId
from chatterbot.trainers import Trainer
import config


class BotTrainer(Trainer):
    def __init__(self, storage=None, **kwargs):
        super(BotTrainer, self).__init__(storage, **kwargs)

    def init_training(self, data):
        for_service = data["for_service"]
        using = data["using"]
        file_or_url = data["using"]
        if not isinstance(for_service, ObjectId):
            handle_training_error(error_type="INVALID_TYPE", data=for_service, type=ObjectId)
        else:
            pass


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