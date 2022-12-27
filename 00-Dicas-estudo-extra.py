### ESTUDOS EXTRAS

## Imprimir na tela com laço FOR

# Forma 1 - usando laço FOR
for element in list:
    print(f'Imprima {element}')

# Forma 2 - usando método range()
for element in range(len(list)):
    print(f'Imprime {list[element]}')  # range() referencia-se pelos índice; diferença da forma 1

## SPLAT OPERATOR - Impressão de elementos de uma lista

# Forma 1 - usando splat operator (*)
print(*list)    # splat operator (*) faz com que imprima todos elementos de uma lista (na mesma linha?)

## Impressão em tela

# Forma 1 - imprimir lista no formato original
print(list)    # com colchetes e separando elementos por vírgula

# Forma 2 - usando o método join() 
print(' '.join(list))    # método join() dá a possibilidade de escolher um delimitador
print(' Eu gosto '.join(my_list))    # neste caso, uma string de saída para cada elemento

