def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo():
    print(f"Olá mundo!")

ola_mundo()