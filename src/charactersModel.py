from random import randint
from bson import ObjectId
from pymongo import MongoClient

class CharactersModel:
    def __init__(self, database):
        self.db = database
    
    def create_character(self, name: str):
        try:
            res = self.db.collection.insert_one({
                "hp":randint(10,25), 
                "xp": 0, 
                "name": name,
                "dmg":randint(8,20),
                "dfs":randint(5,15),
                "kills":0
                })
            print("Player criado!")
            return res.inserted_id 
        #retorna o id -> salvar em uma variavel para utilizar nas outras funções
        except Exception as e:
            print(f"Ocorreu um erro criando player: {e}")
            return None
        

    def update_character(self, id: str, hp: int, xp: int, dmg: int, dfs: int, kills: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"hp": hp, "xp": xp, "dmg": dmg, "dfs": dfs, "kills": kills}})
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro atualizando player: {e}")
            return None
        
    
    def show_player_data(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print("Player:", res["name"])
            print("hp:", res["hp"])
            print("xp:", res["xp"])
            print("dmg:", res["dmg"])
            print("dfs:", res["dfs"])
            print("kills:", res["kills"])

        except Exception as e:
            print(f"Ocorreu um erro mostrando os dados do jogador: {e}")


    def find_all_characters(self):
        try:
            res = self.db.collection.find()
            return res
        except Exception as e:
            print(f"Ocorreu um erro mostrando os jogos existentes: {e}")
        