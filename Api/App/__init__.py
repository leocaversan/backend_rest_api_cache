from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from App.Routes import products, transactions, login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    products.app_router, 
    prefix='/products', 
    responses={404: {"Description" : "Not Found"}}
    )
app.include_router(
    transactions.app_router, 
    prefix='/transactions',
    responses={404: {"Description" : "Not Found"}}
    )
app.include_router(
    login.app_router, 
    prefix='/auth',
    responses={404: {"Description" : "Not Found"}}
    )