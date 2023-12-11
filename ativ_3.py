class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    
    def obter_saldo(self):
        return self.saldo

# Criar uma instância da classe ContaCorrente
conta = ContaCorrente("12345", "João da Silva")

# Depositar um valor na conta
conta.deposito(1000)

# Realizar um saque
conta.saque(500)

# Alterar o nome do correntista
conta.alterar_nome("João Oliveira")

# Obter o saldo atual
saldo_atual = conta.obter_saldo()

# Exibir informações da conta
print("Número da conta:", conta.numero_conta)
print("Nome do correntista:", conta.nome_correntista)
print("Saldo atual:", saldo_atual)
