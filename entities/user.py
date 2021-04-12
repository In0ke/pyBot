from loader import db


class User:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.database = db

    def get_token_from_db(self):
        pass
