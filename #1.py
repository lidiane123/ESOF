# connect_db.py
# 01_create_db.py
import sqlite3
conn = sqlite3.connect('clientes.db')
conn.close()
> python3 01_create_db.py
> dir *.db
