from typing import Union
from pydantic import BaseModel

class Product(BaseModel):
    id:str = None
    title: str = None
    price: float = None
    zipcode: str = None
    seller: str = None
    thumbnailHd: str = None
    date: str = None


class Card(BaseModel):
    card_number: str = None
    value: int = None
    cvv: int = None
    card_holder_name: str = None 
    exp_date: str = None


class Transaction(BaseModel):
    _id:str = None
    client_id: str = None
    client_name: str = None
    total_to_pay: int = None
    credit_card: Card


class Name_client(BaseModel):
    name:str = None


class User(BaseModel):
    id: str
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class credentials(BaseModel):
    username: str
    password: str

