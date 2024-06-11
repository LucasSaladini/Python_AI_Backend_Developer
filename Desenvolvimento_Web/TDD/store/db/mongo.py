from motor.motor.asyncio import AsyncIOMotorClient

class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.client

db_client = MongoClient()