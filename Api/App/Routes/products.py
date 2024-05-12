from fastapi import APIRouter, Depends, HTTPException

from App.Controllers.product_controller import Product_controller
from App.Models.models import Product
from App.Auth.security import Authentication

product_controller = Product_controller()

app_router = APIRouter()

@app_router.get('/')
async def index():
    return {
            'On': 'Fire'
            }


@app_router.get('/starstore/products')
async def get_all_products(
    user: dict =  Depends(Authentication.get_authenticated_user_from_session)
    ):
    return product_controller.get_all_products()


@app_router.post('/starstore/products')
async def store_product(
    data:Product, 
    user: dict =  Depends(Authentication.get_authenticated_user_from_session)
    ) -> Product:
    if product_controller.register_product(data):
        return {
                "_Id":data.id,
                "title":data.title,
                "price":data.price,
                "zipcode":data.zipcode,
                "seller":data.seller,
                "thumbnailHd":data.thumbnailHd,
                "date":data.date
                }
    raise HTTPException(
                status_code=404,
                detail="Error to complete registration"
            )
