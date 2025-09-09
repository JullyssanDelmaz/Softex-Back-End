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

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def __str__(self):
        return f"O saldo é {self.saldo}."
    def depositar(self, valor):
        saldo += valor
        print(f"O saldo da conta é {saldo}.")
    def sacar(self, valor):
        if saldo>= valor:
            saldo-=valor
            print(f"O saldo da conta é {saldo}.")
mov1 = ContaBancaria("Jullyssan", 250)
mov1.depositar()