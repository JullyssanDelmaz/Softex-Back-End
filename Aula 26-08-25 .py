cadastro = {"nome": "Lucas",
            "idade": 25,
            "email": "lucas@email.com"}
print(cadastro.get("nome"))


cliente = {"nome":"Amanda",
           "idade": 31}
if cliente.get("telefone") == None:
    print("Não informado")

livro = {"título":"1984",
         "autor": "George Orwell",
         "ano": 1949}
for i in livro.keys():
    print(i)

livro["disponível"]="True"
print(livro)
#print(livro.pop("ano"))
livro_removido= livro.pop("ano")
print(livro_removido )

compras = {"banana":8,
           "kiwi":20,
           "laranja":3,
           "banana":8,
           "maçã":1,
           "banana":8}
x=0
for i in compras.values():
    x+=i
total= print(x)

frutas = {"maçã":3,
          "banana":5,
          "laranja":2}
for itens, quantidade in frutas.items():
    if quantidade>2:
        print(itens,quantidade)
    
        
    


usuario = {"login": "joaosilva"}
if usuario.get("senha") == None:
    usuario["senha"] = "123456"
print(usuario)



capitais = {"SP": "São Paulo",
            "RJ":"Rio de Janeiro",
            "MG":"Belo Horizonte"}
for estado, capital in capitais.items():
    print(f"A capital de {estado} é {capital}")

    


produto = {"nome": "Teclado",
           "estoque": 15 }
produto.update({"estoque":25})
print(produto)
produto["estoque"]+=10
print(produto)







        
    


