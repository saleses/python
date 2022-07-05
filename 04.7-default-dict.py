# Módulo Collections -> são melhorias para utilização das coleções python dicionário
# Tema: Default Dict (padrão dicionários)

'''
O assunto estudado em dicionários é utilizado para Default Dict
OBSERVAÇÃO: coleções DefaultDict, como outras funcionalidades, são detalhadas no site python.org
'''
# revendo dicionário
#dicionario = {'curso': 'Programação em Python: Essencial'}
#print(dicionario)           # imprime chave e valor do dicionário
#print(dicionario['curso'])  # imprime o valor da chave

# Default Dict -> ao criar um dicionário utilizando o default dict, informamos um valor default.
# pode-se utilizar um lambda. Este valor será utilizado sempre que não houver um valor definido.
# Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído
# Lambda: são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores. 

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)     # resultado vazio

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)   # imprime a chave 'curso' e seu valor

print(dicionario['outro'])  # A chave 'outro' não existe. Retornará vazio
print(dicionario)           # Retorna as chave 'curso' e a chave 'outro' que é igual a vazio. E não KeyError

