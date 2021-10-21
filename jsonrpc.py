#!/usr/bin/env python

# pip install requests


# Curl ex:
# 
# curl -v --user-agent "AuthServiceProxy/0.1" --data-binary '{"version": "1.1", "method": "gettransaction", "params": ["1e519e12a210c9ef458553d05850ffd6441ed354303d623aa0dbcb5c8e29ee8d"], "id": 1}' -H 'context-type: application/json;' -H "Authorization: Basic cnBjdXNlcjplZDJkZWI3MzgxNzUzYWU5NzA4ZWNmNmY5NWM1YmU3NTRjN2M5YjNlODY3ZDVlZDExOTQ3NmM2ZWVjNGY2NTFl" http://127.0.0.1:18332/


import requests
import json
import configparser

def config(file):
    fd = open(file,"r")
    data = fd.read()
    fd.close()

    sectionData=f"""
    [section]
    {data}
    """

    configparser.ConfigParser()

user="rpcuser"
password="edbb2deb7381753ae9708ecf6f95c5be754c7c9b3e867d5ed119476c6eec4f651e"
port=18332
url = f"http://localhost:{port}/"

payload = {
    "version" : "1.1",
    "method": "gettransaction",
    "params": ["1e519e12a210c9ef458553d05850ffd6441ed354303d623aa0dbcb5c8e29ee8d"],
    "id": 0,
}
session = requests.Session()
session.auth = (user, password)

response = session.post(url, json=payload)
print(response)
