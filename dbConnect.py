from motor.motor_asyncio import AsyncIOMotorClient
client = AsyncIOMotorClient("mongodb+srv://admin:admin@cluster0.ziyz4fu.mongodb.net/?appName=Cluster0")

db = client["gube"]
productCollection = db["products"]