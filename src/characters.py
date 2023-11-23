## Creating Classes for Player, Enemies and NPC's
## Created by Tales Machado Prudente
 
#!!!!!!!!!!!!!!STUDY PYTHON OOP

class Player:
    def __init__(self, hp, xp, name, dmg, dfs, kills, paths = None):
        self.hp = hp
        self.xp = xp
        self.name = name
        self.dmg = dmg
        self.dfs = dfs
        self.kills = kills
        self.paths = paths
        
    def level_up(self):
        if self.xp <= xp_necessario:
            print('Subiu de nível!')
            self.nivel += 1 

##Enemies will attack player when they are at the same path and after every action
class Enemy:
    def __init__(self, hp, xp, name, dmg, dfs):
        self.hp = hp
        self.xp = xp
        self.name = name
        self.dmg = dmg
        self.dfs = dfs

#NPC's are interactive, can talk with player
#There's no way to defeat a NPC
class Npc:
    def __init__(self, name):
        self.name = name

    def message(message):
        print(message)