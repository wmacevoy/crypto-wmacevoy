#!/usr/bin/env python

# pip install requests

import requests
import json
import configparser
import pathlib
from pathlib import Path
from coinbase.wallet.client import Client

def getConfig(file=None):
    if (file == None):
        file = str(pathlib.Path.home() / "projects" / "crypto-wmacevoy-private" / "coinbase.conf")

    fd = open(file,"r")
    data = fd.read()
    fd.close()

    config=configparser.ConfigParser()
    config.read_string(f"""
    [default]
    {data}
    """)

    return config['default']

config=getConfig()

coinbasesecret=str(config.get('coinbasesecret',''))
coinbasekey=str(config.get('coinbasekey',''))

assert(len(coinbasesecret)!=0)
assert(len(coinbasekey)!=0)

client = Client(api_key=coinbasekey, api_secret=coinbasesecret)
user = client.get_current_user()
print(user)
