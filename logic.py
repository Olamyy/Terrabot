from chatterbot.logic import LogicAdapter


class TheBotLogic(LogicAdapter):
    def __init__(self, **kwargs):
        super(TheBotLogic, self).__init__(kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        pass
