import httpx
from config.config import Config

config = Config()


async def delete_all_user_answers_by_user_id(user_id: int):
    url = f"{config.POLL_SERVICE_BASE_URL}/poll/user/{user_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()

        except httpx.HTTPStatusError as exception:
            print(f"Error in delete all user-answers for {user_id} with error: {exception.response}")
            return None
