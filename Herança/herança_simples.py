class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
                 
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "ABC-1234", 2)
# print(moto)
moto.ligar_motor()

carro = Carro("branco", "XDE-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "GFD-8712", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()