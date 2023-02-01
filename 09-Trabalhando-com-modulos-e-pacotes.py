## Trabalhando com módulos e pacotes

## 1. Módulo random
'''
O que são módulos? 
- Em Python, módulo é um arquivo contendo definições e comandos para serem utilizados em outros programas.
- Há diversos módulos que fazem parte da biblioteca padrão
- são assim definidos para reutilização e simplificação dos códigos

Módulo Random
- possui várias funções para geração de números pseudo-aleatórios

Pacotes (bibliotecas)
- pacotes é outro tipo de módulo que contêm um conjunto de módulos
'''

# Utilização de módulos ou funções

# Forma 1

import random   # importação de todo módulo random (não recomendado)

'''
random() -> gera um vaçpr real pseudo-aleatório entre 0 e 1

Observação: 
ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades
que estiverem dentro do módulo ficarão disponíveis (em memória). Caso você saiba quais funções
você precisa utilizar deste módulo, então esta não seria a forma ideal de utilizar. 
'''

print(random.random())

'''
Veja que para a utilizar a função random() do pacote random, nós colocamos o nome do pacote e o
nome da função, separados por ponto. 

Obs.: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() 
é apenas uma função dentro do módulo random
'''

# Forma 2 - importação de uma função específica do módulo

from random import random    # especificação da função random do módulo random

'''
Obs.: repare que na declaração da função random, não há parênteses '()'. Estes são usada na hora de 
chamar a função
'''

# Exemplo da forma recomendada
for i in range(10):
    print(random())      # muito utilizado em IA


# Função uniform() -> gera um valor real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # o último valor, neste caso o 7, nunca será atingido

# Função randint() -> gera valores INTEIROS pseudo-aleatórios entre os valores estabelecidos

from random import randint

# gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')    # começa em 1 e vai até 60

# choice() -> mostra um valor aleatório de um iterável

from random import choice    # importa a função choice do módulo random

jogadas = ['pedra', 'papel', 'tesoura']    # tupla de opções usadas pela função choice()

print(choice(jogadas))

print(choice('Letras deste iteravel'))     # funciona também neste caso


# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)    # embaralha
shuffle(cartas)  # desembaralha
print(cartas)    # embaralha

print(cartas.pop())  # retira a última carta caso eu precise remover a útlima carta

## 2. Módulos Built-in

'''
Módulos built-in são módulos integrados. Já estão instalados no Python
- os módulos built-in não são carregados de imediato apesar de estarem instalados. Precisa do import

URL ->  https://docs.python.org/3/py-modindex.html -> global module index  (listas os módulos built-in instalados)
'''

# Utilizando alias (apelidos) para módulos/funções
import random as rdm  # criação de alias rdm para função random

print(rdm.random())   # Atenção: não irá funcionar com o nome padrão ao criar o alias

# Importação de todas funções de um módulo utilizando o asterisco (*)

from random import *
print(random())   # repare que não foi necessário descrever o nome do módulos


# Apelidando a função e não o módulo
form random import randint as rdi, random as rdm  # apelido para função ou mais de uma função

print(rdi(5, 89))
print(rdm())

# Costuma-se utilizar tuple para colocar múltiplos imports de um mesmo módulo. Formato usual
from random import (
        random,
        randint,
        shuffle,
        choice
)

print(random())
print(randint(3, 7))

lista = ['Luke', 'Skywalker', 'Jedi']
shuffle(lista)
print(lista)

print(choice('Artificial'))

## 3. Módulos customizados

'''
- Todos os arquivos de códigos que criamos, por exemplo: de aula, são na verdade módulos que podemos reutilizar.
- Chamando as funções, por exemplo, neles criadas pelo desenvolvedor. 

'''
# chamando função feita em arquivo .py, módulos, de aula

from funcoes_com_parametro import soma_impares  # chamada de função de aula anterior (módulo .py)

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9])) # será aprendido a melhor prática a frente

'''
Atenção:
- o nome do módulo, arquivo .py, pode não estar correto. Pois, alterei a sequência do curso (nomes diferentes)
'''

# Importando todo o módulo (Ter acesso a TODOS os elementos do módulo)
import funcoes_com_parametro as fcp   # criação de alias

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)
print(fcp.tupla)
print(fcp.soma_impares(fcp.tupla))

# importando variável do módulo map (arquivo de aula)
from map import cidades, c_para_f   # variável cidade e variável c_para_f que recebe um lambda

print(list(map(c_para_f, cidades)))   # chamada das variáveis de módulo, arquivos .py, estudados em aula.

## 4. Instalando e utilizando módulos externos

'''
Módulos externos

- são módulos que não fazem parte da lib padrão da linguagem
- utilizamos o gerenciador de pacotes Python chamado Pip, Python Installer Package

https://pypi.org -> site com todos os pacotes externos e oficiais da comunidade Python

como utilizar?
- no terminal: utilizar o pip da mesma forma (com características próprias) que o apt-get
- expressão: 
    pip <comando> [options]

- exemplo de instalação e upgrade de um pacote
pip install nome_pacote    -> instalação de um pacote 
pip install --upgrade pip  -> instalação, upgrade de uma nova versão do pip

Atenção: um pacote possui vários módulos
- um bom exercício é acessar o site pip e ver exemplos de pacotes. Por exemplo: colorama para iniciar

- na aula foi realizado testes com o pacote colorama que não vi necessidade de reproduzir neste arquivo. Importa
entender no próprio site e testar no terminal, por exemplo. Também pelo terminal do Pycharm
'''

## 5. Pacotes Python

'''
Módulo x Pacotes
- módulo: é apenas um arquivo Python que pode ter diversas funções para utilização
- pacotes: é um diretório contendo uma coleção de módulos

Obs.: 
- nas versões abaixo de 2.x, um pacote Python deve conter um arquivo denominado __init__.py
- nas versões do Python 3.x acima, não é mais obrigatório a utilização do arquivos __init__.py. Mas ainda é utilizado para manter compatibilidade. 
- os pacotes e módulos são excelentes para organizar códigos de uma aplicação
nota: quando criamos diretórios, pacotes, no pycharm, ele criará o arquivo __init__.py

'''
# Exemplo -> na aula foram criados pacotes com módulos com funções que são chamadas abaixo
# Vale a pena rever

from geek import geek1, geek2  # importa o módulo geek1

from geek.university import geek3, geek4

print(geek1.pi)  # imprime a função pi

print(geek1.funcao1(4, 6))  # executa função 1 do módulo geek2

print(geek2.funcao2())  # executa função 2 do módulo geek2

print(geek3.funcao3())  # executa função 3 do módulo geek3

print(geek4.funcao4())  # executa função 4 do módulo geek4

# Outro exemplo: importação de apenas a função desejada
# pacotes: geek (pacote)
# módulos: geek1.py e geek2.py
# função: funcao1 do módulo geek1.py 

from geek.geek1 import funcao1

print(funcao(6, 9))

## 5. Dunder Main e Dunder Name

'''
Dunder Name e Dunder Main

- Dunder Name -> __name__
- Dunder Main -> __main__

Em Python, são utilizados Dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação. 

# Na linguagem C, temos um programa da seguinte forma:

int main() {

    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

# Em python, se executamos um módulo Python diretamente na linha de comando, internamente o Python
atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

Nota: os testes desta aula são feitas com módulos já estudados. Vale rever para visualizar o que foi feito

'''

# Exemplo (gerar os módulos abaixo para realizar os testes)
# Módulo 1 -> ou seja, arquivo primeiro.py
# else: -> nestes testes abaixo existem apenas para realizar os testes

def funcao1():
    print('Teste qualquer - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado {__name__}')


# Módulo 2 -> ou seja, arquivo segundo.py
import primeiro

def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente')
else:
    print(f'segundo.py foi importado {__name__}')


