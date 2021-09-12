from typing import List

from fastapi import FastAPI, Body, status, HTTPException

from database import create_document, get_all_objects, get_object, update_object, delete_object
from schemas import *
from hashing import Hash
from routers import player

app = FastAPI()

app.include_router(player.router)


@app.post('/road', response_description='Add new road', response_model=RoadModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Roads'])
async def create_road(road: RoadModel = Body(...)):
    return await create_document(road, 'roads')


@app.post('/country', response_description='Add new country', response_model=CountryModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Countries'])
async def create_country(country: CountryModel = Body(...)):
    return await create_document(country, 'countries')


@app.post('/item', response_description='Add new item', response_model=ItemModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Items'])
async def create_item(item: ItemModel = Body(...)):
    return await create_document(item, 'items')


@app.post('/city', response_description='Add new city', response_model=CityModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Cities'])
async def create_city(city: CityModel = Body(...)):
    return await create_document(city, 'cities')


@app.post('/heroclass', response_description='Add new class', response_model=HeroClassModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Hero classes'])
async def create_class(hero_class: HeroClassModel = Body(...)):
    return await create_document(hero_class, 'classes')


@app.post('/horse', response_description='Add new horse', response_model=HorseModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Horses'])
async def create_horse(horse: HorseModel = Body(...)):
    return await create_document(horse, 'horses')


# TODO: add authentication
@app.post('/admin', response_description='Add new admin', response_model=AdminModel,
          status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Admins'])
async def create_admin(admin: AdminModel = Body(...)):
    admin.password = Hash.bcrypt(admin.password)
    return await create_document(admin, 'admins')


@app.get('/roads', response_description='List all roads', response_model=List[RoadModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Roads'])
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@app.get('/countries', response_description='List all countries', response_model=List[CountryModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Countries'])
async def list_countries():
    countries = await get_all_objects('countries')
    return countries


@app.get('/heroclasses', response_description='List all classes', response_model=List[HeroClassModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Hero classes'])
async def list_classes():
    classes = await get_all_objects('classes')
    return classes


@app.get('/horses', response_description='List all horses', response_model=List[HorseModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Horses'])
async def list_horses():
    horses = await get_all_objects('horses')
    return horses


@app.get('/items', response_description='List all items', response_model=List[ItemModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Items'])
async def list_items():
    items = await get_all_objects('items')
    return items


@app.get('/cities', response_description='List all cities', response_model=List[CityModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Cities'])
async def list_cities():
    cities = await get_all_objects('cities')
    return cities


@app.get('/admins', response_description='List all admins', response_model=List[ShowAdminModel],
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Admins'])
async def list_admins():
    admins = await get_all_objects('admins')
    return admins


@app.get('/road', response_description='Get a single road', response_model=RoadModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Roads'])
async def show_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/country', response_description='Get a single country', response_model=CountryModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Countries'])
async def show_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/heroclass', response_description='Get a single class', response_model=HeroClassModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Hero classes'])
async def show_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/horse', response_description='Get a single horse', response_model=HorseModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Horses'])
async def show_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/item', response_description='Get a single item', response_model=ItemModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Items'])
async def show_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/city', response_description='Get a single city', response_model=CityModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Cities'])
async def show_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.get('/admin', response_description='Get a single admin', response_model=ShowAdminModel,
         status_code=status.HTTP_200_OK, tags=['Get methods', 'Admins'])
async def show_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/road', response_description='Update a road', response_model=UpdateRoadModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Roads'])
async def update_road(identifier: Optional[str] = None, name: Optional[str] = None,
                      road: UpdateRoadModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, road, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/country', response_description='Update a country', response_model=UpdateCountryModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Countries'])
async def update_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None,
                         country: UpdateCountryModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, country, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/item', response_description='Update an item', response_model=UpdateItemModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Items'])
async def update_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None,
                      item: UpdateItemModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key], 'city': city_name}, item, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/city', response_description='Update a city', response_model=UpdateCityModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Cities'])
async def update_city(identifier: Optional[str] = None, city_name: Optional[str] = None,
                      city: UpdateCityModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, city, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/heroclass', response_description='Update a class', response_model=UpdateHeroClassModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Hero classes'])
async def update_class(identifier: Optional[str] = None, class_name: Optional[str] = None,
                       hero_class: UpdateHeroClassModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, hero_class, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/horse', response_description='Update a horse', response_model=UpdateHorseModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Horses'])
async def update_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None,
                       horse: UpdateHeroClassModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, horse, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.put('/admin', response_description='Update an admin', response_model=UpdateAdminModel,
         status_code=status.HTTP_200_OK, tags=['Update methods', 'Admins'])
async def update_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None,
                       admin: UpdateAdminModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, admin, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/road', response_description='Delete a road',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Roads'])
async def delete_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/country', response_description='Delete a country',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Countries'])
async def delete_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/heroclass', response_description='Delete a class',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Hero classes'])
async def delete_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/item', response_description='Delete an item',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Items'])
async def delete_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/city', response_description='Delete a city',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Cities'])
async def delete_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/horse', response_description='Delete a horse',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Horses'])
async def delete_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@app.delete('/admin', response_description='Delete an admin',
            status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Admins'])
async def delete_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')
