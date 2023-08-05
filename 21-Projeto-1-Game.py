# PROJETO GAME
'''
Estrutura do projeto game - arquivos e diretórios

1. Criar projeto game
2. Criar pacote (diretório) chamado models no qual estarão os módulos do projeto
   - arquivo __init__.py
   - arquivo calcular.py
3. arquivo game.py (software)
4. arquivo teste.py (teste de código)


'''

#####################
# Arquivo calcular.py

# import (módulo random, função randint)
from random import randint

class Calcular:

    '''criação de atributos: dificuldade, valor1, valor2, operacao, resultado '''
    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # valor aleatório entre 1 e 3 (1 = somar, 2 = diminuir, 3 = multiplicar)
        self.__resultado: int = self._gerar_resultado


    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade


    @property
    def valor1(self: object) -> int:
        return self.__valor1


    @property
    def valor2(self: object) -> int:
        return self.__valor2


    @property
    def operacao(self: object) -> int:
        return self.__operacao


    @property
    def resultado(self: object) -> int:
        return self.__resultado


    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação {op}'


    @property
    def _gerar_valor(self: object) -> int:
        # pass
       '''Implementação 2: gerando condição da função'''
        if self.dificuldade == 1:
            return randint(0, 10):
        elif self.dificuldade == 2:
            return randint(0, 100):
        elif self.dificuldade == 3:
            return randint(0, 1000):
        elif self.dificuldade == 4:
            return randint(0, 10000):
        else:
            return randint(0, 100000):    # deveria enviar msg de dificuldade inválida?


    @property
    def __gerar_resultado(self: object) -> int:
    #    pass
    '''Implementação 2: gerando condição da função'''
    if self.operacao == 1:   # somar
        return self.valor1 + self.valor2
    elif self.operacao == 2:  # diminuir
        return self.valor1 - self.valor2
    else:
        return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        if self.operacao == 2:
            return '-'
        if self.operacao == 3:
            return '*'


    @property
    def checar_resultado(self: object, resposta: int) -> bool:
    #    pass
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta correta')
            certo = True
        else:
            print('Resposta errada')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo


    @property
    def __mostrar_operacao(self: object) -> None:
    #    pass
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')



##################
# Arquivo teste.py
# Teste do software

# import
from models.calcular import Calcular    # importa no próprio projeto a classe calcular do arquivo calcular.py (/modules/calcular.py)

calc: Calcular = Calcular(1)

print(calc)



#################
# Arquivo game.py

from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)



def jogar(pontos: int) -> None:
    # pass -> usado na construção da estrutura do arquivo

    '''Implementação 1: criação da função no segundo momento: após construção de estrutura de todo o projeto'''
    def jogar(pontos: int) -> None:
        dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))


        calc: Calcular = Calcular(dificuldade)    # instância do objeto 


        print('Informe o resultado para a seguinte operação: ')
        calc.mostrar_operacao()


        resultado: int = int(input())


        if calc.checar_resultado(resultado):
            pontos += 1
            print(f'Você tem {pontos} ponto(s).')

        continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] '))


        if continuar:
            jogar(pontos)
        else:
            print(f'Você finalizou com {pontos} ponto(s).')
            print(f'Até a próxima!')



if __name__ == '__main__':
    main()
