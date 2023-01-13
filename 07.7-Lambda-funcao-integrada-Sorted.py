### Função integrada Sorted

'''
Sorted
- é utilizada para ordenar "qualquer" iterável. 
- gera SEMPRE uma lista com os elementos ordenados a partir de uma tupla, ou dicionário, ou set e outros a partir do que foi solicitado para ordenar

- pode ser utilizado com qualquer iterável

- Atenção: não é a função sort(). Esta é usada apenas em listas. 

'''
## Exemplos simples

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))   # Gera uma lista e ordena do menor para o maior
print(numero)            # Ordem original do Set '{}'. É mantida

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))

# Convertendo o resultado para set e tupla
print(set(sorted(numeros)))   # Convertendo para Set
print(tuple(sorted(numeros)))   # Convertendo para Tupla

## Exemplos 2 

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
print(sorted(usuarios, key=len))    # ordenação por tamanho
print(sorted(usuarios, key=lambda usuario: usuario["username"]))    
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))) # pela quantidade de tweets

# Exemplo 3
musicas = [
    {"titulo": "Star Wars Theme", "tocou": 3},
    {"titulo": "Tarrega", "tocou": 2},
    {"titulo": "Fiddler on the Roof", "tocou": 4},
    {"titulo": "Handel ", "tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))                # menos tocada para mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))  # mais tocada para menos tocada

