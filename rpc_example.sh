#!/usr/bin/bash

curl -v \
  --user-agent "AuthServiceProxy/0.1" \
  --data-binary '{"version": "1.1", "method": "gettransaction", "params": ["1e519e12a210c9ef458553d05850ffd6441ed354303d623aa0dbcb5c8e29ee8d"], "id": 1}' \
  -H 'context-type: application/json;' \
  -H "Authorization: Basic cnBjdXNlcjplZDJkZWI3MzgxNzUzYWU5NzA4ZWNmNmY5NWM1YmU3NTRjN2M5YjNlODY3ZDVlZDExOTQ3NmM2ZWVjNGY2NTFl" \
  http://127.0.0.1:18332/