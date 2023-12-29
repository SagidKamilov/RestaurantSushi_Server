from bson import ObjectId


class MongoDBRepository:
    collection: str = None

    def __init__(self, session):
        self.session = session.get_collection(self.collection)

    async def add_one(self, data: dict):
        result = await self.session.insert_one(data)
        new_basket = await self.session.find_one({"_id": result.inserted_id})
        return self._serialize(new_basket)

    async def get_one(self, data: dict):
        basket_id = data.get("id")
        basket = await self.session.find_one({"_id": ObjectId(basket_id)})
        return self._serialize(basket)

    async def get_all(self):
        baskets = []
        cursor = self.session.find()
        async for basket in cursor:
            baskets.append(self._serialize(basket))
        return baskets

    async def edit_one(self, data: dict):
        basket_id = data.get("id")
        existing_basket = await self.session.find_one({"_id": ObjectId(basket_id)})
        if existing_basket:
            result = await self.session.update_one({"_id": ObjectId(basket_id)}, {"$set": data})
            return result.modified_count

    async def delete_one(self, data: dict):
        basket_id = data.get("id")
        result = await self.session.delete_one({"_id": ObjectId(basket_id)})
        return result.deleted_count

    @staticmethod
    def _serialize(document):
        if document:
            document['_id'] = str(document['_id'])
        return document
