import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.Word import Word
from src.core.Player import Player
from src.core.Hangman import Hangman
from interface import interface

tentativa = 0           # declara e seta tentativas de jogadas como 0
letras_erradas = []     # lista para guardar as letras erradas que foram jogadas
letras_corretas = []    # lista para jogar as letras corretas que foram jogadas
Player = Player()
Word = Word()

word = Word.escolhe_palavra()
Hangman = Hangman(Player, Word, tentativa, letras_erradas, letras_corretas)

while True:  # loop principal
    Hangman.iniciar_jogo(tentativa, word)  # iniciar o jogo
    letra = Player.chutar_letra()  # solicitar um chute do jogador
    Hangman.verificar_tentativa()  # verificar a tentativa
    # mostrar palavra atual
    # verificar vitoria
    Hangman.verificar_derrota()  # verificar derrota


if __name__ == "__main__":
    main()