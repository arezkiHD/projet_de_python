from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *
from Menu_Game import *
from EVENT import*

from game_variables import *



# Initialize pygame
pygame.init()

# Screen dimensions
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
#map_matrix = MapLoader("facile").load_map()
map_matrix=np.array(new_map)



# Player settings

font = pygame.font.SysFont("Arial", 50)

#game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")
#pygame.mixer.music.play(-1)








        


        
            




                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
unit1 = unit(x, y, image_player, win,wal1,matrice)
unit2 = unit(x+60, y, image_player, win,wal1,matrice)
texte1 = afiche_texte("hello",1000,30,(255,255,255),win)
introduction_Game = introduction_game(intro_game_picture,win)



units = [unit1 ,unit2 ]     # here if one is active the other should not be active so like that our code will work properlly !!
 

run = True
while run:
    pygame.time.delay(60)
    
    # Handle events
    EVENT = Event_manipulation(pygame.event.get(), run, units, [pygame.K_a, pygame.K_z, pygame.K_h], pygame.K_SPACE, pygame.K_h)
    EVENT.events_handler()
    run = EVENT.run
    
    # Clear the screen
    win.fill((105, 105, 105))
    
    # Handle introduction phase
    introduction_Game.affiche_introduction(pygame.mouse.get_pressed()) # to affiche the first picture of the introduction game 
    
    introduction_Game.chosing( number_of_player ,pygame.mouse.get_pos(),pygame.mouse.get_pressed() ) # to select on the menu if 2v2 or 3v3
    introduction_Game.chosing(unit_selection_player1 ,pygame.mouse.get_pos(),pygame.mouse.get_pressed())   # to select units 
    introduction_Game.chosing(unit_selection_player2 ,pygame.mouse.get_pos(),pygame.mouse.get_pressed())   # to select units 

    



   
    
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


print(introduction_Game.player)
print(introduction_Game.unit)