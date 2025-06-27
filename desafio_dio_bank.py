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

            # resta = saldo_atual - sacando_dinheiro
            # print(f"Saque realizado com sucesso. O valor do saque foi R$ {sacando_dinheiro}")
            # print(f"O saldo remanescente é R$ {resta}.")
            # print(f"Limite de saques: {numero_saques}/3")

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
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

"""
Deposito - devem ser armazenados em um variavel e exibidos na operação de extrato.
Saque - permitir 3 saques diarios com limite max de R$ 500,00 por saque. Exibir mensagem caso naõ tenha saldo.
Devem sera armazenado e exibidos no extrato.
Extrato - Deve listar todos os depositos e saque. No final deve exibir saldo atual. Se o extrato estiver em branco, 
deve exibir a mensagem-> Não foram realizados movimentações.<- o valor deve ter formato R$ 1500.45
"""