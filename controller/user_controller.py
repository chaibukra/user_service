from typing import Optional
from fastapi import APIRouter, HTTPException
from starlette import status
from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int) -> Optional[User]:
    user = await user_service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    user_id = await user_service.create_user(user)
    return {"message": f"User successfully created - the user id is: {user_id}"}



@router.put("/{user_id}")
async def update_user(user_id: int, user: User):
    await user_service.update_user(user_id, user)
    return await get_user_by_id(user_id)


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int):
    await user_service.delete_user_by_id(user_id)
    return {"message": f"User successfully deleted"}


@router.put("/register/{user_id}")
async def register_user_by_id(user_id: int):
    await user_service.register_user_by_id(user_id)
    return {"message": f"User successfully registered"}
