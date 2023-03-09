## Entendendo iteradores e iteráveis

# 1. Iterator x Iterable

'''
- aula com detalhes importantes no uso de iteradores e iteráveis

Diferenças: iterator x iterables

1. Iterator
 - um objeto que pode ser iterado
 - um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

2. Iterable
 - um objeto que irá retornar um iterator quando a função iter() for chamada

'''
nome = 'Nome'   # é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # # é um iterable mas não é um iterator

# retorna iterator
it1 = iter(nome)
it2 = iter(numeros)

# retorna iterable???
print(next(it1))  # letra n
print(next(it1))  # letra o
print(next(it1))  # letra m
print(next(it1))  # letra e

# loop for
'''
O loop for fará um iterable com a variável nome, mesmo não usando a função iter()
'''
for letra in nome:
    print(f'{letra}')

# 2. Criando a sua própria versão de loop


# O que o python na prática está fazendo no loop for? 
# iter([1, 2, 3, 4, 5])
for num in [1, 2, 3, 4, 5]:
    print(num)

# O mesmo caso acima
for letra in 'Cavaleiro andante':
    print(letra)

def meu_for(iteravel):
    it = iter(interavel)      # aplicação do iter em um iterável
    while True:
        try:
            print(next(it))   # imprime toda iterável
        except StopIteration: # para a iteráção ao fim
            break

# chamada da função
meu_for('Antonio Sales')

numeros_int = [1, 2, 3, 4, 5]

# chamada da função
meu_for(numeros)


# 3. Escrevendo um iterador customizado

# laço for com ranger de 0 a 10
fon n in range(11):
    print(n)

# Customização de um range (irá tratar como o range acima)
class Contador:    # declaração de uma classe (conceito em orientação a objeto)
    def __init__(self, menor, maior)    # função especial denominada construtor
        self.menor = menor    # self -> quando tiver uma funçãoi (método) dentro de uma classe
        self.maior = maior    # self -> quando tiver uma função  (método) dentro de uma classe
    
    # os dois métodos abaixo garantem a funcionalidade do iterator
    def __init__(self):
        return self

    def __next__(self)    # o next é aplicado em um iterator
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

con = Contador(1, 61)

print(con.menor)
print(con.maior)

# Exemplo abaixo gera erro; não será um iterator
it = iter(con)

# next garante a aplicação do iterator
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# 4. Geradores
'''
Importante: 
 - Geradores (Generators) são Iterators (Iteradores);

Obs.: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações: 
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generators Functions (Funções Geradoras)

-------------------------------------------------------------------------------
/ Funções                          / Generator Functions                      /
-------------------------------------------------------------------------------
/ Utilizam return                  / utilizam yield                           /
-------------------------------------------------------------------------------
/ Retorna uma vez                  / podem utilizar yield múltiplas vezes     /
-------------------------------------------------------------------------------
/ Quando executada, retorna um valor / quando executada, retorna um generator /
-------------------------------------------------------------------------------

'''
# Exemplo: Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador              # importante (é o return)
        contador = contador + 1

# Obs.: Uma Generator Function não é um Generator. Ela gera um generator. 

gen = conta_ate(5)
gen = list(conta_ate(5))  # fará todos os next de uma vez só

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 5. Teste de memória com Generator

'''
- Generator é bom para obter baixo consumo de memória

'''
# função de sequência de Fibonacci: 1, 1, 2, 3, 5, 8, 13...
# Usando listas

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b    # Fibonacci? -> inverte os valores (a recebe b e b recebe a + b)
    return nums

# Teste da função acima (fazer o teste abaixo em arquivos.py diferentes)
# Usando listas

for n in fib_lista(10000):   # Gera a lista grande para ver teste de memória 
    print(n)

'''
usar o top para verificar o consumo de memória
'''

# Teste de função usando geradores e não lista
# Usando Geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste do generator acima
for n in fib_lista(10000):   # Gera a lista grande para ver teste de memória 
    print(n)

'''
usar o top para verificar e comparar com o de cima
'''

# 6. Teste de velocidade com expressões geradoras

# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num             # Gera um a um

ge1 = nums()

print(ge1)    # Generator (Gerador)

print(next(ge1))
print(next(ge1))
print(next(ge1))
print(next(ge1))

# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)    # Generation Expression (expressão generadora)

print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade
import time                               # Lib de tempo e hora (estudada a frente)

# Generator Expression
gen_inicio = time.time()                                   # calcula o tempo de início
print(sum(num for num in range(100000000))) # 100 milhões
gen_tempo = time.time() - gen_inicio                       # calcula o tempo total 


# List Comprehension
list_inicio = time.time()
print(sum[num for num in range(100000000)])) # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


