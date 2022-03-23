from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import (
    get_object,
    create_document,
    get_all_objects,
    update_object,
    delete_object,
)
from schemas import RoadModel, AdminModel
from update_schemas import UpdateRoadModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(prefix="/road", tags=["Roads"])


@router.post(
    "",
    response_description="Add new road",
    response_model=RoadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_road(
    road: RoadModel = Body(...), current_user: AdminModel = Depends(get_current_user)
):
    """
    Create a road:

    - **current user** should be admin
    - **name**: name of the road
    - **from_obj**: name of the place, where the road starts
    - **to_obj**: name of the place, where the road ends
    - **energy**: value of energy that player needs to pass the road
    """
    return await create_document(road, "roads")


@router.get(
    "s",
    response_description="List all roads",
    response_model=List[RoadModel],
    status_code=status.HTTP_200_OK,
)
async def list_roads():
    """
    Get all roads
    """
    roads = await get_all_objects("roads")
    return roads


@router.get(
    "",
    response_description="Get a single road",
    response_model=RoadModel,
    status_code=status.HTTP_200_OK,
)
async def show_road(identifier: Optional[str] = None, road_name: Optional[str] = None):
    """
    Get a road by name:

    - **road_name**: name of the road
    """
    variables = locals()
    options = {"identifier": "_id", "road_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "roads")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "",
    response_description="Update a road",
    response_model=UpdateRoadModel,
    status_code=status.HTTP_200_OK,
)
async def update_road(
    identifier: Optional[str] = None,
    road_name: Optional[str] = None,
    road: UpdateRoadModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a road by name:

    - **current user** should be admin
    - **road_name**: name of the road
    - **name**: name of the road
    - **from_obj**: name of the place, where the road starts
    - **to_obj**: name of the place, where the road ends
    - **energy**: value of energy that player needs to pass the road
    """
    variables = locals()
    options = {"identifier": "_id", "road_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, road, "roads")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "", response_description="Delete a road", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_road(
    identifier: Optional[str] = None,
    road_name: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a road by name:

    - **current user** should be admin
    - **road_name**: name of the road
    """
    variables = locals()
    options = {"identifier": "_id", "road_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "roads")
    raise HTTPException(status_code=404, detail="Set some parameters")
