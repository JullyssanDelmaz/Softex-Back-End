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
livros.insert(1,"Duna")
print(livros)

#5

if livros==("Silêncio dos inocentes"):
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")

#6

numeros =[1,2,3,2,4,2,5]
print(numeros.count(2))

#7
livros = ["Harry Potter e a Pedra Filosofal", "Sophia", "Vidas Secas"]
for i in livros:
    print(f"O livro {i} é interessante.")

#8
idades =[12,18,25,14,30]
for valor in idades:
    if valor>18:
        print(idades)
    
    
