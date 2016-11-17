# manager_db.py
import os
import sqlite3
import io
import datetime
import names
import csv
from gen_random_values import *
class Connect(object):
def __init__(self, db_name):
try:
# conectando...
self.conn = sqlite3.connect(db_name)
self.cursor = self.conn.cursor()
print("Banco:", db_name)
self.cursor.execute('SELECT SQLITE_VERSION()')
self.data = self.cursor.fetchone()
print("SQLite version: %s" % self.data)
except sqlite3.Error:
print("Erro ao abrir banco.")
return False
def commit_db(self):
if self.conn:
self.conn.commit()
def close_db(self):
if self.conn:
self.conn.close()
print("Conexão fechada.")
class ClientesDb(object):
tb_name = 'clientes'
def __init__(self):
self.db = Connect('clientes.db')
self.tb_name
def fechar_conexao(self):
self.db.close_db()
if __name__ == '__main__':
c = ClientesDb()

