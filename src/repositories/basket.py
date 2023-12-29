from src.repositories.mongodb_repository import MongoDBRepository


class BasketRepository(MongoDBRepository):
    collection = "basket"
