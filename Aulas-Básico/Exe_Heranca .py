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

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email
#     def __str__(self):
#         return f"Nome: {self.nome} | E-mail: {self.email}"
    
#     def saudacao(self):
#         print("Olá, usuário")


# class Cliente(Usuario):
#     print("Olá, Cliente!")
#     ...

# cliente01 = Cliente("Jullyssan", "jullydelmaz@yahoo.com.br")


# Questão 4

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email
#     def __str__(self):
#         return f"Nome: {self.nome} | E-mail: {self.email} | Saldo: {self.saldo}"
    
    
# class Cliente(Usuario):
#     def __init__(self, nome, email, saldo):
#         super().__init__(nome, email)
#         self.saldo = saldo

# cliente01 = Cliente("Jullyssan", "jullydelmaz@yahoo.com.br", 500)
# print(cliente01)


# Questão 5

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email
#     def __str__(self):
#         return f"Nome: {self.nome} | E-mail: {self.email} | Cargo: {self.cargo} | Turno: {self.turno} | Departamento: {self.departamento}"

# class Funcionario(Usuario):
#     def __init__(self, nome, email, cargo, turno):
#         super().__init__(nome, email)
#         self.cargo = cargo
#         self.turno = turno

# class Gerente(Funcionario):
#     def __init__(self, nome, email, cargo, turno, departamento):
#         super().__init__(nome, email, cargo, turno)
#         self.departamento = departamento

# gerente1 = Gerente("Jullyssan", "jdelmaz@git.com", "Gerente Educacional", "Integral", "Pedagógico")
# print(gerente1)

# Questão 6

# class Autenticacao:
#     def __init__(self, email, senha):
#         self.email = email
#         self.senha = senha

#     def login(self, email, senha):
#         if self.email == email and self.senha == senha :
#             return("Login permitido!")
#         else:
#             return("Login não permitido, tente novamente!")

# class Permissao:
#     def __init__(self, departamento):
#         self.departamento = departamento

#     def verificar_permissao(self, departamento):
#         if departamento == "administração":
#             return("Acesso autorizado!")
#         else:
#             return("Acesso autorizado apenas para administradores.")

# class Administrador(Autenticacao, Permissao):
#     def __init__(self, email, senha, departamento):
#         Autenticacao.__init__(self, email, senha)
#         Permissao.__init__(self, departamento)


# usuario01 = Administrador("jdelmaz@git.com", 123456, "pedagógico")
# print(usuario01.login("jdelmaz@git.com", 123456))
# print(usuario01.verificar_permissao("pedagógico"))


# Questão 7


class Autenticacao:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def login(self, email, senha):
        if self.email == email and self.senha == senha :
            return("Login permitido!")
        else:
            return("Login não permitido, tente novamente!")
        
    def status(self):
        return f"Login permitido!"


class Permissao:
    def __init__(self, departamento):
        self.departamento = departamento

    def verificar_permissao(self, departamento):
        if departamento == "administração":
            return("Acesso autorizado!")
        else:
            return("Acesso autorizado apenas para administradores.")
        
    def status(self):
        return f"Acesso autorizado!"

class Administrador(Autenticacao, Permissao):
    def __init__(self, email, senha, departamento):
        Autenticacao.__init__(self, email, senha)
        Permissao.__init__(self, departamento)


usuario01 = Administrador("jdelmaz@git.com", 123456, "pedagógico")
print(usuario01.login("jdelmaz@git.com", 123456))
print(usuario01.verificar_permissao("pedagógico")) 

print(Administrador.__mro__)




        







