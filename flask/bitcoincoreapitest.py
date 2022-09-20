from bitcoincoreapi import BitcoinCoreAPI

# assumes bitcoin core daemon is running

def testPing():
    api = BitcoinCoreAPI()
    result = api.ping()
    expect = {'error': None, 'id': 0, 'result': None}
    assert result  == expect

def testListwallets():
    api = BitcoinCoreAPI()
    result = api.listwallets()
    expect = {'error': None, 'id': 0, 'result': ['testnet-abc123xyz']}
    assert result  == expect

def testGetnewaddress():
    api = BitcoinCoreAPI()
    result = api.getnewaddress()
    assert result['error'] == None
    assert len(result['result']) > 40
