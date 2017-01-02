from chatterbot.storage import MongoDatabaseAdapter
from bot.models import Services, Users, client


class MongoStorageAdapter(MongoDatabaseAdapter):
    def __init__(self, **kwargs):
        super(MongoStorageAdapter).__init__(**kwargs)
        self.database_uri = client
