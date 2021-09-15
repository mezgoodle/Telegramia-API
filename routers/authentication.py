from fastapi import APIRouter, HTTPException, status

from database import get_object
from schemas import Login, AdminModel
from hashing import Hash

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login', response_description='Login into API', response_model=AdminModel,
             status_code=status.HTTP_202_ACCEPTED)
async def login(request: Login):
    user = await get_object({'name': request.username}, 'admins')
    if not Hash.verify(user['password'], request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')
    # generate token
    return user
