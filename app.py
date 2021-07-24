from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas import *
from database import create_document, get_all_objects, get_object, update_object, delete_object

app = FastAPI()


@app.post("/player", response_description="Add new player", response_model=PlayerModel)
async def create_player(player: PlayerModel = Body(...)):
    return await create_document(player, 'players')


@app.post("/road", response_description="Add new road", response_model=RoadModel)
async def create_road(road: RoadModel = Body(...)):
    return await create_document(road, 'roads')


@app.post("/country", response_description="Add new country", response_model=CountryModel)
async def create_country(country: CountryModel = Body(...)):
    return await create_document(country, 'countries')


@app.post("/item", response_description="Add new item", response_model=ItemModel)
async def create_item(item: ItemModel = Body(...)):
    return await create_document(item, 'items')


@app.post("/city", response_description="Add new city", response_model=CityModel)
async def create_city(city: CityModel = Body(...)):
    return await create_document(city, 'cities')


@app.get(
    "/players", response_description="List all players", response_model=List[PlayerModel]
)
async def list_players():
    players = await get_all_objects('players')
    return players


@app.get(
    "/roads", response_description="List all roads", response_model=List[RoadModel]
)
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@app.get(
    "/players/{id}", response_description="Get a single player", response_model=PlayerModel
)
async def show_player(id: str):
    return await get_object(id, 'players')


@app.put("/players/{id}", response_description="Update a player", response_model=UpdatePlayerModel)
async def update_player(id: str, player: UpdatePlayerModel = Body(...)):
    return await update_object(id, player, 'players')


@app.delete("/players/{id}", response_description="Delete a player")
async def delete_player(id: str):
    return await delete_object(id, 'players')
