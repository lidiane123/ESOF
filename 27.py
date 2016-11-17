def inserir_um_registro(self):
try:
self.db.cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, VALUES ('Regis da Silva', 35, '12345678901', 'regis@email.com', '(11) 9876-5342',
'São Paulo', 'SP', '2014-07-30 11:23:00.199000')
""")
# gravando no bd
self.db.commit_db()
print("Um registro inserido com sucesso.")
except sqlite3.IntegrityError:
print("Aviso: O email deve ser único.")
return False
...
if __name__ == '__main__':
c = ClientesDb()
c.criar_schema()
c.inserir_um_registro()
