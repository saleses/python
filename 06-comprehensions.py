# COMPREHENSIONS PYTHON

'''
1. List_comprehension
"""
List comprehension

- Utilizando List Comprehensions pode-se gerar novas listas com dados processados a partir de outro interável

# Sintaxe: 
[ dadofor dado in iterável ]

"""

# Exemplos

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros] # para cada número na lista de números, multiplique por 10 e coloque na lista 'res'
print(res)

"""
Entendendo a expressão: 
- primeira parte: for numero in numeros
- segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

List Comprehensions versus Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numero_dobrados.append(numero_dobrado)

print(numeros_dobrados)

### List comprehensions
print([numero * 2 for numero in numeros])

'''
Em uma linha de código, a list comprehension faz o que o loop usa cerca de quatro
'''

# Outros exemplos

# 1
nome = 'Geek University'
print([letra.upper() for letra in nome ])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# 3
print( [numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

'''
Pode-se adicionar estruturas condicionais lógicas às nossas List Comprehension
'''
# Exemplos

# 6 
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar código acima

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]  # A negação de False é True

# Qualquer número impar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]  # Não precisa negar para que seja True

# 7
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

'''
2. Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) posseuem uma estrutura de dados chamados de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python temos listas
numeros = [1, 'b', 3.234, True, 5]

Obs.: importante para Data Science
'''

# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3
print(listas)
print(type(listas))

# Como acessar os dados? 
print(listas[0][1])  # saída é o número 2
print(listas[2][1])  # saída é o número 8

# Iteração com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# Lista aninhada em  List comprehension 
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerar um tabuleiro /matrix 3 x 3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerar jogadas para o jogo da velha
velha = [[ 'X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]

# Gerar valores iniciais 
print([['*' for i in range(1, 4)] for j in range(1, 4)])

### Dictionary Comprehension

"""
Dictionary Comprehension
- o princípio é o mesmo da list comprehension

Atenção: 
- para criar uma lista: 
lista = [1, 2, 3. 4]

- para criar uma tupla: 
tupla = (1, 2, 3, 4) # 1, 2, 3, 4

- para criar um set (conjunto)
conjunto = {1, 2, 3, 4}

- para criar um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe de um dicionário
{chave:valor for valor in iterável}

"""
# Exemplos 1
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# formato Dictionary Comprehension
quadrado = {chave:valor ** 2 for chave, valore in numeros.itens()}
print(quadrado)

# Exemplos 2 -> para cada valor de uma lista, ou tupla, ou set, faça...
numeros = [1, 2, 3. 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}

# Atenção: importante respeitar as características de cada conceito: tupla, lista, set. etc.

# Exemplos 3
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos 4 - Lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

### Set Comprehension

'''
Set Comprehension
- o princípio é o mesmo de list comprehension

Lista = [1, 2, 3, 4, 5]
Set = [1, 2, 3, 4, 5]
'''

# Exemplo 1 
numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 2
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: fazer alteração na estrutura acima para gerar um dicionário ao invés de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Exemplo 3
letras = {letra for letra in 'Geek University'}
print(letras)
# obs.: observe no resultado que o conjunto não há repetição e nem ordenação

