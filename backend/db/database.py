from pymongo import MongoClient
from core.config import settings


class Database:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient(settings.MONGO_URL)
        return cls._client

    @classmethod
    def get_db(cls):
        return cls.get_client()[settings.DB_NAME]


db = Database.get_db()
collection = db["articles"]

# Create Index for 'id' Field
collection.create_index("id", unique=True)
