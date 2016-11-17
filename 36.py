def gen_cidade(self):
''' conta quantas cidades estão cadastradas e escolhe uma delas pelo id. '''
sql = 'SELECT COUNT(*) FROM cidades'
q = self.db.cursor.execute(sql)
return q.fetchone()[0]
