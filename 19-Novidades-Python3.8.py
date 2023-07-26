# NOVIDADES PYTHON3.8

# 1. O operador Walrus

'''
- atribuição e retorno de valor em uma única expressão

Sintaxe:
variavel := expressao

'''

# Exemplo 1

# Padrão: apenas atribuição
nome = 'Duas torres'
print(nome)

# com operador Walrus: Atribuição e retorno do valor ao mesmo tempo
print(nome := 'Duas torres')


# Exemplo 2

# Padrão
cesta = []
fruta = input("Informe a fruta: ")
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')

# 1. Operador Walrus: python3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

# 2. Argumentos somente posicionais

'''
Argumentos somente posicionais

Abrir console (terminal)

>>> help(float)
- o método, função, float() apresenta uma barra "/". Ou seja, esssa função somente pode usar posições e não atribuições (ex: float(x='67.3'))

'''
# Exemplo 1
valor = '67.3'
print(float(valor))

# Exemplo 2
def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Sociedade do Anel'))   # Funciona
print(cumprimenta_v1(nome='Duas torres'))    # Funciona


# Exemplo 3 - python3.8: dizendo que é apenas posicional
def cumprimenta_v2(nome, /):    # tudo que estiver antes da barra "/" será apenas posicional
    return f'Olá {nome}'

print(cumprimenta_v2('Sociedade do Anel'))
print(cumprimenta_v2(nome='Duas torres'))   # Não irá funcionar


# Exemplo 4 - python3.8: dizendo que é apenas posicional
def cumprimenta_v3(nome, /, mensagem='Olá'):    # apenas o que estiver antes da barra "/" será apenas posicional
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Sociedade'))
print(cumprimenta_v3(nome='Sociedade', mensagem='Hello'))         # funciona
print(cumprimenta_v3(nome='Duas torres', mensagem='Bem-vinda'))   # funciona


# Exemplo 5 - python3.8: dizendo que é apenas posicional
def cumprimenta_v4(nome, mensagem='Olá', /):    # apenas o que estiver antes da barra "/" será apenas posicional
    return f'{mensagem} {nome}'

print(cumprimenta_v4('Sociedade'))
print(cumprimenta_v4(nome='Sociedade', 'Bem-vinda'))          # funciona
print(cumprimenta_v4(nome='Duas torres', mensagem='Hello'))   # Não funciona, tudo após a barra é apenas posicional

# ATENÇÃO: da mesma forma que podemos deixar tudo apenas posicional, podemos OBRIGAR a informação de parâmetro


# Exemplo 6 - python3.8: Obrigatoriedade de informação de parâmetro
def cumprimenta_v5(*, nome):    # todo parâmetro após o asterisco DEVERÃO ser informados
    return f'Ola {nome}'

print(cumprimenta_v5(nome='Sociedade'))    # funciona
print(cumprimenta_v5('Sociedade')          # não funciona


# Exemplo 7 - 
def cumprimentar_v6(nome, /, mensagem1='Olá', *,  mensagem2):
    return f'{Mensagem} {nome} {mensagem2}'

print(cumprimentar_v6('Retorno do rei: ', mensagem1='Terceira parte', mensagem2=' do livro'))   # informar
print(cumprimentar_v6('Retorno do rei: ', mensagem2='última parte'))                            # informar
print(cumprimentar_v6('Retorno do rei: ', 'Autor', 'Tolkien'))                                  # último parâmetro com erro (não informou)


# 3. Tipos de dados mais precisos

'''
Tipos de dados estudados
- int, str, float, List, Set, Dict, etc

Tipagem de dados mais precisos
- Literal type
- Union
- Final
- Type dictiionaries
- Protocols


'''
# Exemplo 1
# Python é de tipagem dinâmica: não estará preso a declaração do tipo de variável 
def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))           # retorna 16
print(dobro('Senhor'))    # retorna SenhorSenhor


# Tipagem precisa Literal type
from typing import Literal

# Função padrão
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:    # um ou outro e não os dois
    pass


# Outro exemplo: sem operação Literal type (mypy não retorna erros)
def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')    # "!r" irá destacar a operação inválida atribuída ao valor


calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
calcula_v1('*', 6, 4)    # operação inválida


# Exemplo: com Literal Type (mypy retorna erros)
def calcula_v1(operacao: Literal['+', '-'], num1: int, num2: int) -> None:   # auxilia mais na checagem do que na utilização do código
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')    # "!r" irá destacar a operação inválida atribuída ao valor


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
calcula_v1('*', 3, 5)    # operação inválida


# Union
# necessidade de retorna em uma função um tipo ou outro de dado

# Exemplos: 
from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:    # retorno do tipo str ou int
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado

# Final
from typing import Final


# Exemplo 1:
NOME: Final = 'Aragorn'

print(NOME)

NOME= 'Senhor dos Anéis'

print(NOME)


# Exemplo 2:
@final          # decorando classes
class Pessoa:
    pass

class Estudante(Pessoa):        # não pode acontecer isso. Herdar pessoa pelo fato dela ser final
    pass

    @final       # decorando métodos (mesmo caso da classe estudante. Não poderia sobrescrever???)
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')


# Typed Dictionaries (tradução: dicionário tipado)

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


automacao = CursoPython(versao='3.8.5', atualizacao=2023)

print(automacao)


outro = CursoPython(algo='vai', coisa=True)

print(outro)   # ocorrerá erros devido os tipos declarados no objeto 'outro'


# Protocol - o que é importa são os atributos ou métodos. O objeto não importa

from typing import Protocol

class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


    def __init(self):


v1 = Venda()


estudar(v1)


# 4. Debugger mais simples com f-string

# Exemplo 1: sem f-string

def multiplicar(num1: float, num2: float)  -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)

print(f'O resultado é {resultado}')

print(f'O resultado é multiplicar(9, 4):.2f')    # .2f -> retorna apenas duas casas decimais

print(f'{(media := 8 / 2)} é a metade de {media * 2}')


# Exemplo 2: sem e com f-string

livro: str = "Sociedade do Anel"

print(f"livro='{livro}'")    # sem f-string

print(f'{livro=}')            # com f-string

print(f'{livro.upper()[::-1] = }')  # no debugger, é mostrado o que foi pedido e o resultado


# 5. Conselho diretor do Python

'''
- VER MATERIAL DE APOIO
'''

# 6. Metadata

'''
O que é metadata (metadados)?
- dados internos


'''

# Exemplo 1
from importlib import metadata

print(metadata.version('pip'))

metadata_pip = metadata.metadata('pip')

print(list(metadados_pip))

print(metadados_pip['Project-URL'])


# Exemplo 2: quantos arquivos no pip
print(len(metadata.files('pip')))

print(metada.requires('django'))    # Mostra o que é requerido para a instalação de um software


# 7. Funções matemáticas e estatísticas

'''
math.prod -> retorna o produto de um container numérico

'''
import math

# Exemplo 1
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = [2, 3, 6, 8]
nuns_v1 = [2, 3, 6, 8]

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

"""
2 * 3 * 6 * 8 -> 288
"""

# Exemplo 2: cálculo da raiz quadrada com resultado inteiro, real, apenas parte inteira e real respectivamente
# math.isqrt (retorna a parte inteira da raiz quadrada de um número)
# math.sqrt (retorna o valor real)

print(math.isqrt(9))      # resultado: 3
print(math.sqrt(9))       # resultado: 3.0
print(math.isqrt(17))     # resultado: 4
print(math.sqrt(17))      # resultado: 4.123105617661


# math.dist (retorna a distãncia euclidiana entre dois pontos, 3D ou 2D)
# Exemplos abaixo são passados containers (tanto faz se é lista ou tupla)

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# math.hypot - retorna a hipotenusa, ou norma Euclidiana
print(math.hypot(*p3d1))   # o asterisco descompactar a lista passando apenas os valores
print(math.hypot(*p2d1))


# Estatística
# statistics.fmean - calcula a média de números reais

valores_reais = [1.45, 6.789, 3.45, 89.98765]
varlores_inteiros = [1, 6, 3, 89]             # mesmo sendo inteiros, serão passados os números em reais

# statistics.geometric_mean - calcula média geométrica de números reais
valores_reais = [1.45, 6.789, 3.45, 89.98765]
varlores_inteiros = [1, 6, 3, 89]          

# statistic.multimode = retorna o valor mais frequente em uma sequência

seq1 = 'Retorno do rei'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]


print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))


# 8. Alertas sobre sintaxes perigosas
'''
Sintaxe warning
- no Python3.8 a informação é melhorada com a Sintaxe Warning. Informando como, talvez, deveria ser o código
'''

# 9. Optimizações
'''
- basicamente trata de melhoria no gerenciamento de uso de memória
'''

