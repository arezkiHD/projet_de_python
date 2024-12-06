from UNIT_main import * 
from WALL import *
from AFFICHE_GAME_RESAULT import * 
from map_loader import *
from Menu_Game import *

from game_variables import *



# Initialize pygame
pygame.init()

# Screen dimensions
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
    EVENT.events_handler(introduction_Game)
    run = EVENT.run
    
    # Clear the screen
    win.fill((105, 105, 105))
    
    # Handle introduction phase
    introduction_Game.affiche_introduction() # to affiche the first picture of the introduction game 
    
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