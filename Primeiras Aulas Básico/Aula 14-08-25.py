LISTAS (adicionando itens)
frutas =["banana", "manga","laranja","morango","banana"]
frutas.append("limão")
frutas.insert(4, "maçã")
print(frutas)
print(frutas[0:3])
temperos = ["pimenta", "sal"]
frutas+=temperos
print(frutas)


Remover Itens
frutas.remove("banana")
print(frutas)
frutas.pop(2)
print(frutas)
del frutas #Serve pra eliminar qualquer coisa dentro do python
del frutas[0] #Serve pra eliminar um item pelo índice dentro da lista
print(frutas.clear()) # Limpar os itens da lista
print(sorted(frutas)) # Sorted serve para colocar a lista em ordem alfabética temporariamente
frutas.sort() # Sort muda definitivamente a ordem da lista
frutas.sort(reverse=True) # Sort reverse muda definitivamente a ordem da lista Z para A
print(frutas)

COPIANDO LISTAS
salada_de_fruta = frutas[:]
print(salada_de_fruta)
salada_de_fruta = []
for fruta in frutas:
    salada_de_fruta.append(fruta)
print(salada_de_fruta)
salada_de_fruta = frutas.copy()
print(salada_de_fruta)

print(frutas.count("banana")) # conta a quantidade de vezes que o elemento aparece dentro da lista

salada_de_fruta.extend(frutas) # Adicionando uma lista à outra
print(salada_de_fruta)

salada_de_fruta.index("banana") # Para descobrir a posição do item Banana
idx_banana = frutas.index("banana") # Verificando o índice da Banana
frutas.pop(idx_banana) # Tirando o item banana pelo índice
print(frutas) # Lista sem a banana
