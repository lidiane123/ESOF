> python3
Python 3.4.0 (default, Apr 11 2014, 13:05:18)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>from connect_db import Connect
>>> dir(Connect)
>>> db = Connect('clientes.db')
>>> dir(db)
>>> db.close_db()
>>> exit()
