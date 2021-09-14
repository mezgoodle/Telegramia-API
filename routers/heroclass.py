from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import HeroClassModel, UpdateHeroClassModel
from typing import Optional, List

router = APIRouter(
    prefix='/heroclass',
    tags=['Hero classes']
)


@router.post('', response_description='Add new class', response_model=HeroClassModel,
             status_code=status.HTTP_201_CREATED)
async def create_class(hero_class: HeroClassModel = Body(...)):
    return await create_document(hero_class, 'classes')


@router.get('es', response_description='List all classes', response_model=List[HeroClassModel],
            status_code=status.HTTP_200_OK)
async def list_classes():
    classes = await get_all_objects('classes')
    return classes


@router.get('', response_description='Get a single class', response_model=HeroClassModel,
            status_code=status.HTTP_200_OK)
async def show_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update a class', response_model=UpdateHeroClassModel,
            status_code=status.HTTP_200_OK)
async def update_class(identifier: Optional[str] = None, class_name: Optional[str] = None,
                       hero_class: UpdateHeroClassModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, hero_class, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete a class',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')
