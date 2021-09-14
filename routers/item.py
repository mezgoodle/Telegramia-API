from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import ItemModel, UpdateItemModel
from typing import Optional, List

router = APIRouter(
    tags=['Items']
)


@router.post('/item', response_description='Add new item', response_model=ItemModel,
             status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemModel = Body(...)):
    return await create_document(item, 'items')


@router.get('/items', response_description='List all items', response_model=List[ItemModel],
            status_code=status.HTTP_200_OK)
async def list_items():
    items = await get_all_objects('items')
    return items


@router.get('/item', response_description='Get a single item', response_model=ItemModel,
            status_code=status.HTTP_200_OK)
async def show_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/item', response_description='Update an item', response_model=UpdateItemModel,
            status_code=status.HTTP_200_OK)
async def update_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None,
                      item: UpdateItemModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key], 'city': city_name}, item, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/item', response_description='Delete an item',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None):
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')
