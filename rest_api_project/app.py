from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Jeanette's Flowers",
        "items": [
            {
                "name": "Sunflower",
                "price": 8.99
            },
            {
                "name": "Rose",
                "price": 12.99
            },
            {
                "name": "Daisy",
                "price": 5.99
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json() 
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201
