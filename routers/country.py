from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import CountryModel, UpdateCountryModel
from typing import Optional, List

router = APIRouter(
    tags=['Countries']
)


@router.post('/country', response_description='Add new country', response_model=CountryModel,
             status_code=status.HTTP_201_CREATED)
async def create_country(country: CountryModel = Body(...)):
    return await create_document(country, 'countries')


@router.get('/countries', response_description='List all countries', response_model=List[CountryModel],
            status_code=status.HTTP_200_OK)
async def list_countries():
    countries = await get_all_objects('countries')
    return countries


@router.get('/country', response_description='Get a single country', response_model=CountryModel,
            status_code=status.HTTP_200_OK)
async def show_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/country', response_description='Update a country', response_model=UpdateCountryModel,
            status_code=status.HTTP_200_OK)
async def update_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None,
                         country: UpdateCountryModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, country, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/country', response_description='Delete a country',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(identifier: Optional[str] = None, name: Optional[str] = None, capital: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name', 'capital': 'capital'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'countries')
    raise HTTPException(status_code=404, detail='Set some parameters')
