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
'''Importação da função reader do módulo CSV'''
from csv import reader

with open('lutador.csv') as arquivo:
    leitor_csv = reader(arquivo)     # O objeto retornado é um iterator
    next(leitor_csv)                 # Pular o cabeçalho
    for linha in leitor_csv:
        '''Cada linha é uma lista'''
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')


'''Importação da função DictReader'''
from csv import DictReader

with open('lutador.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # escolhendo delimitador fora do padrão que é a vírgula
    # leitor_csv = DictReader(arquivo)              # Exemplo sem delimitador
    # next(leitor_csv)                         # Não se usa porque no DictReader usa-se chave e valor. Diferente do exemplo acima: Reader
    for linha in leitor_csv:
        '''Cada linha é um OrderedDict'''
        print(f'{linha['Nomee']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

'''
Obs.:  por padrão o Reader e o DictReader usam a vírgula 
'''

