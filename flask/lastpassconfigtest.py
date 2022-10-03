import os
from lastpassconfig import LastpassConfig

def testValues():
    lpc = LastpassConfig()
    lpc.lastpassUser="wmacevoy@gmail.com"
    lpc.lastpassNote = "testapi.pro.coinbase.com"
    assert lpc.config['key'] == f"examplekey"
    assert lpc.config['secret'] == f"examplesecret"
    assert lpc.config['passphrase'] == f"examplepassphrase"
