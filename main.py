# Importar módulos necessários
import contas
import pessoas
from banco import Banco

# Criar cliente 1
cliente1 = pessoas.Cliente('Bernardo', 22)
conta_corrente1 = contas.ContaCorrente(111, 222, 0, 0)
cliente1.conta = conta_corrente1

# Criar cliente 2
cliente2 = pessoas.Cliente('Gabriela', 24)
conta_poupanca2 = contas.ContaPoupanca(112, 223, 100)
cliente2.conta = conta_poupanca2

# Criar banco
banco = Banco()
banco.clientes.extend([cliente1, cliente2])
banco.contas.extend([conta_corrente1, conta_poupanca2])
banco.agencias.extend([111, 222])

# Autenticar cliente 1 e realizar operações
if banco.autenticar(cliente1, conta_corrente1):
    conta_corrente1.depositar(10)
    cliente1.conta.depositar(100)
    print(cliente1.conta)
