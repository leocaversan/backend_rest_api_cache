from pymongo import MongoClient

class Connection():
    
    def __init__(self, collection_name:str ):
        
        self.host_mongodb = 'mongodb://localhost:27017/'
        self.store_name:str = 'store_app'
        self.collection_name:str = collection_name

    def collection_store(self):    
        print('start connection colletion')
        db = MongoClient(self.host_mongodb)[self.store_name]
        collection = db[self.collection_name]
        
        return collection
    
