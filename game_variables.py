import pygame
import numpy as np 
import os

screan_width = 1280
screan_height = 720

tile_size = 30

x = 30
y = 30


image_player =  pygame.image.load(os.path.join("pictures\humain_male", 'up (2).png')) 
grass_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'grass.png')) 
water_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'water.png')) 
wall_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'wall.png')) 



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
  
      


unit_selection_player1 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 
    "choice1" : { 
        "name" : "U1" ,  
        "pos_x" : 30, 
        "pos_y" : 300 ,
        "picture" : grass_image, 
        "height_before" : 90,
        "width_before" : 90 ,
        "height_after" : 180 ,
        "width_after" : 180 ,
        "number_of_click_min" :2 ,

 },

    "choice2" :{ 
         
    "name" : "U2" ,    
    "pos_x" : 330 , 
    "pos_y" : 300 ,
    "picture" : image_player,
    "height_before" : 90,
    "width_before" : 90 ,
    "height_after" : 180,
    "width_after" :  180 ,
    "number_of_click_max" : 5,
      
      }, 




    "choice3" :{ 
     
"name" : "U3" ,     
"pos_x" : 630 , 
"pos_y" : 300 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,

  
  }, 
}




unit_selection_player2 = {  # here i stock information to chose on the menu to play 2 vs 2 or 3 vs 3 
    "choice1" : {   
        "name" : "U1====" , 
        "pos_x" : 30, 
        "pos_y" : 500 ,
        "picture" : grass_image, 
        "height_before" : 90,
        "width_before" : 90 ,
        "height_after" : 180 ,
        "width_after" : 180 ,
        "number_of_click_min" : 5,

 },

    "choice2" :{ 
         
    "name" : "U2====" ,    
    "pos_x" : 330 , 
    "pos_y" : 500 ,
    "picture" : image_player,
    "height_before" : 90,
    "width_before" : 90 ,
    "height_after" : 180,
    "width_after" :  180 ,
    "number_of_click_max" : 8,
      
      }, 




    "choice3" :{ 
     
 "name" : "U3====" ,    
"pos_x" : 630 , 
"pos_y" : 500 ,
"picture" : image_player,
"height_before" : 90,
"width_before" : 90 ,
"height_after" : 180,
"width_after" :  180 ,

  
  }, 
}


  




#c=number_of_player["choice2"]["number_of_click_max"]
#print(c)
#for __, b in unit_selection.items() :
#    print(b)