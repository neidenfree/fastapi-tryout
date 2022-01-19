import json
from typing import Optional

from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.newBase
collection = db.myCollection

app = FastAPI(title="Random phrase")


@app.get("/get")
async def some() -> str:
    return "You are faggot!"


@app.get("/some")
async def another(first: int, second: int) -> str:
    if first > second:
        return "Вот это пидорас так пидорас, мое почтение"
    return "Гоу фак Ëселф, пидор"


@app.get("/get-one")
async def get_one() -> json:
    a = collection.find_one({}, {"_id": 0})
    return a


@app.get("/get-all")
async def get_all() -> list:
    a = collection.find({}, {"_id": 0})
    result = []
    for elem in a:
        result.append(elem)
    return result


@app.post("/add")
async def add_one(name: str, age: int, location: Optional[str]) -> None:
    collection.insert_one({"name": name, "age": age, "location": location})
    return None


if __name__ == "__main__":
    uvicorn.run(app, host="23.111.121.144", port=8888)
    uvicorn.run(app, host="localhost", port=8888)
