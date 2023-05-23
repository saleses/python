# COLEÇÕES PYTHON

# LISTAS

"""
Listas em python funcionam como vetores ou matrizes. Ou seja, arrays como em outras linguagens. i
Com a diferença de serem DINÂMICAS e também por podermos colocar QUALQUER tipo de dado. 

- Dinâmico: não possui tamanho fixo. Cria-se a lista e adiciona-se elementos. Enquanto houver memória na máquina, a lista pode ser aumentada. 
- Qualquer tipo de dado
- As listas em python são representadas por colchetes '[]'

"""
type([]) # representação de uma lista

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k',' ','U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range[11])

lista5 = list('Geek University')

# Imprimir valores de lista
'''Em uma linha'''
print(*lista_num, sep=", ")
'''Valor por linha '''
print(*lista_num, sep= "\n"
'''Impressão de valor com string: ,end'' faz com que a função/método print() não pule a linha'''
print(f'string: ',end='')
print(*lista)

# Podemos facilmente checar se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o número 8')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort() # ordena numéricos
print(lista1)
lista5.sort() # ordena strings
print(lista5)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em uma lista - função append

print(lista1)
lista1.append(42)
print(lista1)

# obs.: com append, conseguimos adicionar apenas 1 elemento por vez. 
# Mas é possível adicionar um elemento do tipo lista, ou seja, uma lista dentro de outra. O elemento lista será considerado um elemento lista dentro de uma lista. Exemplo abaixo: 

lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Para colocar mais de um elemento em uma lista, e não como uma lista dentro de uma lista como um elemento, usa-se a função extend. Esta função, diferente da função append, é usado para mais de um elemento. Não funciona para um único elemento. Ou seja: 
# append: um único elemento ou lista como um elemento
# extend: para mais de um elemento em uma lista
# obs.: as funções/métodos append() e extend() acrescentam o valor no final da lista

lista1.extend([123, 44, 67])
print(lista1)

# Pode-se inserir um novo elemento na lista informando a posição do índice, usa-se a função insert. 
# Não apaga o valor anterior, joga para o próximo índice

lista1.insert(2, 'Novo valor')
print(lista1)

# Juntar duas listas

lista6 = lista1 + lista2
print(lista6)

# ou 

lista1 = lista1 + lista2

# ou 

lista1.extend(lista2)
print(lista1)


# Revertendo a ordem dos elementos da lista

# forma 1
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# ou

# forma 2
print(lista1[::-1])
print(lista2[::-1])

print(lista1)
print(lista2)

# Cópia de uma lista

lista6 = lista2.copy()
print(lista6)

# Verificação do tamanho de uma lista
print(len(lista4))
print(len(lista5))
print(len(lista6))

# Remoção do último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# Obs.: a função pop não somente remove mas também o retorna (imprime)
# Pode-se também, pela função pop, remover elementos pelo índice. Os elementos à direita serão deslocados para esquerda. Não ficando índice vazio
lista5.pop(2)
print(lista5)

# Remoção de todos elementos de uma lista (esvaziar)
print(lista5)
lista5.clear()
print(lista5)

# Repetir elementos em uma lista; Multiplicando-os
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Converter string para uma lista
# exemplo 1
print(curso)
curso = curso.split()
print(curso)

# obs.: por padrão, o split separa os elementos da lista pelo espaço entre eles

# exemplo 2: 
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # alterando o separador da função split (no caso, vírgula)

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6) # o separador que for desejado
print(curso)  


# Pode-se colocar qualquer tipo de dado em uma lista, inclusive misturando o tipo de dado
lista6 = [1, 2, 34, Tru, 'Geek', 'd', [1, 2, 3], 45454564]
print(lista6)
type(lista6)

# Iterando sobre listas (vai depender do tipo de dado)

# exemplo 1 -> utilizando for
soma = ''
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# exemplo 2 -> utilizando while
carrinho = []
produto = ''

while produto != 'sair'
    print("Adicione o produto na lista ou digite 'sair' para encerrar compras: ")
    produto = input()
    if produto != 'sair'
        carrinho.append(produto)

for produto in carrinho: # é uma lista
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

# ou

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazendo acesso aos elementos de forma indexada
# visualizar como uma círculo

#          0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo  
print(cores[2]) # azul
print(cores[3]) # branco

# fazendo acesso aos elementos de forma inversa
# Pense na lista como um círculo, no qual o final do elemento está ligado ao início da lista

print(cores[-1]) # branco
print(cores[-2]) # azul  
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print(cores[-5]) # Mensagem de erro: Não existe

# treinando o tamanho de uma lista, função len, usando os índices
cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Criação de um índice em uma lista usando a função for
# função enumerate
for indice, cor in enumarate(cores):
    print(indice, cor)

# listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# outros métodos

# INDEX
# encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(6))   # encontrar o índice 6
print(numeros.index(9))   # encontrar o índice 9

# obs.: caso não tenha o elemento desejado na lista, será apresentado ValueError
# obs.: se houve mais de um elemento pesquisado, será mostrado o primeiro índice
print(numeros.index(5))
print(numeros.index(5,1)) # Neste caso, a pesquisa começa do índice 1
print(numeros.index(5,2)) # Neste caso, a pesquisa começa do índice 2

# fazer uma busca dentro de um range definido pelo programador (inicio/fim)
print(numeros.index(0, 3, 6))

# SLICE (vale para string)
# lista(inicio:fim:passo) # semelhante ao range
# range(inicio:fim:passo)

# trabalhando com slice de lista com o parâmetro 'inicio'
lista - [1, 2, 3, 4]
print(lista[1:]) # lista apenas o índice 1
print(lista[1:]) # lista todos elementos a partir do índice 1
print(lista[::]) # lista todos elementos da lista (não há filtro)
print(lista[-1:]) # lista todos elementos iniciando do último elemento

# trabalhando com slice de lista com o parâmetro 'fim'
print(lista[:2]) # lista todos elementos até o índice 2
print(lista[:4]) # lista todos elementos até o índice 4
print(lista[1:3]) # lista elementos do índice 1 ao 3

# trabalhando com slice de lista com o parâmetro 'passo'
print[1::2]  # começa em 1 e vai ao final de 2 em 2
print[::2]  # começa do 0, início, e vai ao final de 2 em 2

# invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

#ou 

nomes = ['Geek', 'University']
nomes.reverse()   # melhor prática

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista


# Unir e ordenar elementos de lista 
listaX = [3, 5, 2, 1, 3, 6, 5, 2, 1, 4]
ordenacao = list(set(multiplos))         # utilização de dois métodos: set e list
print(ordenacao)

# transformação de uma lista em tupla
# atenção: a representação de tuplas é diferente de listas
# [] listas
# () tuplas

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista) # conversão de lista para tupla
print(tupla)
print(type(tupla))

# desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# se houver elementos diferentes para desempacotar ou vice-versa, ter-se-á erro

# copiando uma lista para outro (Shallow Copy e Deep Copy)

# forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, o seja, modificamos uma lista, não afeta a outra. Isso em python
# é chamado de Deep Copy (cópia profunda)

# forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista  # cópia
print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas 
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas. 
# Isso em Python é chamado de Shallow Copy. 


