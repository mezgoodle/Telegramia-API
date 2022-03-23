from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from database import get_object
from hashing import Hash
from auth_token import create_access_token

router = APIRouter(tags=["Authentication"])


@router.post(
    "/login",
    response_description="Login into API",
    status_code=status.HTTP_202_ACCEPTED,
)
async def login(request: OAuth2PasswordRequestForm = Depends()):
    """
    Login into API to get admin permissions:

    - **name**: admin name
    - **password**: admin password
    """
    user = await get_object({"name": request.username}, "admins")
    if not Hash.verify(user["password"], request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )
    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
