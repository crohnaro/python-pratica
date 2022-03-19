from tatu2 import Cliente
from tatu2 import Conta
joao = Cliente('Joao da silva', '99999999')
maria = Cliente('Maria da Silva', '9999999')
conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao],2 ,500)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.extrato()
conta2.estrato()
