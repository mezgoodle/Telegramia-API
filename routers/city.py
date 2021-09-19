from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from oauth2 import get_current_user
from schemas import CityModel, UpdateCityModel, AdminModel
from typing import Optional, List

router = APIRouter(
    prefix='/cit',
    tags=['Cities']
)


@router.post('y', response_description='Add new city', response_model=CityModel,
             status_code=status.HTTP_201_CREATED)
async def create_city(city: CityModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Create a city:

    - **current user** should be admin
    - **name**: city name
    - **is_capital**: boolean value
    - **market**: boolean value
    - **academy**: boolean value
    - **temple**: boolean value
    - **tavern**: boolean value
    - **menagerie**: boolean value
    """
    return await create_document(city, 'cities')


@router.get('ies', response_description='List all cities', response_model=List[CityModel],
            status_code=status.HTTP_200_OK)
async def list_cities():
    """
    Get all cities
    """
    cities = await get_all_objects('cities')
    return cities


@router.get('y', response_description='Get a single city', response_model=CityModel,
            status_code=status.HTTP_200_OK)
async def show_city(identifier: Optional[str] = None, city_name: Optional[str] = None):
    """
    Get a city by name:

    - **city_name**: city name
    """
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('y', response_description='Update a city', response_model=UpdateCityModel,
            status_code=status.HTTP_200_OK)
async def update_city(identifier: Optional[str] = None, city_name: Optional[str] = None,
                      city: UpdateCityModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Update a city by name:

    - **current user** should be admin
    - **city_name**: city name
    """
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, city, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('y', response_description='Delete a city',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(identifier: Optional[str] = None, city_name: Optional[str] = None,
                      current_user: AdminModel = Depends(get_current_user)):
    """
    Delete a city by name:

    - **current user** should be admin
    - **city_name**: city name
    """
    variables = locals()
    options = {'identifier': '_id', 'city_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'cities')
    raise HTTPException(status_code=404, detail='Set some parameters')
