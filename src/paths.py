class Path:
    def __init__(self, id, enemies, npcs):
        self.id = id
        self.enemies = enemies
        self.npcs = npcs

    def get_enemies(self):
        return self.enemies