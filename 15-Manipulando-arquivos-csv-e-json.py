# MANIPULANDO ARQUIVOS CSV E JSON

# 1. Lendo arquivos CSV
'''
CSV - Comma Separeted Values (Valores separados por vírgula)

# Separador por vírgula
1, 2, 3, 4, 5, 6

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6

Obs.: pode-se ter separadores por vírgula dentre outros (vírgula, ponto e vírgula, espaço, etc.)
Obs.: o que se busca: um padrão para separar dados

Limpeza de dados: é o trabalho realizado para buscar o que se deseja de um arquivo


Dica: usar o arquivo lutador.csv para treinar (salvo no Drive)

Site de dados do governo federal: http://dados.gov.br/dataset

'''

## Abertura de arquivo CSV
# Forma não ideal
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[2]    # split: separador de dados. Definido a vírgula
    print(dados)

# Formas ideais

'''
A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV: 
    - reader -> permite que iteremos sobre as linhas do arquivo CSV como listas/
    - DictReader -> permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;
'''

# Importação da função reader do módulo CSV
from csv import reader

with open('lutador.csv') as arquivo:
    leitor_csv = reader(arquivo)     # O objeto retornado é um iterator
    next(leitor_csv)                 # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


# Importação da função DictReader
from csv import DictReader

with open('lutador.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # escolhendo delimitador fora do padrão que é a vírgula
    # leitor_csv = DictReader(arquivo)              # Exemplo sem delimitador
    # next(leitor_csv)                         # Não se usa porque no DictReader usa-se chave e valor. Diferente do exemplo acima: Reader
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f'{linha['Nomee']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}')


'''
Obs.:  por padrão o Reader e o DictReader usam a vírgula
'''

# 2. Escrevendo em arquivos CSV

'''
reader() -> leitor
writer() -> escritor

writerow() -> escreve uma linha

'''

# Exemplo 1 - Writer()

'''
writer() -> gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
writerow() -> para escrever cada linha. Este método recebe uma lista
'''


'''Importação '''
from csv import write

with open('filmes.csv', 'w') as arquivo:    # Criação do arquivo filmes.csv (w: sobrescrever se existir)
    escritor_csv = write(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # Lista de strings
    while filme != 'sair':
        genero = input('Informe o nome do filme: ')
        duracao = input('Informe o gênero: ')
        escritor_csv.writerow([filme, genero, duracao])

'''
obs.: verificar a criação do arquivo 
'''

# Exemplo 2: DictWriter
'''
- diferente do Writer() que trabalha com lista, o DictWriter trabalha com Dicionário
- as chaves do dicionário devem ser as mesmas utilizadas como cabeçalho
'''

'''Importação'''
from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']    # As chaves do cabeçalho deve ser a mesma do writerrow() abaixo
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)    # Passa um container contendo um cabeçalho
    escritorf_csv.writeheader()    # Escreve o cabeçalho no arquivo
    filme = None
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração: (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})  # Escreve a linha


# 3. Conhecendo o Pickle

'''
- a função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização (não se sabe o que tem dentro)
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

Obs.: o módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar com 
arquivos pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.
'''

'''Importação do Pickle'''
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

felix = Gato('Felix')
pluto = Cachorro('Pluto')


# Fazendo a escrita em arquivos pickle

with open('animais.pickle', 'wb') as arquivo:  # w: escrever ; b: binary
    pickle.dump((felix, pluto), arquivo)       # dump: recebe dois parâmetros -> 1: felix e pluto ; 2: arquivo


# Fazendo a leitura de dados em arquivos pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)    # carrega o arquivo Pickle (gato e cachorro são objetos)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')


# 4. Trabalhando com JSON e Pickle

'''
JSON -> JavaScript Object Notation
 - muito comuns
 - um dicionário de chave:valor
 
API -> são meios de comunicação entre os serviços oferecidos por empresas
       (Twitter, Facebook, Youtube...) e terceiros (os desenvolvedores)
'''
# Exemplo 1

'''importação'''
import json

ret = json.dumps(['produto'], {'PlayStation4': ('2TB', 'Novo', '220V', 2340)})  # Será formato para o formato JSON (ao executar, repare a aspas duplas)

print(type(ret))

print(ret)


# Exemplo 2 
class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)    # Aqui, será impresso o dicionário com aspas simples

ret = json.dumps(felix.__dict__)  # Neste caso, por ser formato JSON, aspas duplas

print(ret)

'''
Integrando o JSON com o Pickle
- pip install jsonpickle
'''

# Escrevendo arquivo JSON/Pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

'''
ret = jsonpickle.encode(felix)

print(ret)
'''

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo o arquivo JSON/Pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)


