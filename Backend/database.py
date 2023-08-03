from model import Exercise

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.ExerciseList
collection = database.exercise

async def fetch_one_exercise(title):
    document = await collection.find_one({"title:title"})
    return document

async def fetch_all_exercises():
    exercises = []
    cursor = collection.find({})
    async for document in cursor:
        exercises.append(Exercise(**document))
        return exercises

async def create_exercise(exercise):
    document = exercise
    result = await collection.insert_one(document)
    return document

async def update_exercise(title, desc):
    await collection.update_one({"title":title},{"$set":{
        "description":desc}})
    document = await collection.find_one({"title":title})
    return document

async def remove_exercise(title):
    await collection.delete_one({"title":title})
    return True