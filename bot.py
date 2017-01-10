from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer,TwitterTrainer,UbuntuCorpusTrainer
import config


class Bot:
    def __init__(self):
        self.chatterbot = ChatBot(
            name="Terrabot",
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            logic_adapters=[
                'chatterbot.logic.BestMatch'
            ],
            database='terrabot'
        )

        self.trainer_classes = {
            "list": ListTrainer,
            "corpus": ChatterBotCorpusTrainer,
            "twitter": TwitterTrainer,
            "ubuntu": UbuntuCorpusTrainer,
            "facebook": "",
            "custom": ""
        }

    def handle_response(self, data=None):
        return {
            "status": "success",
            "service_id": data["service_id"],
            "response": {
                "training_details": "[{0} : {1}]".format(data['message'], data['response']),
                "message": "Trained bot... Learnt {} new things".format(len(data))
            }
        }

    def init_training_file(self, data):
        pass

    def train(self, data, training_type=None):
        if training_type == "chat":
            self.chatterbot.set_trainer(ListTrainer)
            for key, values in data.iteritems:
                self.chatterbot.train((data['message'], data['response']))
            return self.handle_response(data)
        else:
            #File Training
            pass
