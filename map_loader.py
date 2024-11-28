from map import Map
from maps_data import facile_maps, moyen_maps, difficile_maps
import random

class MapLoader:
    @staticmethod
    def load_map(level):
        """
        Charge une carte aléatoire selon le niveau.
        Paramètres
            Niveau de difficulté ("facile", "moyen", "difficile").
        """
        if level == "facile":
            layout = random.choice(facile_maps)
        elif level == "moyen":
            layout = random.choice(moyen_maps)
        elif level == "difficile":
            layout = random.choice(difficile_maps)
        else:
            raise ValueError("Niveau invalide. Choisissez parmi 'facile', 'moyen', ou 'difficile'.")

        return Map(name=f"Carte {level.capitalize()}", layout=layout)