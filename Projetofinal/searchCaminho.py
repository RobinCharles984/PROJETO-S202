
class SearchCaminho :
    def __init__(self, database):
        self.db = database


    def getCaminhoById(self, id: int):
        try:
            res = self.db.collection.find_one({"id": id})
            print(f"Caminho achado: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None
        # caminho = db.collection.find({"id": id})
        # return caminho