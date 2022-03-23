from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import (
    get_object,
    create_document,
    get_all_objects,
    update_object,
    delete_object,
)
from schemas import DungeonModel, AdminModel
from update_schemas import UpdateDungeonModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(prefix="/dungeon", tags=["Dungeons"])


@router.post(
    "",
    response_description="Add new dungeon",
    response_model=DungeonModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_dungeon(
    dungeon: DungeonModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Create a dungeon:

    - **current user** should be admin
    - **name**: dungeon's name
    - **description**: dungeon's dictionary
    - **damage**: damage value that player will get
    - **base_time**: basic time to take dungeon, total float number in seconds
    - **treasure**: money value that player will get
    - **members**: dictionary with player's name and his date, when he has started, as a str
    """
    return await create_document(dungeon, "dungeons")


@router.get(
    "s",
    response_description="List all dungeons",
    response_model=List[DungeonModel],
    status_code=status.HTTP_200_OK,
)
async def list_dungeons():
    """
    Get all dungeons
    """
    dungeons = await get_all_objects("dungeons")
    return dungeons


@router.get(
    "",
    response_description="Get a single dungeon",
    response_model=DungeonModel,
    status_code=status.HTTP_200_OK,
)
async def show_dungeon(
    identifier: Optional[str] = None, dungeon_name: Optional[str] = None
):
    """
    Get a dungeon_name by name:

    - **dungeon_name**: dungeon name
    """
    variables = locals()
    options = {"identifier": "_id", "dungeon_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "dungeons")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "",
    response_description="Update a dungeon",
    response_model=UpdateDungeonModel,
    status_code=status.HTTP_200_OK,
)
async def update_dungeon(
    identifier: Optional[str] = None,
    dungeon_name: Optional[str] = None,
    dungeon: UpdateDungeonModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a dungeon:

    - **current user** should be admin
    - **dungeon_name**: dungeon's name
    - **description**: dungeon's dictionary
    - **damage**: damage value that player will get
    - **base_time**: basic time to take dungeon, total float number in seconds
    - **treasure**: money value that player will get
    - **members**: dictionary with player's name and his date, when he has started, as a str
    """
    variables = locals()
    options = {"identifier": "_id", "dungeon_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object(
                {options[key]: variables[key]}, dungeon, "dungeons"
            )
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "", response_description="Delete a dungeon", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_dungeon(
    identifier: Optional[str] = None,
    dungeon_name: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a dungeon:

    - **current user** should be admin
    - **dungeon_name**: dungeon name
    """
    variables = locals()
    options = {"identifier": "_id", "dungeon_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "dungeons")
    raise HTTPException(status_code=404, detail="Set some parameters")
