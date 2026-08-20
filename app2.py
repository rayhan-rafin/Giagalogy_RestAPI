from flask import Flask
from flask_smorest import Api, Blueprint
from marshmallow import Schema, fields
from flask.views import MethodView

app = Flask(__name__)
app.config["API_TITLE"] = "Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)

stores = [
    {
        "name": "store1",
        "items": [
            {"name": "str1_item1", "price": 120}
        ]
    }
]

class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)

class StoreSchema(Schema):
    name = fields.Str(required=True)
    items = fields.List(fields.Nested(ItemSchema))

blp = Blueprint("store", "store", url_prefix="/store", description="Store operations")

@blp.route("/")
class StoreList(MethodView):   # <-- inherit MethodView
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores

api.register_blueprint(blp)
