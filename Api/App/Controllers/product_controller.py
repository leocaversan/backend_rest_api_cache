import json
import os

from App.Models.models import Product
from App.Controllers.connection import Connection 


class Product_controller():

    def __init__(self) -> None:
        self.path_cache : str = "App/Cache/cache_product.json"

    def create_cache(self, products: [Product]):
        with open(self.path_cache, 'w') as f:
            json.dump(products, f, ensure_ascii=False)

    def get_all_products(self):
        
        if os.path.isfile(self.path_cache): return json.load(open(self.path_cache))
        else:
            connection = Connection(collection_name='products')
            collection = connection.collection_store()
            cursor = collection.find({ }).limit(10)
            products = []
            
            for doc in cursor:
                products.append({
                    # '_id' : str(doc['_id']),
                    'title' : str(doc['title']),
                    'price' : float(doc['price']),
                    'zipcode' : str(doc['zipcode']),
                    'seller' : str(doc['seller']),
                    'thumbnailHd' : str(doc['thumbnailHd']),
                    'date' : str(doc['date'])
                })
            self.create_cache(products=products)
            return products
    
    def register_product(self, product: Product) -> bool:
    
        if os.path.isfile(self.path_cache):
            os.remove(self.path_cache)
        
        connection = Connection(collection_name='products')
        collection = connection.collection_store()
        try:
            collection.insert_one({
                    'title' : product.title,
                    'price' : product.price,
                    'zipcode' : product.zipcode,
                    'seller' : product.seller,
                    'thumbnailHd' : product.thumbnailHd,
                    'date' : product.date
            })
            return True
        except Exception as e:
            print(e)
            return False

# print(type(Product_controller.get_all_products()))