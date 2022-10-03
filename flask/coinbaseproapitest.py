from coinbaseproapi import CoinbaseProConfig,CoinbaseProAPI

def testConfig():
    config = CoinbaseProConfig()
    config.lastpassUser="wmacevoy@gmail.com"
    config.lastpassNote = "testapi.pro.coinbase.com"
    assert config.key == f"examplekey"
    assert config.secret == f"examplesecret"
    assert config.passphrase == f"examplepassphrase"

def testGetProducts():
    api = CoinbaseProAPI()
    result = api.get_products()
    ok = False
    for prod in result:
        if prod['id']=='BTC-USD':
            ok = True
    assert ok

def testGetFees():
    api = CoinbaseProAPI()
    result = api.get_fees()
    assert float(result['maker_fee_rate']) > 0.0
    assert float(result['taker_fee_rate']) > 0.0
    

def testGetCurrentUser():
    api = CoinbaseProAPI()
    result = api.get_current_user()
    print(result)
    
