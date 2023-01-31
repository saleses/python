## Trabalhando com módulos e pacotes

## 1. Módulo random
'''
O que são módulos? 
- Em Python, módulo é um arquivo contendo definições e comandos para serem utilizados em outros programas.
- Há diversos módulos que fazem parte da biblioteca padrão
- são assim definidos para reutilização e simplificação dos códigos

Módulo Random
- possui várias funções para geração de números pseudo-aleatórios

Pacotes (bibliotecas)
- pacotes é outro tipo de módulo que contêm um conjunto de módulos
'''

# Utilização de módulos ou funções

# Forma 1

import random   # importação de todo módulo random (não recomendado)

'''
random() -> gera um vaçpr real pseudo-aleatório entre 0 e 1

Observação: 
ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades
que estiverem dentro do módulo ficarão disponíveis (em memória). Caso você saiba quais funções
você precisa utilizar deste módulo, então esta não seria a forma ideal de utilizar. 
'''

print(random.random())

'''
Veja que para a utilizar a função random() do pacote random, nós colocamos o nome do pacote e o
nome da função, separados por ponto. 

Obs.: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() 
é apenas uma função dentro do módulo random
'''

# Forma 2 - importação de uma função específica do módulo

from random import random    # especificação da função random do módulo random

'''
Obs.: repare que na declaração da função random, não há parênteses '()'. Estes são usada na hora de 
chamar a função
'''

# Exemplo da forma recomendada
for i in range(10):
    print(random())      # muito utilizado em IA


# Função uniform() -> gera um valor real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # o último valor, neste caso o 7, nunca será atingido

# Função randint() -> gera valores INTEIROS pseudo-aleatórios entre os valores estabelecidos

from random import randint

# gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')    # começa em 1 e vai até 60

# choice() -> mostra um valor aleatório de um iterável

from random import choice    # importa a função choice do módulo random

jogadas = ['pedra', 'papel', 'tesoura']    # tupla de opções usadas pela função choice()

print(choice(jogadas))

print(choice('Letras deste iteravel'))     # funciona também neste caso


# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)    # embaralha
shuffle(cartas)  # desembaralha
print(cartas)    # embaralha

print(cartas.pop())  # retira a última carta caso eu precise remover a útlima carta

## 2. Módulos Built-in

'''
Módulos built-in são módulos integrados. Já estão instalados no Python
- os módulos built-in não são carregados de imediato apesar de estarem instalados. Precisa do import

URL ->  https://docs.python.org/3/py-modindex.html -> global module index  (listas os módulos built-in instalados)
'''

# Utilizando alias (apelidos) para módulos/funções
import random as rdm  # criação de alias rdm para função random

print(rdm.random())   # Atenção: não irá funcionar com o nome padrão ao criar o alias

# Importação de todas funções de um módulo utilizando o asterisco (*)

from random import *
print(random())   # repare que não foi necessário descrever o nome do módulos


# Apelidando a função e não o módulo
form random import randint as rdi, random as rdm  # apelido para função ou mais de uma função

print(rdi(5, 89))
print(rdm())

# Costuma-se utilizar tuple para colocar múltiplos imports de um mesmo módulo. Formato usual
from random import (
        random,
        randint,
        shuffle,
        choice
)

print(random())
print(randint(3, 7))

lista = ['Luke', 'Skywalker', 'Jedi']
shuffle(lista)
print(lista)

print(choice('Artificial'))

