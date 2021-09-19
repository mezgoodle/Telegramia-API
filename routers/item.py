from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import ItemModel, UpdateItemModel, AdminModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix='/item',
    tags=['Items']
)


@router.post('', response_description='Add new item', response_model=ItemModel,
             status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Create an item:

    - **current user** should be admin
    - **name**: item name
    - **characteristic**: the name of the characteristic which will have a bonus
    - **bonus**: bonus from item to characteristic
    - **city**: city, where item is selling
    - **price**: price of the item
    """
    return await create_document(item, 'items')


@router.get('s', response_description='List all items', response_model=List[ItemModel],
            status_code=status.HTTP_200_OK)
async def list_items():
    """
    Get all items
    """
    items = await get_all_objects('items')
    return items


@router.get('', response_description='Get a single item', response_model=ItemModel,
            status_code=status.HTTP_200_OK)
async def show_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None):
    """
    Get an item by item and city name:

    - **current user** should be admin
    - **item_name**: item name
    - **city_name**: city name, where item is selling
    """
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update an item', response_model=UpdateItemModel,
            status_code=status.HTTP_200_OK)
async def update_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None,
                      item: UpdateItemModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Update an item by item and city name:

    - **current user** should be admin
    - **item_name**: item name
    - **city_name**: city name, where item is selling
    """
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key], 'city': city_name}, item, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete an item',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(identifier: Optional[str] = None, item_name: Optional[str] = None, city_name: str = None,
                      current_user: AdminModel = Depends(get_current_user)):
    """
    Delete an item by item and city name:

    - **current user** should be admin
    - **item_name**: item name
    - **city_name**: city name, where item is selling
    """
    variables = locals()
    options = {'identifier': '_id', 'item_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key], 'city': city_name}, 'items')
    raise HTTPException(status_code=404, detail='Set some parameters')
