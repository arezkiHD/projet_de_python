import pygame
import random
import os
from maps_data import*
import numpy as np
from map_loader import* 

screan_width = 1280
screan_height = 720

tile_size = 30

x = 30
y = 30

map_matrix = MapLoader("facile").load_map()



#image_player =  pygame.image.load(os.path.join("pictures\humain_male", 'up (2).png')) 
grass_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'grass.png')) 
water_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'water.png')) 
wall_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'wall.png')) 
potion_health = pygame.image.load(os.path.join("pictures\maps_picture", 'potion_health.png')) 
potion_power =  pygame.image.load(os.path.join("pictures\maps_picture", 'potion_power.png')) 

win = pygame.display.set_mode((screan_width, screan_height))

player1_pos = [[150, 90], [300, 90], [450, 90], [600, 90]]
player2_pos = [[150, 570], [300, 570], [450, 570], [600, 570]]






##################################################################################################################

# Clasian animations
walk_right_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"right ({i}).png")) for i in range(1, 7)]
walk_left_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"left ({i}).png")) for i in range(1, 7)]
walk_up_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"up ({i}).png")) for i in range(1, 7)]
walk_down_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"down ({i}).png")) for i in range(1, 7)]
menu_picture_Clasian = pygame.image.load("pictures\game_manipulation\Clasian.png")

# Spectre animations
walk_right_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"right ({i}).png")) for i in range(1, 8)]
walk_left_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"left ({i}).png")) for i in range(1, 8)]
walk_up_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"up ({i}).png")) for i in range(1, 8)]
walk_down_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"down ({i}).png")) for i in range(1, 8)]
menu_picture_Spectre = pygame.image.load("pictures\game_manipulation\Spectre.jpg")

# Rapidzio animations
walk_right_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"right ({i}).png")) for i in range(1, 5)]
walk_left_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"left ({i}).png")) for i in range(1, 5)]
walk_up_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"up ({i}).png")) for i in range(1, 5)]
walk_down_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"down ({i}).png")) for i in range(1, 5)]
menu_picture_Rapidzio = pygame.image.load("pictures\game_manipulation\Rapidzio.jpg")

# Berzerk animations
walk_right_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"right ({i}).png")) for i in range(1, 5)]
walk_left_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"left ({i}).png")) for i in range(1, 5)]
walk_up_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"up ({i}).png")) for i in range(1,5)]
walk_down_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"down ({i}).png")) for i in range(1, 5)]
menu_picture_Berzerk = pygame.image.load("pictures\game_manipulation\Berzerk .png")








health_picture=[pygame.image.load(os.path.join("pictures\health_bar",f"health{i}.png")) for i in range(1,6) ]
intro_game_picture=pygame.image.load("pictures\game_manipulation\into_pic.jpg")


number_of_player = {  # Here I stock information to choose on the menu to play 2v2 or 3v3
    "choice1": {
        "name": "2v2",
        "pos_x": screan_width  // 4,  
        "pos_y": screan_height // 2, 
        "picture": grass_image,
        "height_before": 80, 
        "width_before": 160, 
        "height_after": 160, 
        "width_after": 320,  
        "number_of_click_min": 1,
    },

    "choice2": {
        "name": "3v3",
        "pos_x": 3*screan_width //4,
        "pos_y": screan_height //2  ,  
        "picture": water_image,
        "height_before": 80,  
        "width_before": 160,  
        "height_after": 160,  
        "width_after": 320,  
        "number_of_click_max": 2,
    },
}


unit_selection_player1 = {
    "choice1": {
        "name": "unit_Clasian",
        "range_helath": "Clasian: Balanced unit with medium range, 25 dmg/turn, 100 HP",
        "Special": "Heals all allies (25% HP). Basic attack included",
        "pos_x": 100,  
        "pos_y": 100,  
        "picture": menu_picture_Clasian,
        "height_before": 120, 
        "width_before": 120,
        "height_after": 160,  
        "width_after": 160
    },
    "choice2": {
        "name": "unit_Spectre",
        "range_helath": "Spectre: Agile unit with long axis movement, 40 dmg/turn, 75 HP",
        "Special": "Reveal (uncovers hidden areas for one turn). Basic attack included",
        "pos_x": 100,  
        "pos_y": 250,  
        "picture": menu_picture_Spectre,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "choice3": {
        "name": "unit_Rapidzio",
        "range_helath": "Rapidzio: Long-range unit, 15 dmg/turn, 75 HP",
        "Special": "Long shot (high damage, unlimited range). Basic attack included",
        "pos_x": 100, 
        "pos_y": 400, 
        "picture": menu_picture_Rapidzio,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "choice4": {
        "name": "unit_Berzerk",
        "range_helath": "Berzerk: High-damage unit, 40 dmg/turn, 150 HP",
        "Special": "Mass attack (4x4 area, 20 dmg). Basic attack included",
        "pos_x": 100,  
        "pos_y": 550,  
        "picture": menu_picture_Berzerk,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "number of click": {
        "number_of_click_min_for_3v3": 2,
        "number_of_click_max_for_3v3": 5,
        "number_of_click_min_for_2v2": 2,
        "number_of_click_max_for_2v2": 4
    }
}

unit_selection_player2 = {
    "choice1": {
        "name": "unit_Clasian",
        "range_helath": "Clasian: Balanced unit with medium range, 25 dmg/turn, 100 HP",
        "Special": "Heals all allies (25% HP). Basic attack included",
        "pos_x": 100, 
        "pos_y": 550,  
        "picture": menu_picture_Clasian,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "choice2": {
        "name": "unit_Spectre",
        "range_helath": "Spectre: Agile unit with long axis movement, 40 dmg/turn, 75 HP",
        "Special": "Reveal (uncovers hidden areas for one turn). Basic attack included",
        "pos_x": 100, 
        "pos_y": 400,  
        "picture": menu_picture_Spectre,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "choice3": {
        "name": "unit_Rapidzio",
        "range_helath": "Rapidzio: Long-range unit, 15 dmg/turn, 75 HP",
        "Special": "Long shot (high damage, unlimited range). Basic attack included",
        "pos_x": 100, 
        "pos_y": 250,  
        "picture": menu_picture_Rapidzio,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "choice4": {
        "name": "unit_Berzerk",
        "range_helath": "Berzerk: High-damage unit, 40 dmg/turn, 150 HP",
        "Special": "Mass attack (4x4 area, 20 dmg). Basic attack included",
        "pos_x": 100, 
        "pos_y": 100,  
        "picture": menu_picture_Berzerk,
        "height_before": 120,
        "width_before": 120,
        "height_after": 160,
        "width_after": 160
    },
    "number of click": {
        "number_of_click_min_for_3v3": 5,
        "number_of_click_max_for_3v3": 8,
        "number_of_click_min_for_2v2": 4,
        "number_of_click_max_for_2v2": 6
    }
}








# information for each unit 

UNITS_INFORMATION = {
    "unit_Clasian": {
        "name" : "Clasian" ,
        "picture" : walk_down_Clasian[0] , 
        "matrice": matrice_Clasian,
        "walk_right": walk_right_Clasian,
        "walk_left": walk_left_Clasian,
        "walk_up": walk_up_Clasian,
        "walk_down": walk_down_Clasian,
        "walk_count" :6 ,        
        "max_health": 100,
        "base_damage" : 25,
    },
    "unit_Spectre": {
        "name" : "Spectre" ,
        "picture" : walk_down_Rapidzio[0] , 
        "matrice": matrice_Spectre,
        "walk_right": walk_right_Spectre,
        "walk_left": walk_left_Spectre,
        "walk_up": walk_up_Spectre,
        "walk_down": walk_down_Spectre,
        "walk_count" :7 ,
        "max_health": 100,
        "base_damage" : 25,
    },
    "unit_Rapidzio": {
        "name" : "Rapidzio" ,
        "picture" : walk_down_Rapidzio[0], 
        "matrice": matrice_Rapidzio,
        "walk_right": walk_right_Rapidzio,
        "walk_left": walk_left_Rapidzio,
        "walk_up": walk_up_Rapidzio,
        "walk_down": walk_down_Rapidzio,
        "walk_count" :4 ,
        "max_health": 100,
        "base_damage" : 25,

    },
    "unit_Berzerk": {
        "name" : "Berzerk" ,
        "picture" : walk_down_Berzerk[0] , 
        "matrice": matrice_Berzerk,
        "walk_right": walk_right_Berzerk,
        "walk_left": walk_left_Berzerk,
        "walk_up": walk_up_Berzerk,
        "walk_down": walk_down_Berzerk,
        "walk_count" :4 ,
        "max_health": 100,
        "base_damage" : 25,
    }
}




print("==================>",UNITS_INFORMATION.keys())