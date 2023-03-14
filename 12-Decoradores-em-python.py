## Decoradores em Python

# 1. Funções de maior grandeza
'''
Funções de maior grandeza - Higher Orders Functions (HOF)

O que é o conceito de HOF? 
- quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras
funções, e até mesmo criar variáveis do tipo de funções nos nossos programas. 

Obs.: na seção de funções, foi utilizado

Em Python, as funções são cidadões de primeira classe, Firts Class Citizen
'''

# Exemplo 1
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a \ b

def calcular(num1, num2, funcao):  # funcao será a chamada de uma função declarada
    return funcao(num1, num2)

# Testando as funçoes
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


# Nested Functions - Funções Aninhadas
'''
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas)
'''

# Exemplo 2
from random import choice

def cumprimento(pessoa):
    def humor():         # Nested function: função dentro de função
        return choice(('E ai ', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa  

# Teste da função acima
print(cumprimento('Carla'))
print(cumprimento('Penelope'))

# Exemplo 3 - retornar função de outras funções
from random import choice

def faz_me_ir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkk', 'yayayayayaya'))

# Testando
rindo = faz_me_ir()
print(rindo())


# Exemplo 3 
# Inner Functions pode acessar o escopo da função mais externas. 

from random import choice

def faz_me_rir():
    def dando_risada():
        risada = choice(('hahahahahah', 'lolololololo', 'kkkkkkkk'))
        return f'{risada} {pessoa}'
    return

# Teste
rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())

# 2. O que são decoradores?

'''
Decoradores (Decorators)

O que são? 
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;


/-----------------------------------------------\
/              Function Decorator               \
/-----------------------------------------------\


/--------------- Função decorator ----------------\
--------------------------------------------------
-                   Functions                   
--------------------------------------------------
/------------------------------------------------/

'''
# Exemplo de Decorators como funções (Sintaxe não recomendada / Sem açucar sintático)
def seja_educado(funcao):    # retorna a função e não a execução da função
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Smallville')

# Teste 1
teste = seja_educado(saudacao)
teste()

# Teste 2
def raiva():
    print('Eu te odeio')

raiva_educada() = seja_educado(raiva)
raiva_educada()

# Exemplo: Decorators com Syntax Sugar (Açucar sintático) - forma recomendada
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo        # Forma recomentada, melhor prática
def apresentado():
    print('Meu nome é Antônio')

# Testando
apresentando()

# Outro exemplo
@seja_educado_mesmo       # Uso do decorators
def dormir():
    print('Quero dormir')

dormir()

'''
obs.: não confundir um decorator com decorator function

'''

# 3. Decoradores com diferentes assinaturas

'''
Decorators com diferentes assinaturas

- Assinatura de uma função é a sua declaração
Exemplo: 
def nome_funcao(parametro)   # essa é a assinatura da função

Neste ponto do estudo, estamos decorando a assinatura da função

'''
# Revendo conceitos anteriores

# função 1
def gritar(funcao):
    def aumentar(*args, **kwargs):       # Estudado args e kwargs em funções
        return funcao(*args, **kwargs).upper()
    return aumentar

# função 2
@gritar
def saudacao(nome):
    return f'Ola, eu sou o/a {nome}'

# função 3
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando funções acima
print(saudacao('Lívia'))
print(ordenar('Picanha', 'Batata frita')) 

# Mais um exemplo
def lol():
    return 'lol'

print(lol())


# Obs.: pode-se utiliar parâmetros nomeados
print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

# Decorator com argumentos
def verifica_primeiro_argumento(valor):        # primeira função recebe valor de entrada
    def interna(funcao):                       # recebe a função que está sendo decorada
        def outra(*args, **kwargs):            # O comportamento que desejamos aplicar
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento(pizza)
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2)         # o primeiro valor sempre será 10
    return num1 + num2

# Testando
print(soma_dez(10, 12)) # resultado 22

print(soma_dez(1, 21))  # resultado com erro: primeiro argumento deve ser 10 (passado acima) 

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduíche', 'churrasco'))  # resultado com erro: primeiro argumento deve ser pizza (passado acima)


# 4. Preservando Metadata com Wraps

'''
O que são metadatas (metadados)? 
- são dados intrísecos em arquivos

O que são wraps? 
- são funções que envolvem elementos com diversas finalidades

'''

# Caso com problema 
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra """
        print(f'Você está chamando {funcao.__nome__}')       # Fornece o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')      # Fornece a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

# Testando
print(soma(10, 30))

print(soma.__name__)  # Trará o nome da função logar, que não é desejada
print(soma.__doc__)  # Trará a documentação da função logar, que não é desejada


# Solução do caso acima

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)                                          # ESSA DECORATOR RESOLVE O PROBLEMA ACIMA, preserva os metadados
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra """
        print(f'Você está chamando {funcao.__nome__}')       # Fornece o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')      # Fornece a documentação da função
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

# Testando
print(soma(10, 30))

print(soma.__name__)  # Solucionado
print(soma.__doc__)   # Solucionado

print(help(soma))


# 5. Forçando tipos de dados com um decorador

'''
Desenvolvendo um exemplo prático com todo o conteúdo da aula exposto acima

Função zip
a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)
(1, 2), (3, 4), (5, 6)

'''
def forca_tipo(*tipo):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))         # str('Teste'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)         # força o tipo de dado desejado
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Teste', '3')

@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)

dividir('1', 5)

