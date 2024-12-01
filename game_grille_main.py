import pygame
import numpy as np 

from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *
from Player import *



## Initialize pygame
pygame.init()
clock = pygame.time.Clock()  # Pour contrôler le FPS
FPS = 60

## Screen data :
screan_width = 720
screan_height = 600
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
map_matrix = MapLoader("difficile").load_map()
font = pygame.font.SysFont("Arial", 50)

#game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")
#pygame.mixer.music.play(-1)


# Initialize wall and player objects
wall_ = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)
#health_picture = ...  # Image de santé ou autre à définir

# --------------------------------------------- S t a r t   P l a y e r -----------------------------------------------

## Game mode :
game_mode_play = 1  # Pour l'instant, 1 seul mode dispo


## Coordonées ((x,y) en cases) de depart possibles :
points_depart = [[0, 0], [0, 44], [44, 0], [44, 44]]    

# Sélection de deux points aléatoires distincts 
start_p_1, start_p_2 = np.random.choice(len(points_depart), size=2, replace=False)  # Numero qui donne la position en coord, non pas une coord en soit

## Player 1 : Configuration et appel de ses unitées :
player_n_1 = Player(player_number = 1, image_player=image_player, win=win, wall_rect = wall_, start_point = start_p_1, game_mode = game_mode_play, 
        points_depart=points_depart, matrice_zone=None, walk_right=None, walk_left=None, walk_up=None, walk_down=None, number_of_units=4
        )

units_player_1 = [player_n_1.unit_Clasian, 
                  player_n_1.unit_Rapidzio,
                  player_n_1.unit_Berzerk, 
                  player_n_1.unit_Spectre]


## Player 2 : Configuration et appel de ses unitées :
player_n_2 = Player(player_number = 2, image_player=image_player, win=win, wall_rect = wall_, start_point = start_p_2, game_mode = game_mode_play, 
        points_depart=points_depart, matrice_zone=None, walk_right=None, walk_left=None, walk_up=None, walk_down=None, number_of_units=4
        )

units_player_2 = [player_n_2.unit_Clasian, 
                  player_n_2.unit_Rapidzio, 
                  player_n_2.unit_Berzerk, 
                  player_n_2.unit_Spectre]


## Unités des deux equipes : 
units = units_player_1 + units_player_2 


# --------------------------------------------- E V E N T  M A N I P U L A T I O N -----------------------------------------------
class EventManipulation:
    def __init__(self, event_list, units, unit_key_selection, show_zone_key):
        self.event_list = event_list  # Liste des événements capturés
        self.units = units            # Liste des unités à manipuler
        self.unit_key_selection = unit_key_selection  # Liste des touches pour sélectionner les unités
        self.show_zone_key = show_zone_key  # Touche pour afficher la zone

    def events_handler(self, run):
        for event in self.event_list:
            if event.type == pygame.QUIT:  # Quitter le jeu
                run = False
            
            # Gérer la sélection des unités et l'affichage de la zone
            for i, unit in enumerate(self.units):
                if event.type == pygame.KEYDOWN:
                    # Sélectionner/désélectionner une unité
                    if event.key == self.unit_key_selection[i]:
                        unit.is_selected = not unit.is_selected
                    
                    # Montrer ou cacher la zone si l'unité est sélectionnée
                    if event.key == self.show_zone_key and unit.is_selected:
                        unit.toggle_zone()
        
        return run  # Retourne l'état de `run` après traitement des événements             


# -------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- G A M E   L O O P ---------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

run = True

# Boucle principale du jeu
while run:
    # Capturer les événements
    events = pygame.event.get()

    # Manipulation des événements :
    event_handler = EventManipulation(events, units, [pygame.K_a, pygame.K_z], pygame.K_SPACE)
    run = event_handler.events_handler(run)

    # Effacer l'écran (mise de l'ecran en noir) :
    win.fill((0, 0, 0))

    # Dessin éléments de décor
    wall_.wall_drawing()

    # Gérer et afficher les unités
    for unit in units:
        unit.move()  # Mise à jour du mouvement
        unit.draw_zone()  # Dessiner la zone si activée
        unit.draw(health_picture)  # Dessiner l'unité avec son image

        # Supprimer les unités si elles sont marquées pour suppression
        if unit.remove:
            units.remove(unit)

    # Mettre à jour l'affichage
    pygame.display.update()

    # Contrôle des FPS
    clock.tick(FPS)

# Quitter Pygame
pygame.quit()

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
