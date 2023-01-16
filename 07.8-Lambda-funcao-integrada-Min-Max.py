## Função integrada Min() e Max

'''
Min e Max
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos

'''
## Função max()

# Exemplos: 
# obs.: o exemplo abaixo é uma tupla. A função max() valos para lista, tupla, conjunto, dicionário, set...
lista = (1, 8, 4, 99, 34, 129)     # Tupla com números 
print(max(lista))                  # imprime o maior valor da lista

# Exemplo do tipo dicionário
# Atenção nas duas chamadas: índices e valores
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}     # exemplo com dicionário 
print(max(lista))                                                     # imprime o maior índice do dicionario
print(max(dicionario.values()))                                       # imprime o maior valor do dicionario

# Exemplo com programa simples
# Programa recebe dois valores do usuário e mostra o maior
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

print(max(valor1,valor2))         # Imprime o maior entre os valores
print(max(4, 67, 54))             # Imprime o maior de todos
print(max('a', 'b', 'abc'))       # Imprime a letra 'abc'
print(max('a', 'b', 'c', 'g'))    # Imprime a letra 'g' (ordem alfabética?)
print(max('3.145', '5.789'))      # Imprime 5.789
print(max('Ciência de Dados'))       # maior quantidade de caracteres? 


## Função min()

# Exemplos: 
# obs.: o exemplo abaixo é uma tupla. A função max() valos para lista, tupla, conjunto, dicionário, set...
lista = (1, 8, 4, 99, 34, 129)     # Tupla com números 
print(min(lista))                  # imprime o menor valor da lista

# Exemplo do tipo dicionário
# Atenção nas duas chamadas: índices e valores
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}     # exemplo com dicionário 
print(min(lista))                                                     # imprime o menor índice do dicionario
print(min(dicionario.values()))                                       # imprime o menor valor do dicionario

# Exemplo com programa simples
# Programa recebe dois valores do usuário e mostra o menor
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

print(min(valor1,valor2))         # Imprime o menor entre os valores
print(min(4, 67, 54))             # Imprime o menor de todos
print(min('a', 'b', 'abc'))       # Imprime a letra 'abc'
print(min('a', 'b', 'c', 'g'))    # Imprime a letra 'g' (ordem alfabética?)
print(min('3.145', '5.789'))      # Imprime 5.789
print(min('Ciência de Dados'))    # menor quantidade de caracteres. É o espaço em branco 


## Outros exemplos: 
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))          # imprime o maior na ordem alfabética: Tim
print(min(nomes))          # imprime o maior na ordem alfabética: Arya


## Usando lambda para imprimir o nome com amior número de caracter
print(max(nomes, key=lambda nome: len(nome)))   # imprime o de maior qtde de caracter: Ollivander
print(min(nomes, key=lambda nome: len(nome)))   # imprime o de menor qtde de caracter: Tim 


## A mais e menos tocada nas rádios
musicas = [
    {"titulo": "Star Wars Theme", "tocou": 3},
    {"titulo": "Tarrega", "tocou": 2},
    {"titulo": "Fiddler on the Roof", "tocou": 4},
    {"titulo": "Handel ", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))  # música que mais tocou
print(min(musicas, key=lambda musica: musica['tocou']))  # música que menos tocou


## Imprime somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])  # o título da que mais tocou
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])  # o título da que menos tocou

# Imprime a mais e menos tocada sem usar o min(), max() e lambda
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        max = musica['titulo']

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        min = musica['titulo']

