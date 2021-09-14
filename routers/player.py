from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import PlayerModel, UpdatePlayerModel
from typing import Optional, List

router = APIRouter(
    prefix='/player',
    tags=['Players']
)


@router.post('', response_description='Add new player', response_model=PlayerModel,
             status_code=status.HTTP_201_CREATED)
async def create_player(player: PlayerModel = Body(...)):
    return await create_document(player, 'players')


@router.get('s', response_description='List all players', response_model=List[PlayerModel],
            status_code=status.HTTP_200_OK)
async def list_players():
    players = await get_all_objects('players')
    return players


@router.get('', response_description='Get a single player', response_model=PlayerModel,
            status_code=status.HTTP_200_OK)
async def show_player(identifier: Optional[str] = None, nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update a player', response_model=UpdatePlayerModel,
            status_code=status.HTTP_200_OK)
async def update_player(identifier: Optional[str] = None, nickname: Optional[str] = None,
                        username: Optional[str] = None, player: UpdatePlayerModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, player, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete a player',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(identifier: Optional[str] = None,
                        nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')
