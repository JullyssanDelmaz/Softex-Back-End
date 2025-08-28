# FUNÇÕES

def saudacao(): #Criando a função
    print("Olá! Tudo bem?") #Definindo o que a função vai fazer
saudacao() #Chamando a função 

def saudacao():
    return "Olá! Tudo bem?"

def soma(*nuns): # (*nuns) serve pra colocar qualquer limite de valores dentro da função.
    resultado=0
    for numero in nuns:
        resultado+=numero
    return resultado
print(soma(2,3,5,2,7))



