from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

from common.entities.user import User
from ports.database import DatabasePort


class MongoDatabase(DatabasePort):
    def __init__(self, database_uri: str, database: str, collection: str):
        self.collection = MongoClient(database_uri)[database][collection]

    def create(self, data: dict):
        inserted_id = self.collection.insert_one({
            **data,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }).inserted_id
        return self.get(inserted_id)
    
    def update(self, id: str, data: dict):
        self.collection.update_one(
            {"_id": ObjectId(id)},
            { "$set": {
                **data,
                "updated_at": datetime.now(),
            } }
        )
        return self.get(id)

    def delete(self, id: str):
        self.collection.delete_one({"_id": ObjectId(id)})

    def get(self, id: str):
        entity = self.collection.find_one({"_id": ObjectId(id)})
        if not entity:
            return None
        entity["id"] = str(entity["_id"])
        del entity["_id"]
        return entity

