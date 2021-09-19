from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import CountryModel, UpdateCountryModel, AdminModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix='/countr',
    tags=['Countries']
)


@router.post('y', response_description='Add new country', response_model=CountryModel,
             status_code=status.HTTP_201_CREATED)
async def create_country(country: CountryModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Create a country:

    - **current user** should be admin
    - **name**: country name
    - **description**: country description
    - **capital**: capital name of the country
    - **population**: population of the country
    """
    return await create_document(country, 'countries')


@router.get('ies', response_description='List all countries', response_model=List[CountryModel],
            status_code=status.HTTP_200_OK)
async def list_countries():
    """
    Get all countries
    """
    countries = await get_all_objects('countries')
    return countries


@router.get('y', response_description='Get a single country', response_model=CountryModel,
            status_code=status.HTTP_200_OK)
async def show_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    """
    Show a country by name or capital name:

    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('y', response_description='Update a country', response_model=UpdateCountryModel,
            status_code=status.HTTP_200_OK)
async def update_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None,
                         country: UpdateCountryModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Update a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, country, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('y', response_description='Delete a country',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None,
                         current_user: AdminModel = Depends(get_current_user)):
    """
    Delete a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')
