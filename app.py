from fastapi import FastAPI, Body, status
from typing import List

from schemas import *
from database import create_document, get_all_objects, get_object, update_object, delete_object

app = FastAPI()


@app.post('/player', response_description='Add new player', response_model=PlayerModel,
          status_code=status.HTTP_201_CREATED)
async def create_player(player: PlayerModel = Body(...)):
    return await create_document(player, 'players')


@app.post('/road', response_description='Add new road', response_model=RoadModel,
          status_code=status.HTTP_201_CREATED)
async def create_road(road: RoadModel = Body(...)):
    return await create_document(road, 'roads')


@app.post('/country', response_description='Add new country', response_model=CountryModel,
          status_code=status.HTTP_201_CREATED)
async def create_country(country: CountryModel = Body(...)):
    return await create_document(country, 'countries')


@app.post('/item', response_description='Add new item', response_model=ItemModel,
          status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemModel = Body(...)):
    return await create_document(item, 'items')


@app.post('/city', response_description='Add new city', response_model=CityModel,
          status_code=status.HTTP_201_CREATED)
async def create_city(city: CityModel = Body(...)):
    return await create_document(city, 'cities')


@app.post('/heroclass', response_description='Add new class', response_model=HeroClassModel,
          status_code=status.HTTP_201_CREATED)
async def create_class(hero_class: HeroClassModel = Body(...)):
    return await create_document(hero_class, 'classes')


@app.post('/horse', response_description='Add new horse', response_model=HorseModel,
          status_code=status.HTTP_201_CREATED)
async def create_horse(horse: HorseModel = Body(...)):
    return await create_document(horse, 'horses')


@app.get('/players', response_description='List all players', response_model=List[PlayerModel],
         status_code=status.HTTP_200_OK)
async def list_players():
    players = await get_all_objects('players')
    return players


@app.get('/roads', response_description='List all roads', response_model=List[RoadModel],
         status_code=status.HTTP_200_OK)
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@app.get('/countries', response_description='List all countries', response_model=List[CountryModel],
         status_code=status.HTTP_200_OK)
async def list_countries():
    countries = await get_all_objects('countries')
    return countries


@app.get('/heroclasses', response_description='List all classes', response_model=List[HeroClassModel],
         status_code=status.HTTP_200_OK)
async def list_classes():
    classes = await get_all_objects('classes')
    return classes


@app.get('/horses', response_description='List all horses', response_model=List[HorseModel],
         status_code=status.HTTP_200_OK)
async def list_horses():
    horses = await get_all_objects('horses')
    return horses


@app.get('/players', response_description='Get a single player', response_model=PlayerModel,
         status_code=status.HTTP_200_OK)
async def show_player(identifier: str):
    return await get_object(identifier, 'players')


@app.get('/roads/{id}', response_description='Get a single road', response_model=RoadModel,
         status_code=status.HTTP_200_OK)
async def show_road(identifier: str):
    return await get_object(identifier, 'roads')


@app.get('/countries/{id}', response_description='Get a single country', response_model=CountryModel,
         status_code=status.HTTP_200_OK)
async def show_country(identifier: str):
    return await get_object(identifier, 'countries')


@app.get('/heroclasses/{id}', response_description='Get a single class', response_model=HeroClassModel,
         status_code=status.HTTP_200_OK)
async def show_class(identifier: str):
    return await get_object(identifier, 'classes')


@app.get('/horses/{id}', response_description='Get a single horse', response_model=HorseModel,
         status_code=status.HTTP_200_OK)
async def show_horse(identifier: str):
    return await get_object(identifier, 'horses')


@app.put('/players/{id}', response_description='Update a player', response_model=UpdatePlayerModel,
         status_code=status.HTTP_200_OK)
async def update_player(identifier: str, player: UpdatePlayerModel = Body(...)):
    return await update_object(identifier, player, 'players')


@app.delete('/players/{id}', response_description='Delete a player',
            status_code=status.HTTP_200_OK)
async def delete_player(identifier: str):
    return await delete_object(identifier, 'players')


@app.delete('/roads/{id}', response_description='Delete a road',
            status_code=status.HTTP_200_OK)
async def delete_road(identifier: str):
    return await delete_object(identifier, 'roads')


@app.delete('/countries/{id}', response_description='Delete a country',
            status_code=status.HTTP_200_OK)
async def delete_country(identifier: str):
    return await delete_object(identifier, 'countries')


@app.delete('/heroclasses/{id}', response_description='Delete a class',
            status_code=status.HTTP_200_OK)
async def delete_class(identifier: str):
    return await delete_object(identifier, 'classes')
