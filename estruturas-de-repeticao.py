#######################################
#       ESTRUTURAS DE REPETIÇÃO       #
#######################################

# 1. Loop for
'''
for item in interavel:
    //execucao do loop

O loop é usado para iterar sequências ou valores iterável
Exemplos de iteráveis: 
- string
  nome = 'Estdos Unidos da América'
- lista
  lista = [1, 2, 3, 4, 5]
- range
  numeros = range(1,10)
'''

nome = 'Estados Unidos da América'
lista = [1, 2, 3, 4, 5]
numeros = range(1,10)   # necessário transformar em lista

# Exemplo de for 1 (string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (range)
for numero in range(1, 10):
    print(numero)

'''
O valor final não é incluso (10 está fora)
'''

# função enumerate
# [(0, 'E'), (1, 's'), (2, 't'), (3, 'a'), (4, 'd'),... ]
for indice, valor in enumerate(nome):
    print(nome[indice])

# ou 
for indice, letra in enumerate(nome):
    print(letra)

# ou
for _, letra in enumerate(nome): # usa-se o underline para descartar o índice
    print(letra)

# ou
for valor in enumerate(nome):
    print(valor[1])            # imprime apenas o valor 1

# Exemplos de for

# 1
qtde = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtde+1):
    num = int(input(f'Informe o {n}'/{qtde} valor: ))
    soma = soma + num
print(f'A soma é {soma}')

# 2
for letra in nome:
    print(letra, end='')      # Forma de obter saída sem pular linha
'''
Para descobrir outras informações com o esta acima, use dir(help)

CTRL + PRINT com o cursor em cima da função: virá o menu
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

# Convertendo um range para uma lista
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

