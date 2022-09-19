import os
from bitcoincoreconfig import BitcoinCoreConfig

def testDefFile():
    bc = BitcoinCoreConfig()
    assert bc.file == f"{os.getenv('HOME')}/.bitcoin/bitcoin.conf"

def testFile():
    bc = BitcoinCoreConfig()
    bc.file = "myconfig"
    assert bc.file == f"myconfig"

def testValues():
    bc = BitcoinCoreConfig()
    bc.file = "test.conf"
    assert bc.rpcuser == f"testuser"
    assert bc.rpcpassword == f"testpassword"
    assert bc.testnet == 1
    assert bc.url == f"http://localhost:18332/"
