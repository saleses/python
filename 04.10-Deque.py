'''
Módulo Collections - Deque
- é uma lista de alta performance. 
- se assemelha a uma lista
- maior manipulação ao trabalhar com listas
'''

# Importação da coleção Deque
from collections import deque

# Criação do deque
deq = deque('Geek')
print(deq)

# Adicionando elementos com Deque
deq.append('y')     # Adiciona no final
print(deq)          # Adiciona no final
deq.appendleft('k') # Adiciona à esquerda, no início. Ou seja, mais opções com o deq

# Remoção de elementos com Deque
print(deq.pop())      # Remove e retorna o último elemento
print(deq)
print(deq.popleft())  # Remove e retorna o primeiro elemento

