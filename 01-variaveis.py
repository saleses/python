### VARIÁVEIS PYTHON 
print('CURSO PYTHON')
print('Aula 01 - Variáveis\n')

## Declaração de variável

'''
Tipagem dinâmica
- é a característica em que não é necessário a declaração do tipo de variável

Exemplos:
Linguagem C:
int numero = 42  # tipagem não dinâmica

Python:
numero = 42      # tipagem dinâmica

Escopo de variável
- limitação de espaço de uma variável declarada

Tipos de variáveis:
Globais: são reconhecidas por todo o código
Locais:  são reconhecidas apenas nos blocos do código em que estão declaradas

- Expressão de declaração: 
nomeVariável = valorVariável   # Há espaço entre a variável e seu valor

PEP-8: 
- snake_case: para variáveis, funções/métodos
- camelCase: para as classes


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
print('1. Tipo String\n')
print('Formas de declaração de strings:\nstring1 = \'aspas simples\'\nstring2 = \"duas duplas\"\nstring3 = \'\'duplas aspas simples\'\'\nstring4 = \"\"\"tripla aspas duplas\"\"\"\n')

# Declaração de strings
string1 = 'aspas simples'
string2 = 'aspas duplas'
string3 = 'dupla aspas simples'
string4 = 'tripla aspas duplas'

print(f'print1 = {string1}')
print(f'print2 = {string2}')
print(f'print3 = {string3}')
print(f'print4 = {string4}\n')

'''
Em Python, um dado é uma string sempre que estiver entre aspas: simples, duplas, triplas e duplas triplas
(mais comum é a aspas simples)

string1 = 'uma string'
string2 = "outra string"
string3 = ''mais uma string''
string4 = """chega de strings"""
'''

# Exemplos de variáveis string 
print('Exemplo de variáveis string\n')
print('# Declaração de variação nome')
print("nome = \'Nome e Sobrenome\'\n")
print('# IMpressão da variável:')
nome = 'Nome e Sobrenome'
print(f'nome = {nome}')
print(type(nome))

#outro_nome = "Mary's roses"
#print(outro_nome)
#print(type(outro_nome))

# Exemplo de string com scape (pular linha)
#nome_scape = 'Primeiro \nSegundo'
#print(nome_scape)
#print(type(nome_scape))

# Funções: upper() e lower() - converte caracteres em maiúsculo e minúsculo
print('\nFuções: upper() e lower() - converte caracteres de string para maiúsculo e minúsculo')
print('# Declaração de variáveis:')
print("minúscula = \'MENININHA\'")
minuscula = 'MENININHA'
print("maiuscula = \'meninona\'\n")
maiuscula = 'meninona'
print('# Transformação:')
print(minuscula.lower())
print(maiuscula.upper())


# Variáveis Globais e Locais
print('# Variáveis globais e locais')
print('Global: declaradas no ínício do código')
print('Local: declaradas dentro de blocos do código\n')
# Global: normalmente no início do código
#print(f'\nVariável global: declarada no início e válida para todo o código')
print('# Exemplo de declaração de variável global')
print('var_global = \'Variável global\'')
print('var_local = 1')
var_global = 'Variável global'
var_local = 1
print('\nImprime valor de variável e tipo')
print(f'var_global = {var_global}')
print(type(var_global))

# Local: dentro de um bloco da condição IF
print('\n# Exemplo de variável local em bloco de condicional if')
print('if var_local > 10:')
print('    novo = 0               # Declaração de variável local')
print('    novo = var_local + 10')
print("    print(f'Valor de novo é {novo}')")
print('\n# Imprime valor de novo')


### TESTAR VARIÁVEL LOCAL EM BLOCO DE LOOP E ESTUDAR SE VARIÁVEL LOCAL FUNCIONA EM CONDICIONAL TAMBÉM
if (var_local < 10):
    #novo = 0
    novo = var_local + 10              # variável local (novo)
    print(f'novo = {novo}\n')


print('# Teste de impressão de variável local fora do bloco. Espera-se o Resultado: vazio')
print(f'novo = {novo} <- Vazio')


## Tipos numéricos

# Verificação do tipo de variável declarada
'''
Função type()
- identificação do tipo de variável
'''

# Inteiro
print('Tipo inteiro:\n')
num_inteiro = 10
print(f'Valor da variável num_inteiro = {num_inteiro}')
print(type(num_inteiro)) 


# Float (numérico real)
print('Tipo Float - número real:\n')
num_real = 10.1
print(f'Valor da variável num_real = {num_real}')
print(type(num_real))


# Declaração de variáveis em uma linha  
print('Declaração de variáveis em apenas uma linha\nExemplo:\nvalor1, valor2 = 1, 4.4')
valor1, valor2 = 1, 4.4
print(f'Saída da variável valor1: {valor1}')
print(type(valor1))
print(f'Saída da variável valor2: {valor2}')
print(type(valor2))

# Mais de uma variável em uma linha com questionamento
print('Exemplo de entrada de dois valores ou mais por usuário em uma única linha e separado por espaço\n')
n1,n2 = input('Digite dois números inteiros (separados por espaço): ').split()  # separe a entrada de valores com espaço
print(f'n1: {n1}')
print(f'n2: {n2}')
print('Obs.: não funciona com a função/método int(). Deve-se converter após a declaração.')
'''
Obs.: não funcionou utilizando o método int()
'''

# Gerando variáveis de tipos diferentes
print('Geração de variávels de tipos diferentes')
print('num1, *lista1 = 1, 2,3,4')
num1, *lista1 = 1,1,2,3    # Atenção: o regexp '*' gera uma lista com os elementos 1,2,3 -> [1,2,3]
print('Obs.: o asterisco "*" fará com que a variável lista seja do tipo lista')
print(f'variável num1: {num1} -> tipo inteiro')               # tipo integer
print(f'variável lista1: {lista1} -> tipo lista')              # tipo list

# Gerando inteiro e lista vazia (em uma linha)
print(f'Geração de lista vazia')
print('um_numero, *lista2 = 1, ')
um_numero, *lista2 = 1,     # numero = inteiro ; lista = lista vazia (vírgula é importante)
print(f'variável um_numero: {um_numero}')
print(f'variável lista2: {lista2}')
print(type(um_numero))
print(type(lista2))


## Tipo Booleano
print('Tipo Booleano:\n- variáveis com 02 tipos constantes: True or False')
'''
- São variáveis com 02 constantes 
- inicia-se com letra maiúscula

True  -> Verdadeiro
False -> Falso
'''
# Declaração do tipo booleano
print('ativo = False\nprint(ativo)\n')
ativo = False
print(ativo)
print(type(ativo))


## Operação de negação (NOT)
print('Operador de negação - not\nprint(not ativo)\n')
print(not ativo)  # retorna o valor contrário ao declarado na variável booleana


## Operação OR 
print('Operador or\nlogado = False\nprint(ativo or logado)')
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
print('Operador and\nnum5 = 5\nnum8 = 8\n(num5 < num8) and (num8 == 8)')
num5 = 5
num8 = 8
num5 < num8 and num8 == 8  # Testado no terminal

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
print('Conversão de string em lista\nmeu_nome = "Antonio"\nprint(meu_nome.split())')
meu_nome = 'Antonio'
print(meu_nome.split())

# Converte uma string e imprime apenas o índice desejado
print('Imprime índice 0 e 1 da lista\nprint(meu_nome.split()[0])\nprint(meu_nome.split()[1])')
print(meu_nome.split()[0])
print(meu_nome.split()[1])

# Invertendo a string
print('Inverte valores da lista\nprint(nome[::-1])')
print(nome[::-1])          # Pega o primeiro (-1) e inverte

# Imprimir parte de uma string
print('Slice: imprime intervalos\nprint(meu_nome[0:4])\nprint(meu_nome[3:6])')
print(outro_nome[0:4])     # Slice de string
print(outro_nome[2:6])     # Slice de string

# Substituição de caracteres em uma string
print('Substituição de caracteres em uma string\nprint(nome.replace(\'a\', \'u\'))')
print(nome.replace('a', 'u'))

