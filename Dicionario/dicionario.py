pessoa = {"nome": "Lucas", "idade": 30}
print(pessoa)

pessoa = dict(nome="Lucas", idade=30)
print(pessoa)

pessoa["telefone"] = "3333-1234"
print(pessoa)

# Acessando os valores
dados = {"nome":"Lucas", "idade": 30, "telefone": "3333-1234"}
print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

# Acessando e sobrescrevendo
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"
print(dados)