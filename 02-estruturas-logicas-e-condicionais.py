##  ESTRUTURAS LÓGICAS E CONDICIONAIS 

## 1. ESTRUTURAS CONDICIONAIS

# IF, ELSE, ELIF 

idade = 18
if idade < 18:
    print(f'Menor de idade: {idade}')
    print(type(idade))
elif idade == 18:
    print('Tem 18 anos')
else:
    print('maior de idade')

'''
Observações:
- a identação é com base ao PEP8 (4 espaços)
- a condição finaliza com a linha em branco e sem identação
'''

# 2. ESTRUTURAS LÓGICAS

# AND, OR, NOT, IS

'''
Operador unário: not
Operadores binários: and, or, is

and - conjunção
or  - disjunção
not - negação
is  - afirmação

Dica: função tittle() 
nome.title() -> altera a primeira letra para maiúscula
'''

##  Uso de variáveis booleanas em estrutura condicional
#   Declaração de variáveis
ativo = True
logado = True

# Teste de condição com conjunção 'and'
if ativo and logado:
    print('Bem-vindo Fulano!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail')

# Exemplo do operador IS -> aterar operador para teste
if ativo:                  # lê-se: se é igual a ativo:
    print(ativo is True)

# Outro exemplo do operador is
if 1 is 1:
    print('Certa questão')
else: 
    print('Você não estudou')

