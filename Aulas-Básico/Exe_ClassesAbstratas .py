from abc import ABC, abstractmethod

# Questão 1

# class Animal(ABC):
#     @abstractmethod
#     def falar(self):
#        return

# class Cachorro(Animal):
#     def falar(self):
#         print("O cachorro late")
        
        
# class Gato(Animal):
#     def falar(self):
#        print("O gato mia")
      

# animal1 = Cachorro()
# animal1.falar()
# animal2 = Gato()
# animal2.falar()


# Questão 2

# class Animal(ABC):
#     @abstractmethod
#     def falar(self):
#        return

# class Cachorro(Animal):
#     def falar(self):
#         print("O cachorro late")
        
        
# class Gato(Animal):
#     def falar(self):
#        print("O gato mia")
      

# animal1 = Animal()
# animal1.falar()
# Classes abstratas não podem ser instanciadas, somente as classes concretas que herdam os métodos.


# Questão 3

# class FormaGeometrica(ABC):

#     @abstractmethod
#     def area(self, nome:str, b:float, h:float):
        
#         return f"A área da {nome} é {b*h}."
    
#     @abstractmethod
#     def perimetro(self, nome:str, b:float, h:float):
        
#         return f"O perímetro da {nome} é {2*b + 2*h}."
    
# class Retangulo(FormaGeometrica):
    
#     def area(self, nome:str, b:float, h:float):
#         return super().area(nome, b, h) 
#     def perimetro(self, nome:str, b:float, h:float):
#         return super().perimetro(nome, b, h)

# quadra_futsal = Retangulo()
# print(quadra_futsal.area("quadra de futsal",38,18))
# print(quadra_futsal.perimetro("quadra de futsal",38,18))

# quadra_basquete = Retangulo()
# print(quadra_basquete.area("quadra de basquete",28,15))
# print(quadra_basquete.perimetro("quadra de basquete",28,15))

# Questão 4

# class Transporte(ABC):
#     @abstractmethod
#     def mover(self, metros:float):
#         return f"O transporte se moveu por {metros} metros a frente."
#     @abstractmethod
#     def parar(self, ficar:float):
#         return f"O transporte parou em {ficar} metros."
    
# class Carro(Transporte):
#     def mover(self, metros:float):
#         return super().mover(metros)
#     def parar(self, ficar:float):
#         return super().parar(ficar)
    
# lancer = Carro()
# print(lancer.mover(5))

#Não é possível instanciar sem utilizar todos os métodos da classe abstrata.

# lancer = Carro()
# print(lancer.mover(10))
# print(lancer.parar(3))

    
    


