#!/usr/bin/env python

from bitcoin.rpc import RawProxy

url=None
port=18332 # testnet, use None for main net client
conf="/home/user/.bitcoin/bitcoin.conf"

proxy = RawProxy(url,port,conf)

txid="1e519e12a210c9ef458553d05850ffd6441ed354303d623aa0dbcb5c8e29ee8d"
info = proxy.gettransaction(txid)
print(info)
