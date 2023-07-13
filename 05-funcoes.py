# FUNCTIONS PYTHON

'''
1. Definição de funções

- são pequenos trechos de código que realizam tarefas específicas: 
    - quebrando em pequenas partes para realização de tarefas específicas por código
    - pode ou não receber entradas de dados e retornar uma saída de dados
    - muito úteis para executar procedimentos similares por repetidas vezes

Obs.: cuidado para manter a simplicidade do código. Funções devem ser simples, contendo tarefas específicas, finalidade própria, e não repetitivas, chamadas pontuais. 

Exemplo de funções, built-in: 
- print()
- len()
- max()
- min()
- count()
- dentre outras

'''

# Exemplo de utilização de funções integradas. (Built-in são as funções integradas):
#cores = ['verde', 'amarelo', 'azul', 'branco']
#print(cores)                                         # função integrada print()

#curso = 'Programação em Python'
#print(curso)                                         # função recebe um dado, curso, e o imprime

#cores.append('roxo')                                 # função append() adiciona elementos na lista. 
#print(cores)

# Exemplo de erro
#curso.append('Mais dados...')   # Dará erro de atributo
#print(curso)            

# Função clear() limpa os dados de uma lista
#cores.clear()
#print(cores)

# Chamando o help de print
#print(help(print))

'''
Ou seja, as funções podem ter diversas finalidades. São tarefas implementadas, chamadas para execução de algo específico
'''

# PRINCÍPIO DA PROGRAMAÇÃO
# DRY: Don't Repeat Yourself -> Não repita você mesmo / Não repita seu código

'''
Definição de funções
Em python, a forma geral de definir uma função é: 

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde: 
- nome_da_funcao > SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
- parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste bloco, pode ter ou não retorno da função. 

Obs.: veja que para definir uma função, utilizamos a palavra 'def' informando ao Python que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos ':' que é utilizado em python para definir blocos.

'''

############# ORGANIZAÇÃO DESTE ARQUIVO INICIADO COM OS EXEMPLOS ABAIXO #################################

# Exemplo 1
print('Funcão: bem_vindo')
def bem_vindo():                                 # Não há parâmetros de entrada
    print('Hello World!\n')

'''Chamada da função'''
bem_vindo()

'''
Observação: 
Pode existir funções built-in ou outras funções dentro de uma função
'''


# Exemplo 2
print('Função: cantar_parabens')
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()                     # Chama a função cantar_parabens()


# Exemplo 3 -> chamada de função dentro de um loop for
for n in range(5):
    print(n)
    cantar_parabens()   # Função será executada 5 vezes



# Exemplo 4 - Entrada de valor fora da função
print('Função: dobro')
def dobro(n):                                    # Argumento de entrada
    d = n * 2
    print(f'O dobro de {n} é: {d}\n')

num = int(input("Digite um número: "))

'''Chamada'''
dobro(num)


# Exemplo 4 - Neste exemplo a entrada de valores está na própria função
print('Função: soma')
def soma():
    n1 = int(input("Digite primeiro número: "))
    n2 = int(input("Digite segundo número: "))
    s = n1 + n2
    print(f'{n1} + {n2} = {s}\n')

'''Chamada'''
soma()


# Exemplo 4 - Retorna, envia algo para fora da função
print('Função: subtrair_dez')
def subtrair_dez(n):
    return n - 10    # Envia para a chamada da função a expressão "n - 10" para armazenar em variáveis


num = float(input('Digite um número: '))

'''Chamada: guarda valore retornado em variável'''
subtracao = subtrair_dez(num)

print(f'Valor da subtração: {subtracao}\n')

'''PRÁTICA RUIM DO EXEMPLO ACIMA'''
# Uma forma de enviar uma chamada para a variável é declará-la sem os parêntes
subtracao = subtrair_dez    # repare a ausência de parênteses para jogar valor na variável

subtracao()   # chamada da função (com o nome da variável? ou da função? Verificar)


# Exemplo 5 - Cumprimento personalizado
print('Função: oi_fulano')
def oi_fulano():
    nome = str(input("Digite seu nome: "))
    if nome:
        print(f'Como vai {nome}')
    else:
        print('Bom! Não quer falar? Como vai Fulano\n')
    return    # Apenas para ilustrar. Não há necessidade deste retorno. (exemplo: não armazena em variáveis)


################## CONTINUAR TRAZENDO PARA ESTE BLOCO OS CÓDIGOS ABAIXO ##################################


# FUNÇÕES COM RETORNO

'''
numeros = [1, 2, 3]
ret_pop = numeros.pop()          # função pop() remove o último elemento de uma lista e o retorna
print(f'Retorno de pop: {ret_pop}')


ret_print = print(numeros)       # a função print() não tem retorno
print(f'Retorno de print: {ret_print}')

Obs.: quando uma função não retorna nenhum valor, o retorno é do tipo None
'''

# Exemplo de função - sem retorno
def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()  # demonstra que a variável não recebe valor (None), ou seja, não retorna nada
print(f'Retorno {ret}')

quadrado_de_7()       # chamada da função que imprime o quadrado de 7. (imprimir não é igual retorno)


# Refatorar, rescrever um código, a função para que receba o valor
# Exemplo de função - com retorno
def quadrado_de_7():
    return 7 * 7       # return -> é quem retorna o valor (o resultado: 49)

ret = quadrado_de_7()
print(f'Retorno {ret}') 

'''
Não é necessário criar uma variável para obter o retorno de uma função. Veja abaixo

'''
def quadrado_de_7():
    return 7 * 7 

print(f'Retorno: {quadrado_de_7()}')     # Retorno sem uso de variável. Mais simples e direto
print(f'Retorno: {quadrado_de_7() + 1}') # Com operação matemática

# Refatorando a primeira função
def diz_oi():
    return 'Oi '

# A vantagem do retun? Flexibilidade no uso do código
alguém = 'Pedro!'
print(diz_oi() + alguém)


# Obs.: Sbore a palavra reservada return. Veja exemplos abaixo

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado')        # É impresso na tela. Antes do return que finaliza a função
    return 'Oi'
    print('EStou sendo executado após o retorno...')    # Essa linha não será executada

print(diz_oi())
 
# Exemplo 2 - Pode-se ter, em uma função, diferentes returns;
def nova_funcao():
    variavel = True         # Alterar para None ou False para ver resultados abaixo
    if variavel:
        return 4
    elif variavel is None: 
        return 3.2          # será retornado o valor 3.2 e não 4 (ignorado)
    return 'b'              # False: retorna o valor b

print(nova_funcao())


# Exemplo 3 - Pode-se, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
def outra_funcao():
    return 2, 3, 4, 5



num1, num2, num3, num4 = outra_funcao()    # valores do return guardados em variáveis. Não obrigado
print(num1, num2, num3, num4)              # imprime as quatro variáveis

print(outra_funcao())
print(type(outra_funcao()))                # é uma tupla


# Criação de uma função para jogar moeda
#     lib          função                 # será estudado a frente
from random import random                 # importação de uma lib para o código 

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1 (pseudo por ter como a característica de repetição de dados)
    valor = random()
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


# Erros comuns na utilização de um retorno de função. Na verdade não é erro. É uma codificação desnecessária
def eh_impar():
    numero = 5      # Altere o valor da variável para testar
    if numero % 2 != 0:
        return True
    return False    # repare que não foi necessário a utilização do else com return. Boa prática em funções com return

print(eh_impar())

# FUNÇÕES COM PARÂMETROS

'''
Funções com parâmetros (de entrada)

- funções que recebem dados para serem processados dentro dela mesma

Normalmente, em programas, temos: 
entrada -> processamento -> saída

Há funções que:
- não possuem entrada;
- não possuem saída;
- possuem entrada mas não há saída
- não possume entrada mas há saída
- possuem entrada e saída
'''

# Refatorando uma função

# primeiro código
def quadrado_de_7():
    return 7 * 7

# A saída para as impressões abaixo serão idênticas
print(quadrado_de_7()):
print(quadrado_de_7()):
print(quadrado_de_7()):


# Refatorando o código comentado acima acima
def quadrado_de_7(numero):          # lê-se: a função 'quadrado_de_7' recebe parâmetro 'numero'
    return numero * numero

# Chamada da função com resultados de acordo com os parâmetros 
print(quadrado_de_7(7)):
print(quadrado_de_7(2)):
print(quadrado_de_7(5)):

ret = quadrado(6)
print(ret)

# Refatorando a função cantar_parabens()

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o/a {aniversariante}!')

cantar_parabens('Patrícia')       # Chamada da função com parâmetros


# Funções podem ter "n" parâmetros de entrada. Ou seja, podemos receber como entrada em uma função 
# quantos parâmetros forem necessários. Eles são separados por vírgula.
# Exemplos:

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra*(3, 2, 'Curso '))     # Imprime na tela a string Curso 5 vezes
print(outra*(5, 4, 'Python '))    # Imprime na tela a string Python 9 vezes

# Obs.: na chamada da função, temos argumentos e não parâmetros. Estes são declarados na declaração da função
# Parâmetros são variáveis declaradaas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função
# A ordem dos parâmetros deve ser respeitada

# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'  # Não é erro está fora de parênteses a string???

print(nome_completo('São', 'Thomas'))

# Argumentos nomeados (Keyword Arguments)
# - caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='São', sobrenome='Thomas'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Matheus', nome='São'))


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total    
#   return total          # Erro comum: identar o return no for e não no if. Altera o resultado. Teste

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))


# FUNÇÕES COM PARÂMETRO PADRÃO

'''
Funções com parâmetro padrão (Default Paramters)

- funções onde a passagem de parâmetro seja opcional;
'''

# Exemplo de função no qual a passagem de parâmetro é opcional
print('Data Science')
print()


# Exemplo de função com parâmetro obrigatório
def quadrado(numero):
    return ** 2

print(quadrado(3))     # chamada de função quadrado()



def exponencial(numero, potencia=2): # informando um valor padrão, torna este parâmetro opcional na chamada
    return numero ** potencia

print(exponencial(5))     # por padrão eleve ao quadrado (definido por padrão - potencia=2)
print(exponencial(3, 5))  # eleva a potência de acordo com o argumento informado pelo usuário


# Exemplo de definição de todos parâmetros como padrão
def exponencial(numero=1, potencia=2):     # Todos parâmetros como padrão
    return numero ** potencia

print(exponencial())     # não é preciso acrescentar argumentos ao chamar a função

'''
Obs.: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração 
'''

# ERRO
def teste(num=2, potencia):    # repare que o parâmetro default num=2 antecede o outro, potencia
    return num ** potencia

print(teste(6))                 # Ocorrerá erro devido a ordem de declaração da função


# Outros exemplos
def soma(num1=5, num2=3):       # Definição de parâmetros padrão
    return num1 + num2

print(soma(4, 3))  
print(soma(4))     
print(soma())      

def mostra_informacao(nome='nome=João', instrutor=False):
    if nome == 'João' and instrutor:
        return "Bem-vindo instrutor João!"
    elif nome == 'João'
        return 'Eu pensei que você era o instrutor'  # repare que return não é uma função. Não precisa de parêntese para String declarada
    return f'Ola {nome}'

# Teste para cada saída da condição da função - ver os resultados possíveis
print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Kal-El'))
print(mostra_informacao(nome='Jor-El')) 

'''
Por que utilizar parâmetros com valor default? 
- permite ser mais flexível nas funções;
- evita erros com parâmetros incorretos;
- permite trabalhar com exemplos mais legíveis de códigos; 

Quais tipos de daods pode-se utilizar com valores default de parâmetros? 
- Qualquer tipo: numeros, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc.

'''

# Exemplo de declaração de funções como parâmetros
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):  # parâmetro fun é opcional. Corresponde a função soma
    return fun(num1, num2)   # solicitação do parâmetro fun, chama função soma, para os parâmetros declarados

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))              # realiza a soma por ser padrao
print(mat(2, 3, subtracao))   # realiza a subtração por definir a função de subtracao


# Escopo - evitar problemas e confusões
# Variáveis globais
# Variáveis locais

# Exemplo 1:
instrutor = 'Data'   # variável global

def diz_oi():
    instrutor = 'Science'      # a variável local sobrepõem a global. Resultado será Science e não Data
    return f'Oi {instrutor}'

print(diz_oi())


# Exemplo 2: 
def diz_oi():
    prof = 'Data'    # variável local
    return f'Olá {prof}'

print(diz_oi())   # chamado da função sem erro
print(prof)       # Erro pelo fato da variável ser local. Pertence apenas a função diz_oi()

'''
Atenção com variáveis globais no uso de funções
'''

# Exemplo 3 
total = 0       # declaração de variável global

def incrementa():
    global total           # Informação da utilização da variável global na função
    total = total + 1      # variável local inicializada pela global
    return total

# cada impressão terá uma incrementação de valor pedido na função
print(incrementa())
print(incrementa())
print(incrementa())
# Resumo: local tem preferência na global. No caso de operação matemática, inicializar na função
# ou chamar a variável na função (global nome_variável)

# Declaração de funções dentro de outra função
# E forma especial de escopo de variável

def fora():
    contador = 0                 # variável local
    def dentro():                # função dentro da função fora()
        nonlocal contador        # nonlocal: declaração para utilização da função "pai". 
        contador = contador + 1
        return contador
    return dentro()

print((fora))
print((fora))
print((fora))

print(dentro())     # Erro: apenas a função fora() irá conhecer a função dentro por ser uma 'subfunção'


# Documentando funções com Docstrings

'''
O que é Docstrings?

Obs.: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__

Obs.: Podemos ainda fazer acesso à  documentação com a função (help)

'''
# Exemplo 1

def diz_oi():
    """Uma função simples que retorna Oi!"""  # Docstrings da função diz_oi()
    return 'Oi! '

print(diz_oi())

print(help(diz_oi))      # No terminal, esse comando imprime a documentação descrita dentro da função

print(diz_oi.__doc___)   # No terminal, esse comando imprime a documentação da função

# Exemplo 2

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou à 'potencia' informada. 
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

# O Docstring da função acima funcionou bem com o método help, mas funciona com duas formas do exemplo anterior.

print(help(exponencial))      # No terminal, esse comando imprime a documentação descrita dentro da função

print(exponencial.__doc___)   # No terminal, esse comando imprime a documentação da função

# ENTENDENDO O *args

'''
*args
- é um parâmetro de entrada de uma função que pode ser chamado de qualquer coisa. Desde que seja iniciado com asterisco.

Exemplo: 
*.xis

 - mas por convenção, utilizamos *args para definí-lo

mas o que é o *args?
 - O parâmetro *args utilizado em uma função, coloca os valores extras infomados como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis

'''

# Exemplo de chamadas de funções com Error pela diferença de parâmetros chamados (quantidade)
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))         # Irá funcionar. Quantidade de parâmetros idênticas

# print(soma_todos_numeros(4, 6))          # TypeError
# print(soma_todos_numeros(4, 6, 9, 5))    # TypeError  

# Entendendo o *args

def soma_todos_numeros(*args):    # declaração do args (repare: declara-se com *)
    total = 0
    """ Docstrings: o for abaixo faz a soma dos argumentos. Como a função sum()"""
    for numero in args:           # não tem o * (asterisco). Apenas foi acrescentado na definição da função
        total = total + numero
    return total

# A mesma função, com o mesmo resultado com a função sum()
def soma_todos_numeros(*args):    # declaração do args (repare: declara-se com *)
    total = 0
    """ Docstrings: utilizando a função sum()"""
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))


# Exemplo 3: declaração de valores obrigatórios(nome, sobrenome) e *args

def soma_todos_numeros(nome, sobrenome, *args):    # declaração do args (repare: declara-se com *)
    total = 0
    """ Docstrings: utilizando a função sum()"""
    return sum(args)

print(soma_todos_numeros('Tiago', 'Santos'))
print(soma_todos_numeros('Tiago', 'Santos', 1))
print(soma_todos_numeros('Tiago', 'Santos', 2, 3))
print(soma_todos_numeros('Tiago', 'Santos', 2, 3, 4))
print(soma_todos_numeros('Tiago', 'Santos', 3, 4, 5, 6))


# Outro exemplo de utilização de *args
def verifica_info(*args):
    if 'Sapce' in args and 'X' in args:
        return 'Bem-vindo Space'
    return 'Não sei quem você é!'

print(verifica_info())
print(verifica_info(1, True, 'Space', 'X'))
print(verifica_info(1, 'Space', 3.145))


# Mais exemplos
def soma_todos_numeros(*args):
    print(args)                   # veremos que os argumentos representa apenas um elemento
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos_numeros(*numeros))   # Desempacota os argumentos de entrada. Cada um será um elemento da tupla. Repare que é preciso do asterisco neste caso

# ENTENDENDO O **kwargs

"""
**kwargs

- poderíamos denominar este parâmetro de **xis, mas por convenção chamamos de **kwarg
- o **kwargs é mais um parâmetro, mas diferente do *args que coloca os valores em uma tupla. O **kwargs exige que utilizamos parâmetros nomeados e transforma esses parâmetros extras em um dicionário. 
"""

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title} é {cor}')

# chamada abaixo acrescenta dados em um dicionário
cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs.: os parâmetros *args e **kwargs não são obrigatórios (abaixo)
cores_favoritas()
cores_favoritas(space='X')

# Exemplo mais completo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é ...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

'''
Nas nossas funções, podemos ter (NESTA ORDEM): 
- Parâmetros obrigatórios;
  *args;
- Parâmetros default (não obrigatórios);
  **kwargs
'''

# Exemplo
def minha_funcao(num, nome, *args, solteiro=false, **kwargs):  # chave/valor entram no **kwargs
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiros:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')     # obrigatórios
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entender por quê é importante a ordem dos parâmetros na declaração

# Funções com a ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):   # Observe a ordem
    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros (repare no *args)
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):   # Observe a ordem
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', cargo='Instrutor'}
"""

print(mostra_info(1, 2, 3, sobrenome='university', cargo='Instrutor'))

# Desempacotar com **kwargs

# Exemplo 1
def mostra_nomes():
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))  # Desempacota o dicionário

# Exemplo 2
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}


soma_multiplos_numeros(*lista)       # Não é kwargs mas desempacota
soma_multiplos_numeros(*tupla)       # Não é kwargs mas desempacota
soma_multiplos_numeros(*conjunto)    # Não é kwargs mas desempacota

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

Obs.: Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função

#dicionario = dict(d=1, e=2, f=3)      # Type Error
#soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')   # Não funciona porque na função não há **kwargs

soma_multiplos_numeros(**dicionario, lang='Python')


