import os
from fastapi import APIRouter

from App.Controllers.product_controller import Product_controller
from App.Models.models import Product

product_controller = Product_controller()
app_router = APIRouter()
    
@app_router.get('/')
def index():
    return {
            'On': 'Fire'
            }

@app_router.get('/starstore/products')
def get_all_products():

    products = product_controller.get_all_products()
    return products

@app_router.post('/starstore/products')
def store_product(data:Product) -> Product:
    if product_controller.register_product(data):
        return {
                "_Id":"id",
                "title":data.title,
                "price":data.price,
                "zipcode":data.zipcode,
                "seller":data.seller,
                "thumbnailHd":data.thumbnailHd,
                "date":data.date
                }
    return {
        "Error":"404"
    }
