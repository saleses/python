## Função integradda: Reduce()

'''
Atenção! 
- a partir do Python3+, a função reduce() não é mais uma função integrada (built-in). Consequentemente, é necessário importar e utilizá-la a partir do módulo 'functools'

Guido Van Rossum (criador do python): utilize a função reduce() se você realmente precisar dela. Em todo caso, 99% dos casos um loop 'for' é mais legível. 

Para entender o reduce()
- Veja a coleção de dados abaixo: 

dados = [a1, a2, a3, ..., an]

- têm-se uma função que recebe dois parâmetros: 
def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável. 

reduce(funcao, dados)

Como funciona: 
    Passo 1: res1 = f(a1, a2)   # aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final
    Passo3: res3 = f(res2, a4)
    ...
    ...
    ...
    Passo n: resN = f(resM, aN)

- Ou seja, em cada passo ele aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() irá retornar o resultado final. 

Alternativamente, poderíamos ver a função reduce() como: 
- funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

'''

## Exemplos
# Utilização da função reduce() para multiplicar todos os números de uma lista

from functools import reduce     # importar a função reduce() de functools

# dados iterável de uma lista
dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# criação de lambda com dois parâmetros
multi = lambda x, y: x * y

# Execução do reduce()
res = reduce(multi, dados)
print(res)


## Executando o exemplo acima com um loop 'for'
## Atenção! É melhor usar o loop e não o reduce().
res = 1
for n in dados:
    res = res * n

print(res)
'''
Principal diferença do reduce() para o map() e filter() ?
- o reduce() TRABALHA COM DOIS parâmetros. E não um
'''

