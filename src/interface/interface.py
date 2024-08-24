from interface.draw import drawHangman
from core.Hangman import Hangman

#Hangman = Hangman()

def interface(tentativa):
    print("\n********* Hangman *********")
    drawHangman(tentativa)

    print("Palavra: ", "\n")
    print("Letras erradas: ")
    print("Letras corretas: ")

def solicita_letra():
    letra = input("\nDigite uma letra: ")
    return letra

def letra_certa():
    print("Você acertou a letra!")
   
    #Hangman.exibir_palavra_atual()  # printar o desenho agora com a letra inserida

def letra_errada():
    print("Ops, esta letra não está na palavra!")
    # adionar a lista de palavras erradas

def letra_ja_jogada():
    print("Você já tentou essa letra. Escolha outra!\n")

def derrota():
    print("Você perdeu! A palavra era: ")
    # mostrar a palavra

def vitoria():
    print("Parabéns! Você acertou a palavra!")
