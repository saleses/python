# COLEÇÕES MAPAS

'''
Mapas - são conhecidos em python como dicionários
- dicionários são representados por chaves - { }

'''
receita = {'jan': 100,'fev': 200,'mar': 400}
print(receita)
print(type(receita))

# Interar sobre dicionários
for chave in receita:
    print(chave)            # Imprime a chave

for chave in receita:
    print(receita[chave])   # Imprime o valor da chave

# outro exemplo
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessar as chaves utilizando .keys -> modo pythônico
print(receita)         # facilitar visualização
print(receita.keys())  # impressão das chaves

for chave in receita.keys():  # utilizando loop for
    print(receita[chave])

# Acessando valores -> modo pythônico
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor_Máximo*, Valor_Mínimo*, Tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

