# TUPLAS

'''
Tuplas (tuple)

a) tuplas são representadas por parênteses " ( ) " e listas colchetes "[]"
b) tuplas são imutáveis: após criada, não pode ser alterada: adicionar/remoção e etc.
c) operações matemáticas são possíveis se os valores forem do mesmo tipo. 
d) Aceita qualquer tipo de dados

'''
# tupla são representados por parênteses
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

# tuplas são definidas pela vírgula e não pelo parênteses
# o parênteses é a representação de uma tupla
tupla2 = (4)     # inteiro
tupla3 = (4,)    # tupla
tupla4 = 4,      # tupla
print(tupla2)
print(type(tupla2))
print(tupla3)
print(type(tupla3))
print(tupla4)
print(type(tupla4))

# Criar tupla a partir de um range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
# Cada elemento, separado por vírgula, e desempacotada em variáveis
tupla5 = ('Felipe X', 'Programa Python')
nome, profissao = tupla5
print(nome)
print(profissao)
'''
Ocorrerá erro caso o número de variáveis sejam diferentes de elementos
'''

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# Apenas se os valores forem todos inteiros ou reais
tupla6 = (1, 2, 3, 4, 5, 6)
print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))

# Concatenação de tuplas 
tupla7 = (1, 2, 3)
print(tupla7)

tupla8 = (4, 5, 6)
print(tupla8)

print(tupla7 + tupla8)  # Não funcionará, são imutáveis
print(tupla7)
print(tupla8)

tupla9 = tupla7 + tupla8  # gera uma nova tupla com valores das outras

# ou sobrescrevendo...

tupla7 = tupla7 + tupla8  # sobrescreve a variável e não alterar
print(tupla7)
print(tupla8)

# Contando elementos de uma tupla
tupla10 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Santo Antonio')    # Exemplo com string
print(escola)
print(escola.count('o'))

# Dicas: 
# 1. Deve-se utilizar tuplas quando não é necessário alterar dados de uma coleção
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
#meses.append('Novo meês')  # não é possível

# Acessando elemento de uma lista
print(meses[5])

# Imprimir meses da tupla
while i < len(meses):
    print(meses[1])
    1 = i + 1

# Descobrindo index de uma tupla
print(meses.index('Janeiro')
print(meses.index('Janeiro', 6)  # a partir do index 6

# Slice
# tupla[inicio:fim:passo]
print(meses[6:10])

'''
Observação: porque usar tupla? 
1. são mais rápidas do que listas, performance
2. deixam o código mais seguro (imutabilidade dá mais segurança)
'''

# cópia de uma tupla para outra
tupla11 = (1, 2, 3)
print(tupla)

nova = tupla   # na tupla não temos o Shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(outra)

# Visualização dos métodos da tupla
tupla12 = (1, 2, 3)
dir(tupla12)

