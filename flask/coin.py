from flask import Flask

from bitcoincoreapi import BitcoinCoreAPI

app = Flask(__name__)
core = BitcoinCoreAPI()

@app.route("/listwallets")
def listwallets():
    return core.listwallets()

    
