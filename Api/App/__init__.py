from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from App.Routes import products, transactions
app = FastAPI()

origins = [
    "http://localhost:3000", 
    "http://44.219.245.85:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.app_router, prefix='/products')
app.include_router(transactions.app_router, prefix='/transactions')