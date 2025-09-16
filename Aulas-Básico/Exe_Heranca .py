# QUESTÕES SALA

# Questão 1


class Pessoa:
    def __init__(self, nome, idade, genero, estado_civil):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.estado_civil = estado_civil
    def __str__(self):
        return f"Nome: {self.nome}| Idade: {self.idade}| Gênero: {self.genero}| Estado Civil: {self.estado_civil}| Telefone: {self.telefone}| Email: {self.email}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, estado_civil, telefone, email):
        super().__init__(nome, idade, genero, estado_civil)
        self.telefone = telefone
        self.email = email

pessoa1 = Funcionario("Jullyssan", 29, "Feminino","Casada", 81983568023, "jullydelmaz@yahoo.com.br")

print(pessoa1)


# Questão 2