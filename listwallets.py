#!/usr/bin/env python

# pip install requests

import requests
import json
import configparser
import pathlib
from pathlib import Path

def getConfig(file=None):
    if (file == None):
        file = str(pathlib.Path.home() / ".bitcoin" / "bitcoin.conf")

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

testnet=int(config.get('testnet',0))
user=str(config.get('rpcuser',''))
password=str(config.get('rpcpassword',''))
port=int(config.get('port',8332 if not testnet else 18332))

url = f"http://localhost:{port}/"

payload = {
    "version" : "1.1",
    "method": "listwallets",
    "params": [],
    "id": 0,
}

response = requests.post(url, json=payload, auth=(user,password)).json()
print(response)
