## Função integrada Zip

'''
zip()
- cria um iterável (Zip Object) que agrega de cada um dos iteráveis passados como entrada em pares
- pega o primeiro elemento de cada variável do tipo lista e agrupa-os em tupla.
- o mesmo acontece com a tupla e set. Já com o dicionário retorna o agrupamento sem colocá-los em uma tupla
'''

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla, Dicionário
print(list(zip1))    # lista


zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista3, lista2, lista1)
print(list(zip1))

# Pode-se utilizar diferentes iteráveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7. 8. 9. 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))      # o asteriscos é para fazer o desagrupamento (unzip)


## DICA: nos exemplos abaixo, desmembrar e testar as partes no terminal bash é uma boa para o entendimento

# Exemplos mais elaborados
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

# Explicação: do resultado do zip (agrupamento), pega o dado[0] como índice e joga na variável final o 
# maior dentre os dado[1] e dado[2]
final = {dado[0]: max(dado[1],dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Executando o exemplo acima com map()
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

