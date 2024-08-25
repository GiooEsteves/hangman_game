from interface import interface

class Hangman():
    def __init__(self, Player, Word, tentativa_restante, letra_errada, letra_certa, hideWord):
        self.Player = Player
        self.Word = Word
        self.tentativa_restante = tentativa_restante
        self.letra_errada = letra_errada
        self.letra_certa = letra_certa
        self.hideWord = hideWord

    def setHideWord(self, letra, word):
        self.hideWord = self.Word.contem_letra(letra, word, self.hideWord) # testar
                   
    def setTentativaRestante(self, nova_tentativa):
        self.tentativa_restante = nova_tentativa

    def setLetraErrada(self, nova_letra_errada): # TESTAR
        self.letra_errada.append(nova_letra_errada) # adiciona a lista de letras erradas

    def setLetraCerta(self, nova_letra_certa): # TESTAR
        self.letra_certa.append(nova_letra_certa) # adiciona a lista de letras certas
    
    def iniciar_jogo(self, letras_certas, letras_erradas, hideWord):    
        interface.interface(self.tentativa_restante, letras_certas, letras_erradas, hideWord) # iniciar jogo

    def verificar_tentativa(self, letra, word):
        if letra in self.letra_certa + self.letra_errada:
            interface.letra_ja_jogada()
        elif letra in word: # testar se funciona
            self.setHideWord(letra, word) # testar
            self.setLetraCerta(letra)
            interface.letra_certa() 
        else:
            self.setTentativaRestante(self.tentativa_restante + 1)
            self.setLetraErrada(letra)
            interface.letra_errada() 

    def verificar_vitoria(self): # TESTAR
        if all(item.isalpha() for item in self.hideWord):
            interface.vitoria()
            return True 
        return False
        
    def verificar_derrota(self, word): #TESTAR
        if self.tentativa_restante == 7:
            interface.derrota(word)
            return True
        return False
       
    def exibir_palavra_atual(self, hideWord): 
        # puxar da interface
        pass 