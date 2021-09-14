from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import CityModel, UpdateCityModel
from typing import Optional, List

router = APIRouter(
    prefix='/cit',
    tags=['Cities']
)


@router.post('y', response_description='Add new city', response_model=CityModel,
             status_code=status.HTTP_201_CREATED)
async def create_city(city: CityModel = Body(...)):
    return await create_document(city, 'cities')


@router.get('ies', response_description='List all cities', response_model=List[CityModel],
            status_code=status.HTTP_200_OK)
async def list_cities():
    cities = await get_all_objects('cities')
    return cities


@router.get('y', response_description='Get a single city', response_model=CityModel,
            status_code=status.HTTP_200_OK)
async def show_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('y', response_description='Update a city', response_model=UpdateCityModel,
            status_code=status.HTTP_200_OK)
async def update_city(identifier: Optional[str] = None, city_name: Optional[str] = None,
                      city: UpdateCityModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, city, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('y', response_description='Delete a city',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')
