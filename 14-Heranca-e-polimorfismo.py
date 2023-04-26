## Herança e Polimorfismo
'''
Herança (Inheritance, herança em inglês)

- é a possibilidade de aproveitar código e, também, extender classes.
- com a herança, a partir de uma classe existente, pode-se extender outra classe que paasa a herdar
atributos e métodos da classe herdada.

Exemplo com duas entidades: Cliente e Funcionario

Classe
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

Obs.: abaixo tem-se exemplo de classes Cliente e Funcionarios herdando atributos da classe Pessoa, mais genérica.

Quando uma classe herda de outra classe, a classe herdada é conhecida por: 
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada: 
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

Sobrescrita de método (Overriding)
- ocorre quando reescrevemos/reimplementamos um método presente na super classe
'''
## 1. HERANÇA

# Exemplo de código das entidades acima

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = nome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):    # Recebe como herança os atributos da classe Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(nome, sobrenome, cpf)        # Forma1 de executar a super classe Pessoa (Menor usual)
        self.__renda = renda


class Funcionario(Pessoa):    # Recebe como herança os atributos da classe Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)       # Forma 2 de execução da super Classe Pessoa (Mais usual)
        self.__matricula = matricula

    # Realização de  Overriding method
    def nome_completo(self):
        print(super().nome_completo())    # Acesso a atributo ou método da super classe (Classe Pai)
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula } Nome: {self.__Pessoa__nome}'


cliente1 = Cliente('Geraldo', 'Santo', '123.456.789-00', 6000)
funcionario1 = Funcionario('Arlindo', 'Sales', '987.654.321-00', 1234)

cliente1.nome_completo()
funcionario1.nome_completo()

# Visualização do que está sendo realizado 
print(Cliente1.__dict__)
print(Funcionario1.__dict__)


## 2. PROPRIEDADES
'''
Propriedades (Properties)

Em linguagem de programação como o Java, ao declararmos atributos privados nas classes, 
costumamos a criar métodos públicos para manipulação desses atributos. Esses métodos 
são conhecidos por getters e setters. Os getters retornam o valor do atributo e os setters 
alteram o valor do mesmo. 

# Formato usual da Linguagem Java

class Conta:

    contador = 0    # Atributo de classe

    def __init__(self, titular, saldo, limite):    # método construtor
        self.__numero = Conta.contador + 1         # Atributos de instâncias 
        self.__titular = titular                   # Atributos de instâncias
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Getters e Setters
    # Getters: retorna
    # Setters: altera
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self):
        return self.__limite


conta1 = Conta('Antonio', 3000, 5000)
conta2 = Conta('Barbara', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Forma 1: não é a ideal (acesso a elemento privado deve ser apenas de dentro)
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas é {soma}')

# Forma 2: é o ideal
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')


print(conta1.__dict__)
conta1.set_limite(9999999)   # alterando valor dos atributos
print(conta1.__dict__)
'''

# Forma Pythonica
# Utilização de @property -> por padrão, são getters
# Utilização de @limite -> são os setters

class Conta:

    contador = 0    # Atributo de classe
    
    # Sempre criar os atributos de forma privada
    def __init__(self, titular, saldo, limite):    # método construtor
        self.__numero = Conta.contador + 1         # Atributos de instâncias 
        self.__titular = titular                   # Atributos de instâncias
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # Se necessário de acesso aos atributos privados, usar os @property (apenas acessar) e @limite (alterar atributos)
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    # Criação de função de retorna saldo + limite
    # uma @property que cria uma função
    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Antonio', 3000, 5000)
conta2 = Conta('Barbara', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Forma 1: não é a ideal (acesso a elemento privado deve ser apenas de dentro)
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas é {soma}')

# Forma 2: é o ideal
soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')


print(conta1.__dict__)
conta1.limite = 765434
print(conta1.__dict__)
print(conta1.limite)

# Saída da propriedade que contêm uma função. Não é uma função. É uma propriedade (repare: não tem parênteses após valor_total)
print(conta1.valor_total)
print(conta2.valor_total)


