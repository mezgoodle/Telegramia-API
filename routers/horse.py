from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import HorseModel, UpdateHorseModel
from typing import Optional, List

router = APIRouter(
    tags=['Horses']
)


@router.post('/horse', response_description='Add new horse', response_model=HorseModel,
             status_code=status.HTTP_201_CREATED)
async def create_horse(horse: HorseModel = Body(...)):
    return await create_document(horse, 'horses')


@router.get('/horses', response_description='List all horses', response_model=List[HorseModel],
            status_code=status.HTTP_200_OK)
async def list_horses():
    horses = await get_all_objects('horses')
    return horses


@router.get('/horse', response_description='Get a single horse', response_model=HorseModel,
            status_code=status.HTTP_200_OK)
async def show_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/horse', response_description='Update a horse', response_model=UpdateHorseModel,
            status_code=status.HTTP_200_OK)
async def update_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None,
                       horse: UpdateHorseModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, horse, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/horse', response_description='Delete a horse',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')
