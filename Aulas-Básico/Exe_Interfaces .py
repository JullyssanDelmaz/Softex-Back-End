from abc import ABC, abstractmethod

# Questão 1

# class Pagamento(ABC):
#     @abstractmethod
#     def processar(self, valor):
#         return
    
# class CartaoCredito(Pagamento):
#     def processar(self, valor):
#         return f"Processando pagamento de R${valor: .2f} com cartão de crédito."

# class Boleto(Pagamento):
#     def processar(self, valor):
#         return f"Processando pagamento de R$ {valor: .2f} com Boleto Bancário."

# pag_cartao = CartaoCredito()
# pag_boleto = Boleto()

# print(pag_cartao.processar(150.75))
# print(pag_boleto.processar(78.90))

# Questão 2

# class Ligavel(ABC):
#     @abstractmethod
#     def ligar(self):
#         pass

# class Desligavel(ABC):
#     @abstractmethod
#     def desligar(self):
#         pass
    
# class Computador(Ligavel, Desligavel):
#     def ligar(self):
#         return "Computador ligado"
#     def desligar(self):
#         return "Computador desligado"
    
# pc = Computador()

# print(pc.ligar())
# print(pc.desligar())

# Questão 3

# class Imprimivel(ABC):
#     @abstractmethod
#     def imprimir(self):
#         pass
# class Exportavel(ABC):
#     @abstractmethod
#     def exportar(self):
#         pass
# class Relatorio(Imprimivel, Exportavel):
#     def imprimir(self):
#         return f"Imprimindo arquivo"
#     def exportar(self):
#         return f"Exportando arquivo"

# arquivo = Relatorio()
# print(arquivo.imprimir())
# print(arquivo.exportar())


# Questão 4

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} está sendo salvo...")
    
    def buscar(self, id):
        print(f"O id {id} está sendo procurado...")



arquivo = RepositorioMemoria()
print(arquivo.salvar("pdf"))
print(arquivo.buscar(5))


# O repositório não implementa apenas um método, só todos juntos.



    

