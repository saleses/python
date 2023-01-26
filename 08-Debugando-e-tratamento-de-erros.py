## Debugando e tratamento de erros

## 1) ERROS MAIS COMUNS EM PYTHON

'''
Atenção:  é essencial ler e prestar atenção às mensagens de erros do código
- traceback: saída de erros

'''
## 1. SintaxeError: erro de escrita no código

# Definição de nome da função
def funcao:                     # sem o parênteses na definição do nome: funcao()
    print('Treinamento Python')

## 2. Uso de palavras reservadas em criação de variável

None = 1     # Não vai aceitar
list = 1     # Vai aceitar mas não é uma boa prática
#return       # Deve ser utilizada dentro de uma função: uma função que retorna (return) algo.

## 3: NameError: ocorre quando uma variável ou função não foi definida

funcao_name()   # chamada de função não definida

# Outro exemplo de NameError
a = 18
if a < 10:
    msg = 'É menor que 10'     # Não será lido o bloco IF

print(msg)                     # Gera erro. A varíavel é local, dentro do if (Deve-se inicializá-la fora do bloco if. Ou seja, variável global)


## 4. TypeError: quando uma função/operação/ação é aplicada a um tipo errado

print(len(5))    # O objecto do tipo int não tem a função len()

print('Nome' + [])  # Erro na concatenação de uma String com lista ou com int

## 5. IndexError: quando tenta-se acessar um elemento em uma lista ou outro tipo de dado indexxado utilizando índice inválido

lista = ['Mega']
print(lista[2])      # Erro por não existir o elemento 2
print(lista[0][10])  # Erro por não existir a posição [10]

## 6. ValueError: ocorre quando uma função/operacao built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado

print(int('42'))             # String de valor 42
print(int('Texto qualquer')) # Valor inapropriado. Não é possível converter um string em inteiro

## 7.KeyError: quando tenta-se acessar um dicionário com uma chave que não existe
dic = {}           # Dicionário criado sem chave
print(dic['Bola']) # KeyError porque não há chave definida

dic = {'Bola': 'Penalty'}  # Dicionário com chave criada
print(dic['Bola'])         # Impressão correta do valor da chave 'Bola'

## 8. AttributeError: quando uma variável não tem um Atributo/função
# O conceito será visto em aula de Orientação a objeto
tupla = (11, 2, 31, 4)
print(tupla.sort())        # a função sort() é usada em lista e não em tupla

## 9. IndentationError: quando não respeita-se a identação do Python (4 espaços)
def nova():
print('Teste de identação')    # não há identação dentro da função

# outro exemplo sem identação
for i in range(10):
i + 1                       # sem identação
print(i)                    # sem identação

## Dica: no site do Python.org, acesse: Library Reference > Exception tem vários tipos de erros de código
## Obs.: Exceptions e Erros são sinônimos em programação
## Obs.: Importante ler e prestar atenção na saída de erro. 


## 2) levantando os próprios erros com raise

'''
raise
- lança exceções, mas não as trata. Apenas lança, apresenta os erros para debugados
- não é uma função. É uma palavra reservada como o def ou outra palavra reservada em Python
- Simplificando, o raise é útil para criar nossas próprias exceções e mensagens de erros.
- Obs.: o raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado

- Sintaxe: 
raise TipoDOErro('Mensagem de erro')

'''

# Exemplo 1
raise ValueError('Valor Incorreto')   # Será lançado no  Trackback o erro da string em questão

# Exemplo 2
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma String')  # caso o texto não for string, lança exceção
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')    # caso texto não for string, lança exceção
    print(f'O texto {texto} será impresso na cor {cor}')

colore('nome', '4')  #  a chamada do numeral 4 não é string e sim inteiro, vai dar erro. 

# Exemplo 3
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma String')  # caso o texto não for string, lança exceção
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')    # caso texto não for string, lança exceção
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')
    

colore('True', 'verde')  # Chamada da função sem erro
colore('True', 'preto')  # Chamada da função apresentará erro

## 3) Bloco Try/Except
'''
O bloco Try/Except para tratar erros que podem ocorrer no código
- previne que o programa pare de funcionar e o usuário receba mensagem de erro inesperadas. Evita a visualização de erros pelo usuário

- A maneira mais simples é (tente isso (try), senão use (except) isso): 

try:
    //execução da problemática
except:
    //o que deve ser feito em caso de problema

'''
# Exemplo 1 - Tratamento a um erro genérico, a saída não será de erro do sistema e sim a exceção abaixo
# Erro genérico não é a melhor prática. Melhor especificar
try:           # tenta executar a função abaixo
    nome()
except:i       # capturar a exceção da função acima
    print('Ocorreu algum erro inesperado')

# Exemplo 2 - Tratamento a um erro genérico
try:           
    len(5)    
except:i       
    print('Ocorreu algum erro inesperado')

# Exemplo 3 - Tratando um erro específico
try:
    funcao()
except TypeError:       # Especificando o erro
# execpt NameError:     # se declarar o tipo de erro errado, não surtirá efeito e o S.O lançará o erro default
    print('Você está utilizando uma função inexistente')


# Exemplo 4 - Tratando um erro específico
try:
    len(5)
except TypeError as err:  # Útil para mandar mensagem de erro para log 
    print('Aplicação gerou o seguinte erro: {err}')

# Exemplo 5 - Tratando mais de um erro de uma vez (no exemplo, apenas 02)
try:
    len(5)
except NameError as erra:           # NameError
    print(f'Deu NameError: {erra}')
except TypeError as errb:           # TypeError
    print(f'Deu NameError: {erra}')
except:                             # Forma genérica: qualquer outro erro
    print('Deu um erro diferente')

# Exemplo 6 - Tratando erro em função -> repare que dentro da função há o tratamento de erro do código desejado
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:            # conforme exemplo acima, caso precise de outro tratamento, só acrescentar except
        return None

dic = {"nome": "Saulo"}
print(pega_valor(dic, "sobrenome")) # Repare, não existe a chave sobrenome. Gera erro


## 4) Bloco Try, Except, Else e Finally

'''
Try / Except / Else / Finally

- Quando devo tratar um erro? 

1) Toda entrada de dado deve ser tratada (SEMPRE)

Obs.: a função do usuário é distruir seu sistema

'''
# Exemplo 1 - else: para cada except, pode ser usado o else

try:
    num = int(input('Informe um número: '))   # Variável local
except ValueError:
    print(f'Valor incorreto')
else:                                 # Caso não ocorra o erro ValueError (imprime a msg abaixo)
    print(f'Você digitou {num}')

# Exemplo 2 - Finally: o bloco finally é sempre executado. Independente de ocorrer a exceção
# O finally, geralmente, é utilizado para fechar ou desalocar recursos.
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print('Você digitou o número {num}')
finally:
    print('Executando o finally')

# Exemplo 3 - Função recebe dois valores e efetua a divisão
# Dica: para pegar o erro correto, para tratar é importante ler a saída (tipo de erro, linha, ...)
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print('Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo 4 - Forma mais simples que o anterior
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError,ZeroDivisionError) as err:   # Criação de exceções em uma linha
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


## 4) Debugando código com PDB (PDB: Python Debugger)

'''
Debugando com PDB
- Bug: inseto

'''

# Exemplo 1: utilizando o 'print'. Não é legal
def dividir(a, b):
    print(f'a={a}, b={b}')     # não usual
    try:
        return int(a) / int(b)
    except (ValueError,ZeroDivisionError) as err: 
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

'''
Existem formas mais profissionais de se fazer um debug do que no exemplo acima. Utilizando o 'print'
Em python, pode-se fazer isso em diferentes IDEs, como o PyCharm ou o PDB: Python Debugger
'''

# Exemplo 2: com o Pycharm -> como estudei com o terminal, pesquisar a opção de debugger do pycharm ou rever aula
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError,ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))
'''
usa-se o break point, botão debug ao lado do play (canto superior direita)
'''

# Exemplo 3: com PDB - Python Debugger
# necessário importar a biblioteca pdb e utilizar a função set_trace()
'''
Comandos básicos do PDB
l (lista onde estamos no código
n (próxima linha))
p (imprime variável)
c (continua a execução - finaliza o debugging)

'''
import pdb

nome = 'Larissa'
sobrenome = 'não sei'
pdb.set_trace()               # uso do PDB
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 4: com PDB, outra forma

i# import pdb   -> já importado acima

nome = 'Larissa'
sobrenome = 'não sei'
#import pdb; pdb.set_trace()     # ver comentário abaixo
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

'''
Porque utilizar este formato? 
O debug é utilizado durante o desenvolvimento. Normalmente os 'imports' de bibliotecas são iniciados no início 
do código. Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente onde 
vamos debugar, e ao finalizar já fazemos a remoção.
'''

# Exemplo 3
# A partir do python3.7 não é mais necessário importar o PDB. É uma função built-in (integrada) chamada breakpoint()
nome = 'Larissa'
sobrenome = 'não sei'
breakpoint()         # PDB built-in
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

'''
Obs.: cuidado com conflitos entre nomes de variáveis e os comandos do pdb; veja abaixo
'''

# Exemplo 4
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c   # nomes não representativos, ruins. Opte por nomes significativos

print(soma(1, 3, 5, 7))
'''
Como os nomes das variáveis são os mesmos dos comandos dos pdb, devemos utilizar o comando p para imprimir
as variáveis. Ou seja, p nome_da_variavel
'''

