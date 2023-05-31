# TRABALHANDO COM DATA E HORA

# 1. Manipulação de data e hora
'''
Módulo built-in (integrado) de data e hora chamado datetime

'''

import datetime

'''ver opções '''
#print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna data e hora corrente
print(datetime.datetime.now())   # Formato: 2023-05-30 20:30:29.826914

# datetime.datetime(Ano, mês, dia, hora, minuto e milésimo)
print(repr(datetime.datetime.now()))


# replace() ajuste de data e hora
inicio = datetime.datetime.now()
print(inicio)    # Imprime data e hora atual

# Alteração do horário
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

# Criação de data e hora
evento = datetime.datetime(2019, 1, 1, 0)
print(evento)

print(type(evento))
print(type('31/12/2018'))

print(evento)

# Exemplos de recebimento de data e hora de usuários
nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
print(nascimento)
print(type(nascimento))  # Será impresso um tipo string

nascimento = nascimento.split('/')  # Vai pegar a entrada do tipo string e separadas com barra

# Conversão para inteiro e escolhendo a ordem das posições
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento)) 


# Acesso individual dos elementos de data e hora

print(evento.year)         # ano 
print(evento.month)        # mês 
print(evento.day)          # dia
print(evento.hour)         # hora
print(evento.minute)       # minuto
print(evento.second)       # segundo
print(evento.microsecond)  # microsegundo


print(dir(evento))   # Vendo possibilidades com o método 


# 2. Trabalhando com deltas de data e hora
'''
Deltas: trabalhando com diferença entre data e hora

data_inicial = dd/mm/yyyy 12:55:34.98765
data_final = dd/mm/yyyy   13:34:23.98765

data = data_final - data_inicial

'''
import datetime

# Data atual
date_hoje = datetime.datetime.now()

# Dia do aniversário
aniversario = datetime.datetime(2024, 27, 01, 0)

# Cálculo do delta
tempo_para_evento = aniversario - data_hoje

print(type(atempo_para_evento))
print(repre(atempo_para_evento))
print(tempo_para_evento)

print(tempo_para_evento.days)
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 3600 } horas...')

# Outro exemplo

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)   # Utilização da classe timedelta
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)


# 3. Métodos de data e hora

import datetime


# Diferenças: 
# Com now() pode-se especificar uma timezone (Fuso horário)
agora = datetime.datetime.now() # now
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.now()  # today
print(agora)
print(type(agora))
print(repr(agora))


# combine() -> Manutenção agendada para meia-noite 
manutenção = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))


# weekday() ->  Encontrar o dia da semana
# os dias da semana do método weekday() começam em 0, sendo o primeiro dia, segunda-feira
manutenção = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())


# Exemplo

aniversario = input('Qual dia de seu nascimento? dd/mm/yyyy')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um domingo ')


# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


hoje = datetime.datetime.today()
print(hoje)

# Documentação python: ver library datetime (tabela de strftime com formatos diversos)
hoje_formato = hoje.strftime('%d/%m/%y') 
hoje_formato = hoje.strftime('%d de %B de %Y')  # usado pela função acima

'''
Dica de library
pip install textblob

-> tradução de textos
'''
# Exemplo de uso da library textblob

import datetime
from textblob import TextBlob

# Com o TestBlob a função/método fica bem mais simples. (obs.: a informação é realtime, necessita da internet)
# não é recomendado fazer online pela demora
def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()
print(formata_data(hoje))



# Usando strptime (diferente de strftime)

nascimento = datetime.datetime.strptime('10/04/1998', '%d%m%Y')

print(nascimento)

nascimento = input('Digite sua data de nascimento (dd/mm/yyyy): ')
nascimento = datetime.datetime.strptime(nascimento, '%d%m%Y')
print(nascimento)


# Usando apenas a hora

almoco = datetime.time(12, 30, 0)  # Hora, minuto, segundo

# Marcando tempo de execução do código com timeit (comparação entre Loop, List Comprehension e Map)

import timeit

'''Loop for - Expressão que executará várias vezes para calcular o tempo'''
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

# Map
tempo = timeit.timeit('"-".join(map(str(n) for n in range(100)))', number=10000)


# Outro exemplo de timeit
import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

# Teste de tempo de uma função. Exemplo com a  partial()
print(timeit.timeit(functools.partial(teste, 2), number=10000))


