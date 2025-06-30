menu = """
=======Operações Disponiveis======    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

Digite a opção desejada
=================================
"""

saldo = 0
limite = 500
extrato_depositos = []
extrato_saques = []
numero_saques = len(extrato_saques)
LIMITE_SAQUES = 3


while True:


    opcao = input(menu)

    if opcao == "d":
        adicionar_dinheiro = float(input("Qual o valor que deseja depostiar? "))
        saldo += adicionar_dinheiro
        saldo_atual = saldo
        extrato_depositos.append(adicionar_dinheiro)
        print(f"Deposito realizado com sucesso. Seu saldo é R$ {saldo_atual}.")
        print(f"Extrato dos depositos realizados: {extrato_depositos}")
        

    elif opcao == "s":
        sacando_dinheiro = float(input("Qual o valor que deseja sacar? "))
        if sacando_dinheiro <= 500.00:
            if numero_saques < LIMITE_SAQUES:
                numero_saques += 1
                resta = saldo_atual - sacando_dinheiro
                print(f"Saque realizado com sucesso. O valor do saque foi R$ {sacando_dinheiro}")
                print(f"O saldo remanescente é R$ {resta}.")
                print(f"Limite de saques: {numero_saques}/3")

            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou. Você atingiu o número máximo de 3 saques diários.")

        elif saldo_atual < sacando_dinheiro:
            print("Não será possível sacar o dinheiro por falta de saldo")
        else:
            print("Limite maximo de saque permitido R$ 500.00. Por favor, digite outro valor.")
        
        if sacando_dinheiro <= 500.00 and numero_saques < LIMITE_SAQUES:
            extrato_saques.append(sacando_dinheiro)
            print(f"Extrato dos saques realizados: {extrato_saques}")
        else:
            pass

        


    elif opcao == "e":
        if not extrato_saques and not extrato_depositos:
            print("Não foram realizados movimentações.")
            #print(f"Lista de todos os saques {extrato_saques}")
        else:
            print(f"Lista de todos os saques {extrato_saques}")
            print(f"Lista de todos os depositos {extrato_depositos}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
