# 1.Import FastAPI
from fastapi import FastAPI
from models import Programmer, Languages
from typing import List

# 2.Initialize the app
app = FastAPI()

# 3.Mock db
db: List[Programmer] = [
    Programmer(id= 1, name="Dennis Ritchie", languages=[Languages.b, Languages.c]),
    Programmer(id= 2, name="Brian Wilson Kernighan", languages=[Languages.c]),
    Programmer(id= 3, name="James Gosling", languages=[Languages.java]),
    Programmer(id= 4, name="Guido van Rossum", languages=[Languages.python]),
    Programmer(id= 5, name="Brendan Eich", languages=[Languages.javascript])
]

# 4.Create endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hi/{name}")
async def say_hi(name):
  return {"message": "Hi " + name}

# @app.get("/programmers", response_model=list[Programmer])
# async def get_programmers():
#     return db

@app.get("/programmers", response_model=list[Programmer])
async def get_all_programmers(skip: int = 0, limit: int = 5) -> list[Programmer]:
    return db[skip: skip + limit]

@app.get("/programmers/{programmer_id}", response_model=Programmer)
async def get_programmer(programmer_id: int):
    response = next((programmer for programmer in db if programmer.id == programmer_id), None)
    return response

@app.post("/programmers", response_model=Programmer)
async def add_new_programmer(programmer: Programmer):
    db.append(programmer)
    return programmer