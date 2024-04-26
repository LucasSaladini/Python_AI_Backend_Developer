class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("Latindo")


c = Cachorro("Chappie", "preto")
c.falar()

print("ola mundo")
del c
print("ola mundo")
print("ola mundo")
print("ola mundo")