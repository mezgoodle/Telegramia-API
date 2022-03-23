from fastapi import APIRouter, status, HTTPException, Body, Depends

from database import (
    get_object,
    create_document,
    get_all_objects,
    update_object,
    delete_object,
)
from schemas import RaidModel, RaidLevelModel, AdminModel
from update_schemas import UpdateRaidModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(prefix="/raid", tags=["Raids and raids' levels"])


@router.post(
    "",
    response_description="Add new raid",
    response_model=RaidModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_raid(
    raid: RaidModel = Body(...), current_user: AdminModel = Depends(get_current_user)
):
    """
    Create a raid:

    - **current user** should be admin
    - **name**: raid name
    - **description**: raid description
    - **members**: dictionary with the players' names, their times to pass the raid level and level itself
    """
    return await create_document(raid, "raids")


@router.get(
    "s",
    response_description="List all raids",
    response_model=List[RaidModel],
    status_code=status.HTTP_200_OK,
)
async def list_raids():
    """
    Get all raids
    """
    raids = await get_all_objects("raids")
    return raids


@router.get(
    "levels",
    response_description="List all raid levels",
    response_model=List[RaidLevelModel],
    status_code=status.HTTP_200_OK,
)
async def list_raidlevels(raid_name: Optional[str] = None):
    """
    Get all raid levels by raid level:

    - **raid_name**: raid name
    """
    raid_levels = await get_all_objects("raid_levels", {"raid_name": raid_name})
    return raid_levels


@router.get(
    "",
    response_description="Get a single raid",
    response_model=RaidModel,
    status_code=status.HTTP_200_OK,
)
async def show_raid(identifier: Optional[str] = None, raid_name: Optional[str] = None):
    """
    Show a raid by name:

    - **raid_name**: raid name
    """
    variables = locals()
    options = {"identifier": "_id", "raid_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "",
    response_description="Update a raid",
    response_model=UpdateRaidModel,
    status_code=status.HTTP_200_OK,
)
async def update_raid(
    identifier: Optional[str] = None,
    raid_name: Optional[str] = None,
    raid: UpdateRaidModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a raid by name:

    - **current user** should be admin
    - **raid_name**: raid name
    - **name**: raid name
    - **description**: raid description
    - **members**: dictionary with the players' names, their times to pass the raid level and level itself
    """
    variables = locals()
    options = {"identifier": "_id", "raid_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, raid, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "", response_description="Delete a raid", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_raid(
    identifier: Optional[str] = None,
    raid_name: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a raid by name:

    - **current user** should be admin
    - **raid_name**: raid name
    """
    variables = locals()
    options = {"identifier": "_id", "raid_name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")
