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
