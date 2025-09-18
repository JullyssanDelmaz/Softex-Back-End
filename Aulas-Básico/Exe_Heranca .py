# QUESTÕES SALA

# Questão 1


# class Pessoa:
#     def __init__(self, nome, idade, genero, estado_civil):
#         self.nome = nome
#         self.idade = idade
#         self.genero = genero
#         self.estado_civil = estado_civil
#     def __str__(self):
#         return f"Nome: {self.nome}| Idade: {self.idade}| Gênero: {self.genero}| Estado Civil: {self.estado_civil}| Telefone: {self.telefone}| Email: {self.email}"

# class Funcionario(Pessoa):
#     def __init__(self, nome, idade, genero, estado_civil, telefone, email):
#         super().__init__(nome, idade, genero, estado_civil)
#         self.telefone = telefone
#         self.email = email

# pessoa1 = Funcionario("Jullyssan", 29, "Feminino","Casada", 81983568023, "jullydelmaz@yahoo.com.br")

# print(pessoa1)


# Exercício POO:Herança

# Questão 1 e 2 

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email
#     def __str__(self):
#         return f"Nome: {self.nome} | E-mail: {self.email}"
    
#     def exibir_informacoes(self):
#         return f"O nome do usuário é {self.nome} e o email é {self.email}."


# class Cliente(Usuario):
#     ...   

# cliente01 = Cliente("Jullyssan", "jullydelmaz@yahoo.com.br")
# print(cliente01.exibir_informacoes())


# Questão 3

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def __str__(self):
        return f"Nome: {self.nome} | E-mail: {self.email}"
    
    def saudacao():
        print("Olá, usuário")


class Cliente(Usuario):
    ...

cliente01 = Cliente("Jullyssan", "jullydelmaz@yahoo.com.br")





