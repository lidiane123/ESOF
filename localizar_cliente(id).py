def atualizar(self, id):
try:
c = self.localizar_cliente(id)
if c:
# solicitando os dados ao usuário
# se for no python2.x digite entre aspas simples
self.novo_fone = input('Fone: ')
self.db.cursor.execute("""
UPDATE clientes
SET fone = ?
WHERE id = ?
""", (self.novo_fone, id,))
# gravando no bd
self.db.commit_db()
print("Dados atualizados com sucesso.")
else:
print('Não existe cliente com o id informado.')
except e:
raise e
