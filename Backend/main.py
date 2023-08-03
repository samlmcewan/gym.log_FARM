from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# App object
app = FastAPI()

from database import(
    fetch_one_exercise,
    fetch_all_exercises,
    create_exercise,
    update_exercise,
    remove_exercise,
)

from model import(Exercise)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Ping":"Pong"}

@app.get("/api/exercise") 
async def get_exercise():
    response = await fetch_all_exercises()
    return response

@app.get("/api/exercise{title}", response_model=Exercise) 
async def get_exercise_by_id(title):
    response = await fetch_one_exercise(title)
    if response:
        return response
    raise HTTPException(404, f"There is no exercise with the title {title}")

@app.post("/api/exercise", response_model=Exercise) 
async def post_exercise(exercise:Exercise):
    response = await create_exercise(exercise.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad request")

@app.put("/api/exercise{title}", response_model=Exercise) 
async def put_exercise(title:str, desc:str):
    response = await update_exercise(title, desc)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad request")

@app.delete("/api/exercise{title}") 
async def delete_exercise(title):
    response = await remove_exercise(title)
    if response:
        return "Successfully deleted exercise"
    raise HTTPException(404, f"There is no exercise with the title {title}")
