from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "store1",
        "items": [
            {
                "name": "str1_item1",
                "price": 120
            }
        ]
    }
]


# @app.route("/store", methods=['GET'])
@app.get("/store")  # shorthand for above, same for post
# only one method per endpoint, multiple will overwrite (last one remmains)
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": [
            {
                "name": "str2_item1",
                "price": 150
            }
        ]
    }
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def add_item(name):
    request_data = request.get_json()
    for target_store in stores:
        if name == target_store["name"]:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            target_store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not in database"}, 404
