nome = "Caixa Eletrônico".center(20, "=")
menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""

extrato = ""

saldo = 0
deposito = 0
saque = 0

saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3

while True:    
    print(nome, menu, sep="\n")
    opcao = input("Digite a opção: ")

    if opcao == "d":
        deposito = int(input("\nDigite o valor de depósito: R$ "))

        if (deposito > 0):
            saldo += deposito
            extrato += f"\n- Depósito realizado no valor de R$ {deposito:.2f}\n"
            print("\n= Depósito realizado com sucesso!")            
        else:
            print("\n Erro ao realizar o depósito!")

        input("\nConfirme para continuar")

    elif opcao == "s":
        if (saques_realizados == LIMITE_SAQUES_DIARIOS):
            print("\nLimite de saques diários atingidos!")
            input("\nConfirme para continuar")
            continue

        print(f"\n* Total de saques disponiveis [{3 - saques_realizados}]")
        print("\n* Limite máximo de R$ 500,00 por saque\n")
        saque = int(input("Digite o valor que deseja sacar: R$ "))
        if (saque > 500):
            print("\n    O valor do saque não pode exceder R$ 500,00!")
        elif (saque < 1):
            print("\n    O valor do saque não pode ser menor que R$ 1,00!")
        elif (saque <= saldo):
            saldo -= saque
            saques_realizados += 1
            extrato += f"\n- Saque realizado no valor de R$ {saque:.2f}\n"
            print("\n= Saque realizado com sucesso!")            
        else:
            print("\n    Saldo insuficiente para realizar o saque")

        input("\nConfirme para continuar")

    elif opcao == "e":        
        print("Extrato".center(20, "="), extrato, sep="\n")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        input("Confirme para continuar")

    elif opcao == "q":
        break

    else:
        print("Opção inválida!")