menu = """
    ########### MENU ###########

    [1] Depositar
    [2] Sacar
    [3] Exibir extrato bancário
    [0] Sair

    ############################

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_diario_saques = 3


while True:

    opcao= input(menu)

    if opcao == "1":
        print ("Opção escolhida: Depositar")
        valor_deposito = float(input("Digite o valor a ser depositado (ou 0 para cancelar): "))
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
        
    elif opcao == "2":
        
        print ("Opção escolhida: Sacar")
        valor_saque = float(input("Digite o valor a ser sacado (ou 0 para cancelar): "))
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


    elif opcao == "3":
        print ("Opção escolhida: Exibir extrato bancário")
        print("\n########### EXTRATO ###########")
        print("Não foram registradas movimentações de saque ou depósito." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("#################################")
    
    elif opcao == "0":
        print ("Opção escolhida: Sair")
        break
    
    else:
        print ("""    Opção inválida. Por favor, selecione uma opção válida do Menu.
    Selecione 1 para Depositar, 2 para Sacar, 3 para Exibir extrato bancário ou 0 para Sair""")
