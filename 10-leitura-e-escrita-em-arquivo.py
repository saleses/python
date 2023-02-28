## Leitura e escrita em arquivo

# 1. Leitura de arquivos

'''
Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open()
- Forma mais simples: utilização de um parâmetro, o nome do arquivo. Retornando um _io.TextIOWrapper
- é com o objetio _io.TextIOWrapper que o trabalho é realizado

https://docs.python.org/3/library/functions.html#open

Obs.: por padrão, a função open() abre o arquivo para leitura. 

- o retorna de um arquivo, salvo em variável por exemplo, é uma string
'''

# Exemplo - function open()
# para teste, crie um arquivo .txt com conteúdo simples no corpo

arquivo = open('texto.txt')    # ver a necessidade de path na função ou não
print(arquivo)
print(type(arquivo))

'''
- Na saída terá o name, mode (rwx) encoding e tipo 

- Para ler o conteúdo de um arquivo, após sua abertura, função open(), usa-se a função read()
'''

# função read()
print(arquivo.read())

'''
Obs.: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse funciona como o 
cursor quando estamos escrevendo. Ou seja, ao imprimir o texto (comando print acima) ele vai estar posicionado para ler o conteúdo após o que foi impresso na tela. Se tiver lido tudo, não terá saída na tela porque nada mais existe para ser lido.

'''
print(arquivo.read())    # não terá nada na saída, porque o cursor estará no final do primeiro

# 2. Seek e Cursors

'''
seek()
- a função seek() é utilizada para movimentar o cursor pelo arquivo
- recebe um parâmetro para indicar a posição do cursor

'''
# Exemplos: crie arquivo texto.txt com 5 linhas de texto para realizar os comandos abaixo
arquivo = open('texto.txt')  # abre o arquivo em um objeto
print(type(arquivo))         
print(arquivo.read())        # lê o arquivo até o final; cursos estará no final do texto
print(arquivo.read())        # não haverá nada para ler; o cursor já está no final no texto

# Movimentando o cursor: função seek()
arquivo.seek(0)   # volta o cursor para a posição 0 (zero)
print(arquivo.read())     # leitura do arquivo a partir da posição atual do cursor, zero

arquivo.seek(22)          # leva cursor para possível 22
print(arquivo.read())     # lê informação a partir da posição 22


## Função readline() -> função lê arquivo linha a linha

print(arquivo.readline())   # sem parâmetro: imprime a primeira linha e joga o cursor para a próxima
print(arquivo.readline())   # imprime a segunda linha; ponto em que o cursor posicionou após o print anterior

# verificando o retorno da função readline
ret = arquivo.readline()
print(type(ret))       # tipo string
print(ret)             # imprime a linha
print(ret.split(' '))  # transforma em uma lista separando por espaço


## Função readlines

linhas = print(arquivo.readlines())   # retorna uma lista com cada linha como um índice
print(len(linhas))                    # retorna quantidade de linhas do arquivo
'''
Obs.: quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o programa. Essa conexão é chamada de streaming. Ao finalizar, deve-se finalizar a conexão com a função close()

Boa prática ao trabalhar com arquivo

1. abrir o arquivo
arquivo = open('texto.txt')

2. Manipulação desejada com o arquivo. Por exemplo: leitura
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto. Neste caso, retorna False

3. Fechar o arquivo
arquivo.close()

print(arquivo.closed)   # verifica novamente se o arquivo está aberto. Neste caso, retorna True

print(arquivo.read())   # ao ler o arquivo fechado, dará erro. Deve-se abrir novamente
'''

# Outro exemplo da função read() com parâmetro preenchido
arquivo = open('texto.txt')

print(arquivo.read(50))      # imprime 50 caracteres do arquivos

## 3. Bloco with
'''
Bloco with

Passos para trabalhar com arquivos
1. abrir arquivo
2. Manipular arquivo
3. Fechar arquivo

- o bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o 
bloco with

'''
# Exemplo 1: forma pythonica de manipular arquivos. 
with open('texto.txt') as arquivo:  # Traduzindo: com abertura do texto.txt, chame-o de arquivo e imprima linhas
    print(arquivo.readlines())
    print(arquivo.close)        # retorna False porque está dentro do bloco with

print(arquivo.read())     # a saída deste print imprime vazio. Foi fechado ao final do bloco with
print(arquivo.closed)     # retorna True porque o bloco with finalizou e fechou o arquivo

## 4. Escrevendo em arquivos

'''
Escrevendo em arquivos

Obs.: ao abrir um arquivo para leitura - open() -, não podemos realizar a escrita. Apenas ler. Desta forma,
se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever. 

Obs.: ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

- para escrever dados em um arquivos, após abri-lo utilizamos a função write().
- Esta função recebe uma string como parâmetro, caso contrário, por exemplo o tipo int, ocorrerá erro

Obs.: caso o arquivo já exista. Irá substituir o conteúdo para o novo escrito. Subscreve.
'''

# Exemplo de escrita - modo 'w' - write (escrita) em novo arquivo
# Forma pythonica

with open('novo.txt', 'w') as arquivo:     # o padrão é leitura 'r'. Para escrita, acrescentamos 'w'
    arquivo.write('Escrever dados em arquivo é muito fácil.'\n)
    arquivo.write('Podemos colocar quantas linhas quisermos.'\n)
    arquivo.write('Esta é a última linha.'\n)

'''
Mesmo exemplo substituíndo dados de um arquivos existente
'''

with open('novo.txt', 'w') as arquivo:  # escrevendo em arquivo existente
    arquivo.write('Novos dados.'\n)
    arquivo.write('Outros podemos colocar quantas linhas quisermos.'\n)
    arquivo.write('Mais está última linha.'\n)

# Exemplo não pythonico. 
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')
arquivo.close()

# Outro exemplo
with open('Thomas.txt', 'w') as arquivo:
    arquivo.write('São Thomas ' * 10)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair'
            arquivo.write(fruta)
            arquivo.write('\n')           # pula linha
            # outra forma de pular linha
            arquivo.write(fruta + '\n')   # curti mais; escrita e pula linha em uma linha apenas
        else:
            break    # finalizar o loop com a palavra 'sair'. Será True

## 5. Modos de arquivos

'''
Modos de abertura de arquivo

r -> read, default
w -> write, sobrescreve
x -> create exclusive; falha se existir
a -> adiciona linhas sem apagar conteúdo, acrescenta. Caso não exista, cria do zero e adiciona conteúdo
   - no modo 'a' - append -, não há controle do cursos? 
+ -> abre no modo de atualização: leitura e escrita

Site com a lista completa de modos de abertura
https://docs.python.org/3/library/functions.html#open

'''

# Exemplo com verificação de erro (arquivo existente ou não)
try:
    with open('arquivo_novo.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo. \n')
except FileExistsError:
    print('Arquivo existente!')

# Exemplo de abertura de arquivo, escrevendo em um arquivo existente (com conteúdo gerado anteriormente)
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair'
            # outra forma de pular linha
            arquivo.write(fruta + '\n')   # adiciona mais frutas no arquivo criado anteriormente
        else:
            break    # finalizar o loop com a palavra 'sair'. Será Tru


# Outro exemplo 
with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo! \n')
    arquivo.write('Nova linha \n')
    arquivo.write('Mais uma linha \n')

# Abre arquivo atualizando as informações (atenção no comportamento com outros modos de leitura: 'w', 'r'...) 
with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo! \n')
    arquivo.write('Nova linha \n')
    arquivo.write('Mais uma linha \n')

# 6. StringIO

'''
StringIO

Atenção: para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão. 
 - permissão de leitura -> para ler arquivo
 - permissão de escrita -> para escrever no arquivo

StringIO - Utilizado para ler e criar arquivos em memória
'''
# importação do StringIO
from io import StrinIO

mensagem = 'Este é apenas uma string normal'

# Pode-se criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')  -> essa linha e a de cima são equivalentes

# Criado o arquivo, pode-se utilizar o conhecimento estudado
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Pode-se inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())


# 7. Sistema de arquivos - Navegação

'''
Sistema de arquivos - navegação

- para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os 
os -> Operation System

Dica: 
1. pode-se abrir arquivo com programação python direto no console shell

'''
# Importando módulo os
import os

# getcwd() -> pega o current work diretctory - diretório de trabalho corrente
# Retorna o path absoluto
# Simular ao comando pwd
print(os.getcwd())

# para mudar o diretório, pode-se utilizar o chdir()
os.chdir('..')

# Exemplo de navegação com python
print(os.getcwd())   # path absoluto atual (exemplo: /home/antonio/curso/python)

os.chdir('..')
print(os.getcwd())   # path absoluto atual (exemplo: /home/antonio/curso)

os.chdir('..')
print(os.getcwd())   # path absoluto atual (exemplo: /home/antonio/)

os.chdir('..')
print(os.getcwd())   # path absoluto atual (exemplo: /home/)

os.chdir('..')
print(os.getcwd())   # path absoluto atual (exemplo: /)

# Pode-se checar se um diretório é absoluto ou relativo
print(os.path.isabs('/home/antonio'))  # True

## Obs.: para usuários Windows
## Se você, infelizmente, estiver utilizando um computador com Windows, 
## terá que ter cuidado ao verificar diretórios
## Exemplo abaixo (repare as barras com escapes)

print(os.path.isabs('C:\\Users\\geek'))  # Lord Sith

# Identificação do S.O
print(os.name)     # posix (Linux e Mac), nt (Windows)
print(os.uname())  # resposta com mais detalhes da informação da máquina

# importação do módulo sys
# import sys
print(sys.platform)  # mesmo resultado da importação do módulo os acima

# import os (já carregado acima)

# '/home/antonio/workspace/sistema'
print(os.getcwd())  # mostra o path absoluto

res = os.path.join(os.getcwd(), 'dir1', 'dir2')  # junta o dir1 e dir2 -> dir1/dir2

os.chdir(res)   # altera o diretório

print(os.getcwd())  # /home/antonio/workspace/sistema/dir1/dir2

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o 
# diretório que será juntado ao atual

# import os (importado acima)
# listdir() -> lista os arquivos e diretórios
print(os.listdir())
print(len(os.listdir()))  # qtde de diretórios e arquivos do diretório atual

# Pode-se listar arquivos e diretórios com mais detalhes com scandir()
print(list(os.scandir())
arquivos = list(os.scandir())

print(arquivos)
print(dir(arquivos[0]))

print(arquivos[0].inode())    # numeração deste elemento
print(arquivos[0].is_dir)     # é um diretório? False
print(arquivos[0].is_file)    # É um arquivo? True
print(arquivos[0].is_symlink) # É um link  simbólico? False
print(arquivos[0].is_name)    # NOme do arquivo
print(arquivos[0].is_path)    # Caminho até o arquivo
print(arquivos[0].is_stat)    # Estatísticas...

# obs.: ao utilizar a função scandir(), é importante fechá-la, assim que aberto o arquivo. 
scanner.close()   # fechando arquivo

# 8. Sistema de arquivos - manipulação

'''

'''
