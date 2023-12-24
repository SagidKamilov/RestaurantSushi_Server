from pymongo import MongoClient

class MongoDBRepository:

    def __init__(self):
        self.base = MongoClient("mongodb://localhost:27017")
        self.connection = self.base["basket"]["basket"]

    def add_one(self, data: dict):
        basket_data = self.connection.insert_one(data)
        return basket_data

    def get_one(self, data: dict):
        basket_data = self.connection.find_one(filter=data)
        return basket_data

    def del_one(self, data: dict):
        basket_data = self.connection.delete_one(filter=data)
        return basket_data