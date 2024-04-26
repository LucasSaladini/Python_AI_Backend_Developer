class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Buzinando")
    
    def parar(self):
        print("Parando a bicicleta")
    
    def correr(self):
        print("Correndo com a bicicleta")

    # def __str__(self):
    #     return f"Bicicle: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)

# b1.buzinar()
# b1.correr()
# b1.parar()

# print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1)