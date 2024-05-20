<h1 align="center" 
    style="font-weight: bold;"
    >
    Rest with cache 💻
</h1>
<div align="center" >
    <img align="center" alt="Python" height="45" width="70" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-plain.svg">
    <img align="center" alt="Mongo" height="20" width="70" src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white">
    <img align="center" alt="FastAPI" height="80" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original-wordmark.svg">
    <img align="center" alt="docker" height="60" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg">
</div>

<p align="center">
    • <a href="#started">Getting Started</a> 
    • <a href="#routes">API Endpoints</a> 
</p>

<p align="center">
    <b>
        This API is a simple store, that you can registrate transactions and products on the database, and use cache to consults. The API don't consult database without necessity.
    </b>
</p>

<h2 id="started" align="center" >
    🚀 Getting started
</h2>

To run this project localy you will need to install `docker` and `docker compose`. After install thats components just follow this steps.

<h3> 
    Prerequisites 
</h3>

Here are all prerequisites necessary to runner the project.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


<h3>
    Starting
</h3>


- To run the app, run the command.
````bash
docker-compose up 
````
- After up the app, access with that endpoint to test functionalitys and documentation

````
http://localhost:8000/docs
````

<h2 id="routes">
    📍 API Authentication
</h2>

To access the functions is required the userId and username to realize requests, those informations are required to pass for the cookies of the browser.

Was created a fake database to simulate the users, you can use this information to send requests.

````
session_id=22222
username=alice
````


<h2 id="routes">
    📍 API Endpoints
</h2>

Here you can list the main routes of your API, and what are their expected request.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /auth/</kbd>     | Authenticate user into the API, see [request details](#post-auth-detail)
| <kbd>GET /products/starstore/products/</kbd>     | Return all the products on database, see [request details](#get-starstore-products-detail)
| <kbd>POST /products/starstore/products/</kbd>     | Register products, see [request details](#post-starstore-products-detail)
| <kbd>POST /transactions/starstore/history/</kbd>     | Return all the transactions on database, see [request details](#post-transactions-starstore-history-detail)
| <kbd>POST /transactions/starstore/buy</kbd>     | Register transaction, see [request details](#post-transactions-starstore-buy-detail)

<h3 id="post-auth-detail">
    POST /auth
</h3>

**REQUEST**
```json
{
  "username": "string",
  "password": "string"
}
```
**RESPONSE**
```json
{
  "id": "string"
}
```

<h3 id="get-starstore-products-detail">
    GET /products/starstore/products/
</h3>

**RESPONSE**
```json
[
    {
        "title": "string",
        "price": 0.0,
        "zipcode": "string",
        "seller": "string",
        "thumbnailHd": "string",
        "date": "string"
    }
]
```
<h3 id="post-starstore-products-detail">
    POST /products/starstore/products/
</h3>

**REQUEST**
```json
{
    "title": "string",
    "price": 0.0,
    "zipcode": "string",
    "seller": "string",
    "thumbnailHd": "string",
    "date": "string"
  }
```
**RESPONSE**
```json
{
    "title": "string",
    "price": 0.0,
    "zipcode": "string",
    "seller": "string",
    "thumbnailHd": "string",
    "date": "string"
  }
```
<h3 id="get-transactions-starstore-history-detail">
    GET /transactions/starstore/history/
</h3>

**RESPONSE**
```json
[
  {
    "_id": "string",
    "client_id": "string",
    "client_name": "string",
    "total_to_pay": 0.0,
    "credit_card": {
      "card_number": "string",
      "value": "string",
      "cvv": "string",
      "card_holder_name": "string",
      "exp_date": "string"
    }
  }
]
```
<h3 id="post-transactions-starstore-buy-detail">
    POST /transactions/starstore/buy/
</h3>

**REQUEST**
```json
{
    "_id": "string",
    "client_id": "string",
    "client_name": "string",
    "total_to_pay": 0.0,
    "credit_card": {
        "card_number": "string",
        "value": "string",
        "cvv": "string",
        "card_holder_name": "string",
        "exp_date": "string"
        }
}
```
**RESPONSE**
```json
{
  "client_id": "string",
  "client_name": "string",
  "total_to_pay": 0,
  "credit_card": {
    "card_number": "string",
    "value": 0,
    "cvv": 0,
    "card_holder_name": "string",
    "exp_date": "string"
  }
}
```
