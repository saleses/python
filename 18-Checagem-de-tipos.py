# CHECAGEM DE TIPO
'''
1. Tipagem dinâmica x Tipagem estática
- PEP 484

2. Duck Typing (Tipagem Pato) -> nível avançado


3. Type Hinting (Nível avançado de codificação em Python)


4. Checagem de Tipos com MyPy
- auxilia na checagem dos tipagem do código
- inicialmente, surgiu para ser uma linguagem de programação. Depois virou checagem de tipagem python

5. Tipos em comentários

- é a declaração de um tipo dentro de um comentário
- verifica pelo Mypy
- Atenção: o mais recomendado é a utilização do Type Hinting
- usa-se Type Hiting ou Tipos em comentários e nunca os dois


'''

# Type Hiting (importante entender conceito: estudar)
# Exemplo 1
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Antonio'))


# Exemplo 2
def cabecalho(texto: str, alinhamento: bool = True) -> str:     # recebe str e booleano e retorna string
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')  # Centraliza o texto com um total de 50 caracteres contando o espaço dentro das aspas.


print(cabecalho('lord of the ring'))

print(cabecalho('lord of the ring', alinhamento=False))

# Não é a melhor prática (o código não falará nada mas o código esperava receber boolean e não string)
print(cabecalho('lord of the ring', alinhamento='Legal'))


# Checagem de tipos com MyPy
# mypy-lang.org

# ATENÇÃO: como usar o MyPy
# install: pip install mypy
#
# Usando o código acima, basta sair do arquivo de código e verificar com o comando abaixo: 
# mypy nome_codigo.py
# Obs.: só faz sentido usar o mypy com a utilização do Type Hiting
# Python é de tipagem dinâmica, porém é importante usar esse recurso. Apesar de queda de performance (no que achar válido)
# Prós e contras do Type Hiting
'''
Pró
- encontrar erros do código
- mypy: faz checaagem do código antes de executar
- melhora a documentação do código
- melhora a utilização das IDE's

Contras
- a partir do python3.7
- queda da performance

'''

# Fazendo uso de anotations
'''
- auxilia na utilização do Type Hiting
- são as anotações do tipo de declaração (Exemplo do código acima são: str, bool, ...)

Como fazer as anotações(exemplos)

texto: str  # correto
texto:str   # incorreto
texto : str # incorreto

...) -> str # correto
...) ->str  # incorreto
...)->str   # incorreto


'''
# Exemplo 1 -> apenas para entender o __annotations__
import math

def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circunferencia.__annotations__)  # Na execução será impresso os anotations do código (auxílio)


# Declaração de variáveis (nível avançado)
# Exemplos:
nome: str = 'Return of the king'
peso: float = 3.0
ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)  # Trás os tipos declarados acima


# Exemplo: utilização na orientação a objeto
class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade 
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'

p = Pessoa(nome='Two Towers', idade=74, peso=85.8)

print(p.__dict__)

print(p.__annotations__)  # Não há annotations nos objetos somente nos métodos 

print(p.andar.__annotations__)  # Há anotações no método andar 

print(p.__init__.__annotations__) # Há anotações 


# 5. Tipos em comentários
import math

def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circunferencia(8))

print(circunferencia('Texto'))   # Dará erro

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho1(texto=43, alinhamento='texto')

# Funciona - apenas mais uma forma
def cabecalho2(
        texto,  # str
        alinhamento=True  # type:bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)

# 6. Tipos de Python na prática 
# -> são containers: porque possuem vários tipos de dados dentro dele; vários objetos

# Código de prática

nome: list = ['Eu', 'Robo']

versoes: tuple = (3, 4, 7)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)

# Typing
# Especificando cada entrada 
import typing Dict, List, Tuple, Set


nome: List[str] = ['Eu', 'Robo']

versoes: Tuple[int, int, int] = (3, 4, 7)

opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores: Set[int] = {3, 4, 5, 6}

# Código mais avançado
import random

# https://www.alt-codes.net/suit-cards.php
# acrescentar imagens das cartas no espaço de string da variável NAIPES (abrir site, clicar imagem para clipboard e colar)

NAIPES= ''.split()
CARTAS= '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Crua um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acorde com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])   # Distribuição de cartas para cada jogador

# Visualizção da distribuição de cartas
# baralho = criar_baralho()
# print(distribuir_cartas(baralho))

def jogar():
    """Iniciar um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}  # método zip irá distribuir cada carta para um jogador por vez

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

### Ideia do curso
### Criar um novo arquivo com o código acima (jogo) e acrescentar os Type Hiting
### Versão do professor abaixo comentado

import random
'''
from typing import List, Tuple, Set, Dict
'''

# https://www.alt-codes.net/suit-cards.php
# acrescentar imagens das cartas no espaço de string da variável NAIPES (abrir site, clicar imagem para clipboard e colar)

NAIPES= ''.split()
CARTAS= '2 3 4 5 6 7 8 9 10 J Q K A'.split()

'''
CARTA = Tuple[str, str]
BARALHO = List[CARTA]
'''

def criar_baralho(aleatorio:bool = False):  -> BARALHO:   ## ALTERAÇÃO (retorna o baralho)
    """Crua um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:  ## ALTERAÇÃO 
    """Gerencia a mão de cartas de acorde com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])   # Distribuição de cartas para cada jogador

# Visualizção da distribuição de cartas
# baralho = criar_baralho()
# print(distribuir_cartas(baralho))

def jogar()  -> None:   ## ALTERAÇÃO
    """Iniciar um jogo de cartas para 4 jogadores"""
    cartas: BARALHO = criar_baralho(aleatorio=True)   ## ALTERAÇÃO
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}  # método zip irá distribuir cada carta para um jogador por vez    ### ALTERAÇÃO

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)   ## ALTERAÇÃO
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()

