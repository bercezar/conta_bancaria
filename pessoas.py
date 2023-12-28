
import contas

class Pessoa:
    def __init__(self,nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,idade: int):
        self._nome = idade
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self,nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = contas.Conta | None


if __name__ == '__main__':
    c1 = Cliente('Bernardo', 22)
    c1.conta = contas.ContaCorrente(123,345,500,0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Gabriela', 24)
    c2.conta = contas.ContaPoupanca(123,345,500)
    print(c2)
    print(c2.conta)
