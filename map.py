class Map:
    TILE_EFFECTS = {
        0: "Wall",         # Infranchissable
        1: "Grass",        # Traversable
        2: "Forbidden",    # Réduit la santé
        3: "Shield"        # Bonus de santé/défense
    }

    def __init__(self, name, layout):
        """
        Initialise une carte.

        Paramètres:
            Nom de la carte.
            Matrice représentant les types de cases (0, 1, 2, 3).
        """
        self.name = name
        self.layout = layout

    def get_tile_effect(self, x, y):
        """
        Renvoie l'effet de la case à une position donnée.

        Paramètres
            Coordonnée X.
            Coordonnée Y.
        """
        if 0 <= y < len(self.layout) and 0 <= x < len(self.layout[0]):
            return self.TILE_EFFECTS.get(self.layout[y][x], "Unknown")
        return "Hors limites"

    def apply_tile_effect(self, unit, x, y):
        """
        Applique l'effet de la case à une unité.

        Paramètres
            L'unité affectée.
            Coordonnée X.
            Coordonnée Y.
        """
        effect = self.get_tile_effect(x, y)
        if effect == "Forbidden":
            unit.health -= 10  # Réduit la santé de l'unité
            print(f"{unit.name} perd 10 PV en traversant un passage interdit!")
        elif effect == "Shield":
            unit.health += 5  # Augmente la santé de l'unité
            print(f"{unit.name} gagne 5 PV grâce à un bouclier!")

    def display(self):
        for row in self.layout:
            print(" ".join(str(tile) for tile in row))