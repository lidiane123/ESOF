# 05_create_data_param.py
import sqlite3
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()
# solicitando os dados ao usuário
p_nome = input('Nome: ')
p_idade = input('Idade: ')
p_cpf = input('CPF: ')
p_email = input('Email: ')
p_fone = input('Fone: ')
p_cidade = input('Cidade: ')
p_uf = input('UF: ')
p_criado_em = input('Criado em (yyyy-mm-dd): ')
