import sqlite3

conexao = sqlite3.connect('escola_v2.db') # Conectando no banco de dados
cursor = conexao.cursor() # Usando o banco no python

cursor.execute("SELECT * FROM Aluno")
query_result = cursor.fetchall()
print(query_result)
conexao.close()