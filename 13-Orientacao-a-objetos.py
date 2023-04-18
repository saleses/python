## Programação Orientada a Objetos (POO)

'''
Paradigmas de programação (metodologia de desenvolvimento de software)
- maneira de pensar o softwares
- quais paradigmas mais utilizados: estruturada, funcional e orientação a objeto
- os paradigmas dependem da linguagem
Exemplo:
- linguagem C: estruturada
- Java: orientação a objeto
- Python: multiparadigma -> estruturada, funcional e orientada a objeto

Objetivo da Orientação a objeto: 
- mapear objetos do mundo real para modelos computacionais

Principais componentes (elementos)
- classe: o modelo do objeto no mundo real representado computacionalmente
- atributos: características de um objeto. Uma classe pode ter nenhum ou vários atributos
- métodos: comportamento do objeto, ações do objetos (Atenção: métodos são as funções. Ou seja, método é uma função dentro de uma classe)
- construtor: é um método especial utilizado para criar objetos de uma determinada classe.
- objeto (ou instâncias): são elementos de um classe. Uma instância de um classe 

'''
# Comparação básica: Estruturada x OO

# Declaração de variável
# 1. Estruturada
nome = 'Bola'
print(type(nome))
numero = 10
print(type(numero))


# 2. Orientação a Objeto
class Produto:      # Criação da classe, modelo para um objeto
    pass            # será visto a frente, apenas para não gerar erro no código
                    # Não há método nem atributo

kimono = Produto()  # construtor padrão da classe produto, método especial para criação do objeto kimono. Repare: produto entre parênteses
print(kimono)       # Por não ter valor, apresentará apenas o espaço reservado em memória do objeto
print(type(kimono)) # Mostra que é uma classe do tipo Produto. Então o objeto é um tipo, instância de classe? 


## 1. Classes
'''
O que são classes?
- são modelos dos objetos do mundo real sendo representados computacionalmente

Classes contêm:
- atributos: representam as características do objeto. OU seja, pelos atributos conseguimos representar computacionalmente os estados do
  objeto. No caso do exemplo abaixo, lâmpada, possivelmente iríamos querer saber se a a lâmpada é 110 ou 220 volts, se é branca, amarela ou 
  outra cor, e etc.

- Mêtodos (funções): representam os comportamentos do objeto. OU seja, as ações que este objeto pode realizar no sistema. No caso da lâmpada,
  um comportamento é ligar e desligar. 

- Definição: class
- em python, é possível ter mais de uma classe em um único arquivo. 

Classes internas:
- int(), list(), set() -> exemplos de uma classe interna. São em minúsculas
- para as classes criadas pelo desenvolvedor, use sempre o padrão CamelCase

Obs.: ao planejar um software e definimos as classes do sistema, chamamo-as de entidades. Ou seja, entidade é uma classe. 
'''
# Exemplo: sistema para automatizar o controle de lâmpadas de uma residência

class Lampada:        # Declaração da classe -> por padrão, o nome da classe inicia com maiúscula em cada palavra (Camel Case)
    pass              # utilizado quando existe um bloco não utilizado


lamp = Lampada()

print(type(lamp))
# Fim do bloco da classe 

## 2. Atributos
'''
Atributos
- representam as caracteríesticas do objeto. 
- representação computacional dos estados de um objeto

Em python, os atributos são divididos em 3 grupos: 
   1. atributos de Instância
   2. atributos de Classes
   3. atributos Dinâmicos

'''
# Atributos de Instâncias
# são atributos declarados dentro do método construtor que é um método especial utilizado para a construção do objeto
# self -> objeto que executa um método (veja-os abaixo). Usualmente, é o primeiro parâmetro

class Lampada:

    def __init__(self, voltagem, cor): # o método __init__ é o construtor da classe
        self.voltagem = voltagem     # declaração de atributos de instância ( __voltagem )
        self.cor = cor               # declaração de atributos da instância ( __cor )
        self.ligada = False          # declaração de atributos da instância ( __ligada )


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

'''
Atributos públicos e atributos privados

Por convenção, todo o atributo de uma classe é público. Ou seja, pode ser acessado em todo o projeto
Caso deseja-se demonstrar que determinado atributo deve ser tratado como privado, ou seja, acessado/utilizado somente dentro da própria classe, utiliza-se duplo underscore " __ " no início do nome. 

Este formato, duplo underscore, é conhecido como Name Mangling. 
'''
class Acesso:

    def __init__(self, email, senha):
        self.email = email           # atributo público
        self.__senha = senha         # atributo privado

    def mostra_senha(self):
        print(self.__senha)           # atributo privado

    def mostra_email(self):
        print(self.email)

'''
Obs.: Lembre-se que a declaração de atributo como público ou privado em Python é apenas uma convenção. Não impede o acesso de atributos
sinalizados como privados fora da classe.
'''
# Exemplo
user = Acesso('user@gmail.com', '123456')

print(user.email)
# print(user.__senha)

print(user._Acesso__senha)    # Temos acesso, ma não deveria fazer este acesso

user.mostra_senha()    # não tem print porque a função, que já está na classe, pede a impressão
user.mostra_email()

'''
Para finalizar, o que significa atributo de instância? 
- significa que para criar instâncias/objetos de uma classe, todas elas terão atributos

'''

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321') 

user1.mostra_email()
user2.mostra_email()


# Atributos de Classes

'''
Cada instãncia com seus valores

Os atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já 
inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe
ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor
para este atributo.

'''

# Refatorar a classe Produto
class Produto:
    
    # Atributo de classe
    imposto = 1.05    # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1              # Atributos de instâncias
        self.nome = nome                            # Atributos de instâncias
        self.descricao = descricao                  # Atributos de instâncias
        self.valor = (valor * Produto.imposto)      # Atributo de classe
        Produto.contador = self.id                  # atributo de classe

p1 = Produto('PlayStation 4', 'Vídeo game', 2300)
p2 = Produto('Xbox S', 'Vídeo game', 4500)

print(p1.valor)    # Acesso possível, mas incorreto de um atributo de classe (pela instância)
print(p2.valor)

# Obs.: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)   # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Atenção.: Em Java, os atributos de classe são chamados no Python de atributos estáticos. 


# Atributos dinâmicos
'''
Atributo de instãncia que pode ser criado em tempo de execução
Obs.: o atributo dinâmico será exclusivo da instância que o criou

'''

p1 = Produto('PlayStation 4', 'Video Game', 2300 )
p2 = Produto('Arroz', 'Mercearia', 5.99 )


# Criando um atributo dinâmico em tempo de execução
p2.peso = '5kg'    # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso} ')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso} ')

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)

## 3. Métodos
'''
Atenção: entender função para estudar métodos

Métodos
- comparando com o paradigma estrutural, seriam as funçóes
- representa os comportamentos do objeto. Ou seja, ações que este objeto pode realizar
- Em python, dividimos os métodos em 2 grupos: 
    - métodos de instância
    - métodos de classe

- O método dunder init, __init__, é um método especial chamado de construtor. Sua função é construir o objeto a partir da classe. 
- todo elemento em python que inicia e finaliza com duplo underline, __nome__, é chamado de dunder (Double Underline)

- os métodos (funções) dunder em python são chamados de métodos mágicos
Obs.1: se aparecer underline apenas no início, não é dunder
Obs.2: por mais que pssamos criar nossas próprias funções utilizando dunder, não é recomendado. Python possuem vários métodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem. Evite ao máximo. 
- métodos são escritos em letras minúsculas. Se for composto, separar com underline
- métodos de classe em python, é conhecido como métodos estáticos em outras linguagem

'''

# 3.1. Métodos de instâncias
'''
obs.: os atributos devem ser criados dentro da classe (self.__cor = cor, por exemplo)
'''

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):  # método __init__ construtor da classe
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def__init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__numero

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto """
        return (self.__valor * (100 - porcentagem)) / 100

# importação da lib passlib
# pip install passlib
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod                   # Decorador: visto anteriormente
    def conta_usuarios(cls):       # cls: é o parâmetro da classe. A própria classe
        print(f'Classe: {cls}')    # Teste
        print(f'TEmos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def__init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha rounds=200000, salt_size=16) 
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    # Criada apenas para exemplo. Além do curso
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):     # Verifica se a senha digitada é igual a do banco de dados
            return True
        return False

# má prática
#    def __correr__(self, metros):    # não é recomendado o desenvolvedor criar métodos dunder
#        print(f'{self.__nome}Estou correndo {metros} metros')


# O produto
p1 = Produto('Playstation 4', 'Video Game', 2300)

# Instânca do método (desconto, acima)
print(p1.desconto(50))    # desconto de 50% de 2300 calculado no método desconto da classe Produto


# Forma errada
print(Produto.desconto(40)) 

# Teste para classe Usuário (senha criptografada)
user1 = Usuario('Antonio', 'Sales', 'ases@hotmail.com', '123456')
user2 = Usuario('Daniel', 'Sales', 'dses@hotmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe o senha: ')
confirma_senha = input('Informe o senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user.__Usuario__senha}')  # Acesso errado



# 3.2. Métodos de classe

user = Usuario('Carlos', 'Augusto', 'caugusto@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()     # Possível, mas incorreta

'''
métodos acima, são métodos públicos. Abaixo, veremos os privados
'''

def __gera_usuario(self):
    return self.__email.split('@')[0]   # retorna o index 0 do email. 


# 3.3. Métodos estáticos

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Thomas', 'Aquino', 'thomas@outlook.com', '123456')

print(user.contador)

print(user.definicao())

# 4. Objetos

'''
Objetos são instâncias da classe. Ou seja, após o mapeamento do objeto para o mundo real para sua representação computacional, devemos poder scriar quantos objetos forem necessários. Podemos pensar nos objetos/instãncias de uma classe como variáveis do tipo definido na classe. 

'''

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente(self, nome, cpf):
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente.__Cliente.__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Objetos / Instâncias de uma classe
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()   # Liga a lâmpada

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Geraldo', 'Antonio', 'dan@gmail.com', '123456')

cli1 = Cliente('Fulano de tal', '123.456.789-99')  # Objeto do tipo Cliente

cc = ContaCorrente(5000, 10000, cli1)

print(cc.mostra_cliente())

cc.__ContaCorrente__cliente.diz()   # Forma errada, mas funcionou. Má prática? 


# 5. Abstração e Encapsulamento

'''
- O grande objetivo da POO é encapsular o código dentro de um grupo lógico e hierárquico utilizando classes. 

Encapsular: cápsula

            classe
-------------------------------
/                             /
/      Atributos e métodos    /
/                             /
-------------------------------

# Relembrando Atributos/Métodos privados em Python
- Pense que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e mum método privado chamado __falar()
- Esses elementos privados só devem/deveriam ser acessados dentro das classes. Mas Python não bloqueia este acesso fora da classe.
Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos privados, conforme:

_Classe_elemento

Exemplo: Acessando elementos privados fora da classe:
    instancia._Pessoa_nome
    instancia._Pessoa_falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário. 

'''

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador    # Atributos, este e os abaixos, são públicos. Para ser privados (__underline). Daí estarão encapsulados 
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador + 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor:
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve er positivo')

    def transferir(self, valor, conta_destino):
        # 1 - remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10    # Taxa de transferência paga por quem realizou a transferência

        # 2 - adicionar o valor na conta de destino
        conta_destino.__saldo += valor

# Testando
conta1 = Conta('Tony', 150.00, 1500)
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# Objetos que alteram os valores dos atributos (sem segurança). Por quê? Porque a declaração dos atributos são públicos
# Os dados não estão encapsulados. 
conta1.numero = 42
conta1.titular = 'Titio'
conta1.saldo = 99999999999
conta1.limite = 99999999999999999999

# Atenção: em python, não há bloqueio para acesso aos dados

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(200)
print(conta1.__dict__)


conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()


