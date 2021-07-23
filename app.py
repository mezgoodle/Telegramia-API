from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import motor.motor_asyncio

from config import DB_PASSWORD
from schemas import *

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://mezgoodle:{DB_PASSWORD}@telegramia.jkq5x.mongodb.net/'
                                                f'telegramia?retryWrites=true&w=majority')
db = client['Telegramia']


@app.post("/", response_description="Add new student", response_model=PlayerModel)
async def create_student(student: PlayerModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await db["students"].insert_one(student)
    created_student = await db["students"].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@app.post("/road", response_description="Add new road", response_model=RoadModel)
async def create_road(road: RoadModel = Body(...)):
    road = jsonable_encoder(road)
    new_road = await db["roads"].insert_one(road)
    created_road = await db["roads"].find_one({"_id": new_road.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_road)


@app.get(
    "/", response_description="List all students", response_model=List[PlayerModel]
)
async def list_students():
    students = await db["students"].find().to_list(1000)
    return students


@app.get(
    "/roads", response_description="List all roads", response_model=List[RoadModel]
)
async def list_roads():
    roads = await db["roads"].find().to_list(1000)
    return roads


@app.get(
    "/{id}", response_description="Get a single student", response_model=PlayerModel
)
async def show_student(id: str):
    if (student := await db["students"].find_one({"_id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.put("/{id}", response_description="Update a student", response_model=PlayerModel)
async def update_student(id: str, student: UpdatePlayerModel = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}

    if len(student) >= 1:
        update_result = await db["students"].update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (
                    updated_student := await db["students"].find_one({"_id": id})
            ) is not None:
                return updated_student

    if (existing_student := await db["students"].find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await db["students"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")
