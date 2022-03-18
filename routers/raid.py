from fastapi import APIRouter, status, HTTPException, Body, Depends

from database import (
    get_object,
    create_document,
    get_all_objects,
    update_object,
    delete_object,
)
from schemas import RaidModel, RaidLevelModel, AdminModel
from update_schemas import UpdateRaidModel, UpdateRaidLevelModel
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
    - **name**: country name
    - **description**: country description
    - **capital**: capital name of the country
    - **population**: population of the country
    """
    return await create_document(raid, "raids")


@router.post(
    "_level",
    response_description="Add new raid",
    response_model=RaidModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_raid_level(
    raid_level: RaidLevelModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Create a raid:

    - **current user** should be admin
    - **name**: country name
    - **description**: country description
    - **capital**: capital name of the country
    - **population**: population of the country
    """
    return await create_document(raid_level, "raid_levels")


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
    response_description="List all raids",
    response_model=List[RaidModel],
    status_code=status.HTTP_200_OK,
)
async def list_raidlevels(name: Optional[str] = None):
    """
    Get all raids
    """
    raid_levels = await get_all_objects("raid_levels", {"name": name})
    return raid_levels


@router.get(
    "_levels",
    response_description="List all raids",
    response_model=List[RaidModel],
    status_code=status.HTTP_200_OK,
)
async def list_raid_levels():
    """
    Get all raids
    """
    raid_levels = await get_all_objects("raid_levels")
    return raid_levels


@router.get(
    "",
    response_description="Get a single raid",
    response_model=RaidModel,
    status_code=status.HTTP_200_OK,
)
async def show_raid(identifier: Optional[str] = None, name: Optional[str] = None):
    """
    Show a country by name or capital name:

    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.get(
    "_level",
    response_description="Get a single raid",
    response_model=RaidModel,
    status_code=status.HTTP_200_OK,
)
async def show_raid_level(identifier: Optional[str] = None, name: Optional[str] = None):
    """
    Show a country by name or capital name:

    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "raid_levels")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "",
    response_description="Update a raid",
    response_model=UpdateRaidModel,
    status_code=status.HTTP_200_OK,
)
async def update_raid(
    identifier: Optional[str] = None,
    name: Optional[str] = None,
    raid: UpdateRaidModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, raid, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "_level",
    response_description="Update a raid",
    response_model=UpdateRaidModel,
    status_code=status.HTTP_200_OK,
)
async def update_raid_level(
    identifier: Optional[str] = None,
    name: Optional[str] = None,
    raid_level: UpdateRaidLevelModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object(
                {options[key]: variables[key]}, raid_level, "raid_levels"
            )
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "", response_description="Delete a raid", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_raid(
    identifier: Optional[str] = None,
    name: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "raids")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "_level",
    response_description="Delete a raid",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_raid_level(
    identifier: Optional[str] = None,
    name: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a country by name or capital name:

    - **current user** should be admin
    - **name**: country name
    - **capital**: capital name of the country
    """
    variables = locals()
    options = {"identifier": "_id", "name": "name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "raid_levels")
    raise HTTPException(status_code=404, detail="Set some parameters")
