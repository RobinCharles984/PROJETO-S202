##imports
#from searchPath import SearchPath
from database import Database
from paths import Path
from characters import Player, Enemy, Npc
from charactersModel import CharactersModel
from random import Random
from characters import Fight

db_path = Database('projeto_final', 'caminhos')
db_character = Database('projeto_final', 'personagens')
characterModel = CharactersModel(db_character)

random = Random()


#class game
class Game:
    def __init__(self):
        pass

    #wholegame
    def launch(self):
        _input = str(input("O que deseja fazer? (1-Criar personagem,    2-Pesquisar personagem,     3- Mostrar todos os personagens): "))  

        enemy = []#creating enemy array

        paths = [ 
            Path(1, 0, 0),                  #Creating paths [id, enemies count(random), npcs(rando 0-1)]
            Path(2, 0, 1),
            Path(3, 1, 1),
            Path(4, random.randint(0, 2), random.randint(0, 1)),
            Path(5, random.randint(0, 2), random.randint(0, 1)),
            Path(6, random.randint(0, 2), random.randint(0, 1)),
            Path(7, random.randint(0, 1), 0)   
        ]
       
       #Creating player and inserting at database
        if _input == "1":
            _input = str(input("Insira o nome do seu personagem: "))
            player = Player(
                hp=random.randint(10, 25),
                xp=0,
                level=0,
                name=_input,
                dmg=random.randint(8, 20),
                dfs=random.randint(5, 15),
                kills=0,
                paths=[]
            )
            id = characterModel.create_character(
                player.hp,
                player.xp,
                player.level,
                player.name,
                player.dmg,
                player.dfs,
                player.kills
            )
            player.show_stats()
        
        if _input == 2:
            _input = str(input("Insira o nome do seu peronagem a ser buscado no bando de dados: "))
            p = characterModel.find_player(_input)
            id = p['_id']
            player = Player(p['hp'],p['xp'], p['level'], p['name'], p['dmg'], p['dfs'], p['kills'],[])
            player.show_stats()

        else:
            findAllCharacters = characterModel.find_all_characters()
            player = Player(p['hp'],p['xp'], p['level'], p['name'], p['dmg'], p['dfs'], p['kills'],[])
            print(p.name)
            exit()    
        ##Story starts

        #Path 0
        print("-------------------------------------------------")
        print("Voce acorda em uma floresta, o clima parece agradavel e o sol raia em seu rosto. Uma placa abaixo da sombra de uma arvore informa que existem sete caminhos lineares a se seguir ate chegar a cidade mais proxima, nao ha outro caminho a se escolher...")
        print("_________________________________________________")
        print("Tem um caminho a sua frente, o que deseja fazer?")
        player.paths = paths[0]
        while(True):
            _input = str(input("(Comandos: Continuar, Sair): "))
            if _input == "Continuar":
                player.paths = paths[1]
                break
            if _input == "Sair":
                exit(1)
            else:
                print("Comando nao encontrado, tente novamente!")
        
        #Path 1
        if(player.paths == paths[1] and paths[1].get_enemies() != None):
            for i in str(paths[1].get_enemies()):
                enemy= Enemy(hp=random.randint(3, 6), xp=random.randint(30, 80), name="Goblin", dmg=random.randint(4, 8), dfs=random.randint(0, 10))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[1] and paths[1].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[2]
                    break
                if _input == "Conversar":
                    npc = Npc("Andre")
                    npc.message("Vamos embora daqui!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[2]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")            

        #Path 2
        if(player.paths == paths[2] and paths[2].get_enemies() != None):
            for i in str(paths[2].get_enemies()):
                enemy = Enemy(hp=random.randint(5, 7), xp=random.randint(50, 100), name="PP Leao", dmg=random.randint(3, 10), dfs=random.randint(2, 7))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[2] and paths[2].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[3]
                    break
                if _input == "Conversar":
                    npc = Npc("Javes")
                    npc.message("Nos proximos caminhos, os inimigos tendem a ficar cada vez mais dificeis!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[3]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")     

        #Path 3
        if(player.paths == paths[3] and paths[3].get_enemies() != None):
            for i in str(paths[3].get_enemies()):
                enemy = Enemy(hp=random.randint(5, 7), xp=random.randint(50, 100), name="Jean", dmg=random.randint(3, 10), dfs=random.randint(2, 7))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[3] and paths[3].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[4]
                    break
                if _input == "Conversar":
                    npc = Npc("Javes")
                    npc.message("Nos proximos caminhos, os inimigos tendem a ficar cada vez mais dificeis!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[4]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!") 
 
        #Path 4
        if(player.paths == paths[4] and paths[4].get_enemies() != None):
            for i in str(paths[4].get_enemies()):
                enemy = Enemy(hp=random.randint(10, 20), xp=random.randint(70, 120), name="Aranha", dmg=random.randint(10, 15), dfs=random.randint(8, 13))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[4] and paths[4].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[5]
                    break
                if _input == "Conversar":
                    npc = Npc("Sid")
                    npc.message("Comando encontrado!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[5]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")        

        #Path 5
        if(player.paths == paths[5] and paths[5].get_enemies() != None):
            for i in str(paths[5].get_enemies()):
                enemy = Enemy(hp=random.randint(30, 50), xp=random.randint(100, 150), name="Little Tiger", dmg=random.randint(20, 35), dfs=random.randint(10, 18))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[5] and paths[5].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[6]
                    break
                if _input == "Conversar":
                    npc = Npc("Mondial")
                    npc.message("Ventania!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[6]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!") 

        #Path 6
        if(player.paths == paths[6] and paths[6].get_enemies() != None):
            for i in str(paths[6].get_enemies()):
                enemy = Enemy(hp=random.randint(30, 50), xp=random.randint(100, 150), name="Little Tiger", dmg=random.randint(20, 35), dfs=random.randint(10, 18))
                enemy.spawn()
                Fight(enemy, player)
                characterModel.update_character(id, player.hp, player.xp, player.level, player.dmg, player.dfs, player.kills)
        
        if(player.paths == paths[6] and paths[6].npcs != None):
            while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente e uma pessoa andando pela floresta.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Conversar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[7]
                    break
                if _input == "Conversar":
                    npc = Npc("Mondial")
                    npc.message("Ventania!")
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!")
        
        while(True):
                print("-------------------------------------------------")
                print("Voce ve mais um caminho a sua frente.")
                print("O que deseja fazer?")
                _input = str(input("(Comandos: Continuar, Sair): "))
                if _input == "Continuar":
                    player.paths = paths[6]
                    break
                if _input == "Sair":
                    exit(1)
                else:
                    print("Comando nao encontrado, tente novamente!") 

        #Path 7 - Ending
        print("Voce chegou no portao de uma cidade, a cidade parece tranquila... mas vazia!")
        print("O unico som que ecoa eh apenas o vento assobiando nas janelas das casas vazias... O que aconteceu aqui?!")
        print("-------------------------------------------------")
        
