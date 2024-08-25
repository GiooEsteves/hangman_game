import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adiciona o diretório pai ao sys.path

from src.core.Word import Word
from src.core.Player import Player
from src.core.Hangman import Hangman

tentativa = 0           # declara e seta tentativas de jogadas como 0
letras_erradas = []     # lista para guardar as letras erradas que foram jogadas
letras_corretas = []    # lista para jogar as letras corretas que foram jogadas
Player = Player()
Word = Word()

word = Word.escolhe_palavra()  # seleciona a palavra da rodada
hideWord = []
for i in range(len(word)):
    hideWord.append("_") # valor inicial

Hangman = Hangman(Player, Word, tentativa, letras_erradas, letras_corretas, hideWord)

while True:  # loop principal
    Hangman.iniciar_jogo(Hangman.letra_certa, Hangman.letra_errada, Hangman.hideWord)  # iniciar o jogo
    letra = Player.chutar_letra()  # solicitar um chute do jogador
    Hangman.verificar_tentativa(letra, word)  # verificar a tentativa
    Hangman.exibir_palavra_atual(hideWord)  # printar o desenho agora com a letra inserida
    
    if Hangman.verificar_vitoria(hideWord) is True:  # verificar vitoria
        break
    if Hangman.verificar_derrota(word) is True:  # verificar derrota
        break