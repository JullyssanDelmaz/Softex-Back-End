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

class Cachorro:
    especie = "Canis lupus familiaris"
    def __init__(self, nome:str, idade:int, raca:str="caramelo"):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    def __str__(self):
        return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\n Idade: {self.idade}"
    def latindo(self):
        print("auauauau")
    def correr(self, metros):
        print(f"{self.nome} correu {metros}m")

auau = Cachorro("Bob", 15)
auau.latindo()
auau.correr(50)
