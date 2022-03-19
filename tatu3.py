class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo = 0, limite = 0):
        conta.__init__(self, cliente, numero, saldo)
        self.limite = limite
    def saque(self, valor):
        if sel.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])
