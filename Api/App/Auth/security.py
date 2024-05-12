from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from App.Models.models import UserInDB
from App.Utils.database import Database

class Authentication():
    
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def get_user(self, db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def verify_password(plain_password:str, hashed_password:str) -> str:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(plain_password, hashed_password)


    def get_password_hash(password:str) -> str:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)


    def get_authenticated_user_from_session(request:Request):
        session_id = request.cookies.get("session_id")
        user = request.cookies.get("username")
        if session_id == None or user not in Database.fake_users_db or Database.fake_users_db[user]["id"] != session_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid session id provided"
            )
        return Database.fake_users_db[user]
