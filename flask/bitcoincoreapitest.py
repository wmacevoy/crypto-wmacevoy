from bitcoincoreapi import BitcoinCoreAPI

def testListwallets():
    # assumes bitcoin core daemon is running
    api = BitcoinCoreAPI()
    result = api.listwallets()
    expect = {'error': None, 'id': 0, 'result': ['testnet-abc123xyz']}
    assert result  == expect
