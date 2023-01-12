### Funções integradas - Any e All

'''
Any e All
- são built-in

all()
- retorna True se "todo" os elementos do iterável forem verdadeiros ou ainda se estiver vazio
- é um Booleano

any()
- retorna True se "algum" os elementos do iterável forem verdadeiros e se estiver vazio retorna False
- é um Booleano

'''
# Exemplos all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False, porque o zero é False
print(all([1, 2, 3, 4]))     # Todos os números são verdadeiros? True, por padrão os numerais são True
print(all[])                 # Todos os números são verdadeiros? True, vazio retorna True
print(all('Sales'))          # Toda string é verdadeiro? True 

# verifica as letras iniciais de cada elemento
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))    # Retorna True (posição '0' de nome )

# verifica se todos os elementos são números pares
print(all([ num for num in [4, 2, 10, 6, 8] if num % 2 == 0])         )

# Exemplos any()

print(any([0, 1, 2, 3, 4]))         # True
print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# Verifica se há 'algum' número par
print(any(num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0))  # Retorna True
