import pygame 
from UNIT_main import *
from Units_move_map import *


# ON part du principe que la map fait 25 par 45
""" 
-- UNITS :

- Clasian  : Zone de deplacement moyenne,                            degats moyens 25pnts/turn , santé moyenne 100 pnts
- Rapidzio : Zone de deplacement Large  ,                            degats Faible 15pnts/turn , santé Faible  75  pnts
- Berzerk  : Zone de deplacement Faibe  ,                            degats Eleve  40pnts/turn , santé Elevée  150 pnts
- Spectre  : Zone de deplacement Faibe mais tres Large sur les axes, degats Eleve 40 pnts/turn , santé Faible  75  pnts
"""

walk_right  = [pygame.image.load(os.path.join("pictures\humain_male",f"right ({i}).png")) for i in range(1,6) ]
walk_left   = [pygame.image.load(os.path.join("pictures\humain_male",f"left ({i}).png")) for i in range(1,6) ]
walk_up     = [pygame.image.load(os.path.join("pictures\humain_male",f"up ({i}).png")) for i in range(1,6) ]
walk_down   = [pygame.image.load(os.path.join("pictures\humain_male",f"down ({i}).png")) for i in range(1,5) ]
health_picture=[pygame.image.load(os.path.join("pictures\health_bar",f"health{i}.png")) for i in range(1,5) ]





class Units(Unit):
    def __init__(self, pos_x, pos_y, image_player, win, wall_rect, health_level, base_dammage, matrice_zone= matrice , walk_right=walk_right, walk_left=walk_left, walk_up = walk_up , walk_down = walk_down):
        Unit.__init__(self, pos_x, pos_y, image_player, win, wall_rect, health_level, base_dammage, matrice_zone= matrice , walk_right=walk_right, walk_left=walk_left, walk_up = walk_up , walk_down = walk_down)

# CHANGER L'UNIT EN AJOUTANT health_level, base_dammage, start_point = int[1 or 2]


class Player:

    """"
    Attributs :
        player_number : int : 1 ou 2
        __pos_x : list[int][4]
        __pos_y : list[int][4]
        image_player : 
        win
        wall_rect 
        start_point : int : 1 a 4
        matrice_zone= matrice (matrice de la map)
        walk_right=walk_right
        walk_left=walk_left
        walk_up = walk_up
        walk_down = walk_down
        number_of_units = 4
        game_mode = soit choix position joueur puis joueur sachant que joeur qui choisi en premier est choix random // choix random pour les deux


""" 
    
    def __init__(
        self, player_number, image_player, win, wall_rect, start_point, game_mode, points_depart, matrice_zone=None,
        walk_right=None, walk_left=None, walk_up=None, walk_down=None, number_of_units=4):

        self.player_number = player_number
        self.image_player = image_player
        self.win = win
        self.wall_rect = wall_rect
        self.start_point = start_point
        self.game_mode = game_mode
        self.number_of_units = number_of_units
        self.points_depart = points_depart

        # Obtenir les positions initiales pour chaque unité
        unit_positions = self.get_depart_positions(start_point, game_mode,points_depart)

        # Créer les unités avec leurs positions initiales et propriétés
    # Classian :    
        self.unit_Clasian = Units(
            unit_positions["Classian"][0], unit_positions["Classian"][1],
            image_player, win, wall_rect, health_level=100, base_dammage=25,
            matrice_zone=matrice_Clasian, walk_right=walk_right, walk_left=walk_left,
            walk_up=walk_up, walk_down=walk_down
        )

    # Rapidzio :
        self.unit_Rapidzio = Units(
            unit_positions["Rapidzio"][0], unit_positions["Rapidzio"][1],
            image_player, win, wall_rect, health_level=75, base_dammage=15,
            matrice_zone=matrice_Rapidzio, walk_right=walk_right, walk_left=walk_left,
            walk_up=walk_up, walk_down=walk_down
        )

    # Berzerk :
        self.unit_Berzerk = Units(
            unit_positions["Berzerk"][0], unit_positions["Berzerk"][1],
            image_player, win, wall_rect, health_level=150, base_dammage=40,
            matrice_zone=matrice_Berzerk, walk_right=walk_right, walk_left=walk_left,
            walk_up=walk_up, walk_down=walk_down
        )

    # Spectre :
        self.unit_Spectre = Units(
            unit_positions["Spectre"][0], unit_positions["Spectre"][1],
            image_player, win, wall_rect, health_level=75, base_dammage=40,
            matrice_zone=matrice_Spectre, walk_right=walk_right, walk_left=walk_left,
            walk_up=walk_up, walk_down=walk_down
        )



    def get_depart_positions(self, start_point, game_mode, points_depart):
        base_x, base_y = points_depart[start_point - 1]                 # points_depart[1 - 1] = points_depart[0] = [0, 0]

        # Ajustements en fonction du start_point et game_mode
            # Choix position de depart du joueur :  {Potentoellement a mettre dans game}
            # start_point == random(1,4) sachant que c'est joueur un puis deuxieme 
            # positions en cases, pas en pixels

        if game_mode == 1:  # Mode standard
            if start_point == 1:                # (0, 0)
                return {
                    "Classian": (base_x, base_y),
                    "Rapidzio": (base_x + 1, base_y),
                    "Berzerk": (base_x + 1, base_y + 1),
                    "Spectre": (base_x, base_y + 1),
                }
            elif start_point == 2:                # (0, 44)
                return {
                    "Classian": (base_x, base_y),
                    "Rapidzio": (base_x, base_y - 1),
                    "Berzerk": (base_x + 1, base_y - 1),
                    "Spectre": (base_x + 1, base_y),
                }
            elif start_point == 3:                # (44, 0)
                return {
                    "Classian": (base_x, base_y),
                    "Rapidzio": (base_x - 1, base_y),
                    "Berzerk": (base_x - 1, base_y + 1),
                    "Spectre": (base_x, base_y + 1),
                }
            elif start_point == 4:                # (44, 44)
                return {
                    "Classian": (base_x, base_y),
                    "Rapidzio": (base_x, base_y + 1),
                    "Berzerk": (base_x - 1, base_y + 1),
                    "Spectre": (base_x - 1, base_y),
                }
        elif game_mode == 2:  # Mode alternatif (hypothétique)
            print("game_mode error")

            # Ajouter des règles pour les autres start_point ici si nécessaire
        else:
            raise ValueError("Game mode non pris en charge ou start_point invalide")

        raise ValueError("Start_point invalide, doit etre entre 1 et 4 compis")














