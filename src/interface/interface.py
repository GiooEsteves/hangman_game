from interface.draw import drawHangman

def interface(tentativa, letras_certas, letras_erradas, hideWord):
    print("\n********* Hangman *********")
    drawHangman(tentativa)
    print("Palavra: ", hideWord, "\n") # mostrar o tamanho da palavra
    print("Letras erradas: ", letras_certas)
    print("Letras corretas: ", letras_erradas)
    print()
    
def solicita_letra():
    letra = input("\nDigite uma letra: ")
    return letra

def letra_certa():
    print("Você acertou a letra!")

def letra_errada():
    print("Ops, esta letra não está na palavra!")

def letra_ja_jogada():
    print("Você já tentou essa letra. Escolha outra!\n")

def derrota(word):
    print("Você perdeu! A palavra era: ", word)

def vitoria():
    print("Parabéns! Você acertou a palavra!")