from datetime import timedelta, datetime

import jwt

from server_updater.infrastructure.fastapi.users.user_manager import UserManager


class AuthManager:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager

    def verify_user(self, username: str, password: str) -> bool:
        user = self.user_manager.get_user(username)
        if user is None:
            return False
        return pwd_context.verify(password, user["password"])

    def create_access_token(
        self, username: str, expires_delta: timedelta = None
    ) -> str:
        to_encode = {"sub": username}
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
