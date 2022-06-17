
################################
#      VARIÁVEIS PYTHON        #
################################

# Declaração de variável

'''
Declaração de variáveis
nome_da_variável = valor_da_variáve
'''
nome_variável = 'Estudo Python'  # Exemplo

'''
Tipagem dinâmica
- em Python não é preciso informar o tipo da variável a ser declarada

Exemplo em C:
int numero - 42  # tipagem não dinâmica

Exemplo Python:
numero = 42  # tipagem dinâmica

Escopo de variável
- limitação de espaço de uma variável declarada

Tipos:
Globais: são reconhecidas por todo o código
Locais:  são reconhecidas apenas nos blocos do código em que estão declaradas

'''

# Exemplo de variável global
num = 1
print(num)
print(type(num))

# Exemplo de variável local, dentro de um bloco
if num > 10:
    novo = num + 10   # variável local (novo)
    print(novo)


# TIPO NUMÉRICO

'''
Operadores:
+  adição
-  subtração
*  multiplicação
/  divisão com resultado em tipo real (ponto flutuante)
// divisao com retorno de inteiros
%  operação de módulo: resto de uma operação
** potência

- Python permite melhor visualização de números no código com o underline (Exemplo: 1_000_000)

type() -> função retorna o tipo da variável
dir(num)  -> função que retorna as possíveis operações com um determinado número (no terminal)

obs.: em python não há limite no tamanho da variável. O limite é a memória disponível

'''

# TIPO FLOAT

# Declaração de variável numérica 
num_inteiro = 10
print(type)  # function type retorna o tipo de dado na variável

# Declaração de variável float
num_real = 10.1
print(num)
print(type(num_real))  # imprime o tipo float

# Dupla atribuição 
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Converter float para int ou vice-versa
res = int(valor1)  # exemplo de conversão em inteiro
print(res)
print(type(res))

# Número complexo
variavel = 5j
print(variavel)
print(type(variavel))

'''
Obs.: converter float em inteiro tem-se como consequência a perda de precisão (perde o decimal)
'''

# TIPO BOOLEANO

'''
- São variáveis com 02 constantes 
- inicia-se com letra maiúscula

True  -> Verdadeiro
False -> Falso

'''

# Declaração do tipo booleano
ativo = False
print(ativo)
print(type(ativo))

# Operação de negação (not)
print(not ativo)  # retorna o valor contrário ao declarado na variável booleana

# Operação OR 
logado = False
print(ativo or logado)  # a operação lógica, disjuntiva, depende de 02 valores booleanos

'''
Disjunção (or)
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
'''

# Operação AND 
num1 = 5
num2 = 8
num1 < num2 and num1 = 8  # Testado no terminal

'''
Conjunção (AND)
True or True   -> True
True or False  -> False
False or True  -> False
False or False -> False
'''

# TIPO STRING

'''
Em Python, um dado é uma string sempre que estiver entre aspas: simples, duplas, triplas e duplas triplas
- a mais comum é a aspas simples
'''

string1 = 'uma string'
string2 = "outra string"
string3 = '''mais uma string'''
string4 = '''chega de strings '''


# Exemplos com variáveis
nome = 'João Carioca'
print(nome)
print(type(nome))

outro_nome = "Mary's roses"
print(outro_nome)
print(type(outro_nome))

nome_scape = 'Primeiro \nSegundo'
print(nome_scape)
print(type(nome_scape))

# Converte caracteres em maiúsculo e minúsculo
print(nome.upper())
print(nome.lower())


'''
Lista
- os índices de uma lista iniciam com ZERO
Exemplo: 
[ 0,   1,   2,    3,    4,    5,    6  ]
['A', 'm', 'a',  'd',  'e',  'u',  's' ]

'''

# Converte uma string em uma lista
print(nome.split())

# Converte uma string e imprime apenas o índice desejado
print(nome.split()[0])
print(nome.split()[1])

# Invertendo a string
print(nome[::-1])  # Pega o primeiro (-1) e inverte

# Imprimir parte de uma string
print(outro_nome[0:4])  # Slice de string
print(outro_nome[2:6])  # Slice de string

# Substituição de caracteres em uma string
print(nome.replace('a', 'u'))

