# https://flask.palletsprojects.com/en/2.2.x/installation/

```bash
sudo apt install python3.10-venv
mkdir flask
cd flask
python3 -m venv venv
. venv/bin/activate
pip install flask
pip install requests
pip install pytest
pip install coinbase
```

Create hello.py

```bash
. venv/bin/activate
flask --app hello run
```

Try localhost:5000 and see "Hello World"

Test api
```bash
. venv/bin/activate
pytest *test.py
```

Basic coin server
```bash
. venv/bin/activate
flask --app coin run
```

Access to coinbase API:

- Create a Lastpass account
- `sudo apt-get install lastpass-cli`


- Create a coinbase pro API passphrase/key/secret, store it in a lastpass secure note called `api.pro.coinbase.com` like
```
passphrase=....
key=....
secret=....
```
and a note called `testapi.pro.coinbase.com` like
```
passphrase=examplepassphrase
key=examplekey
secret=examplesecret
```

You should be able to run `pytest -s lastpassconfigtest.py coinbaseproapitest.py` and pass all tests.


