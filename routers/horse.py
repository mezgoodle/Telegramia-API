from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import HorseModel, UpdateHorseModel, AdminModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix='/horse',
    tags=['Horses']
)


@router.post('', response_description='Add new horse', response_model=HorseModel,
             status_code=status.HTTP_201_CREATED)
async def create_horse(horse: HorseModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Create a horse:

    - **current user** should be admin
    - **name**: horse name
    - **bonus**: speed bonus from horse
    - **city**: city name, where horse is selling
    - **price**: price of the horse
    """
    return await create_document(horse, 'horses')


@router.get('s', response_description='List all horses', response_model=List[HorseModel],
            status_code=status.HTTP_200_OK)
async def list_horses():
    """
    Get all horses
    """
    horses = await get_all_objects('horses')
    return horses


@router.get('', response_description='Get a single horse', response_model=HorseModel,
            status_code=status.HTTP_200_OK)
async def show_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None):
    """
    Get a horse by name

    - **horse_name**: horse name
    """
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update a horse', response_model=UpdateHorseModel,
            status_code=status.HTTP_200_OK)
async def update_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None,
                       horse: UpdateHorseModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Update a horse by name

    - **current user** should be admin
    - **horse_name**: horse name
    """
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, horse, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete a horse',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_horse(identifier: Optional[str] = None, horse_name: Optional[str] = None,
                       current_user: AdminModel = Depends(get_current_user)):
    """
    Delete a horse by name

    - **current user** should be admin
    - **horse_name**: horse name
    """
    variables = locals()
    options = {'identifier': '_id', 'horse_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'horses')
    raise HTTPException(status_code=404, detail='Set some parameters')
