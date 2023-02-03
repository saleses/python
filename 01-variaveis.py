### VARIÁVEIS PYTHON 

## Declaração de variável

'''
Tipagem dinâmica
- Python não é preciso informar o tipo da variável a ser declarada

Exemplos:
- em linguagem C:
int numero = 42  # tipagem não dinâmica

- em Python:
numero = 42      # tipagem dinâmica

Escopo de variável
- limitação de espaço de uma variável declarada

Tipos de variáveis:
Globais: são reconhecidas por todo o código
Locais:  são reconhecidas apenas nos blocos do código em que estão declaradas

- Expressão de declaração:
nome_da_variável = valor_da_variável   # Há espaço entre a variável e seu valor

Dicas: 

1)
Em python, a escrita de numerais pode ser representada por underline '_' para facilitar a visualização
- numero = 1_000_000
2) 
dir(num)  -> função que retorna as possíveis operações de um determinado número (no terminal)

Observação: em python não há limite no tamanho da variável. O limite é a memória disponível

Operadores lógicos: 
+  adição
-  subtração
*  multiplicação
/  divisão com resultado em tipo real (ponto flutuante)
// divisao com retorno de inteiros
%  operação de módulo: resto de uma operação
** potência
num ** 0.5 raiz quadrada
'''

## Tipo String
'''
Em Python, um dado é uma string sempre que estiver entre aspas: simples, duplas, triplas e duplas triplas
(mais comum é a aspas simples)

string1 = 'uma string'
string2 = "outra string"
string3 = ''mais uma string''
string4 = """chega de strings"""
'''

# Exemplos de variáveis string 
nome = 'João Carioca'
print(nome)
print(type(nome))

outro_nome = "Mary's roses"
print(outro_nome)
print(type(outro_nome))

# Exemplo de string com scape (pular linha)
nome_scape = 'Primeiro \nSegundo'
print(nome_scape)
print(type(nome_scape))

# Função upper() e lower()
# Converte caracteres em maiúsculo e minúsculo
print(nome.upper())
print(nome.lower())

# Variáveis Globais e Locais
# Global: normalmente no início do código
num = 1
print(num)
print(type(num))

# Local: dentro de um bloco da condição IF
if num > 10:
    novo = num + 10   # variável local (novo)
    print(novo)


## Tipos numéricos

# Verificação do tipo de variável declarada
'''
Função type()
- identificação do tipo de variável
'''

# Inteiro
num_inteiro = 10
print(num_inteiro)
print(type(num_inteiro)) # função type(num_inteiro) retorna o tipo inteiro 


# Float (numérico real)
num_real = 10.1
print(num_real)
print(type(num_real))    # função type(num_real) imprime o tipo float


# Declaração de variáveis em uma linha  
valor1, valor2 = 1, 4.4
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Gerando variáveis de tipos diferentes
num1, *lista = 1,1,2,3    # Atenção: o regexp '*' gera uma lista com os elementos 1,2,3 -> [1,2,3]
print(num1)               # tipo integer
print(lista)              # tipo list

# Gerando inteiro e lista vazia (em uma linha)
numero, *lista = 1,     # numero = inteiro ; lista = lista vazia (vírgula é importante)
print(numero)           # tipo integer
print(lista)            # tipo list

## Tipo Booleano

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


## Operação de negação (NOT)
print(not ativo)  # retorna o valor contrário ao declarado na variável booleana


## Operação OR 
logado = False
print(ativo or logado)  # a operação lógica, disjuntiva, depende de 02 valores booleanos

'''
Disjunção (or)
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
'''

## Operação AND 
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

## Tipo números complexos, conversão de números e dicas extras

# Número complexo
variavel = 5j
print(variavel)
print(type(variavel))

# Converter float para int ou vice-versa
# Obs.: converter float em inteiro tem-se como consequência a perda de precisão (perde o decimal)
res = int(valor1)  # exemplo de conversão em inteiro
print(res)
print(type(res))

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
print(nome[::-1])          # Pega o primeiro (-1) e inverte

# Imprimir parte de uma string
print(outro_nome[0:4])     # Slice de string
print(outro_nome[2:6])     # Slice de string

# Substituição de caracteres em uma string
print(nome.replace('a', 'u'))

