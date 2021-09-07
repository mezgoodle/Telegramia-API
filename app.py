from typing import List

from fastapi import FastAPI, Body, status, HTTPException, Response

from database import create_document, get_all_objects, get_object, update_object, delete_object
from schemas import *

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
async def list_players(response: Response):
    players = await get_all_objects('players', response)
    return players


@app.get('/roads', response_description='List all roads', response_model=List[RoadModel],
         status_code=status.HTTP_200_OK)
async def list_roads(response: Response):
    roads = await get_all_objects('roads', response)
    return roads


@app.get('/countries', response_description='List all countries', response_model=List[CountryModel],
         status_code=status.HTTP_200_OK)
async def list_countries(response: Response):
    countries = await get_all_objects('countries', response)
    return countries


@app.get('/heroclasses', response_description='List all classes', response_model=List[HeroClassModel],
         status_code=status.HTTP_200_OK)
async def list_classes(response: Response):
    classes = await get_all_objects('classes', response)
    return classes


@app.get('/horses', response_description='List all horses', response_model=List[HorseModel],
         status_code=status.HTTP_200_OK)
async def list_horses(response: Response):
    horses = await get_all_objects('horses', response)
    return horses


@app.get('/player', response_description='Get a single player', response_model=PlayerModel,
         status_code=status.HTTP_200_OK)
async def show_player(response: Response, identifier: Optional[str] = None, nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/road', response_description='Get a single road', response_model=RoadModel,
         status_code=status.HTTP_200_OK)
async def show_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/country', response_description='Get a single country', response_model=CountryModel,
         status_code=status.HTTP_200_OK)
async def show_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/heroclass', response_description='Get a single class', response_model=HeroClassModel,
         status_code=status.HTTP_200_OK)
async def show_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/horse', response_description='Get a single horse', response_model=HorseModel,
         status_code=status.HTTP_200_OK)
async def show_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/player', response_description='Update a player', response_model=UpdatePlayerModel,
         status_code=status.HTTP_200_OK)
async def update_player(identifier: Optional[str] = None, nickname: Optional[str] = None,
                        username: Optional[str] = None, player: UpdatePlayerModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, player, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/player', response_description='Delete a player',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(identifier: Optional[str] = None,
                        nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/road', response_description='Delete a road',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/country', response_description='Delete a country',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/heroclass', response_description='Delete a class',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')
