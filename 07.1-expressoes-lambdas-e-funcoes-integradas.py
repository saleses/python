### Expressões Lambdas
'''
Utilizando Lambdas

O que é são?
- as expressões lambdas, ou simplesmente Lambdas, são funções anônimas. Sem nome

Função em python:
def soma(a, b):
    return a + b

Declaração de Lambda
lambda x: expressao_desejada

'''
# Exemplo de função python: 
# Implementando função
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Exemplo de expressão Lambda para resolver a mesma função acima
# atenção: existe apenas uma entrada, a letra 'x' 
lambda x: 3 * x + 1

# Exemplo de Lambda mais usual
calc = lambda x: 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressoes lambdas com múltiplas entradas
# entradas: nome, sobrenome
# função strip(): remoção de espaços no início e final da variável e não entre palavras da string
# função title(): faz com que apenas a primeira letra fique em maiúscula
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' +  sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo('   FELICITY      ', ' jones '))

# Lambda com nenhuma ou várias entradas
amar = lambda : 'Como não amar Python? '
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ..., xn: <expressao>


print(amar())
print(um(6))
print(dois(5, 7))
print(tres(3, 6, 9))

# Obs.: passando mais argumentos do que parâmetros declarados, ocorrerá erros

# Outros exemplos
# utilizando lista
autores = ['Isaac Asimov'. 'Ray Bradbury'. 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

# Uso comum do Lambda
autores.sort(key=lambda sobrenome: sobrenome.split(' '[-1].lower()))
print(autores)

'''
Explicação do código Lambda acima: 
- funcao split(' '): separa o nome e sobrenomes e cada elemento da lista autores e, para cada um, transforma o nome e sobrenome em elementos de uma lista. Ou seja, cada elemento uma lista.
- [-1]: reverte a ordem pegando o último elemento, cada sobrenome. 
- lower(): coloca todos em minúsculo
- sort(key=lambda): pega como chave de ordenação o resultado do lambda que é listar pelo sobrenome.

DICA: 
- utilização do HELP: exemplo abaixo é utilizado no terminal
- mostra a utilização da função sort() em listas: '[]'
help([].sort)
'''

# Função Quadrática (ou função ao quadrado?)
f(x) = a * x ** 2 + b * x + c

# Definição da função
def geradora_funcao_quadratica(a, b, c):                    # valores da função quadrática
    """Retorna a função f(x) = a * x ** 2 + b * x + c """   
    return lambda x: a * x ** 2 + b * x + c     # declaração do Lambda

teste = geradora_funcao_quadratica(2, 3, -5)    # atribui valores aos elementos a, b e c da função

# atribui valor de x ao lambda, dentro da função geradora_funcao_quadratica, e imprime resultado
print(teste(0))
print(teste(1))
print(teste(2))

# Executando a função sem uso da variável teste
print(geradora_funcao_quadratica(3, 0, 1)(2))

'''
Aplicação de Lambdas na prática
- filtragem de dados
- ordenação de dados
Obs.: a utilização de lambdas não se limita aos exemplos acima
'''

