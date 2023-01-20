## Funcao-integrada-Len-Abs-Sum-Round

'''
Len, Abs, Sum, Round

a) len()
- retorna o tamanho, número de itens, de um iterável

b) abs()
- retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal

c) sum()
- recebe como parâmetro um iterável. Pode receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial
Obs.: o valor inicial default é ZERO

d) round()
- retorna um número arredondado para n dígitos de precisão após a casa decimal. 
- Caso a precisão não seja informada, retorna o inteiro mais próximo da entrada.

'''

# Exemplo: len()
print(len('Sistema Operacional'))
print(len([1, 2, 3, 4, 5]))                         # Lista
print(len((1, 2, 3, 4, 5)))                         # Tupla
print(len({1, 2, 3, 4, 5}))                         # Set
print(len({ 'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}))   # Dicionário

print(len(range(0, 10)))

## Atenção: por trás dos panos, quando utilizamos a função len() o Python faz o seguinte: 
## Dunder len
print('Sistemas GNU-Linux'.__len__())   # o que a função faz é aplicar o dunder: __len__()

# Exemplo: abs()
# obs.: apenas o valor absoluto: sempre positivo
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Exemplo sum()
print(sum([1, 2, 3, 4, 5]))   # lista
print(sum([1, 2, 3, 4, 5], 5))   # ,5 é o valor inicial (utilizado em taxa de uma lista de valores)

print(sum([3.145, 5.678]))   # lista

print(sum((1, 2, 3, 4, 5)))   # tupla

print(sum({1, 2, 3, 4, 5}))   # set

print(sum({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}))   # dicionário

# Exemplo round()
print(round(10.2)) 
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(sum({1.2828282828, 9)) 

