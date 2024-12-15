#from UNIT_main import * 
#from WALL import *
from unit_add_work_imad import * 
from wall_adding_imad_code import * 
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
map_matrix = MapLoader("facile").load_map()
game_music = pygame.mixer.music.load("Arcade fast flow1.ogg")

pygame.mixer.music.play(-1)
                            
                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
introduction_Game = introduction_game(intro_game_picture,win)


player1=Player(player1_pos,False,intro_game_picture,wal1)
player2=Player(player2_pos,True ,intro_game_picture,wal1)


aff = affiche_resault()


 

run = True
mode = True 
while run:
    pygame.time.delay(60)
     # Clear the screen
    win.fill((0,0,0))


    
    # Handle events
    EVENT = Event_manipulation(pygame.event.get(), run, [pygame.K_a, pygame.K_z, pygame.K_e, pygame.K_r],[ pygame.K_q ,pygame.K_s ,pygame.K_d , pygame.K_d  ])
    EVENT.events_handler(player1,player2)
    run = EVENT.run
    
    introduction_Game.affiche_introduction_click_start_start(pygame.mouse.get_pressed()) # to affiche the first picture of the introduction game 
    #  def chosing_2v2_or_3v3(self,corsur_position,press_mouse , number_of_player= number_of_player   ) :
    introduction_Game.chosing_2v2_or_3v3( pygame.mouse.get_pos(),pygame.mouse.get_pressed() ) # to select on the menu if 2v2 or 3v3
    introduction_Game.chosing_units_for_player1(pygame.mouse.get_pos(),pygame.mouse.get_pressed() ,player1) 
    introduction_Game.chosing_units_for_player2(pygame.mouse.get_pos(),pygame.mouse.get_pressed() ,player2 ) 

    if introduction_Game.i == introduction_Game.last_click and mode :
        player1.initialize_units()
        player2.initialize_units()

        
        mode = False            
    wal1.wall_drawing(introduction_Game, player2.units + player1.units)
    if introduction_Game.i >= introduction_Game.last_click :
        aff.draw_results(player1 , player2 )


   


    

    player2.play(player1,introduction_Game,(255,0,0))
    player1.play(player2,introduction_Game,(0,255,0))             # Update display
    pygame.display.update()

pygame.quit()

print(player1.units_choice , player2.units_choice)


for u in player1.units + player2.units  :
    if isinstance(u, Classian) :
        print(" it is classian ")
 
    elif isinstance(u , Rapidzio) :
        print("it is rapidzio ")
     
    elif isinstance(u , Berzerk): 
        print("it is Berzerk")
    else :
        print("spectre  ")
 
  


