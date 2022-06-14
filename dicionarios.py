# COLEÇÕES EM PYTHON - DICIONÁRIOS

'''
Os dicionários python, como em outras linguagens, são conhecidas como mapas
- são mapeamentos com atribuição de personalizada de uma chave e valor. Uma chave possuidora de valor
- Dicionários são coleções do tipo chave/valor
- nas listas e tuplas também existe chave/valor (índice e valor). Implícito
- no dicionários fica explícito, com chaves definidas pelo desenvolvedor
- representação: chaves e separados por dois-pontos. 
- exemplo: {chave:valor}
- pode-se utilizar listas e tuplas com dicionários

Quando utilizar dicionários?
Resposta: forma mais fácil e com melhor visualização de cada informação. 

'''
# Criação de dicionários
# Forma 1:

paises = {'br':'Brasil', 'eua':'Estados Unidos', 'py':'Paraguai'}  #  três elementos de chave/valor
print(paises)
print(type(paises))

# Forma 2: menos comum
paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai') 
print(paises)
print(type(paises))

# Acesso a elementos 
# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])    # acessando o elemento via chave
'''
caso a chave não exista, a saída será de KeyError
'''

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))    # Chave inexistente do .get resultará um tipo 

'''
Tipo None
- o tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como 
vazio. Porém, falar que é um tipo sem tipo é mais apropriado

obs.: o tipo None é SEMPRE especificado com a primeira letra maiúscula
obs.: o tipo None em python é sempre considerado False

Pode-se utilizar None quando queremos criar uma variável e inicializá-la como o tipo sem tipo antes de recebermos um valor final. Exemplo abaixo:
'''
numeros = None
print(numeros)
print(type(numeros))

numeros = 1.44, 2.74, 13.5
print(numeros)
print(type(numeros))  # será apresentado tipo tupla

russia = paises.get('ru')  # buscar valor por chave inexistente 'ru'

if russia:
    print('Encontrei o país')
else: 
    print('Não encontrei o país')


#Definindo um valor padrão caso não encontre um valor desejado

pais = paises.get('ru', russia)  # Valor padrão caso não exista valor, será russia

print('br' in paises)               # Resultado: True. Existe a chave/valor
print('ru' in paises)               # Resultado: False. Valor não existe
print('Estados Unidos' in paises)   # Resultado: False. Não é feito busca por valor

# Outro exemplo:
if 'ru' in paises:
    russia = paises['ru'] # resposta caso haja a chave. Senão, desconsidera

# Pode-se utilizar qualquer tipo de dados (int, float, string, boolean), inclusive lista, tupla dicionário, como chaves de dicionários

# Utilização de tuplas em dicionários
# As tuplas são boas opções para utilização como chaves de dicionários por serem imutáveis
localidades = {
        (35.6895, 39.6917): 'Escritório em Tókio',
        (40.7128, 74.0060): 'Escritório em Nova Iorque',
        (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em dicionários
# como as listas, os dicionários não são imutáveis
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2 
novo_dado = {'mai': 500}
receita.update('novo_dado')  # ou receita.update({'maio': 500})
print(receita)

# Atualizar dados em um dicionário
# Forma 1
receita['maio'] = 550
print(receita)

# Forma 2 
receita.update({'mai': 600})
print(receita)
'''
Obs.: 
1) a forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesa
2) em dicionários, NÃO podemos ter chaves repetidas
'''

#  Remover dados de um dicionário
receita2 = {'jan': 230, 'fev': 100, 'mar': 200}

# Forma 1: mais comum 
retorno = receita2.pop('mar')
print(retorno)
'''
OBS.:
1) não precisa SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
2) ao remover um objeto, o valor deste objeto é sempre retornado
'''

# Forma 2
del receita['fev']
print(receita)
'''
Obs.: 
1) neste caso o valor removido não é retornado
'''

# Comparação na utilização de dicionários, tuplas e listas

'''
Carrinhos de Compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço:
    Produto 2:
        - nome:
        - quantidade:
        - preco:
'''
# LISTAS
carrinho1 = []

produto1 = ['Bicicleta', 1, 2300.00]
produto2 = ['Atari', 1, 10000.00]

carrinho1.append(produto1)
carrinho1.append(produto2)

print(carrinho)
'''
Notas:
- com listas, tem-se que saber qual é o índice de cada informação no produto
'''

# TUPLAS
carrinho2 = []

produto1 = ('Bicicleta', 1, 2300.00)
produto2 = ('Atari', 1, 10000.00)

carrinho2 = (produto1, produto2)

3) Dicionário

carrinho3 = []

produto1 = {'Bicicleta', 1, 2300.00}
produto2 = {'Atari', 1, 10000.00}

carrinho3.append(produto1)
carrinho3.append(produto2)

'''
Obs.:
 - a visualização no resultado com o uso de dicionário é melhor (rever isso em conceito)
'''

# Métodos de dicionários
# dir({})

d = dict(a=1, b=2, c=3)  # criação de dicionário de forma não tão usual
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)
d.clear()
print(d)

# copiar dicionário para outro
# Forma 1 - Deep Copy

novo = d.copy()  # Deep Copy
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow Copy
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')   # a = chave e b = valor
print(outro)
print(type(outro)

# definição de chaves com um valor preestabelecido
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') # [] chaves , 'desconhecido' valor das chaves
print(usuario)
print(type(usuario))

'''
- O método fromkeys recebe dois parâmetros: um iterável e um valor
- gera para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
'''
# Outro exemplo -> diferança na definição acima: não a colchetes. Cada caracter é uma chave
veja = {}.fromkeys('teste', 'valor')   # para cada letra, não irá repeti-las, teremos uma chave. 
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')   # cada número do range - 1, 2, 3, ..., 10 - teremos uma chave
print(veja)


