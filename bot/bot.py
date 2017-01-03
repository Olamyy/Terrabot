from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer,TwitterTrainer,UbuntuCorpusTrainer

import config


class Bot():
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

    def train(self, **kwargs):
        training_type = kwargs["training_type"]
        for_service = kwargs["for_service"]
        using = kwargs["using"]
        trainer = config.TRAINER_CLASSES[training_type]
        self.chatterbot.set_trainer(trainer)
