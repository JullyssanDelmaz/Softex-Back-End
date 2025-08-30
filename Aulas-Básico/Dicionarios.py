#1
aluno = {"nome": "Jullyssan",
         "idade": 29,
         "nota": 7.5}

#2
produto ={"nome":"Caneta",
          "preço": 2.5,
          "estoque": 100}
print(produto.get("nome"))
print(produto.get("estoque"))

#3
pessoa = {"nome": "Carlos",
          "idade": 30}
pessoa["cidade"]="São Paulo"
print(pessoa)

# Questão 4

carro = {"marca": "Ford",
         "modelo": "Fiesta",
         "ano": 2010}
carro.pop("ano")
print(carro)


# Questão 5

contato = {"nome": "Ana",
           "email": "ana@email.com"}
if contato.get("telefone") == None:
    print("Não informado")


# Questão 6

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
def palavras_repetidas(palavras):
    contagem = {}
    for elemento in palavras:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    return contagem
dic_palavras = palavras_repetidas(palavras)
print(dic_palavras)





# Questão 7

d = {"a": 1, "b": 2, "c": 3}
invertido_d = {valor: chave for chave, valor in d.items()}
print(invertido_d)


# Questão 8

notas_alunos = {"Ana": [4,6,9],
                "Bianca": [3,6,4],
                "Camilly": [10,9,7]}
def media_alunos(notas_alunos):
   for nome, notas in notas_alunos.items():
      soma = 0
      for nota in notas:
         soma+=nota
      media = soma/3
      print(f"{nome}: {media :.2f}")
media_alunos(notas_alunos)


#9


dict_1 = {"Ana": 17,
           "Arthur": 18,
           "Bianca": 16,
           "Ester": 17,
           "Fernanda": 17,
           "Gabriel": 19
           }
dict_2 = {"Ana": 19,
          "Camilly": 18,
          "Daniel": 18,
          "Evelly": 18,
          "Israel": 19,
          "Julia": 18
          }
def conca_dict(dict_1, dict_2):
   dicts = dict_1.copy()
   dicts.update(dict_2)
   return dicts
print(conca_dict(dict_1, dict_2))



# 10

pontuacoes = {"Joao": 50,
              "Maria": 80,
              "Pedro": 70
              }
for i in sorted(pontuacoes, key=pontuacoes.get, reverse=True):
    print(i, pontuacoes[i])

        