from datetime import datetime
class Caixa:
    def __init__(self, nome, conta, saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
        self.operacao = []

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            data = datetime.now()
            self.operacao.append(["SAQUE: ", valor, data.ctime()])
            print(f'Saque de {valor} realizado com sucesso.')
        else:
            print('Saldo insulficiente.')
        
    def deposito(self, valor):
        self.saldo += valor
        data = datetime.now()
        self.operacao.append(["DEPÓSITO: ", valor, data.ctime()])
        print(f'Depósito de {valor} realizado com sucesso.')

    def extrato(self):
        print(f'CC N° {self.conta} {self.nome.title()}')
        for i in self.operacao:
            print(i[0], i[1], '.....Data: ', i[2])
        print(f'\nSaldo total: {self.saldo}')

    def escolha(self, acao):
        if acao == 'saque':
            entrada = float(input('Qual o valor: '))
            x.saque(entrada)
        elif acao == 'deposito':
            entrada = float(input('Qual o valor: '))
            x.deposito(entrada)
        elif acao == 'extrato':
            x.extrato()


x = Caixa('fernando', 1234, 500)
while True:
    print('>>>SAQUE\n>>>DEPOSITO\n>>>EXTRATO')
    operacao = str(input('Digite o operação: ')).lower().strip()
    if operacao == 'sair':
        break
    else:
        x.escolha(operacao)
        