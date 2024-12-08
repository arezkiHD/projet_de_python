from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *
from Menu_Game import *
from EVENT import*
from PLAYER import*

from game_variables import *



# Initialize pygame
pygame.init()

# Screen dimensions

pygame.display.set_caption("My Game")
#map_matrix = MapLoader("facile").load_map()
map_matrix=new_map



# Player settings

font = pygame.font.SysFont("Arial", 50)

#game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")
#pygame.mixer.music.play(-1)








        


        
            




                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)
introduction_Game = introduction_game(intro_game_picture,win)
 #def __init__(self,units_positions,units_choice  , image_player,wall):

player1=Player(player1_pos,["unit_Spectre","unit_Clasian", "unit_Spectre","unit_Clasian"],False,intro_game_picture,wal1)
player2=Player(player2_pos,["unit_Spectre","unit_Clasian" , "unit_Spectre","unit_Clasian"],True ,intro_game_picture,wal1)

 

run = True
while run:
    pygame.time.delay(60)
    
    # Handle events
    EVENT = Event_manipulation(pygame.event.get(), run, player1.units,player2.units, [pygame.K_a, pygame.K_z, pygame.K_e, pygame.K_r ])
    EVENT.events_handler(player1,player2)
    run = EVENT.run
    
    # Clear the screen
    win.fill((105, 105, 105))
    
    # Handle introduction phase
    introduction_Game.affiche_introduction(pygame.mouse.get_pressed()) # to affiche the first picture of the introduction game 
    
    introduction_Game.chosing( number_of_player ,pygame.mouse.get_pos(),pygame.mouse.get_pressed() ) # to select on the menu if 2v2 or 3v3
    introduction_Game.chosing(unit_selection_player1 ,pygame.mouse.get_pos(),pygame.mouse.get_pressed())   # to select units 
    introduction_Game.chosing(unit_selection_player2 ,pygame.mouse.get_pos(),pygame.mouse.get_pressed())   # to select units 

    wal1.wall_drawing(introduction_Game, player2.units +player1.units)

    player2.play(introduction_Game)

    player1.play(introduction_Game)
    
    
    
    



    # Update display
    pygame.display.update()

pygame.quit()


print("=================>>", player1.play_times)
