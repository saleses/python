## Função integrada: Reversed

'''
Obs.: não confundir a função reverse() estudadas em listas
- reverse() apenas em lista
- reversed() em qualquer iterável -> essa é a grande diferença
'''
# Exemplo - função reverse()

# A função reverse() funciona apenas em listas e não em tuplas, set, dicionários...
lista = [1, 2, 3, 4, 5]
lista.reverse()         # inverte os valores da lista
print(lista)

# Exemplo - função reserved()
res = reversed(lista)
print(res)
print(type(res))              # função reversed() retorna um iterável chamado List Reverse Iterato
print(list(reversed(lista)))  # conversão do reversed() para lista
print(tuple(reversed(lista))) # conversão do reversed() para tupla

# Em conjunto (set), não definimos a ordem dos elementos
# Conjunto Set
print(set(reversed(lista)))   # conversão do reversed() para set

# Iteração sobre o reversed
for letra in reversed('Nova York'):
    print(letra, end='')

# Sem o for acima
print(''.join(list(reversed('Nova York'))))

# com o slice de strings
print('Nova York'[::-1])

# Usando o reversed() para executa um for reverso
for n in reversed(range(0, 10)):
    print(n)

# usando apenas o range
for n in range(9, -1, -1):
    print(n)

