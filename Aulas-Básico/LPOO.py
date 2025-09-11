# class Cachorro:
#     especie = "Canis lupus familia"
#     nome = "Toto"
#     raca = "caramelo"
#     idade = 2

# auau = Cachorro()
# print(auau)
# print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")
#     #pass # ou 3 pontos (...)


# class Cachorro:
#     especie = "Canis lupus familiaris"
#     def __init__(self, nome, raca, idade): # dois underlines
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade
# dog = Cachorro("Rex", "caramelo", 3)
# #print(dog.especie, dog.nome, dog.raca, dog.idade, sep="\n") # ou usar __str__

# def __str__(self):
#     return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\n Idade: {self.idade}"
# print(dog)

# class Cachorro:
#     especie = "Canis lupus familiaris"
#     def __init__(self, nome:str, idade:int, raca:str="caramelo"):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade
#     def __str__(self):
#         return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\n Idade: {self.idade}"
#     def latindo(self):
#         print("auauauau")
#     def correr(self, metros):
#         print(f"{self.nome} correu {metros}m")

# auau = Cachorro("Bob", 15)
# auau.latindo()
# auau.correr(50)


# Questão 1

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# pessoa1 = Pessoa("André", 34)
# pessoa2 = Pessoa("Letícia", 29)

# print(f"O nome é {pessoa1.nome} e a idade {pessoa1.idade} anos.")
# print(f"O nome é {pessoa2.nome} e a idade {pessoa2.idade} anos.")


# Questão 2

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def __str__(self):
#         return f"Nome: {self.nome}\n Idade: {self.idade}"
#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# pessoa1 = Pessoa("André", 34)
# pessoa2 = Pessoa("Letícia", 29)
# pessoa1.apresentar()
# pessoa2.apresentar()


# Questão 3

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca= marca
#         self.modelo = modelo
#         self.ano = ano
#     def expor(self):
#         print(f"O carro {self.modelo}, da marca {self.marca} do ano de {self.ano} é o meu favorito!")
# carro1 = Carro("Mitsubshi", "Lancer", 2016)
# carro2 = Carro("Volkswagen", "Fusca", 1967)
# carro3 = Carro("Toyota", "Hilux", 2025)

# carro1.expor()
# carro2.expor()
# carro3.expor()


# Questão 4

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca= marca
#         self.modelo = modelo
#         self.ano = ano
#     def expor(self):
#         print(f"O carro {self.modelo}, da marca {self.marca} do ano de {self.ano} é o meu favorito!")
# carro1 = Carro("Mitsubshi", "Lancer", 2016)
# carro2 = Carro("Volkswagen", "Fusca", 1967)
# carro3 = Carro("Toyota", "Hilux", 2025)
# carro2.ano = 1976

# carro2.expor()


# Questão 5

# class ContaBancaria:
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo
#     def __str__(self):
#         return f"O saldo é {self.saldo}."
#     def __repr__(self):
#         return f"ContaBancaria(titular= {self.titular!r}, o saldo={self.saldo!r})"
    


#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"O saldo da conta é {self.saldo}.")


#     def sacar(self, valor):
#         self.saldo-=valor
#         print(f"O saldo da conta é {self.saldo}.")

# mov1 = ContaBancaria("Jullyssan", 250)
# mov1.depositar(140)
# mov1.sacar(90)

# Questão 6

# class ContaBancaria:
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo
#     def __str__(self):
#         return f"O saldo é {self.saldo}."
#     def __repr__(self):
#         return f"ContaBancaria(titular= {self.titular!r}, o saldo={self.saldo!r})"
    


#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"O saldo da conta é {self.saldo}.")


#     def sacar(self, valor):
#         if valor > self.saldo:
#             print("Saldo insuficiente")
#         else:
#             self.saldo-=valor
#             print(f"O saldo da conta é {self.saldo}.")

# mov1 = ContaBancaria("Jullyssan", 250)
# mov1.sacar(300)


# Questão 7 e 8

# class Aluno:

#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota
#     def __str__(self):
#         return f"Aluno: {self.nome} - Nota: {self.nota}"
#     def __repr__(self):
#         return f"(aluno={self.nome!r}, nota={self.nota!r})"
    
# aluno1 = Aluno("Gabriela", 9.5)
# aluno2 = Aluno("Kalina", 5)


# class Turma:
#     def __init__(self):
#         self.alunos = [ ]
#     def cadastro_alunos(self, aluno):
#         self.alunos.append(aluno)
        

# turma1 = Turma()
# turma1.cadastro_alunos(aluno1)
# turma1.cadastro_alunos(aluno2)
# print(turma1.alunos)
# print(aluno1)
# print(aluno2)

# Questão 9

# class Cachorro:
#     especie = "Canis familiaris"
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def __str__(self):
#         return f"O cachorro {self.nome} tem {self.idade} anos de idade."
    
# cachorro007 = Cachorro("Berlim", 4)
# print(cachorro007.especie)
# cachorro007.especie= "Canis gatis"
# print(cachorro007.especie)


    

