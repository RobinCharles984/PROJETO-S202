from searchCaminho import SearchCaminho
from database import Database
from paths import Path
from characters import Player, Enemy, Npc

#a cada nivel a quantidade necessaria de xp dobra~
#nivel 2 = 100xp
#após cada caminho escolhido, sugerir 3 outros caminhos

db_caminho = Database('projeto', 'caminhos')
xp_necessario = 100

class Caminho:
    def __init__(self, id, bichos, npcs):
        self.id = id
        self.bichos = bichos
        self.npcs = npcs



personagem1 = Player('juh', 0, 1, 0, [])       
caminho1 = Path(1, 10, 2)

caminho_escolhido = int (input('Qual caminho deseja escolher? \n1 - caminho 1'))
buscar = SearchCaminho(db_caminho)
buscar.getCaminhoById(caminho_escolhido)


# #fazer busca no bd pelo id
# if caminho_escolhido == caminho1.id:
#     personagem1.caminhos_escolhidos.append(caminho_escolhido)
#     personagem1.bichos_abatidos += caminho1.bichos
#     personagem1.xp += caminho1.bichos *10
#     if personagem1.xp >= xp_necessario:
#         personagem1.level_up()
#         xp_necessario *=2


# print(personagem1.nick)
# print(personagem1.bichos_abatidos)
# print(personagem1.nivel)
# print(personagem1.xp)
# print(personagem1.caminhos_escolhidos)
# print(xp_necessario)


