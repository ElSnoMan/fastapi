from typing import List
from fastapi import APIRouter, HTTPException
from app.models.users import User, users_db


router = APIRouter()


@router.get('/', tags=['users'], response_model=List[User])
async def get_users():
    return users_db


@router.get('/{email}', response_model=User)
async def get_user_by_email(email: str):
    for user in users_db:
        if user['email'] == email:
            return user
    raise HTTPException(status_code=404, detail='User not found')
