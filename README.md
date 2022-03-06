## references

```
https://www.youtube.com/watch?v=dam0GPOAvVI

Note: he is using vscode in a windows environment; I am using Linux and vim.
```

## environment
```
   52  apt install python3.8-venv
   53  python3 -m venv venv
   55  source venv/bin/activate
```

## pips

```
   69  pip install flask
   70  pip install flask-login
   71  pip install flask-sqlalchemy
```

## running
```
python3 main.py
```

## testing
```
   39  curl -X GET http://127.0.0.1:5000/
   43  curl -X GET http://127.0.0.1:5000/login
   44  curl -X GET http://127.0.0.1:5000/logout
   46  curl -X GET http://127.0.0.1:5000/sign-up
```

## directory (this checkin)

```
(venv) steve@minty:~/projects/webserver$ tree -I 'venv|__pycache__'
.
├── main.py
├── README.md
└── website
    ├── auth.py
    ├── __init__.py
    ├── models.py
    ├── static
    ├── templates
    └── views.py

3 directories, 6 files
```


