from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import CityModel, UpdateCityModel
from typing import Optional, List

router = APIRouter()


@router.post('/city', response_description='Add new city', response_model=CityModel,
             status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Cities'])
async def create_city(city: CityModel = Body(...)):
    return await create_document(city, 'cities')


@router.get('/cities', response_description='List all cities', response_model=List[CityModel],
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Cities'])
async def list_cities():
    cities = await get_all_objects('cities')
    return cities


@router.get('/city', response_description='Get a single city', response_model=CityModel,
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Cities'])
async def show_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/city', response_description='Update a city', response_model=UpdateCityModel,
            status_code=status.HTTP_200_OK, tags=['Update methods', 'Cities'])
async def update_city(identifier: Optional[str] = None, city_name: Optional[str] = None,
                      city: UpdateCityModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, city, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/city', response_description='Delete a city',
               status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Cities'])
async def delete_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')
