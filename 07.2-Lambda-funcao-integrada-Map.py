# LAMBDA - Map

'''
Map
- faz-se mapeamento de valores para função
- Tem-se:
    - dados iteráveis: a1, a2, a3, ..., an
    - funções: f(x)
- utiliza-se a função map(f, dados) para 'mapear' cada elemento dos dados e aplicar a função desejada
- Map Object: f(a1), f(a2), f(...), f(an)
'''

# importação de biblioteca
import math

# função para cálculo de área (raio: 'r')
def area(r):
    """Calcula a área de um círculo com raio 'r': """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

# lista
raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum de cálcular
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma com o uso de Map

# Map é uma função que recebe dois parâmetros: a função e o interável
# ou seja, o map faz o mapeamento de uma função e o retorna
areas = map(area, raios)  # Expressão do Map
print(list(areas))

print(type(areas))     # retorna o tipo Map Object
print(list(areas))     # converte para lista (pode ser tupla e etc)
'''
Prática: seria usado uma expressão lambda e não uma função. Veja abaixo: 
'''

# Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
'''
Obs.: Após utilização do Map, a lista neste caso, será zerada. A memória é limpa após utilização.
'''

# Exemplos: 
# Tupla declarada
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

# Fórmula de conversão de Celsius para Fareinheit -> f = 9/5 * c + 32
# Lambda -> dado[0] é a primeira posição e dado[1], a segunda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32 )

# conversão para lista
print(list(map(c_para_f, cidades)))

'''
No map somente é possível um parâmetro
'''

