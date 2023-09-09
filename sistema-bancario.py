global saldo
global total_saque_diario
global numero_saques_diarios

transacoes = []
numero_saques = 0

VALOR_LIMITE_SAQUES = 500
NUM_LIMITE_SAQUES = 2

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        transacoes.append(f'Depósito: +{valor: .2f}')
        print(f'Depósito de R${valor: .2f} realizado com sucesso.')
    else:
        print('Valor de depósito inválido.')

def extrato():
    print(f'=================')
    print(f'==== Extrato ====')
    print(f'=================')
    print('Transações:')
    for transacao in transacoes:
        print(transacao)
    print(f'Saldo: R${saldo: .2f}')

def sacar(valor):
    global saldo
    global total_saque_diario
    global numero_saques_diarios

    if valor <= 0: 
        print(f'Valor do saque deve ser maior que zero.')
        return
    
    if valor > saldo:
        print(f'Valor do saque deve ser menor ou igual ao saldo.')
        return
    
    if numero_saques_diarios > NUM_LIMITE_SAQUES:
        print(f'Número de saques diarios excedido.')
        return
    
    if (valor + total_saque_diario) > VALOR_LIMITE_SAQUES:
        print(f'Valor limite para saque diario excedido.')
        return
        
    total_saque_diario += valor
    numero_saques_diarios += 1
    saldo -= valor
    transacoes.append(f'Saque: -{valor}')
    print(f'Saque de R${valor} realizado com sucesso.')
    

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """



saldo = 0
total_saque_diario = 0
numero_saques_diarios = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        extrato()   

    elif opcao =="q":
          break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

      
#     if valor > 0:
#           saldo += valor
#           extrato += f'Deposito: R$ {valor: .2f}\n'
#     else:
#           print("Operação falhou! O valor informado é inválido. Tente novamente!")

#     if opcao == 's':

#         valor = float(input("Informe o valor do saque: "))
# ,
#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES
      
#     if excedeu_saldo:
#         print("Operação falhou! Você não possui saldo sufuciente.")

#     elif excedeu_limite:
#         print("Operação falhou! O valor do saque excedeu o limite.")
      
#     elif excedeu_saques:
#         print("Operação falhou! Número de saques foi excedido.")

#     elif valor > 0:
#         saldo -= valor

#         extrato += f'Saque: R$ {valor: .2f}\n'

#         numero_saques += 1

    # else: 
    #     print("Operação falhou! O valor informado é inválido.")

    # if opcao == "e":
    #     transacoes
    #     print("\n=============EXTRATO==============")
    #     print("Não foram realizadas movimentações." if not extrato else extrato)
    #     print(f"\nSaldo: R$ {saldo: .2f}")
    #     print("===============================")        

    # elif opcao =="q":
    #       break
    # else:
    #     print("Operação inválida, por favor selecione novamente a operação desejada.")