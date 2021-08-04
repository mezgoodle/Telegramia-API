from fastapi import FastAPI, Body
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


@app.post("/heroclass", response_description="Add new class", response_model=HeroClassModel)
async def create_class(hero_class: HeroClassModel = Body(...)):
    return await create_document(hero_class, 'classes')


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
    "/countries", response_description="List all countries", response_model=List[CountryModel]
)
async def list_countries():
    countries = await get_all_objects('countries')
    return countries


@app.get(
    "/heroclasses", response_description="List all classes", response_model=List[HeroClassModel]
)
async def list_classes():
    classes = await get_all_objects('classes')
    return classes


@app.get(
    "/players/{id}", response_description="Get a single player", response_model=PlayerModel
)
async def show_player(id: str):
    return await get_object(id, 'players')


@app.get(
    "/roads/{id}", response_description="Get a single road", response_model=RoadModel
)
async def show_road(id: str):
    return await get_object(id, 'roads')


@app.get(
    "/countries/{id}", response_description="Get a single country", response_model=CountryModel
)
async def show_country(id: str):
    return await get_object(id, 'countries')


@app.get(
    "/heroclasses/{id}", response_description="Get a single class", response_model=HeroClassModel
)
async def show_class(id: str):
    return await get_object(id, 'classes')


@app.put("/players/{id}", response_description="Update a player", response_model=UpdatePlayerModel)
async def update_player(id: str, player: UpdatePlayerModel = Body(...)):
    return await update_object(id, player, 'players')


@app.delete("/players/{id}", response_description="Delete a player")
async def delete_player(id: str):
    return await delete_object(id, 'players')


@app.delete("/roads/{id}", response_description="Delete a road")
async def delete_road(id: str):
    return await delete_object(id, 'roads')


@app.delete("/countries/{id}", response_description="Delete a country")
async def delete_country(id: str):
    return await delete_object(id, 'countries')


@app.delete("/heroclasses/{id}", response_description="Delete a class")
async def delete_class(id: str):
    return await delete_object(id, 'classes')
