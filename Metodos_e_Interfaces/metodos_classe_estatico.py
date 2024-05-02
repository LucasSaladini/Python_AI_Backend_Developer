class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # print(cls)
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Lucas", 30)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1993, 9, 28, "Lucas")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(30))
print(Pessoa.e_maior_idade(17))