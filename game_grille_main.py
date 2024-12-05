import pygame
import numpy as np 

from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *



# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 1280
screan_height = 720



win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
#map_matrix = MapLoader("facile").load_map()
map_matrix=np.array(new_map)



# Player settings
x = 30
y = 30

font = pygame.font.SysFont("Arial", 50)

#game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")
#pygame.mixer.music.play(-1)



class Event_manipulation():
    def __init__(self, event,run, units,unit_key_selection,show_zone_key, introduction_move ):
        self.event = event 
        self.run= run 
        self.units = units 
        self.unit_key_selection= unit_key_selection
        self.show_zone_key =show_zone_key
        self.introduction_move = introduction_move 
        

    def events_handler(self,introduction_game):
        for event in self.event :
            if event.type == pygame.QUIT:
                self.run = False
            for i,unit in enumerate(self.units) :
                # here to manipulate the key sected for each unit 
                if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                    unit.is_selected = not unit.is_selected  

                if event.type == pygame.KEYDOWN and event.key == self.show_zone_key and unit.is_selected:
                    unit.toggle_zone()
                if event.type == pygame.MOUSEBUTTONDOWN and  introduction_game.i == 0:
                    introduction_game.i += 1  
                
                
        



class introduction_game():
    def __init__ (self,introduction_pictures,moving_key, win = win) :
        self.introduction_pictures=introduction_pictures
        self.moving_key=moving_key
        self.win = win 
        self.i = 0  # this one i use it because i will use the mouse press for other reason so i add the condition when i == 0  
    def affiche_introduction(self) :
        if self.i==0 :           
            self.win.blit(self.introduction_pictures, (0,0, screan_width  , screan_height ))
    def chosing_units_number_to_play(self , play_by_2 , play_by_3 ,corsur_position,press_mouse) :  # here i will use the same method to work with unit chosing so i will try to generlize it and creat son classes !!!!
           if self.i>0:
            pos_x_play_by_2 = 100 
            pos_y_play_by_2 = 100 
            pos_x_play_by_3 = 500 
            pos_y_play_by_3 =100
            [ corsur_position_x , corsur_position_y ] =corsur_position
            if self.i != 3:
                if corsur_position_x >=  pos_x_play_by_2-100 and corsur_position_x <= pos_x_play_by_2 + 100  and corsur_position_y >=  pos_y_play_by_2-100 and corsur_position_y <= pos_y_play_by_2 +100  :
                    play_by_2=pygame.transform.scale(play_by_2,(80,30))                
                    self.win.blit(play_by_2, (pos_x_play_by_2,pos_y_play_by_2, 80  , 30 )) 
                    if( press_mouse[2])  : # the right mouse press
                        self.i +=1

                else:
                    play_by_2=pygame.transform.scale(play_by_2,(50,30))                
                    self.win.blit(play_by_2, (pos_x_play_by_2,pos_y_play_by_2, 50  , 30 )) 

                if corsur_position_x >=  pos_x_play_by_3 and corsur_position_x <= pos_x_play_by_3 + 50  and corsur_position_y >=  pos_y_play_by_2 and corsur_position_y <= pos_y_play_by_2 +50 :
                    play_by_3=pygame.transform.scale(play_by_3,(80,30)) 
                    self.win.blit(play_by_3, (pos_x_play_by_3,pos_y_play_by_3, 80  , 30 ))
                    if( press_mouse[2])  :
                        self.i +=1


                else :
                    play_by_3=pygame.transform.scale(play_by_3,(50,30)) 
                    self.win.blit(play_by_3, (pos_x_play_by_3,pos_y_play_by_3, 50  , 30 ))

    
            


        


        
            




                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
unit1 = unit(x, y, image_player, win,wal1,matrice)
unit2 = unit(x+60, y, image_player, win,wal1,matrice)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)
introduction_Game = introduction_game(intro_game_picture,pygame.MOUSEBUTTONDOWN)


units = [unit1 ,unit2 ]     # here if one is active the other should not be active so like that our code will work properlly !!
 

run = True
while run:
    pygame.time.delay(60)
    
    # Handle events
    EVENT = Event_manipulation(pygame.event.get(), run, units, [pygame.K_a, pygame.K_z, pygame.K_h], pygame.K_SPACE, pygame.K_h)
    EVENT.events_handler(introduction_Game)
    run = EVENT.run
    
    # Clear the screen
    win.fill((105, 105, 105))
    
    # Handle introduction phase
    introduction_Game.affiche_introduction()
    introduction_Game.chosing_units_number_to_play(grass_image, image_player, pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    
    # Draw walls
    for Unit in units:
        wal1.wall_drawing(introduction_Game, Unit)

    # Draw and update all units
    units_to_remove = []  # Temporary list for units to remove
    for Unit in units:
        Unit.move()
        Unit.draw_zone()
        Unit.draw(health_picture, introduction_Game)
        if Unit.remove:
            units_to_remove.append(Unit)
    
    # Remove marked units after iteration
    for Unit in units_to_remove:
        units.remove(Unit)

    # Update display
    pygame.display.update()

pygame.quit()
