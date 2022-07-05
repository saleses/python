'''
Módulo Collections: Ordered Dict

'''
# Em um dicionário, a ordem de inserção dos elementos não é garantida. Exemplo: 
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# OrderedDict: é um dicionário, que nos garante a ordem de inserção dos elementos

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Diferença entre Dict e Ordered Dict

# Dicionários comuns
dict1 = {'a': 1,'b': 2}
dict2 = {'b': 2,'a': 1}
print(dict1 == dict2)    # Resposta: True, já que a ordem não importa

# Ordered Dict
ordem_dict1 = {'a': 1,'b': 2}
ordem_dict2 = {'b': 2,'a': 1}

print(ordem_dict1 == ordem_dict2)    # Resposta: False, já que a ordem importa


