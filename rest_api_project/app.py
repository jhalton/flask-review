from flask import Flask

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
