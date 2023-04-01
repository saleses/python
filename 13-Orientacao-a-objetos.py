## Programação Orientada a Objetos (POO)

'''
Paradigmas de programação (metodologia de desenvolvimento de software)
- maneira de pensar o softwares
- quais paradigmas mais utilizados: estruturada, funcional e orientação a objeto
- os paradigmas dependem da linguagem
Exemplo:
- linguagem C: estruturada
- Java: orientação a objeto
- Python: multiparadigma -> estruturada, funcional e orientada a objeto

Objetivo da Orientação a objeto: 
- mapear objetos do mundo real para modelos computacionais

Principais componentes (elementos)
- classe: o modelo do objeto no mundo real representado computacionalmente
- atributos: características de um objeto. Uma classe pode ter nenhum ou vários atributos
- métodos: comportamento do objeto, ações do objetos (Atenção: métodos são as funções. Ou seja, método é uma função dentro de uma classe)
- construtor: é um método especial utilizado para criar objetos de uma determinada classe.
- objeto (ou instâncias): são elementos de um classe. Uma instância de um classe 

'''
# Comparação básica: Estruturada x OO

# Declaração de variável
# 1. Estruturada
nome = 'Bola'
print(type(nome))
numero = 10
print(type(numero))


# 2. Orientação a Objeto
class Produto:      # Criação da classe, modelo para um objeto
    pass            # será visto a frente, apenas para não gerar erro no código
                    # Não há método nem atributo

kimono = Produto()  # construtor padrão da classe produto, método especial para criação do objeto kimono. Repare: produto entre parênteses
print(kimono)       # Por não ter valor, apresentará apenas o espaço reservado em memória do objeto
print(type(kimono)) # Mostra que é uma classe do tipo Produto. Então o objeto é um tipo, instância de classe? 


## 1. Classes
'''
O que são classes?
- são modelos dos objetos do mundo real sendo representados computacionalmente

Classes contêm:
- atributos: representam as características do objeto. OU seja, pelos atributos conseguimos representar computacionalmente os estados do
  objeto. No caso do exemplo abaixo, lâmpada, possivelmente iríamos querer saber se a a lâmpada é 110 ou 220 volts, se é branca, amarela ou 
  outra cor, e etc.

- Mêtodos (funções): representam os comportamentos do objeto. OU seja, as ações que este objeto pode realizar no sistema. No caso da lâmpada,
  um comportamento é ligar e desligar. 

- Definição: class
- em python, é possível ter mais de uma classe em um único arquivo. 

Classes internas:
- int(), list(), set() -> exemplos de uma classe interna. São em minúsculas
- para as classes criadas pelo desenvolvedor, use sempre o padrão CamelCase

Obs.: ao planejar um software e definimos as classes do sistema, chamamo-as de entidades. Ou seja, entidade é uma classe. 
'''
# Exemplo: sistema para automatizar o controle de lâmpadas de uma residência

class Lampada:        # Declaração da classe -> por padrão, o nome da classe inicia com maiúscula em cada palavra (Camel Case)
    pass              # utilizado quando existe um bloco não utilizado


lamp = Lampada()

print(type(lamp))
# Fim do bloco da classe 

