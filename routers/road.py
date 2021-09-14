from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import RoadModel, UpdateRoadModel
from typing import Optional, List

router = APIRouter(
    tags=['Roads']
)


@router.post('/road', response_description='Add new road', response_model=RoadModel,
             status_code=status.HTTP_201_CREATED)
async def create_road(road: RoadModel = Body(...)):
    return await create_document(road, 'roads')


@router.get('/roads', response_description='List all roads', response_model=List[RoadModel],
            status_code=status.HTTP_200_OK)
async def list_roads():
    roads = await get_all_objects('roads')
    return roads


@router.get('/road', response_description='Get a single road', response_model=RoadModel,
            status_code=status.HTTP_200_OK)
async def show_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/road', response_description='Update a road', response_model=UpdateRoadModel,
            status_code=status.HTTP_200_OK)
async def update_road(identifier: Optional[str] = None, name: Optional[str] = None,
                      road: UpdateRoadModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, road, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/road', response_description='Delete a road',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_road(identifier: Optional[str] = None, name: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'roads')
    raise HTTPException(status_code=404, detail='Set some parameters')
