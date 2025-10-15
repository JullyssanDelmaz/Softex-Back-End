from abc import ABC, abstractmethod

# Questão 1

# class Livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor
#     def __str__(self):
#         return f"'{self.titulo}' de {self.autor}"

# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#         self.livros_favoritos = []

#     def livro_favorito(self, livro):
#         self.livros_favoritos.append(livro)

#     def listar_livros(self):
#         if not self.livros_favoritos:
#             print(f"{self.nome} não tem livros favoritos.")
#         else:
#             print(f"Livros favoritos de {self.nome}:")
#             for livro in self.livros_favoritos:
#                 print(f"{livro}")

# livro1 = Livro("Dom Casmurro", "Machado de Assis")
# pessoa1 = Pessoa("Renata")
# pessoa1.livro_favorito(livro1)
# pessoa1.listar_livros()

# Questão 2

# class Onibus:
#     def __init__(self, linha, numero):
#         self.linha = linha
#         self.numero = numero

#     def embarcar(self, nome_aluno):
#         print(f"{nome_aluno} embarcou na linha {self.linha}, no ônibus de número {self.numero}.")

# class Aluno:
#     def __init__(self, nome_aluno):
#         self.nome = nome_aluno

#     def conhece(self,onibus):
#         print(f"{self.nome} conhece o ônibus.")
#         onibus.embarcar(self.nome)

# linha1 = Onibus("Vasco da Gama/Cruz Cabugá", 622)
# aluno1 = Aluno("Vitão")
# aluno1.conhece(linha1)

# Questão 3

# class Funcionario:
#     def __init__(self,nome,cargo):
#         self.nome = nome
#         self.cargo = cargo

#     def exibir_informacoes(self):
#         print(f"Funcionário: {self.nome} | Cargo: {self.cargo}")

# class Departamento:
#     def __init__(self, nome_dep):
#         self.nome_dep = nome_dep
#         self.funcionarios = []

#     def add_funcionario(self,funcionario):
#         self.funcionarios.append(funcionario)

#     def listar_funcionarios(self):

#         print(f"Departamento: {self.nome_dep}")
#         if not self.funcionarios:
#             print("Nenhum funcionário neste departamento.")
#         else:
#             for func in self.funcionarios:
#                 func.exibir_informacoes()

# func1 = Funcionario("Jully","Professora de Matemática")
# func2 = Funcionario("Letícia", "Professora de Biologia")
# func3 = Funcionario("Vanesca","Professora de matemática")
# func4 = Funcionario("Josi","Professora de Português")

# dept1 = Departamento("Educação")

# dept1.add_funcionario(func1)
# dept1.add_funcionario(func2)
# dept1.add_funcionario(func3)
# dept1.add_funcionario(func4)

# dept1.listar_funcionarios()

# Questão 4

# class Jogador:
#     def __init__(self, nome, posicao):
#         self.nome = nome
#         self.posicao = posicao

#     def exibir_informacoes(self):
#         print(f"Jogador: {self.nome} | Posição: {self.posicao}")


# class Time:
#     def __init__(self, nome_time):
#         self.nome_time = nome_time
#         self.jogadores = [] 

#     def adicionar_jogador(self, jogador):
#         self.jogadores.append(jogador) 

#     def listar_jogadores(self):
#         print(f"Time: {self.nome_time}")

#         if not self.jogadores:
#             print("Nenhum jogador cadastrado.")
#         else:
#             for jogador in self.jogadores:
#                 jogador.exibir_informacoes()

# j1 = Jogador("Vini Jr", "Atacante")
# j2 = Jogador("Roberto Carlos", "Lateral")
# j3 = Jogador("Dida", "Goleiro")

# time_brasil = Time("Seleção Brasileira")

# time_brasil.adicionar_jogador(j1)
# time_brasil.adicionar_jogador(j2)
# time_brasil.adicionar_jogador(j3)

# time_brasil.listar_jogadores()


# Questão 5

# class Motor:
#     def __init__(self, potencia):
#         self.potencia = potencia
#         print(f"Motor de {self.potencia}cv criado.")

#     def ligar(self):
#         print("Motor ligado.")

#     def __del__(self):
#         print(f"Motor de {self.potencia}cv destruído.")


# class Carro:

#     def __init__(self, modelo, potencia_motor):

#         self.modelo = modelo
#         self.motor = Motor(potencia_motor)
#         print(f"Carro {self.modelo} criado.")

#     def ligar(self):
#         print(f"Ligando o carro {self.modelo}...")
#         self.motor.ligar()

#     def __del__(self):
#         print(f"Carro {self.modelo} destruído.")


# meu_carro = Carro("Fusca", 80)
# meu_carro.ligar()
# del meu_carro


# Questão 6

# class Comodo:
#     def __init__(self, nome):
#         self.nome = nome
#         print(f"Cômodo '{self.nome}' criado.")

#     def __del__(self):
#         print(f"Cômodo '{self.nome}' destruído.")


# class Casa:
#     def __init__(self, endereco):
#         self.endereco = endereco
#         self.comodos = []
#         print(f"Casa criada no endereço: {self.endereco}")

#         self.adicionar_comodo("Sala")
#         self.adicionar_comodo("Cozinha")
#         self.adicionar_comodo("Quarto")
#         self.adicionar_comodo("Banheiro")

#     def adicionar_comodo(self, nome_comodo):
#         comodo = Comodo(nome_comodo)
#         self.comodos.append(comodo)

#     def listar_comodos(self):
#         print(f"Cômodos da casa em {self.endereco}:")

#         for comodo in self.comodos:
#             print(f"{comodo.nome}")

#     def __del__(self):
#         print(f"Casa no endereço {self.endereco} destruída.")


# casa1 = Casa("Rua Senador Milton Campos, 254")
# casa1.listar_comodos()
# del casa1