#Main launches or exit the game
#from database import Database
from game import Game

game = Game()
_input = str (input("Deseja iniciar o jogo? (S/N)"))

if _input =='S':
    game.launch()
    
