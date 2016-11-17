def inserir_com_parametros(self):
# solicitando os dados ao usuário
self.nome = input('Nome: ')
self.idade = input('Idade: ')
self.cpf = input('CPF: ')
self.email = input('Email: ')
self.fone = input('Fone: ')
self.cidade = input('Cidade: ')
self.uf = input('UF: ') or 'SP'
date = datetime.datetime.now().isoformat(" ")
self.criado_em = input('Criado em (%s): ' % date) or date
try:
self.db.cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", (self.nome, self.idade, self.cpf, self.email, self.fone,
self.cidade, self.uf, self.criado_em))
# gravando no bd
self.db.commit_db()
print("Dados inseridos com sucesso.")
except sqlite3.IntegrityError:
print("Aviso: O email deve ser único.")
return False
