## Creating Classes for Player, Enemies and NPC's
## Created by Tales Machado Prudente
 
#!!!!!!!!!!!!!!STUDY PYTHON OOP

#imports
from random import Random

#variable
random = Random()

class Player:

    def __init__(self, hp: int, xp: int, level: int, name: str, dmg: int, dfs: int, kills: int, paths: int = None):
        self.hp = hp
        self.xp = xp
        self.level = level
        self.name = name
        self.dmg = dmg
        self.dfs = dfs
        self.kills = kills
        self.paths = paths
        
    def get_xp(self, xp):
        xp_levelup = 100
        self.xp += xp
        if self.xp >= xp_levelup:
            self.level += 1
            xp_levelup = (xp_levelup * self.level)
            self.hp += (self.hp * (self.level * 0.25))
            self.dmg += (self.dmg * (self.level * 0.25))
            self.dfs += (self.dfs * (self.level * 0.25))
            print("Subiu de nivel!!!")
            print("Nome: ", self.name)
            print("HP: ", self.hp)
            print("Level: ", self.level)
            print("Damage: ", self.dmg)
            print("Defense: ", self.dfs)
            print("Kills: ", self.kills)
        

##Enemies will attack player when they are at the same path and after every action
class Enemy:
    def __init__(self, hp: int, xp: int, name: str, dmg: int, dfs: int):
        self.hp = hp
        self.xp = xp
        self.name = name
        self.dmg = dmg
        self.dfs = dfs

    def spawn(self):
        print("Um ", self.name, " apareceu!")

class Fight():
    def __init__(self, e:Enemy, p: Player):
        while(e.hp != 0 and p.hp != 0):
            ("-------------------------------------------------")
            command = str(input("Comandos: Atacar, Defender, Fugir: "))

            if command == "Atacar":
                e.hp -= p.dmg
                print(e.name, " tomou ", p.dmg, "!")
            if command == "Defender":
                damage = (e.dmg - (p.dfs * random.random()))
                p.hp -= damage
                print("Voce tomou ", damage, " de dano!")
            if command == "Fugir":
                print("Voce fugiu!")
                break
            if e.hp <= 0:
                ("-------------------------------------------------")
                print("Voce derrotou ", e.name, " e recebeu ", e.xp, " XP!")
                ("-------------------------------------------------")
                p.get_xp(e.xp)
                break

#NPC's are interactive, can talk with player
#There's no way to defeat a NPC
class Npc:
    def __init__(self, name: str):
        self.name = name

    def message(self, message):
        print("_________________________________________________")
        print(self.name, ": ", message)
        print("_________________________________________________")