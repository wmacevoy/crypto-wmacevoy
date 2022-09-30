import os
from coinbaseconfig import CoinbaseConfig

def testValues():
    bc = CoinbaseConfig()
    bc.lastpassUser="wmacevoy@gmail.com"
    bc.lastpassNote = "exampleapi.coinbase.com"
    assert bc.coinbasekey == f"examplekey"
    assert bc.coinbasesecret == f"examplesecret"
