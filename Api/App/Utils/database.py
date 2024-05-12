class Database():
    fake_users_db = {
        "leo": {
            "id":"11111",
            "username": "leo",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$2b$12$6IXwHM8wMy5dImdxWITR5.jcFJorBW//IVoYbWsV0vTD3kvojZv0i",
            "disabled": False,
        },
        "alice": {
            "id":"22222",
            "username": "alice",
            "full_name": "Alice Wonderson",
            "email": "alice@example.com",
            "hashed_password": "$2b$12$oX8a7nQ1QfWylC2PLnnzYuVPstlezW6a14605uS1CArHVfdPCLTcS",
            "disabled": True,
        },
    }
