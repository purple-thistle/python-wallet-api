from flask import Flask
from flask_restful import Resource, Api
from wallet import wallet;

app = Flask(__name__)
api = Api(app)

mywallet = wallet.Wallet()

class Wallet(Resource):
    def get(self, amount):
        mywallet.spend_cash(amount)
        return {"balance": mywallet.get_balance()}
    def put(self, amount):
        mywallet.add_cash(amount)
        return {"balance": mywallet.get_balance()}
class Balance(Resource):
    def get(self):
        return {"balance": mywallet.get_balance()}

api.add_resource(Balance, '/balance')
api.add_resource(Wallet, '/wallet/<int:amount>')


if __name__ == '__main__':
    app.run(debug=True)
