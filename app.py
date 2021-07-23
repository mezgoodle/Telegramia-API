from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas import *
from database import create_document, get_all_objects, get_object, update_object, delete_object

app = FastAPI()


@app.post("/", response_description="Add new student", response_model=PlayerModel)
async def create_student(student: PlayerModel = Body(...)):
    return await create_document(student, 'students')


@app.post("/road", response_description="Add new road", response_model=RoadModel)
async def create_road(road: RoadModel = Body(...)):
    return await create_document(road, 'roads')


@app.get(
    "/", response_description="List all students", response_model=List[PlayerModel]
)
async def list_students():
    students = await get_all_objects('students')
    return students


@app.get(
    "/roads", response_description="List all roads", response_model=List[RoadModel]
)
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@app.get(
    "/{id}", response_description="Get a single student", response_model=PlayerModel
)
async def show_student(id: str):
    return await get_object(id, 'students')


@app.put("/{id}", response_description="Update a student", response_model=UpdatePlayerModel)
async def update_student(id: str, student: UpdatePlayerModel = Body(...)):
    return await update_object(id, student, 'students')


@app.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    return await delete_object(id, 'students')
