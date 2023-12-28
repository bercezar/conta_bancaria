from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, agencia: float, conta: float
                 , saldo: float) -> None:
        self.agencia = agencia
        self.num_conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:...
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhar(f'DEPÓSITO -:> R${valor}')
    def detalhar(self, msg) -> None:
        print(f'{msg} \nSeu saldo é de R${self.saldo:.2f} \n')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.num_conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhar(f'SAQUE -:> R${valor}')
            return self.saldo
        
        print('Não foi possível sacar, consulte o seu saldo')
        self.detalhar(f'SAQUE NEGADO (R${valor})')

    

class ContaCorrente(Conta):
        def __init__(self, agencia: float, conta: float,
                      saldo: float, limite=500) -> None:
            super().__init__(agencia, conta, saldo)
            self.limite = limite

        def sacar(self, valor: float) -> float:
            valor_pos_saque = self.saldo - valor 
            limite_max = -self.limite

            if valor_pos_saque >= limite_max:
                self.saldo -= valor
                self.detalhar(f'SAQUE -:> R${valor}')
                return self.saldo
            
            print('Não foi possível sacar o valor desejado')
            print(f'Seu limite é de R${ -self.limite:.2f}')
            self.detalhar(f'SAQUE NEGADO (R${valor})')
        def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.num_conta!r}, {self.saldo!r}, '\
                f'{self.limite!r})'
            return f'{class_name}{attrs}'
 
                    
if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222, 100)
    cp1.depositar(100)
    cp1.sacar(50)
    cc1 = ContaCorrente(111,222, 300)
    cc1.sacar(100)
    cc1.sacar(200)
    cc1.sacar(300)
    cc1.sacar(210)
