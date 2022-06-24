# MODULO COLLECTIONS - COUNTER

'''
Implimentação alternativa
Collections -> High-performance Container Datetypes

Counter -> recebe um interável como parâmetro e cria um objeto do tipo Collection Counter que é parecida com um dicionário, contando como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento

'''

# utilizar o import
from collections import Counter

# Pode-se utilizar qualquer iterável. Abaixo: lista
list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 43, 34]

# utilizar o counter
res = Counter(lista)
print(type(res))
print(res)           # como resultado, obtem-se chave/valor com elemento:qtde

# Exemplo 2
print(Counter('Curso Python')) # como resultado, chave/valor com elemento:qtde

# exemplo 3 
texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável, que todos possam editar e melhorar. """

palavras = texto.split()
#print(palavras)

res1 = Counter(palavras) # mostra a qtde de palavras do texto
print(res1)

# Encontrando as cinco palavras com mais ocorrências
print(res.most_commom(5))

