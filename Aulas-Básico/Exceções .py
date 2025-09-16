# Questão 1
# try:
#     numero = int(input("Digite um número inteiro: "))
#     print("Você digitou:", numero)

# except ValueError:
#     print("Erro! Você não digitou um número inteiro.")


# Questão 2

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resultado = num1 * num2

#     print(f"Resultado da multiplicação: {resultado}")

# except ValueError:
#     print("Erro! Você precisa digitar apenas números.")

# Questão 3

# try:
#     numero = int(input("Digite um número inteiro: "))

# except ValueError:
#     print("Erro! Você não digitou um número inteiro.")

# else:
#     print(f"Parabéns! Você digitou o número {numero}")

# Questão 4


# try:
#     arquivo = open("dados.txt", "r")  # Tenta abrir o arquivo no modo leitura
#     conteudo = arquivo.read()
#     print("Arquivo aberto com sucesso!")
#     print(conteudo)

# except FileNotFoundError:
#     print("Erro: O arquivo 'dados.txt' não foi encontrado.")

# finally:
#     print("Fechando o programa")

# Questão 5


# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Você tentou dividir por zero.")
#     return a / b

# try:
#     resultado = dividir(10, 2)
#     print("Resultado:", resultado)

# except ZeroDivisionError as erro:
#     print("Erro ao dividir:", erro)

# Questão 6


# class IdadeInvalidaError(Exception):
#     pass

# def cadastrar_idade(idade):
#     if idade < 0:
#         raise IdadeInvalidaError("Idade não pode ser negativa!")
#     print(f"Idade {idade} cadastrada com sucesso.")

# try:
#     idade = int(input("Digite sua idade: "))
#     cadastrar_idade(idade)

# except IdadeInvalidaError as erro:
#     print("Erro:", erro)

# except ValueError:
#     print("Erro: Você precisa digitar um número inteiro.")

# Questão 7


# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resultado = num1 / num2

# except ValueError:
#     print("Erro: Você precisa digitar apenas números.")

# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")
    
# else:
#     print(f"Resultado da divisão: {resultado}")

#Questão 8

# try:
#     numero = int(input("Digite um número inteiro: "))

# except ValueError:
#     print("Erro: Você não digitou um número inteiro.")

# else:
#     if numero % 2 == 0:
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} é ímpar.")

# finally:
#     print("Fim do programa.")


# Questão 9


class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
    return saldo - valor

try:
    saldo = float(input("Digite seu saldo atual: "))
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    
    novo_saldo = sacar(saldo, valor_saque)
    print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}")

except SaldoInsuficienteError as erro:
    print("Erro:", erro)
    
except ValueError:
    print("Erro: Digite apenas números válidos.")