import pygame
import numpy as np 

from UNIT_AREZKI import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 


# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 720
screan_height = 600
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")


# Player settings
x = 30
y = 30

font = pygame.font.SysFont("Arial", 50)

#game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")
#pygame.mixer.music.play(-1)



class Event_manipulation():
    def __init__(self, event,run, units,unit_key_selection,show_zone_key ):
        self.event = event 
        self.run= run 
        self.units = units 
        self.unit_key_selection= unit_key_selection
        self.show_zone_key =show_zone_key
        

    def events_handler(self):
        for event in self.event :
            if event.type == pygame.QUIT:
                self.run = False
            for i,unit in enumerate(self.units) :
                # here to manipulate the key sected for each unit 
                if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                    unit.is_selected = not unit.is_selected  

                if event.type == pygame.KEYDOWN and event.key == self.show_zone_key and unit.is_selected:
                    unit.toggle_zone()
                
                
# Initialize wall and player objects
wal1 = Wall(grass_image, "map.txt", tile_size, win, tile_size, tile_size)
unit1 = unit(x, y, image_player, win,matrice)
unit2 = unit(x*5, y*5, image_player, win,matrice)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)


# Game loop
run = True
while run:
    pygame.time.delay(60)
    EVENT = Event_manipulation(pygame.event.get(),run,[unit1, unit2],[pygame.K_a , pygame.K_z ], pygame.K_SPACE  )
    EVENT.events_handler()
    run=EVENT.run
    
    
        
    unit1.move() 
    unit2.move() 
        

    
    

    win.fill((0,0,0))
    wal1.wall_drawing()
    unit1.draw_zone()
    unit1.draw()

    unit2.draw_zone()
 
   
    unit2.draw()
    
    

    pygame.display.update()

pygame.quit()
