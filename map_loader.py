from maps_data import *
import random 

class MapLoader:
    def __init__ (self,level ):
        self.level = level 

    def load_map(self):
        """
        Charge une carte aléatoire selon le niveau.
        Paramètres
            Niveau de difficulté ("facile", "moyen", "difficile").
        """
        if self.level == "facile":
            matrix_map = random.choice(facile_maps)
        elif self.level == "moyen":
            matrix_map = random.choice(moyen_maps)
        elif self.level == "difficile":
            matrix_map = random.choice(difficile_maps)
        else:
            raise ValueError("Niveau invalide. Choisissez parmi 'facile', 'moyen', ou 'difficile'.")

        return matrix_map