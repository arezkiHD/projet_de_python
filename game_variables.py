import pygame
import random
import os
from maps_data import*
import numpy as np

screan_width = 1280
screan_height = 720

tile_size = 30

x = 30
y = 30



#image_player =  pygame.image.load(os.path.join("pictures\humain_male", 'up (2).png')) 
grass_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'grass.png')) 
water_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'water.png')) 
wall_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'wall.png')) 

win = pygame.display.set_mode((screan_width, screan_height))

player1_pos = [[300,120],[420,120],[720,120],[1020,120]]
player2_pos = [[300,600],[420,600],[720,600],[1020,600]]





##################################################################################################################

import pygame
import os

# Clasian animations
walk_right_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"right ({i}).png")) for i in range(1, 7)]
walk_left_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"left ({i}).png")) for i in range(1, 7)]
walk_up_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"up ({i}).png")) for i in range(1, 7)]
walk_down_Clasian = [pygame.image.load(os.path.join("pictures\direction_chara", "Clasian", f"down ({i}).png")) for i in range(1, 7)]

# Spectre animations
walk_right_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"right ({i}).png")) for i in range(1, 8)]
walk_left_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"left ({i}).png")) for i in range(1, 8)]
walk_up_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"up ({i}).png")) for i in range(1, 8)]
walk_down_Spectre = [pygame.image.load(os.path.join("pictures\direction_chara", "spectre", f"down ({i}).png")) for i in range(1, 8)]

# Rapidzio animations
walk_right_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"right ({i}).png")) for i in range(1, 5)]
walk_left_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"left ({i}).png")) for i in range(1, 5)]
walk_up_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"up ({i}).png")) for i in range(1, 5)]
walk_down_Rapidzio = [pygame.image.load(os.path.join("pictures\direction_chara", "rapidzio", f"down ({i}).png")) for i in range(1, 5)]

# Berzerk animations
walk_right_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"right ({i}).png")) for i in range(1, 5)]
walk_left_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"left ({i}).png")) for i in range(1, 5)]
walk_up_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"up ({i}).png")) for i in range(1,5)]
walk_down_Berzerk = [pygame.image.load(os.path.join("pictures\direction_chara", "berzerk", f"down ({i}).png")) for i in range(1, 5)]





health_picture=[pygame.image.load(os.path.join("pictures\health_bar",f"health{i}.png")) for i in range(1,6) ]
intro_game_picture=pygame.image.load("pictures\game_manipulation\into_pic.jpg")







number_of_player = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 
    "choice1" : {
        "name" : "2v2" ,
        "pos_x" : 100, 
        "pos_y" : 100 ,
        "picture" : grass_image, 
        "height_before" : 40,
        "width_before" : 100 ,
        "height_after" : 100,
        "width_after" : 200 ,
        "number_of_click_min" : 1 ,

 },

    "choice2" :{ 
    "name" : "3v3" ,   
    "pos_x" : 400, 
    "pos_y" : 100 ,
    "picture" : water_image,
    "height_before" : 40,
    "width_before" : 100 ,
    "height_after" : 100,
    "width_after" : 200 ,
    "number_of_click_max" : 2,

      }, 
}
  
      

unit_selection_player1 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 and also s
    "choice1": { 
        "name": "unit_Clasian",
        "pos_x": 30, 
        "pos_y": 300,
        "picture": walk_up_Clasian[0], 
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
    },
    "choice2": { 
        "name": "unit_Spectre",    
        "pos_x": 330, 
        "pos_y": 300,
        "picture": walk_up_Spectre[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
    },
    "choice3": {
        "name": "unit_Rapidzio",     
        "pos_x": 450,
        "pos_y": 300,
        "picture": walk_up_Rapidzio[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
    },
    "choice4": {
        "name": "unit_Berzerk",    
        "pos_x": 660,
        "pos_y": 500,
        "picture": walk_up_Berzerk[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
    },
    "number of click": {
        "number_of_click_min_for_3v3": 2,
        "number_of_click_max_for_3v3": 5,
        "number_of_click_min_for_2v2": 2,
        "number_of_click_max_for_2v2": 4
    }
}

unit_selection_player2 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 
    "choice1": {
        "name": "unit_Clasian", 
        "pos_x": 30,
        "pos_y": 500,
        "picture": grass_image, 
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180,
        "number_of_click_min": 5
    },
    "choice2": {
        "name": "unit_Spectre",    
        "pos_x": 330,
        "pos_y": 500,
        "picture": walk_up_Spectre[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180,
        "number_of_click_max": 8
    },
    "choice3": {
        "name": "unit_Rapidzio",    
        "pos_x": 450,
        "pos_y": 500,
        "picture": walk_up_Rapidzio[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
    },
    "choice4": {
        "name": "unit_Berzerk",    
        "pos_x": 660,
        "pos_y": 500,
        "picture": walk_up_Berzerk[0],
        "height_before": 90,
        "width_before": 90,
        "height_after": 180,
        "width_after": 180
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
        "matrice": matrice_Clasian,
        "walk_right": walk_right_Clasian,
        "walk_left": walk_left_Clasian,
        "walk_up": walk_up_Clasian,
        "walk_down": walk_down_Clasian,
        "walk_count" :6 ,
    },
    "unit_Spectre": {
        "matrice": matrice_Spectre,
        "walk_right": walk_right_Spectre,
        "walk_left": walk_left_Spectre,
        "walk_up": walk_up_Spectre,
        "walk_down": walk_down_Spectre,
        "walk_count" :7 ,
    },
    "unit_Rapidzio": {
        "matrice": matrice_Rapidzio,
        "walk_right": walk_right_Rapidzio,
        "walk_left": walk_left_Rapidzio,
        "walk_up": walk_up_Rapidzio,
        "walk_down": walk_down_Rapidzio,
        "walk_count" :4 ,

    },
    "unit_Berzerk": {
        "matrice": matrice_Berzerk,
        "walk_right": walk_right_Berzerk,
        "walk_left": walk_left_Berzerk,
        "walk_up": walk_up_Berzerk,
        "walk_down": walk_down_Berzerk,
        "walk_count" :4 ,
    }
}




print(UNITS_INFORMATION.keys())