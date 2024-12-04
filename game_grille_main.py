import pygame
import numpy as np 

from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *



# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 720
screan_height = 800
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
map_matrix = MapLoader("facile").load_map()



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
                if event.type == pygame.MOUSEBUTTONDOWN and introduction_game.move :
                    introduction_game.move = False
                
                
        



class introduction_game():
    def __init__ (self,introduction_pictures,moving_key, win = win) :
        self.introduction_pictures=introduction_pictures
        self.moving_key=moving_key
        self.move = True
        self.win = win 
    def affiche_introduction(self) :
        if self.move :           
            self.win.blit(self.introduction_pictures, (0,0, screan_width  , screan_height ))
            




                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
unit1 = unit(x, y, image_player, win,wal1,matrice)
unit2 = unit(x*5, y*5, image_player, win,wal1,matrice)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)
introduction_Game = introduction_game(intro_game_picture,pygame.MOUSEBUTTONDOWN)


units = [unit1 ,unit2]

# Game loop
run = True
while run:
    pygame.time.delay(60)
    EVENT = Event_manipulation(pygame.event.get(),run,units,[pygame.K_a , pygame.K_z, pygame.K_h], pygame.K_SPACE, pygame.K_h  )
    EVENT.events_handler(introduction_Game)
    run=EVENT.run
    win.fill((0,0,0))
    wal1.wall_drawing()

    for Unit in  units : 
        introduction_Game.affiche_introduction()   
        Unit.move()         
        Unit.draw_zone()
        Unit.draw(health_picture,introduction_Game)
        if Unit.remove :
            units.remove(Unit)
       
    
    pygame.display.update()

pygame.quit()
