VALOR_LIMITE_SAQUES = 500
NUM_LIMITE_SAQUES = 2


class Banco:
    def __init__(self):
        self.lista_conta = []
        self.numero_conta = 0

    def getNumeroConta(self):
        self.numero_conta += 1
        return self.numero_conta
    
    def listarContas(self):
        print(f'=========================')
        print(f'==== Lista de Contas ====')
        print(f'=========================')
        print('Transações:')
        for conta in self.lista_conta:
            print(f'Número da conta: { conta.numero_conta } Titular: { conta.titular }')

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0, ):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []
        self.numero_saques_diarios = 0
        self.total_saque_diario = 0
        self.ultima_data_saque = None
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f'Depósito: +{valor: .2f}')
            print(f'Depósito de R${valor: .2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor <= 0: 
            print(f'Valor do saque deve ser maior que zero.')
            return
        
        if valor > self.saldo:
            print(f'Valor do saque deve ser menor ou igual ao saldo.')
            return
        
        if self.numero_saques_diarios > NUM_LIMITE_SAQUES:
            print(f'Número de saques diarios excedido.')
            return
        
        if (valor + self.total_saque_diario) > VALOR_LIMITE_SAQUES:
            print(f'Valor limite para saque diario excedido.')
            return
            
        self.total_saque_diario += valor
        self.numero_saques_diarios += 1
        self.saldo -= valor
        self.transacoes.append(f'Saque: -{valor}')
        print(f'Saque de R${valor} realizado com sucesso.')
        
    def extrato(self):
        print(f'=================')
        print(f'==== Extrato ====')
        print(f'=================')
        print('Transações:')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Saldo: R${self.saldo: .2f}')


menu = """

[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Contas
[gc] Get Conta    ---> a ideia é localizar uma conta para deposito, saque e etc...
[sc] Sair Conta   ---> a ideia é sair da conta selecionada e poder selecionar outra na sequencia
[q] Quit

=> """



# saldo = 0
# total_saque_diario = 0
# numero_saques_diarios = 0

def main():
    print("abrindo sistema bancario...")

    meu_banco = Banco()

    while True:
        opcao = input(menu)

        

        if opcao == "c":
            numero_conta = meu_banco.getNumeroConta()
            titular = float(input("Informe o nome do titular: "))
            valor = float(input("Informe o valor do depósito inicial: "))
            minha_conta = ContaBancaria(numero_conta, titular, valor)




        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            minha_conta.depositar(valor)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            minha_conta.sacar(valor)

        elif opcao == "e":
            minha_conta.extrato()   

        elif opcao == "l":
            meu_banco.listarContas()   

        elif opcao =="q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

  