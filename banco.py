import contas
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None
            ):
        #Posso criar um banco sem agências, sem cliente e sem contas
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    def checar_agencia(self, conta):
        if conta.agencia not in self.agencias:
            print('_checa_agencia', False)
            return False
        print('_checa_agencia', True)
        return True

    def checar_conta(self,conta):
        if conta not in self.agencias:
            print('_checa_conta', False)
            return False
        print('_checa_conta', True)
        return True
    
    def checar_cliente(self,cliente):
        if cliente not in self.clientes:
            print('_checa_cliente', False)
            return False
        print('_checa_cliente', True)
        return True

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
    
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self.checar_agencia(conta) and \
        self.checar_cliente(cliente) and \
        self.checar_conta(conta) and \
        self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.agencias!r}, {self.clientes!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1 = pessoas.Cliente('Bernardo', 22)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Gabriela', 24)
    cc2 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cc2
    banco = Banco()
    banco.clientes.extend([c1,c2])
    banco.contas.extend([cc1,cc2])
    banco.agencias.extend([111,222])
    

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
