# 1

livros = ["Harry Potter e a Pedra Filosofal", "Sophia", "Vidas Secas"]
# print(livros)

# # 2
# print(livros[0],livros[2])

# #3
# livros.append("Dom Casmurro")
# livros.append("Memórias Póstumas de Brás Cubas")
# print(livros)

#4
# livros.insert(1,"Duna")
# print(livros)

# #5

# if livros==("Silêncio dos inocentes"):
#     livros.remove("Silêncio dos inocentes")
# else:
#     print("Livro não encontrado")

# #6

# numeros =[1,2,3,2,4,2,5]
# print(numeros.count(2))

# #7
# livros = ["Harry Potter e a Pedra Filosofal", "Sophia", "Vidas Secas"]
# for i in livros:
#     print(f"O livro {i} é interessante.")

#8
# idades =[12,18,25,14,30]
# for valor in idades:
#     if valor>=18:
#         print(valor)

#9
# valores = [10, 20, 30, 40]
# y=0
# for x in valores:
#     y+=x
#     print(y)
    


#10
# notas = []
# aluno_1 = []
# soma_a1 = 0
# i= 0
# while i <3:
#     nota_1 = int(input(f"Escreva a {i+1}° nota: "))
#     aluno_1.append(nota_1)
#     i+=1
#     soma_a1+=nota_1
# notas.append(aluno_1)

# aluno_2 = []
# soma_a2 = 0
# x=0
# while x<3:
#     nota_2 = int(input(f"Escreva a {x+1}° nota: "))
#     aluno_2.append(nota_2)
#     x+=1
#     soma_a2+=nota_2
# notas.append(aluno_2)
# print(notas)
# print(f"A média do primeiro aluno é {soma_a1/3 :.2f}.")
# print(f"A média do segundo aluno é {soma_a2/3 :.2f}.")

#11

tabuleiro = [["[]" for _ in range(8)] for _ in range(8)]
elementos_1 = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
elementos_2 = ["pea", "pea", "pea", "pea", "pea", "pea", "pea", "pea"]

tabuleiro[0] = elementos_1
tabuleiro[1] = elementos_2
tabuleiro[6] = elementos_2
tabuleiro[7] = elementos_1

for linha in tabuleiro:
    print(linha)
