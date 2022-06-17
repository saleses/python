#######################################
#  ESTRUTURAS LÓGICAS E CONDICIONAIS  #
#######################################

# ESTRUTURAS CONDICIONAIS
# 1. if, else, elif

idade = 18
if idade < 18:
    print('Menor de idade')
    print(idade)
elif idade == 18:
    print('Tem 18 anos')
else:
    print('maior de idade')

'''
Observações:
- a identação é com base ao PEP8 (4 espaços)
- a condição finaliza com a linha em branco e sem identação
'''

# ESTRUTURAS LÓGICAS
# AND, OR, NOT, IS

'''
Operadores unários: not
Operadores binários: and, or, is

AND - conjunção
OR  - disjunção
NOT - negação
IS  - afirmação

Informação: 
nome.title() -> altera a primeira letra para maiúscula
'''

ativo = True
logado = True

# Testar a condição alterando o operador lógico
if ativo and logado:
    print('Bem-vindo Fulano!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail')

# Exemplo do operador IS -> aterar operador para teste
if ativo:  # é igual a -> if is ativo:
    print(ativo is True)

# Outro exemplo do operador is
if 1 is 1:
    print('Certa questão')
else: 
    print('Você não estudou')

