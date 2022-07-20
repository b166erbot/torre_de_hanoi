import curses
curses.initscr()
from time import sleep

from src.base import Base


def jogadas(numero):
    return (2 ** numero) - 1


class Tela:
    def __init__(self):
        self.tela = curses.newwin(24, 80, 0, 0)
        self.tela.refresh()

    
    def imprimir_buffer(self, textos: list[str]):
        for texto in textos:
            self.tela.addstr(texto + '\n')

    def limpar_tela(self):
        self.tela.erase()

    def atualizar(self):
        self.tela.refresh()


def proximo_passo(tela, base, movimento: list, dormir: int = 0.5):
    tela.imprimir_buffer(base.desenhar())
    tela.imprimir_buffer([f"\n\ncontagem = {base.movimentos}"])
    tela.atualizar()
    base.mover(*movimento)
    tela.limpar_tela()
    sleep(dormir)


def main():
    tela = Tela()
    base = Base()
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'primeira'])
    proximo_passo(tela, base, ['segunda', 'primeira'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    proximo_passo(tela, base, ['primeira', 'terceira'])
    proximo_passo(tela, base, ['primeira', 'segunda'])
    proximo_passo(tela, base, ['terceira', 'segunda'])
    tela.imprimir_buffer(base.desenhar())
    tela.imprimir_buffer([f"\n\ncontagem = {base.movimentos}"])
    pecas = 6
    tela.imprimir_buffer([f"dá pra se fazer a torre de hanoi com {jogadas(pecas)} jogadas caso ela tenha {pecas} peças."])
    tela.imprimir_buffer(["E eu não irei otimizar esse desafio."])
    tela.atualizar()
    sleep(9)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        curses.endwin()