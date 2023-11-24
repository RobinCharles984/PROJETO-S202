#Searching paths in the database
class SearchPath :
    def __init__(self, database):
        self.db = database


    def getPathById(self, id: int):
        try:
            res = self.db.collection.find_one({"id": id})
            print(f"Caminho achado: {res}")
            return res
        except Exception as e:
            print(f"Caminho nao encontrado: {e}")
            return None
