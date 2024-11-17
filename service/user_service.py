import datetime
from typing import Optional
from fastapi import HTTPException
from api.internalApi.poll_service import poll_service_api
from model.user import User
from repository import user_repository


async def get_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)


async def create_user(user: User) -> int:
    return await user_repository.create_user(user)


async def update_user(user_id, user):
    existing_user = await get_by_id(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404, detail=f"Can't update user with id: {user_id}, user not found"
        )
    else:
        await user_repository.update_user(user_id, user)


async def delete_user_by_id(user_id):
    existing_user = await get_by_id(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404, detail=f"Can't delete user with id: {user_id}, user not found"
        )
    else:
        await poll_service_api.delete_all_user_answers_by_user_id(user_id)
        await user_repository.delete_user_by_id(user_id)


async def register_user_by_id(user_id):
    existing_user = await get_by_id(user_id)
    if not existing_user:
        raise HTTPException(
            status_code=404, detail=f"Can't register user with id: {user_id}, user not found"
        )
    else:
        joining_data = datetime.datetime.now(datetime.UTC)
        await user_repository.register_user_by_id(user_id, joining_data)
