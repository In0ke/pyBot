from typing import Dict

from loader import db


class User:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.database = db

    def get_api_token(self) -> Dict[str, str]:
        """
        @return: Возвращает токен для работы с API CloudVPS
        """
        token = self.database.get_user_token(self.user_id)
        return {"Authorization": f"Bearer {token}"}
