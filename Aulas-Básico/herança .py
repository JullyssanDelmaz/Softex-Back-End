# class Animal:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def som(self):
#         print("som indefinido")

# class Cachorro(Animal):
#     def som(self):
#         print("au au")

# dog = Cachorro("rex", 2)
# print(dog.nome)
# print(dog.idade)
# dog.som()



# class Mamifero: # Classe do tipo Mãe / Pai
#     def __init__(self, idade, habitat, som):
#         self.idade =  idade
#         self.habitat = habitat
#         self.som = som
#         self.prole = "gestação"
#         self.alimentacao_infantil = "leite"

#     def som(som):
#         print(som)

# class Morcego(Mamifero): #n Classe tipo Filho
#     def __init__ (self, idade, habitat, som, locomocao = "vôo"):
#         super().__init__(idade, habitat, som) # Trazendo os atributos da classe Mãe
#         self.locomocao = locomocao

#zubat = Morcego(1, "laje", "assobio")
# print(zubat.idade)
# print(zubat.habitat)
# print(zubat.som)
# print(zubat.locomocao)

# class Gato(Mamifero):
#     def __init__(self, idade, habitat, som, especie, raca, cor_olho):
#         super().__init__(idade, habitat, som)
#         self.especie = especie
#         self.raca = raca
#         self.cor_olho = cor_olho
#     def __str__(self):
#         return f"O mamífero de idade {self.idade} pode ser localizado no {self.habitat} {self.som}, sua espécie é {self.especie} a raça é {self.raca} e a cor de seus olhos é {self.cor_olho}."
    
#     def arranhar(sel):
#         print(" O gato está arranhando o sofá")

# gato1 = Gato(3, "Cama da Vovó", "miando", "Felinis", "Siamês", "azul")
# print(gato1)
# gato1.arranhar()


class Mamifero: # Classe do tipo Mãe / Pai
    def __init__(self, idade, habitat, som): #especie):
        self.idade =  idade
        self.habitat = habitat
        self.som = som
        #self.especie = especie
        self.prole = "gestação"
        self.alimentacao_infantil = "leite"

    def __str__(self):
        return f"O mamífero de idade {self.idade}, que vive no habitat {self.habitat} e {self.som} tem cor {self.cor} e espécie {self.especie}."

    def som(som):
        print(som)

class AnimaisVoadores:
    def __init__(self, cor):
        self.cor = cor
    def movimentar(self):
        print("Voando")
    
class Morcego(Mamifero, AnimaisVoadores):
    def __init__(self, idade, habitat, som, cor, especie="Desmodus rotundus"):
        self.especie = especie
        AnimaisVoadores.__init__(self, cor)
        Mamifero.__init__(self, idade, habitat, som)

batone = Morcego(10, "pé de jambo", "chiar", "preta")

print(batone)


