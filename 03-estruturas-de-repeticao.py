###  ESTRUTURAS DE REPETIÇÃO

# 1. Loop for
'''
Expressão: 

for item in interavel:
    //execucao do loop

O loop é usado para iterar um determinado item em sequências

Exemplos de iteráveis: 
- string, listas, tuplas, dicionários, conjuntos, etc

'''
## Exemplos:

# Declaração de string, lista e range
nome = 'Estados Unidos da América'
lista = [1, 2, 3, 4, 5]
numeros = range(1,10)        # necessário transformar em lista

# Exemplo de for com String
for letra in nome:
    print(letra)

# Exemplo de for com Lista
for numero in lista:
    print(numero)

# Exemplo de for Range
for numero in range(1, 10):
    print(numero)           # o valor 10 não está incluso, será lido de 1 a 9

# Função Enumerate - enumeração dos índices de cada valor de uma lista.

for indice in enumerate(nome)
    print(indice)               # imprime o índice e seu valor correspondente
'''
Resultado:
(0, 'E')
(1, 's')
(2, 't')
(3, 'a')
...
...
...
- informação dos índices para cada iteração
'''

# ou (declarando dois parâmetros, imprime-se apenas o que for solicitado na função print() )
for indice, letra in enumerate(nome):   # i: índice ; letra: valor correspondente a cada índice
    print(letra)                        # imprime apenas o valor de cada índice

''' 
Resultado:
E
s
t
a
...
...
...
- informação apenas dos valores de cada iteração
'''

# ou
for _, letra in enumerate(nome): # usa-se o underline para descartar o índice
    print(letra)

# ou
for valor in enumerate(nome):
    print(valor[1])            # imprime apenas o valor 1

# Exemplos de for

# 1 -> Soma uma determinada quantidade (qtde) de números (num) digitados de um range
qtde = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtde+1):
    num = int(input(f'Informe o {n}/{qtde} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

# 2 -> imprime na tela sem pular linha (end='')
for letra in nome:
    print(letra, end='')
'''
Para descobrir outras informações com o esta acima, use dir(help)

CTRL + PRINT com o cursor em cima da função: virá o menu (dica para o Pycharm)
'''

# Tabela de Emojis Unicode
# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' + num)

# 2. Range

'''
Range não é uma estrutura de repetição. É um método, uma função. 
- utilizado no loop for
- são utilizados para gerar sequências numéricas e não de forma aleatória mas de maneira especificada


'''
# estrutura do range: 
# range(valor_de_parada) -> o valor de parada não inclusive (início padrão 0 e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2
# range(valor_inicio, valor_parada)
for num in range(3, 11):
    print(num)

# Forma 3
# range(valor_inicio, valor_parada, passo)
for num in range(1, 10, 2):
    print(num)

# Forma 4 (o inverso da forma 3)
# range(valor_inicio, valor_parada, passo) -> o parâmetro passo determina a ordem inversa
for num in range(10, 0, -1):
    print(num)

# Cria uma lista de 10 elementos (0, 1, 2,...,9). Joga o tamanho de um range em lista
lista = list(range(10))
print(lista)

'''
lista = range(10) é um formato ERRADO!
'''

# 3. Loop while
'''
Regra geral: 

while expressao_booleana:
    //execucao do loop

- a condição de parada do loop while é a expressão booleana (Verdadeiro ou Falso)
'''
num1 = 1

# Exemplo 1
while num1 < 10:
    print(num1)
    num1 = numero + 1  # contador
'''
Cuidado: há risco de loop infinito. Importante utilizar um contador para incrementar ou decrementar um valor
'''

# Exemplo 2
resposta = ' '

while resposta != 'sim':
    resposta = input('Finalizou a tarefa? Digite sim ou não')


# 4. Saindo do loop com break 

'''
Utilizado para sair de loops de maneira projetada
'''

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    comando = input("Digite 'sair' para finalizar: ")
    if comando == 'sair':
        break

