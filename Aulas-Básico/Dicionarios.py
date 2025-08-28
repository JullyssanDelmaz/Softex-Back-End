#1
# aluno = {"nome": "Jullyssan",
#          "idade": 29,
#          "nota": 7.5}

#2
# produto ={"nome":"Caneta",
#           "preço": 2.5,
#           "estoque": 100}
# print(produto.get("nome"))
# print(produto.get("estoque"))

#3
# pessoa = {"nome": "Carlos",
#           "idade": 30}
# pessoa["cidade"]="São Paulo"
# print(pessoa)

# #4
# carro = {"marca": "Ford",
#          "modelo": "Fiesta",
#          "ano": 2010}
# carro.pop("ano")
# print(carro)


# #5
# contato = {"nome": "Ana",
#            "email": "ana@email.com"}
# if contato.get("telefone") == None:
#     print("Não informado")


#6

# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
# def palavras_repetidas(palavras):
#     contagem = {}
#     for elemento in palavras:
#         contagem[elemento] = contagem.get(elemento, 0) + 1
#     return contagem
# dic_palavras = palavras_repetidas(palavras)
# print(dic_palavras)





# #7
# d = {"a": 1, "b": 2, "c": 3}
# invertido_d = {valor: chave for chave, valor in d.items()}
# print(invertido_d)


# 8
notas_alunos = {"Ana": [4,6,9],
                "Bianca": [3,6,4],
                "Camilly": [10,9,7]}
def media_alunos(notas_alunos):
   for valor in notas_alunos.items():
      print(valor)
      for nota in valor[1]:
         soma = 0
         soma+=nota
      media = soma/3
      print(f" {media :.2f}")

    
    
    