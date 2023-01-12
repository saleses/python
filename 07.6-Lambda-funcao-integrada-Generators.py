### Funcao integrada - Generators Expression

'''
Generators Expression (Tuple comprehension)

Diferente das: 
    - List Comprehension
    - Dictionary Comprehension
    - Set Comprehension

estudadas anteriormente, Tuple Comprehension é chamada de Generator Expression. Difere na denominação


- após a utilização, será removida da memória. Zerando o resultado
- consomem menos recurso que o List Comprehension, mais performático. Melhor para checagem, não joga em memória. List comprehension, joga para a memória. 
'''
# Exemplo
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# List Comprehension
print(any([nome[0] == 'C' for nome in nomes]))  # repare: há colchetes '[ ]'delimitando a List Comprehension

# Generators (Tuple Comprehension)
print(any(nome[0] == 'C' for nome in nomes))  # repare: não há colchetes '[ ]' delimitando o Generator

###  Teste de verificação: diferença entre List Comprehension e Generators

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator 
res = (nome[0] == 'C' for nome in nomes)  # repare que o colchetes não existe 
print(type(res))
print(res)

'''
Conceitos importantes: 
- O generator consome menos recursos que a list, Dictionary e Set Comprehension porque usa menos recurso em memória. (Mais performático). 
- Não gera de imediato os valores solicitados, ele prepara um objeto para que no momento necessário gere os dados. 
'''

# Exemplo com import

# Comceito: a função getsizeof() retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Skywalker' ocupa de memória. Quanto maior a string, mais espaço ocupa
print(getsizeof('Skywalker'))
print(getsizeof('Luke Skywalker'))

# Gera uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gera uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})  # utiliza chaves '{}'

# Gera uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)}) # utiliza sintaxe diferente -> x: x * 10 ...

# Gera uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))   # sem colchetes ou chaves. Apenas o parêntese da função

print('Verificação de consumo de memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# É possível realizar iteração no Generator Expression? Sim!
gen = (x * 10 for x in range(1000))
print(gen)         # repare esse resultado. Informa a criação de um objeto
print(type(gen))   

for num in gen:
    print(num)     # nesto ponto é gerado os valores guardados pelo Generator Expression


