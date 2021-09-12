from fastapi import APIRouter, status, HTTPException, Body
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import PlayerModel, UpdatePlayerModel
from typing import Optional, List

router = APIRouter()


@router.post('/player', response_description='Add new player', response_model=PlayerModel,
             status_code=status.HTTP_201_CREATED, tags=['Post methods', 'Players'])
async def create_player(player: PlayerModel = Body(...)):
    return await create_document(player, 'players')


@router.get('/players', response_description='List all players', response_model=List[PlayerModel],
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Players'])
async def list_players():
    players = await get_all_objects('players')
    return players


@router.get('/player', response_description='Get a single player', response_model=PlayerModel,
            status_code=status.HTTP_200_OK, tags=['Get methods', 'Players'])
async def show_player(identifier: Optional[str] = None, nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('/player', response_description='Update a player', response_model=UpdatePlayerModel,
            status_code=status.HTTP_200_OK, tags=['Update methods', 'Players'])
async def update_player(identifier: Optional[str] = None, nickname: Optional[str] = None,
                        username: Optional[str] = None, player: UpdatePlayerModel = Body(...)):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, player, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('/player', response_description='Delete a player',
               status_code=status.HTTP_204_NO_CONTENT, tags=['Delete methods', 'Players'])
async def delete_player(identifier: Optional[str] = None,
                        nickname: Optional[str] = None, username: Optional[str] = None):
    variables = locals()
    options = {'identifier': '_id', 'nickname': 'name', 'username': 'telegram_name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'players')
    raise HTTPException(status_code=404, detail='Set some parameters')
