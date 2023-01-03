## Função integrada Filter

'''
Função filter()
- tem como objetivo filtrar dados de uma determinada coleção


'''
## Introdução com duas formas de calcular a média. Primeira com duas função e segunda com uma.
## Cálculo de média (02 funções)

# Tupla (a definição de tupla pode ser com parêntese ou não)
valores = 1, 2, 3, 4, 5, 6

# função sum() faz a soma de valores
# função len() retorna a quantidade, tamanho de valores; 6 valores neste caso
media = (sum(valores) / len(valores))
print(media)

## Cálculo de média importando biblioteca (01 função)

# Importação da biblioteca statistic; trabalha com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Cálculo da média com a função mean()
# mean(): realiza o cálculo da média de um conjunto de valores. Simplifica exemplo acima
media = statistics.mean(dados)

'''
Observação: 
- Assim como a função map(), a filter() recebe dois parâmetros: uma função e um iterável
- Exemplo abaixo:
'''

## FILTER()

# Realização do Filtro utilizando lambda
res = filter(lambda valor: valor > media, dados)  # LAMBDA (valor > media retorna True ou False)
print(list(res))                          # Lista resultados do filtro: maior que a média
print(f'Média: {media}')                  # impressão da média para facilitar a visualização

'''
Atenção:
- Assim como a função map(), após a utilização desta, o valor de 'res' sai da memória
- Verifique a saída abaixo: 
'''
print(list(res))                          # Valor vazio. 

# Remoção de dados faltantes

# Exemplo 1
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)         # imprime países com os dados faltantes, sem países

res = filter(None, paises)         # None em filter() remove os dados faltantes
print(list(res))

# Exemplo 2: feito com Lambda
# usando a variável 'paises' do exemplo acima
res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)      # outra forma de executar

# Imprime os países sem espaços faltantes
print(list(res))

'''
Diferença entre Map() e Filter()

- map(): recebe dois parâmetros - 01 função e 01 iterável - e retorna um objeto mapeando uma função para cada elemento do iterável. 
   - Retorna valores que não sejam True ou False
- filter(): recebe dois parâmetros - 01 função e 01 iterável - e retorna um objeto filtrando apenas os elementos de acordo com a função. 
   - Retorna valores booleanos, ou seja, True ou False. 
'''

# Exemplo 3: filtra os usuários inativos, sem tweets.  

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

'''
Atenção: uma lista vazia em booleano é igual a False
'''

# print(usuários)       # impressão na tela de todo os tweets

# cria lista com usuários que não fizeram tweets
# len(): quantidade de valores na lista
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Refatoração: outra forma
inativos = list(filter(lambda u: not u['tweets']) usuarios))
print(inativos)

# Combinação de filter() e map()

# lista de nomes
nomes = ['Vanessa', 'Ana', 'Maria']

# Criação de uma lista com as regras abaixo: 
# 1. Texto: Sua instrutora é + nome_instrutora
# 2. Nome deve conter apenas 5 caracteres

# lista
# Ordem de execução: primeiro o filter() e depois o map()
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
'''
Testar em terminal como exercício
'''

