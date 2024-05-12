import json
import os

from App.Models.models import Transaction
from App.Config.connection import Connection 

class Transactions_controller():
    def __init__(self) -> None:
        self.path_cache : str = "App/Cache/cache_transactions.json"
    

    def create_cache(self, transaction: [Transaction]):
        with open(self.path_cache, 'w') as f:
            json.dump(transaction, f, ensure_ascii=False)
    

    def get_history(self) -> [Transaction]:
        if os.path.isfile(self.path_cache): return json.load(open(self.path_cache))
        else:
            try:
                connection = Connection(collection_name='transactions')
                collection = connection.collection_store()
                transactions = []
                all_transactions = collection.find({ })
                for doc in all_transactions:
                    transactions.append({
                        '_id' : str(doc['_id']),
                        'client_id' : str(doc['client_id']),
                        'client_name' : str(doc['client_name']),
                        'total_to_pay' : float(doc['total_to_pay']),
                        'credit_card' : {
                            'card_number' : str(doc['credit_card']['card_number']),
                            'value' : str(doc['credit_card']['value']),
                            'cvv' : str(doc['credit_card']['cvv']),
                            'card_holder_name' : str(doc['credit_card']['card_holder_name']),
                            'exp_date' : str(doc['credit_card']['exp_date']),
                        } 
                     
                    })
                self.create_cache(transaction=transactions)
                return transactions
            
            except Exception as e:
                print(e)
                return {
                    "Error":"404"
                }


    def register_transaction(self, transaction:Transaction) -> Transaction:
        if os.path.isfile(self.path_cache):
            os.remove(self.path_cache)
        try:
            connection = Connection(collection_name='transactions')
            collection = connection.collection_store()
            collection.insert_one({
                'client_id' : transaction.client_id,
                'client_name' : transaction.client_name,
                'total_to_pay' : transaction.total_to_pay,
                'credit_card' : {
                    'card_number' : transaction.credit_card.card_number,
                    'value' : transaction.credit_card.value,
                    'cvv' : transaction.credit_card.cvv,
                    'card_holder_name' : transaction.credit_card.card_holder_name,
                    'exp_date' : transaction.credit_card.exp_date,
                    }
            })
            return True
        
        except Exception as e:
            print(e)
            return False


    def get_transaction_by_client(self, client_name:str) -> [Transaction]:
        try:
            connection = Connection(collection_name='transactions')
            collection = connection.collection_store()
            transactions = []
            all_transactions_by_client = collection.find({'client_name':str(client_name) })
            for doc in all_transactions_by_client:
                transactions.append({
                    # Transaction(**all_transactions_by_client[doc])
                    '_id' : str(doc['_id']),
                    'client_id' : str(doc['client_id']),
                    'client_name' : str(doc['client_name']),
                    'total_to_pay' : float(doc['total_to_pay']),
                    'credit_card' : {
                        'card_number' : str(doc['credit_card']['card_number']),
                        'value' : str(doc['credit_card']['value']),
                        'cvv' : str(doc['credit_card']['cvv']),
                        'card_holder_name' : str(doc['credit_card']['card_holder_name']),
                        'exp_date' : str(doc['credit_card']['exp_date']),
                    }
                })
            return transactions[0]
        
        except Exception as e:
            print(e)
            return {
                "Error":f"Client not found {e}"
            }