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

Word = Word()
word = Word.escolhe_palavra()

Hangman = Hangman()
interface.interface(tentativa) # iniciar jogo

Player = Player()
letra = Player.chutar_letra()

if Word.contem_letra(letra, word): # if true
    interface.letra_certa()

"""
while tentativa <=7:  # loop principal
    

    letra = interface(tentativa)

    for letra in letras_erradas:
        pass

    tentativa += 1
"""