import sqlite3

# Questão 1

# conexao = sqlite3.connect('Aulas-Básico/escola_v2.db') # Conectando no banco de dados
# cursor = conexao.cursor() # Usando o banco no python

# cursor.execute("SELECT * FROM Aluno")
# query_result = cursor.fetchall()
# print(query_result)
# conexao.close()

# Questão 2

# conexao = sqlite3.connect('Aulas-Básico/escola_v2.db')
# cursor = conexao.cursor()

# cursor.execute ("""
#                 SELECT nome, (nota1 + nota2)/2.0 AS media
#                 FROM Aluno
#                 ORDER BY media DESC
#                 LIMIT 10
#                 """)
# melhores_alunos = cursor.fetchall()
# print("Top 10 alunos por média: ")
# for aluno in melhores_alunos:
#     print(f"Aluno: {aluno[0]}, Média: {aluno[1]: .2f}")

# conexao.close()

# Questão 3

# conexao = sqlite3.connect('Aulas-Básico/escola_v2.db')
# cursor = conexao.cursor()

# cursor.execute("""
#     SELECT *
#     FROM Aluno
#     LEFT JOIN Turma
#     ON Aluno.id_turma = Turma.id
# """)
# dados = cursor.fetchall()
# print("Dados combinados (Aluno + Turma):")
# for linha in dados:
#     print(linha)

# conexao.close()

# Questão 4

conexao = sqlite3.connect('Aulas-Básico/escola_v2.db')
cursor = conexao.cursor()

cursor.execute("""
    SELECT *
    FROM Aluno
    LEFT JOIN Turma
    ON Aluno.id_turma = Turma.id
    WHERE Turma.id = 2
""")
dados = cursor.fetchall()
print("Alunos da turma 2:")
for linha in dados:
    print(linha)

conexao.close()
