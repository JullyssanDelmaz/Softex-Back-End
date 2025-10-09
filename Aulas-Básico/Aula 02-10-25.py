from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def movimentar(self,metros:float):
#         print(f"O animal se deslocou {metros} metros")
# animal1 = Animal()
# animal1.movimentar(5)

# class Pessoa(ABC):
#     @abstractmethod
#     def comer(self):
#         print("A pessoa está comendo")
#     @abstractmethod
#     def andar(self):
#         print("A pessoa está andando")
#     @abstractmethod
#     def dormir(self):
#         print("A pessoa está dormindo")

# class Estudante(Pessoa):
#     def comer(self):
#         return super().comer()
#     def andar(self):
#         return super().andar()
#     def dormir(self):
#         return super().dormir()
    
# joao = Estudante()
# joao.comer()
# joao.andar()
# joao.dormir()



# # Questão 1

# class Pessoa(ABC):
#     @abstractmethod
#     def falar(self):
#         print("A pessoa está falando.")
#     @abstractmethod
#     def andar(self):
#         print("A pessoa está andando.")
#     @abstractmethod
#     def comer(self):
#         print("A pessoa está comendo.")

# class Funcionario(Pessoa):
#     def falar(self):
#         return super().falar()
#     def andar(self):
#         return super().andar()
#     def comer(self):
#         return super().comer()

# class Aluno(Pessoa):
#     def falar(self):
#         return super().falar()
#     def andar(self):
#         return super().andar()
#     def comer(self):
#         return super().comer()
    
# jullyssan = Funcionario()
# jullyssan.comer()
# jully = Aluno()
# jully.andar()


# Questão 2

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        ...
    @abstractmethod
    def andar(self):
        ...
    @abstractmethod
    def comer(self):
        ...

class Funcionario(Pessoa):
    def falar(self):
        print("Ele está falando.")
    def andar(self):
        print("Ele está andando.")
    def comer(self):
        print("Ele está comendo.")

class Aluno(Pessoa):
    def falar(self):
        print("Ele falou.")
    def andar(self):
        print("Ele andou.")
    def comer(self):
        print("Ele comeu.")
    
jullyssan = Funcionario()
jullyssan.falar()
jully = Aluno()
jully.andar()