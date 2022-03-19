from tatu import Cliente
from tatu import Conta

joão = Cliente('João da Silva', '9999999999999')
maria = Cliente('Maria da Silva', '028402830284')
print('Nome: %s. Telefone: %s.' %(joao.nome, joao.telefone))
print('Nome: %s. Telefone %s.' %(maria.nome, maria.telefone))

conta1 = Conta([joão], 1, 1000)
conta2 = Conta([maria, joão], 2 , 500)
conta1.resumo()
conta2.resumo()
