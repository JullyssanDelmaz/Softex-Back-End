# Questão 1

# class ContaBancaria:
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.__saldo = saldo 

#     def get_saldo(self):
#         return self.__saldo

   
#     def set_saldo(self, valor):
#         if valor < 0:
#             print("Erro: O saldo não pode ser negativo.")
#         else:
#             self.__saldo = valor
#             print(f"Saldo atualizado para R$ {self.__saldo}")


# conta = ContaBancaria("Maria", 100)
# print("Saldo inicial:", conta.get_saldo())  

# conta.set_saldo(200)  
# conta.set_saldo(-50)   


# Questão 2

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        if len(str(novo_cpf)) == 11:  
            self.__cpf = novo_cpf
            print("CPF atualizado com sucesso.")
        else:
            print("CPF inválido.")

    
    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        if len(str(nova_identidade)) >= 6:  
            self.__identidade = nova_identidade
            print("Identidade atualizada com sucesso.")
        else:
            print("Identidade inválida.")


p1 = Pessoa("João", "01/01/2000", "12345678901", "MG123456")

print("CPF inicial:", p1.get_cpf())
p1.set_cpf("98765432100")   # válido
p1.set_cpf("123")           # inválido

print("Identidade inicial:", p1.get_identidade())
p1.set_identidade("SP987654")  # válido
p1.set_identidade("12")        # inválido