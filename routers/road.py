from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import RoadModel, UpdateRoadModel, AdminModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(
    prefix='/road',
    tags=['Roads']
)


@router.post('', response_description='Add new road', response_model=RoadModel,
             status_code=status.HTTP_201_CREATED)
async def create_road(road: RoadModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    return await create_document(road, 'roads')


@router.get('s', response_description='List all roads', response_model=List[RoadModel],
            status_code=status.HTTP_200_OK)
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@router.get('', response_description='Get a single road', response_model=RoadModel,
            status_code=status.HTTP_200_OK)
async def show_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update a road', response_model=UpdateRoadModel,
            status_code=status.HTTP_200_OK)
async def update_road(identifier: Optional[str] = None, name: Optional[str] = None,
                      road: UpdateRoadModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, road, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete a road',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_road(identifier: Optional[str] = None, name: Optional[str] = None,
                      current_user: AdminModel = Depends(get_current_user)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')
