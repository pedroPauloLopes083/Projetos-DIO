import textwrap

def menu():
    menu = """\n
    ########### MENU ###########

    [1] Depositar
    [2] Sacar
    [3] Exibir extrato bancário
    [4] Nova conta
    [5] Listar contas do usuário
    [6] Novo usuário
    [0] Sair

    ############################

"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
        if valor_deposito < 0:
            print("Valor inválido. O valor do depósito deve ser um número inteiro positivo.")
        elif valor_deposito == 0:
            print("Operação de depósito cancelada.")
        elif valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou. O valor informado é inválido. Tente novamente.")
        
        return saldo, extrato

def sacar(saldo, valor_saque, extrato, limite, numero_saques, limite_diario_saques):
    if valor_saque < 0:
        print("Valor inválido. O valor do saque deve ser um número inteiro positivo.")
    elif valor_saque > saldo:
        print("Saldo Insuficiente.")
    elif valor_saque > limite:
        print("O valor do saque excede o limite diário permitido.")
    elif numero_saques >= limite_diario_saques:
        print("Limite diário de saques excedido. Tente novamente amanhã.")
    elif valor_saque == 0:
        print("Operação de saque cancelada.")
    elif valor_saque > 0:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou. O valor informado é inválido. Tente novamente.")
    
    return saldo, extrato

def extrato_bancario(saldo, /, *, extrato):
    print("\n########### EXTRATO ###########")
    print("Não foram registradas movimentações de saque ou depósito." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("#################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do novo usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe um usuário com este CPF. Não é possível criar um novo usuário para este CPF.")
        return

    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua Data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço (Logradouro, Número - Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado. Por favor, tente mais uma vez.")

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
    agencia = "0001"
    limite_diario_saques = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao= menu()

        if opcao == "1":
            print ("Opção escolhida: Depositar")
            valor_deposito = float(input("Digite o valor a ser depositado (ou 0 para cancelar): "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
            
        elif opcao == "2":
            
            print ("Opção escolhida: Sacar")
            valor_saque = float(input("Digite o valor a ser sacado (ou 0 para cancelar): "))

            saldo, extrato = sacar(
                 saldo=saldo,
                 valor_saque=valor_saque,
                 extrato=extrato,
                 limite=limite,
                 limite_diario_saques=limite_diario_saques,
                 numero_saques=numero_saques

            )
        elif opcao == "3":
            print ("Opção escolhida: Exibir extrato bancário")
            extrato_bancario(saldo, extrato=extrato)

        elif opcao == "4":
            print ("Opção escolhida: Nova conta")
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            print ("Opção escolhida: Listar contas do usuário")
            listar_contas(contas)

        elif opcao == "6":
            print ("Opção escolhida: Novo usuário")
            criar_usuario(usuarios)
        
        elif opcao == "0":
            print ("Opção escolhida: Sair")
            break
        
        else:
            print ("""Opção inválida. Por favor, selecione uma opção válida do Menu.
        \n Selecione 1 para Depositar, 2 para Sacar, 3 para Exibir extrato bancário ou 0 para Sair""")



main()