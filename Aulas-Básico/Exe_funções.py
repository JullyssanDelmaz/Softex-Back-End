# Questão 1

# def saudacao():
#     print("Olá, bem-vindo ao Python!")
# print(saudacao)

# Questão 2

# x = int(input("Escreva um valor: "))
# def dobro(x):
#     return 2*x
# print(dobro(x))


# Questão 3

# def soma(a, b):
#     return a + b

# resultado = soma(10, 20)
# print("Soma de 10 + 20 =", resultado)

# Questão 4

# def mensagem(nome="visitante"):
#     print(f"Olá, {nome}!")

# mensagem("Maria")
# mensagem()


# Questão 5

# def operacoes(a, b):
#     soma = a + b
#     subtracao = a - b
#     multiplicacao = a * b
#     return soma, subtracao, multiplicacao

# s, sub, mult = operacoes(10, 5)
# print("Soma:", s)
# print("Subtração:", sub)
# print("Multiplicação:", mult)


# Questão 6

# def media(*numeros):
#     if len(numeros) == 0:
#         return 0
#     return sum(numeros) / len(numeros)

# print("Média de 3 valores:", media(10, 20, 30))
# print("Média de 5 valores:", media(5, 10, 15, 20, 25))
# print("Média de 7 valores:", media(2, 4, 6, 8, 10, 12, 14))


# Questão 7

# def dados_pessoais(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")


# dados_pessoais(nome="Jullyssan", idade=29, cidade="Recife")


# Questão 8

# def calculadora(a, b, operacao):
#     def somar(x, y): return x + y
#     def subtrair(x, y): return x - y
#     def multiplicar(x, y): return x * y
#     def dividir(x, y): return x / y if y != 0 else "Erro: divisão por zero"

#     if operacao == "soma":
#         return somar(a, b)
#     elif operacao == "subtracao":
#         return subtrair(a, b)
#     elif operacao == "multiplicacao":
#         return multiplicar(a, b)
#     elif operacao == "divisao":
#         return dividir(a, b)
#     else:
#         return "Operação inválida"

# print(calculadora(10, 5, "soma"))
# print(calculadora(10, 5, "subtracao"))
# print(calculadora(10, 5, "multiplicacao"))
# print(calculadora(10, 5, "divisao"))


# Questão 9

# def aplicar_operacao(a, b, funcao):
#     return funcao(a, b)

# def soma(a, b): return a + b
# def multiplicacao(a, b): return a * b

# print("Soma:", aplicar_operacao(3, 4, soma))
# print("Multiplicação:", aplicar_operacao(3, 4, multiplicacao))