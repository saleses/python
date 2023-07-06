# Testes com Python
# Realizando testes automatizados e não manuais


'''
Por que testar códigos?
- reduzir bugs (problemas) no código
- testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos
- testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos
- testes garantem que a refatoração não tragam novos bugs



Exemplo de estrutura de aplicação web

         Aplicação Web
--------------------------------------
/         Frontend e backend         /
--------------------------------------
/        testes automatizados        /
--------------------------------------


TDD - Nova vertente de testes

- TDD: Test Driven Development (Desenvolvimento Guiado por testes): os testes são escritos antes do código
  - com TDD é utilizado estágios de desenvolvimento
  - Escreve-se o código mínimo suficiente para testar e vai corrigindo e progredindo no código restante (ou seja, executar com sucesso)
  - Então refatora o código para a realizar a funcionalidade e testa novamente
  - Uma vez que o teste passe, o recurso é considerado completo

- Estes estágios de testes de desenvolvimento são quase como um mantra que os desenvolvedores seguem, conhecidos como: 
    - Red
    - Green
    - Refatoração
'''

# 1. Assertions (afirmações, questionamentos, checagens)

'''
- Palavra reservada: assert

- Em python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes
- Utiliza-se o'assert' em uma expressão para verificar sua validade
- caso verdadeira, retorna None; caso contrário, apresenta a mensagem AssertionError.

Obs.: a palavra 'assert' pode ser utilizada em qualquer função ou código. Não é exclusivo de teste. 

Exemplo para terminal:

>>> assert 4 == 4
>>> assert 4 == 2

'''
# Exemplo 1:
def soma_numeros_inteiros(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

ret = soma_numeros_inteiros(2, 4)   # resultado: 6
print(ret)
ret = soma_numeros_inteiros(-2, 4)   # AssertionError -> retornar o erros
print(ret)


# Exemplo 2: 
def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorverte',
        'doces',
        'batata-frita',
        'cachorro quente'
            ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))

'''
ALERTA: Cuidado ao utilizar 'assert'
- se o programa Python for executado com o parâmetro -O, (exemplo: python3.8 -O nome.py) nenhum assertion será validado. OU seja, inibe todos assertions do código. Não é a melhor forma o assert. 

'''

# 2. Doctests

'''
São testes que colocamos na docstring das funções/métodos Python

Para rodar um teste do doctest: 
    - python -m doctest -v nome_do_modulo.py


- Utiliza o terminal para realizar o teste

'''
# Exemplo 1:

def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)   # Inicio do docteste
    3                # Fim do docteste
    """
    return a + b

print(soma(3, 4))    # Resultado: 7

# Exemplo 2 - Utilizando o TDD
# Neste caso com o uso do TDD, será passado os estágios de testes TDD. 


# Estágio 1: nenhuma chamada irá funcionar, código incompleto

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (mostr recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    pass


# Estágio 2: três falhas e não 4 falhas

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])           # Este irá funcionar
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (mostr recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return []


# Estágio 3: Todas funções funcionarão

def duplicar(valores):
    """duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([]) 
    []

    >>> duplicar(['a', 'b', 'c'])  
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (mostr recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elementos for elemento in valores]


# Erro inesperado...
# Dentro do doctest, o Python não reconhece string com aspas duplas. Deve ser simples

def fala_oi():
    """Fala oi

    >>> fala_oi()
    "Oi"           # Erro
    """
    return 'oi'


# Último caso estranho...
# Se houver espaços após alguma linha. Na aula foi o True após a verdade()
def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True


