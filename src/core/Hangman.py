from interface import interface

class Hangman():
    def __init__(self, Player, Word, tentativa_restante, letra_errada, letra_certa):
        self.Player = Player
        self.Word = Word
        self.tentativa_restante = tentativa_restante
        self.letra_errada = letra_errada
        self.letra_certa = letra_certa

    def setTentativaRestante(self, nova_tentativa):
        self.tentativa_restante = nova_tentativa

    def setLetraErrada(self, nova_letra_errada):
        self.letra_errada.append(nova_letra_errada) # adiciona a lista de letras erradas

    def setLetraCerta(self, nova_letra_certa):
        self.letra_certa.append(nova_letra_certa) # adiciona a lista de letras certas
    
    def iniciar_jogo(self, palavra):    
        interface.interface(self.tentativa_restante, palavra) # iniciar jogo

    def verificar_tentativa(self, letra, word):
        if self.Word.contem_letra(letra, word):
            self.setLetraCerta(letra)
            interface.letra_certa()
        else:
            self.setTentativaRestante(self.tentativa_restante + 1)
            self.setLetraErrada(letra)
            interface.letra_errada()

    def verificar_vitoria(self):
        # se vitoria:
            interface.vitoria()

    def verificar_derrota(self):
        if self.tentativa_restante == 7:
            interface.derrota()
            return False
        
    def exibir_palavra_atual(self):
        # implementar as letras jogadas certas na palavra exibida
        pass 