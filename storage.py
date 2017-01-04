from chatterbot.storage import MongoDatabaseAdapter
from pymongo import MongoClient

import config


class MongoStorageAdapter(MongoDatabaseAdapter):
    def __init__(self, **kwargs):
        super(MongoStorageAdapter, self).__init__(**kwargs)
        self.database_name = config.db_name
        self.database_uri = config.db_uri
        self.client = MongoClient(self.database_uri)
        self.database = self.client[self.database_name]
        self.statements = self.database['training']
