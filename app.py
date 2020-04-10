from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
# from flask_jwt import JWT, jwt_required, JWTError


from endpoints.user import User, UserList, UserRegister, ShippingRegister, BillingRegister, ShippingAddress, BillingAddress
from endpoints.inventory import Inventory, InventoryProductList, Shopping
from endpoints.purchase_history import PurchaseHistory
from endpoints.scan_history import ScanHistory, ScanHistoryRegister
from endpoints.cart import Cart
# from db.database import create_database


# Create the application instance
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return "Pineapples's Flask API"

api.add_resource(User, '/users/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UserRegister, '/user/register')
api.add_resource(Inventory, '/product/<string:productId>')
api.add_resource(InventoryProductList, '/products')
api.add_resource(PurchaseHistory, '/history/<string:name>')
api.add_resource(ScanHistory, '/history/scan/<string:user_id>')
api.add_resource(ScanHistoryRegister, '/history/scan')
api.add_resource(Shopping, '/shopping')
api.add_resource(ShippingAddress, '/users/<string:user_id>/shippingaddress')
api.add_resource(BillingAddress, '/users/<string:user_id>/billingaddress')
api.add_resource(ShippingRegister, '/users/<string:user_id>/shippingregister')
api.add_resource(BillingRegister, '/users/<string:user_id>/billingregister')
api.add_resource(Cart, '/cart/<string:userid>')



if __name__ == '__main__':
    app.run(debug=True)