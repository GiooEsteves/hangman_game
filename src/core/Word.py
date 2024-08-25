import random
from core.words import frutas

class Word():
    def escolhe_palavra(self):
        palavra = random.choice(frutas)
        return palavra

    def contem_letra(self, letra, palavra, hideWord):
        for i in range(len(palavra)):
            if letra == palavra[i]:
                hideWord[i] = letra  # adiciona letra certa à palavra
                return hideWord