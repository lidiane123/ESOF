def close_db(self):
if self.conn:
self.conn.close()
print("Conexão fechada.")
