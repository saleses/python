'''
Módulo Collections - Named Tuple

'''
# Revisão tupla
tupla = (1, 2, 3)
print(tupla[1])

# Named Tuple -> são tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

# Importando
from collections import namedTuple

# Precisamos definir o nome e parâmetros.
# Forma 1 - declaração Named Tuple
cachorro = namedTuple('cachorro', 'idade raca nome')

# Forma 2 - declaração Named Tuple
cachorro = namedTuple('cachorro', 'idade, raça, nome')

# Forma 3 - declaração Named Tuple
cachorro = namedTuple('cachorro', ['idade', 'raca', 'nome'])

# Declaração da tupla
ray = cachorro(idade=2, raca='chow-chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 1
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2
print(ray.idade)  # idade
print(ray.raca)   # raca
print(ray.nome)   # nome

# Descobrindo indice
print(ray.index('chow-chow'))
print(ray.count('chow-chow'))

