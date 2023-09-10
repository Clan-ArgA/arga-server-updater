from typing import Dict

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import FastAPI
# from fastapi.security import OAuth2PasswordBearer
# from passlib.context import CryptContext
#
# from server_updater.infrastructure.fastapi.auth.auth_manager import AuthManager
# from server_updater.infrastructure.fastapi.users.user_manager import UserManager

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# user_manager = UserManager()
# auth_manager = AuthManager(user_manager)
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @app.post("/token", response_model=dict)
# async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Dict:
#     username = form_data.username
#     password = form_data.password
#     if not auth_manager.verify_user(username, password):
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     access_token = auth_manager.create_access_token(username)
#     return {"access_token": access_token, "token_type": "bearer"}


@app.get("/", response_model=str)
def get_home():
    return "Clan Arga server updater"


@app.get("/status", response_model=dict)
def get_status():
    return {"status": "alive"}
