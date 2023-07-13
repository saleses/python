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

# 3. Introdução ao módulo Unittesti - DECLARADO NA AULA COMO O MAIS IMPORTANTE

'''
-> É APENAS INTRODUÇÃO. TEMA GRANDE QUE DEMANDARIA UM CURSO INTEIRO

Unittest -> Testes Unitários

- O que são? é a forma de testar unidades individuais de código fontes
   - Unidades individuais: funções, métodos, classes, módulos e etc. 

Obs.: teste unitário não é específico da linguagem Python. É conceito geral de desenvolvimento de código

- para criar os testes, se cria classes que herdam de unittest.TestCase e a partir de então ganha-se todos os 'assertions' presentes no módulo. 

TestCase -> casos de teste para sua unidade

# Conhecendo as assertions (entender melhor)
   - Tem no site doc.python.org/ (pesquisar library Unit test)
   - importante

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com underline (exemplo: test_comer -> teste da função comer)

Dicas:

1. Para executar os testes com unittest
 - python3.8 nome_do_modulo.py

2. Para executar os testes com unittes no modo verbose
 - python3.8 nome_do_modulo.py -v (verbose)

3. Docstrings nos testes
 - pode-se acrescentar Docstrings no teste


obs.: pelo terminal é melhor a visualização de erros e acertos
Dica:
    - F -> significa falha
    - ponto "." -> significa OK
'''

# Exemplo 1 - Atenção neste exemplo: refere-se a mais de um arquivo: módulo de código (programa) e de teste separados, mas no mesmo projeto


################## Módulo de código (programa) de nome atividade.py ##############################
def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'Só vivemos uma vez'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} :('
    
def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False


################## Arquivo de teste (nome: teste.py): testes unitários #######################
import unittest


from atividades import comer, dormir    # importa módulo de código acima

class AtividadesTestes(unittest.TestCase):    # Teste unitário (Boa prática: chamar a classe de teste com termo do mesmo nome do módulo)
    
    def test_comer_saudavel(self):                      # Cada função no Unittest é um teste
        '''Testando o retorno com comida saudável'''
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_saborosa(self):                      # Segundo teste (separar os teste é importante para o debug)
        '''Testando o retorno com comida saborosa'''
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),    # Utilização de argumentos nomeados (explicado na aula de funções)
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        '''Testando o retorno dormindo pouco'''
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        '''Testando o retorno dormindo muito'''
        self.assertEqual(
            dormir(10),
            'Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(pessoa):
        '''Testando o retorno de comediantes'''
        # self.assertEqual(eh_engracada('Sergio Malandro'), False )
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertFalse(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')

if __name__ == '__name__':
    unittest.main()

'''
Tipos de Assertions
  - https://docs.python.org/3/library/unittest.html

assertEqual(a, b)          a == b
assertNotEqual(a, b)       a != b
assertTrue(x)              bool(x) is True
assertFalse(x)             bool(x) is False
assertIs(a, b)             a is b
assertIsNot(a, b)          a is not b
assertIsNone(x)            x is None
assertIsNotNone(x)         x is not None
assertIn(a, b)             a in b
assertNotIn(a, b)          a not in b
assertIsInstance(a, b)     isinstance(a, b)
assertNotIsInstance(a, b)  not isinstance(a, b)

'''

# 3.1. Antes e após HOOKS

'''
Unittest - Antes e após hooks

hooks - são os testes em si. A execução dos testes
- antes ou depois

Métodos:
1. setup() -> executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;
2. tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de dados


'''
####################### ARQUIVO DE TESTE ########################################

import unittest

class ModuloTest(unittest.TestCase):    # a ordem das funções abaixo não importa. Será executado setup primeiro e por útlimo tearDown()

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apóes o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apóes o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass


       
################################# CÓDIGO - robo.py ###################################

class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades


    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BOOP BEEP BOOP. EU SOU {self.__nome.upper()}'
        return 'Bateria fraca. Por favor, recarregue e tente novamente'

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateriaa -= custo
            self.__habilidades.append(nova_habilidade)
            return f'Uau! EU APRENDI {nova_habilidade.upper()}'
        return 'Bateria insuficiente. Por favor, recarregue e tente novamente'

################################## NOVO ARQUIVO - robo_testes.py #################################

import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)   # acessará todos os métodos abaixo
        print('setUP() sendo executado...')

    def test_carregar(self):
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)
        
    def test_dizer_nome(self):
        self.assertEqual(megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('tearDown() sendo executado...')    # conectaria a um banco ou arquivo, por exemplo

if __name__ == "__main__":
    unittest.main()

