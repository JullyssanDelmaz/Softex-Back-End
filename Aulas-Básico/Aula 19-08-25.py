# lista1=[]
# for i in range(10):
#     lista1.append(i*2)
# print(lista1)

# TUPLAS

# nome ="Fred"
# print(list(nome))
# tupla1=1,
# print(type(tupla1))

tupla2=("Fred", "João", "Maria", "Maria", "João", "Maria", "Fred")
print(tupla2.index("João"))
print(tupla2.count("Maria"))

#CONJUNTO SET

testando = {"Fred", "Maria"} # O dicionário precisa ter {"nome: Fred"}

teste = {1,2}
teste.add(3)
print(teste)
teste.clear()
print(teste)

frutas = {"banana", "limão", "tomate"}
legumes = {"cenoura", "tomate", "beterraba"}
print(frutas.difference(legumes)) #Operação DIFERENÇA DE CONJUNTOS
print(frutas.discard("banana"))
print(frutas)
print(legumes & frutas) #Intersecção
print(legumes | frutas) #Adição de conjuntos

#Site w3schools



# DICIONÁRIO

dados_alunos = {"nome":"Fred",
                "Idade":"36",
                "Endereço":"Rua x",
                "Turma":("Turma 34", "Turma 36")}

dados_alunos = {[]"nome":"Fred",
                "Idade":"36",
                "Endereço":"Rua x",
                "Turma":("Turma 34", "Turma 36")]}