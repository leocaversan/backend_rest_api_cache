import os
from fastapi import APIRouter

from App.Controllers.transactions_controller import Transactions_controller
from App.Models.models import Transaction, Name_client
from App.Controllers.connection import Connection 

transaction_controller = Transactions_controller()
app_router = APIRouter()
    
@app_router.get('/')
def index():
    return {
            'On': 'Fire'
            }

@app_router.get('/starstore/history')
def get_all_transactions():

    transactions = transaction_controller.get_history()
    return transactions

@app_router.post('/starstore/history')
def get_transaction_client(data: Name_client):

    transactions_by_client = transaction_controller.get_transaction_by_client(data.name)
    return transactions_by_client
   

@app_router.post('/starstore/buy')
def buy_product(transaction:Transaction) -> Transaction:

    if transaction_controller.register_transaction(transaction):
        return {
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
                }
    return {
        "Error":"404"
    }
