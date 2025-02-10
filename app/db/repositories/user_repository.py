# app/db/repositories/user_repository.py
class UserRepository:
    async def get_by_id(self, user_id: int) -> User:
        # Получение пользователя из БД