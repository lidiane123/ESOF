def inserir_randomico(self, repeat=10):
''' Inserir registros com valores randomicos names '''
lista = []
for _ in range(repeat):
date = datetime.datetime.now().isoformat(" ")
fname = names.get_first_name()
lname = names.get_last_name()
name = fname + ' ' + lname
email = fname[0].lower() + '.' + lname.lower() + '@email.com'
c = gen_city()
city = c[0]
uf = c[1]
lista.append((name, gen_age(), gen_cpf(),
email, gen_phone(),
city, uf, date))
try:
self.db.cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", lista)
self.db.commit_db()
print("Inserindo %s registros na tabela..." % repeat)
print("Registros criados com sucesso.")
except sqlite3.IntegrityError:
print("Aviso: O email deve ser único.")
return False
