from fastapi import APIRouter, HTTPException

from App.Auth.security import Authentication
from App.Models.models import credentials
from App.Utils.database import Database

app_router = APIRouter()

@app_router.post('/')
async def authentication(
    credentials:credentials
): 
    
    if credentials.username not in Database.fake_users_db or Authentication.verify_password(Authentication.get_password_hash(credentials.password), Database.fake_users_db[credentials.username]["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {
        "id": Database.fake_users_db[credentials.username]["id"]
        } 