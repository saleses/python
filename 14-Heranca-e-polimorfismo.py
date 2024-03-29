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

## 3. Método super()

'''
Método super()
- refere-se a super classe

'''
class Animal:

    def __init__(self, nome, especie):
        self,__nome = nome
        self,__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):    # subclasse ou classe filha da super classe Animal

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)  # funciona, mas não é recomendado
        super().__init__(nome, especie)         # boa prática
        super().faz_som('auauauauauaua')        # boa prática
        self.__raca = raca

felix = Gato('Felix', 'Felino', 'Angorá')    # Instância do objeto felix
felix.faz_som('miau')


## 4. Herança múltipla
'''
Herança múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

A herança múltipla pode ser feita de duas formas:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;
'''

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):    # herda das classes Base1, Base2 e Base3
    pass

# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3)   # herda indiretamente a Base2 e Base1
    pass


'''
Obs.: não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos
e métodos da super classe
'''

# Exemplo 3

class Animal:                     # Classe base

    def __init__(self, nome):     # método construtor
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):            # herda da classe Animal

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):            # Herda da classe Animal

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):  # Herança Múltipla Indireta: herda de Animal através de Terrestre e Aquatico

    def __init__(self, nome):
        super().__init__(nome)

# Teste
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Method Resolution Order - MRO -> tem relação com a ordem declarada na classe com Herança múltipla


# Objeto é instãncia de...
print(f'Tux é instância de Pinguim? {isinstance(tux, Pinguim)}')       # a função/método isinstance retorna True ou False
print(f'Tux é instância de Aquático? {isinstance(tux, Aquático)}')
print(f'Tux é instância de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instância de object? {isinstance(tux, object)}')i      # por padrão uma classe ao ser criada, herda o tipo object

'''
Exemplo: 
class Pessoa(object):   # é a mesma coisa que class Pessoa():
    pass

Todas saídas serão verdadeiras (True) porque existe heranças
'''

# 5. MRO - Method Resolution Order

"""
MRO é a ordem de execução dos métodos. Quem será executado primeiro

Em python, pode-se conferir a ordem de execução de três formas:
    1) via propriedade da classe __mro__
    2) via método mro()
    3) via help

Terminal:
# >>> from mro import Pinguim  (importar para testar as linhas abaixo)
# >>> Pinguim.__mro__   (vai mostrar a ordem)
# >>> Pinguim.mro()     (vai mostrar a ordem)
# >>> help(Pinguim)

"""

# Comentário abaixo é o exemplo acima modificado para explicação de MRO

"""
# Exemplo 3

class Animal:                     # Classe base

    def __init__(self, nome):     # método construtor
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):            # herda da classe Animal

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):            # Herda da classe Animal

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):  # Herança Múltipla Indireta: herda de Animal através de Terrestre e Aquatico

    def __init__(self, nome):
        super().__init__(nome)

# Teste
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar()
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.cumprimentar())  # Method Resolution Order - MRO -> tem relação com a ordem declarada na classe com Herança múltipla


Resultado: altera a ordem

# Pinguim(Aquático, Terrestre)
Saída: Eu sou Tux da terra
"""

# 6. POLIMORFISMO

'''
Poli: Muitas, Mofis: Formas
- são os objetos com múltiplas formas

Quando se reimplementa um método presente na classe pai em classes filhas estamos realizando uma sobrescrta de método (Overriding)
- o overriding é a melhor representação do polimorfismo

'''

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método')

    def comer(self):
        print('f{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__Animal__nome} fala wau wau')     # Cada animal fala de um jeito. Uma característica do polimorfismo


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__Animal__nome} fala miau!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.__Animal__nome}   ')

# Testes
felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Cachorro('Pluto')
mickey.comer()
mickey.falar()


# 7. Métodos mágicos

"""
Métodos mágicos são todos os métodos que utilizam dunder. (Dunder: Double Underscore)

Dunder init -> __init__

Dunder repre -> Representação de objeto


"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):   # método da classe Object. Faz a representação de um objeto -> objeto Livro alocado em um endereço de memória
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):    # Aparentemente igual. Tem preferência entre os métodos. Este será utilizado
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livros1 = Livro('Python Rocks!', 'Aula Python', 400)
livros2 = Livro('AI with Python', 'Aula Python', 350)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
print(livro1 * 3)


# Deleção de variáveis da memória
'''
No terminal: 
# >>> nome = Antonio
# >>> print(nome)
# >>> del nome

'''

