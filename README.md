# simple user authenticated flask web site.


## references

This is my interpretation of :

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
    │   └── index.js
    ├── templates
    │   ├── base.html
    │   ├── home.html
    │   ├── login.html
    │   ├── logout.html
    │   └── sign_up.html
    └── views.py

3 directories, 12 files

```

## looking at the database

```
(venv) steve@minty:~/projects/webserver/website$ sqlite3 database.db
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> .tables
note  user
sqlite> select * from note;
1|Note 1|2022-03-06 22:18:51|1
3|Note 3|2022-03-06 22:19:03|1
sqlite> select * from user;
1|steve1281@hotmail.com|sha256$dQdevwDJtW6eJ9zZ$659027747e1d8425aea3b2b71090dea0c0418c1e559f3f8062449ed2177ea7ab|Steve
sqlite> .quit
```


## curl hax

* assuming an email of steve1281@hotmail.com and a password of 1234

Login with:

```
steve@minty:~/Desktop$ curl "http://localhost:5000/login" -H "Content-Type: application/x-www-form-urlencoded" -d "email=steve1281%40hotmail.com&password=1234" -X POST -c cookies.txt
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/">/</a>. If not click the link.
```

* then you can access via the cookie you created:

```
steve@minty:~/Desktop$ curl "http://localhost:5000/" -b cookies.txt 
<!DOCTYPE html>
<html>
...
				
				<div class="alert alert-success alter-dismissable fade show" role="alert">
					Logged in successfully
					<button type="button" class="close" data-dismiss="alert">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				
...			
			
<h1 align="center">
	Notes
</h1>
<ul class="list-group list-group-flush id="notes">
	   
	   <li class="list-group-item">Note 1
		   <button type="button" class="close" onClick="deleteNote(1)">
			<span aria-hidden="true">&times;</span>
		   </button>
	   </li>
	   
	   <li class="list-group-item">Note 3
		   <button type="button" class="close" onClick="deleteNote(3)">
			<span aria-hidden="true">&times;</span>
		   </button>
	   </li>
	   
</ul>
...
```

