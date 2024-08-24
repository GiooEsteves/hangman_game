import random
from core.words import frutas

class Word():
    def __init__(self):
        pass

    def escolhe_palavra(self):
        palavra = random.choice(frutas)
        return palavra

    def contem_letra(self, letra: str, palavra: str):
        for i in range(len(palavra)):
            if letra == palavra[i]:
                return True
    