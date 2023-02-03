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


