from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer,TwitterTrainer,UbuntuCorpusTrainer
import config


class Bot:
    def __init__(self):
        self.chatterbot = ChatBot(
            name="Terrabot",
            storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
            logic_adapters=[
                'chatterbot.logic.BestMatch'
            ],
            output_adapter='chatterbot.output.TerminalAdapter',
            database='chatterbot-database'
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
            "response": {
                "training_details": data,
                "message": "Trained bot using {0}. Learnt {1} new things".format(data["using"], 5)
            }
        }

    def train(self, data):
        training_type = data["training_type"]
        using = data["using"]
        # @Todo: Do more with the data provided
        # @Todo: Conviniently use the data passed be it file or url
        if isinstance(using, str):
            self.prep_url(data["using"])
        else:
            using = "file"
            self.prep_url(using)

        trainer = self.trainer_classes[training_type]
        self.chatterbot.set_trainer(trainer)
        # self.train(using)
        return self.handle_response(data)

    def prep_url(self, param):
        pass


