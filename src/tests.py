import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.Word import Word
from src.core.Player import Player
from src.core.Hangman import Hangman

Player = Player()
Word = Word()
tentativa = 0
letras_erradas = []     # lista para guardar as letras erradas que foram jogadas
letras_corretas = []    # lista para jogar as letras corretas que foram jogadas
word = Word.escolhe_palavra()  # seleciona a palavra da rodada

hideWord = []
for i in range(len(word)):
    hideWord.append("_")

Hangman = Hangman(Player, Word, tentativa, letras_erradas, letras_corretas, hideWord)

while True:
    Hangman.iniciar_jogo(Hangman.letra_certa, Hangman.letra_errada, Hangman.hideWord) # iniciar jogo (FUNCIONANDO)
    letra = Player.chutar_letra() # solicitar um chute do jogador (FUNCIONANDO)
    Hangman.verificar_tentativa(letra, word) # verificar a tentativa
