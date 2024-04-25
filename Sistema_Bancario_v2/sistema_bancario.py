import textwrap

def menu():
    menu = """
        [u] Criar Usuário
        [c] Criar Conta
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        [lc] Listar Contas
    => """
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo suficiente para realizar a operação")
    elif excedeu_limite:
        print("Você não tem limite para realizar a transação")
    elif excedeu_saques:
        print("Você excedeu o número de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato

def deposito(saldo, valor, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Não é possível depositar valores negativos")

def extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if(usuario):
        print("\nJá existe um usuário com esse CPF!")
        return
    
    nome_usuario = input("Insira seu nome: ")
    data_de_nascimento_usuario = input("Insira sua data de nascimento (dd-mm-aaaa): ")
    cpf_usuario = input("Insira seu CPF (somente números): ")
    endereco_usuario = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")
    usuarios.append({"Nome": nome_usuario, "Data de Nascimento": data_de_nascimento_usuario, "CPF": cpf_usuario, "Endereço": endereco_usuario})

    print("=== Usuário criado com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)
        if opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                listar_contas=LIMITE_SAQUES
            )
        
        elif opcao == "e":
            extrato(saldo, extrato=extrato)

        elif opcao == "lc":
            listar_contas(contas)

        elif  opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor, selecione novamente a operação desejada.")

main()