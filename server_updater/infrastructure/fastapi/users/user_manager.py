from typing import Dict


class UserManager:
    def __init__(self):
        self.fake_users_db: Dict[str, dict] = {
            "testuser": {
                "username": "testuser",
                "password": "$2b$12$4dQ7xHCP.8uhgYg8kz/LieGivAKq63hiy1K/pI6dD6M5I0hbfqNJ0G",
            }
        }

    def get_user(self, username: str) -> dict:
        return self.fake_users_db.get(username)
