from functools import reduce

# Questão 1

# lista = [1, 2, 3, 4, 5]
# dobro=lambda lista:lista*2
# print(list(map(dobro,lista)))


# Questão 2

# lista = [10, 15, 20, 25, 30]
# pares=lambda num: num%2==0
# print(list(filter(pares, lista)))


# Questão 3

# lista = [1, 2, 3, 4, 5]
# soma = reduce (lambda v1,v2 : v1+v2, lista)
# print(soma)


# Questão 4

# lista = ["uva", "banana", "maçã", "laranja"]
# ordem = sorted(lista, key = lambda x: len(x))
# print(ordem)


# Questão 5

# lista = ["ana", "pedro", "maria"]
# maiscula = list(map(lambda nome: nome.capitalize(), lista))
# print(maiscula)


# Questão 6

# lista = [2, 3, 4, 5]
# multiplicacao = reduce(lambda v1,v2 : v1*v2, lista)
# print(multiplicacao)


# Questão 7

lista = ["banana", "uva", "maçã", "laranja"]
ordem = sorted(lista, key=lambda palavra: palavra[-1])
print(ordem)
