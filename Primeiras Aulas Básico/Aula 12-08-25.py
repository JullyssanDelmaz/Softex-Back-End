# CONDICIONAIS (IF, ELIF E ELSE)

# # Questão 1
# valor = int(input("Escreva um valor qualquer: "))
# if valor%2==0:
#     print(f"O número {valor} é par!")
# else:
#     print(f"O número {valor} é ímpar!")

# # Questão 2
# nota = float(input("Escreva a nota: "))
# if nota>=7:
#     print("Aluno aprovado!")
# elif nota>=5 and nota<7:
#     print("Aluno em recuperação!")
# else:
#     print("Aluno reprovado!")

# # Questão 3
# v1 = float(input("Escreva o primeiro valor: "))
# v2 = float(input("Escreva o segundo valor:"))
# if v1 == v2:
#     print(f"Os números {v1} e {v2} são iguais")
# elif v1 > v2:
#     print(f"O número {v1} é maior que {v2}")
# else:
#     print(f"O número {v2} é maior que {v1}")

# # Questão 4
# idade = int(input("Escreva a idade: "))
# if idade<= 12:
#     print("Criança")
# elif idade<=17:
#     print("Adolescente")
# elif idade<=64:
#     print("Adulto")
# else:
#     print("Idoso")

 
# LAÇOS (FOR E WHILE)

# Questão 1

# for x in range(1,11):
#     print(x)

# # Questão 2
# valor = int(input("Escreva um valor: "))
# for x in range(1,11):
#     print(f"{valor}x{x} = {valor*x}")

# Questão 3
soma = 0
while True:
    x = int(input("Escreva um valor qualquer, para parar, escreva 0:"))
    if x== 0:
        break
    else:
        soma+=x
print(soma)
   