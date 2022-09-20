from flask import Flask

from bitcoincoreapi import BitcoinCoreAPI

app = Flask(__name__)
core = BitcoinCoreAPI()

@app.route("/ping")
def ping():
    return core.ping()

@app.route("/listwallets")
def listwallets():
    return core.listwallets()

@app.route("/getnewaddress", defaults={'label': '', 'address_type' : 'bech32'})
@app.route("/getnewaddress/<label>", defaults={'address_type' : 'bech32'})
@app.route("/getnewaddress/<label>/<address_type>")
def getnewaddress(label='',address_type='bech32'):
    return core.getnewaddress(label,address_type)
