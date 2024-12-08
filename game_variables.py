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



image_player =  pygame.image.load(os.path.join("pictures\humain_male", 'up (2).png')) 
grass_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'grass.png')) 
water_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'water.png')) 
wall_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'wall.png')) 

win = pygame.display.set_mode((screan_width, screan_height))

player1_pos = [[300,120],[420,120],[720,120],[1020,120]]
player2_pos = [[300,600],[420,600],[720,600],[1020,600]]


# Load animations





walk_right=[pygame.image.load(os.path.join("pictures\humain_male",f"right ({i}).png")) for i in range(1,6) ]
walk_left=[pygame.image.load(os.path.join("pictures\humain_male",f"left ({i}).png")) for i in range(1,6) ]
walk_up=[pygame.image.load(os.path.join("pictures\humain_male",f"up ({i}).png")) for i in range(1,6) ]
walk_down=[pygame.image.load(os.path.join("pictures\humain_male",f"down ({i}).png")) for i in range(1,5) ]
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
    "picture" : image_player,
    "height_before" : 40,
    "width_before" : 100 ,
    "height_after" : 100,
    "width_after" : 200 ,
    "number_of_click_max" : 2,

      }, 
}
  
      


unit_selection_player1 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 and also stock for each one the chosen units 
    "choice1" : { 
        "name" : "unit_Clasian" ,  
        "pos_x" : 30, 
        "pos_y" : 300 ,
        "picture" : grass_image, 
        "height_before" : 90,
        "width_before" : 90 ,
        "height_after" : 180 ,
        "width_after" : 180 ,
        "number_of_click_min" :2 ,
        "matrice": matrice_Clasian ,
        "walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,
        

 
 },

    "choice2" :{ 
         
    "name" : "unit_Spectre" ,    
    "pos_x" : 330 , 
    "pos_y" : 300 ,
    "picture" : image_player,
    "height_before" : 90,
    "width_before" : 90 ,
    "height_after" : 180,
    "width_after" :  180 ,
    "number_of_click_max" : 5,
    "matrice ":matrice_Spectre,
    "walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,
      
      }, 




    "choice3" :{ 
     
"name" : "unit_Rapidzio" ,     
"pos_x" : 450 , 
"pos_y" : 300 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,
"matrice" : matrice_Rapidzio,
"walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,

  
  },

    "choice4" :{ 
     
 "name" : "unit_Berzerk" ,    
"pos_x" : 660 , 
"pos_y" : 500 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,
"matrice" : matrice_Berzerk, 
"walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,


  
  },  
}




unit_selection_player2 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 
    "choice1" : {   
        "name" : "unit_Clasian" , 
        "pos_x" : 30, 
        "pos_y" : 500 ,
        "picture" : grass_image, 
        "height_before" : 90,
        "width_before" : 90 ,
        "height_after" : 180 ,
        "width_after" : 180 ,
        "number_of_click_min" : 5,
        "matrice" : matrice_Clasian ,
        "walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,

 },

    "choice2" :{ 
         
    "name" : "unit_Spectre" ,    
    "pos_x" : 330 , 
    "pos_y" : 500 ,
    "picture" : image_player,
    "height_before" : 90,
    "width_before" : 90 ,
    "height_after" : 180,
    "width_after" :  180 ,
    "number_of_click_max" : 8,
    "matrice" :matrice_Spectre,
    "walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,
      
      }, 




    "choice3" :{ 
     
 "name" : "unit_Rapidzio" ,    
"pos_x" : 450 , 
"pos_y" : 500 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,
"matrice" :matrice_Rapidzio,
"walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,
  
  }, 


    "choice4" :{ 
     
 "name" : "unit_Berzerk" ,    
"pos_x" : 660 , 
"pos_y" : 500 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,
"matrice" : matrice_Berzerk, 
"walk_right" : walk_right ,
"walk_left" : walk_left,
"walk_up" : walk_up,
"walk_down" : walk_down ,


  
  }, 



}







# Matrices pour la zone de deplacement



  

random.shuffle(player1_pos)
print(player1_pos[0])