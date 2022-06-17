# CONJUNTOS

'''
- Conjuntos é uma referência a Teoria de conjuntos em matemática
- Os conjuntos no python são denominados Sets. 
  - Sets (conjuntos) não possuem valores duplicados
  - Sets (conjuntos) não possuem valores ordenados
  - Elementos não são acessados por um índice, ou seja, não são indexados
- Usado quando precisa-se armazenar elementos, mas não há preocupação com ordenação. Não há chaves e valores. 
- São referenciados com chaves '{ }'

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python
 - um dicionário tem chave/valor
 - um conjunto tem apenas valor

'''
# Definição de conjuntos
# Forma 1
conjunto1 = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # números repetidos são desconsiderados
print(conjunto1)
print(type(conjunto1))
'''
obs.: Os números repetidos não geram erros. São desconsiderados
'''

conjunto2 = {1, 2, 3, 4, 5}
print(conjunto2)
print(type(conjunto2))

# Verificar existência de elemento
if 3 in conjunto1:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Visualização da não repetição e desordenação dos elementos de um conjunto
# Listas e tuplas aceitam duplicação de elementos. 
# Dicionários não replicam chaves
# Conjuntos não aceitam valores duplicados
# listas, tuplas e dicionários mantêm a ordem; conjuntos é aleatória

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 12, 1, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto3 = {99, 2, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto3} com {len(conjunto3)} elementos')

# Conjuntos aceitam tipos de dados diferentes
S = {1, 'b', True, 34, 22, 44}
print(S)
print(type(S))

# Iteração com Set (conjunto)
for valor in S:
    print(valor)

# Utilidades da coleção Sets

# Exemplo 1: formulário de cadastro de visitantes em museu com a coleção lista
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá'] 
print(len(cidades))      # retorna a quantidade de elementos da lista
print(len(set(cidades))) # retorna a quantidade de cidades existentes por usar o set, conjunto, em cidades

# Adicionar elementos a um conjunto
conjunto4 = {1, 2, 3}
conjunto4.add(4)  # adiciona elemento; duplicidade não gera erro, apenas desconsidera
print(conjunto4)

# Remoção de elementos

# Exemplo 1 .remove
print(conjunto4)
conjunto4.remove(3)     # não é índice, e sim valor; remove o valor
'''
Caso o valor não exista, será gerado error
'''

# Exemplo 2 .discard
print(conjunto4)
conjunto4.discard(2)

'''
Em conjuntos, nenhum valor é retornado como nos dicionários
'''

# Copiar um conjunto para outro
# Forma 1 - Deep Copy

conjunto5 = {1, 2, 3}
print(conjunto5)
novo = conjunto5.copy()
print(novo)

novo.add(4)

print(novo)
print(conjunto5)

# Forma 2 - Shallow Copy
conjunto6 = {1, 2, 3}

novo1 = conjunto6
novo1.add(4)

print(novo1)
print(conjunto6)

# Remoção de todos os itens de um conjunto
conjunto7 = {1, 2, 3}
print(conjunto7)

conjunto7.clear()
print(conjunto7)

# Métodos matemáticos de conjuntos

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Union - união entre dois conjuntos

# Forma 1 - melhor forma
unicos1 = estudantes_python.union(estudantes_java)  # poderia ser o inverso
print(unicos1)

# Forma 2 - utilizando o pipe ' | '
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Intersection - interseção entre os grupos

# Forma 1
ambos1 = estudantes_python.intersection(estudantes_java)  # poderia ser o inverso
print(ambos1)

# Forma 2 - utilizando o & comercial
ambos2 = estudantes_python | estudantes_java
print(ambos2)

# Diferença entre os conjuntos 
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# para valores inteiros ou reais

conjunto8 = {1, 2, 3, 4, 5, 6}
print(sum(conjunto8))
print(max(conjunto8))
print(min(conjunto8))
print(len(conjunto8))

