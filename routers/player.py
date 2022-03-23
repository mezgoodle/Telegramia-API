from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import (
    get_object,
    create_document,
    get_all_objects,
    update_object,
    delete_object,
)
from schemas import PlayerModel, AdminModel
from update_schemas import UpdatePlayerModel
from oauth2 import get_current_user
from typing import Optional, List

router = APIRouter(prefix="/player", tags=["Players"])


@router.post(
    "",
    response_description="Add new player",
    response_model=PlayerModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_player(
    player: PlayerModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Create a player:

    - **current user** should be admin
    - **user_id**: user id from Telegram
    - **telegram_name**: the user nickname in Telegram
    - **name**: game name
    - **level**: player level
    - **experience**: current player experience
    - **health**: current player health
    - **energy**: current player energy
    - **strength**: current player strength
    - **agility**: current player agility
    - **intuition**: current player intuition
    - **intelligence**: current player intelligence
    - **hero_class**: player hero class
    - **nation**: name of the country where player was born
    - **money**: current player money
    - **items**: list of items that player has
    - **mount**: description of the mount
    - **current_state**: place where player is at this time
    """
    return await create_document(player, "players")


@router.get(
    "s",
    response_description="List all players",
    response_model=List[PlayerModel],
    status_code=status.HTTP_200_OK,
)
async def list_players():
    """
    Get all players
    """
    players = await get_all_objects("players")
    return players


@router.get(
    "",
    response_description="Get a single player",
    response_model=PlayerModel,
    status_code=status.HTTP_200_OK,
)
async def show_player(
    identifier: Optional[str] = None,
    nickname: Optional[str] = None,
    username: Optional[str] = None,
):
    """
    Get a player by nickname or username

    - **nickname**: player name in the game
    - **username**: player name in the Telegram
    """
    variables = locals()
    options = {"identifier": "_id", "nickname": "name", "username": "telegram_name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, "players")
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.put(
    "",
    response_description="Update a player",
    response_model=UpdatePlayerModel,
    status_code=status.HTTP_200_OK,
)
async def update_player(
    identifier: Optional[str] = None,
    nickname: Optional[str] = None,
    username: Optional[str] = None,
    player: UpdatePlayerModel = Body(...),
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Update a player by nickname or username

    - **current user** should be admin
    - **nickname**: player name in the game
    - **username**: player name in the Telegram
    - **user_id**: user id from Telegram
    - **telegram_name**: the user nickname in Telegram
    - **name**: game name
    - **level**: player level
    - **experience**: current player experience
    - **health**: current player health
    - **energy**: current player energy
    - **strength**: current player strength
    - **agility**: current player agility
    - **intuition**: current player intuition
    - **intelligence**: current player intelligence
    - **hero_class**: player hero class
    - **nation**: name of the country where player was born
    - **money**: current player money
    - **items**: list of items that player has
    - **mount**: description of the mount
    - **current_state**: place where player is at this time
    """
    variables = locals()
    options = {"identifier": "_id", "nickname": "name", "username": "telegram_name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object(
                {options[key]: variables[key]}, player, "players"
            )
    raise HTTPException(status_code=404, detail="Set some parameters")


@router.delete(
    "", response_description="Delete a player", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_player(
    identifier: Optional[str] = None,
    nickname: Optional[str] = None,
    username: Optional[str] = None,
    current_user: AdminModel = Depends(get_current_user),
):
    """
    Delete a player by nickname or username

    - **current user** should be admin
    - **nickname**: player name in the game
    - **username**: player name in the Telegram
    """
    variables = locals()
    options = {"identifier": "_id", "nickname": "name", "username": "telegram_name"}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, "players")
    raise HTTPException(status_code=404, detail="Set some parameters")
