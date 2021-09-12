from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import HeroClassModel, UpdateHeroClassModel
from typing import Optional, List

router = APIRouter()


@router.post('/heroclass', response_description='Add new class', response_model=HeroClassModel,
             status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Hero classes'])
async def create_class(hero_class: HeroClassModel = Body(...)):
    return await create_document(hero_class, 'classes')


@router.get('/heroclasses', response_description='List all classes', response_model=List[HeroClassModel],
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Hero classes'])
async def list_classes():
    classes = await get_all_objects('classes')
    return classes


@router.get('/heroclass', response_description='Get a single class', response_model=HeroClassModel,
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Hero classes'])
async def show_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/heroclass', response_description='Update a class', response_model=UpdateHeroClassModel,
            status_code=status.HTTP_200_OK, tags=['Update methods', 'Hero classes'])
async def update_class(identifier: Optional[str] = None, class_name: Optional[str] = None,
                       hero_class: UpdateHeroClassModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, hero_class, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/heroclass', response_description='Delete a class',
               status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Hero classes'])
async def delete_class(identifier: Optional[str] = None, class_name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'class_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'classes')
    raise HTTPException(status_code=404, detail='Set some parameters')
