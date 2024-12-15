from unit_add_work_imad import * 
from wall_adding_imad_code import * 
from AFFICHE_GAME_RESAULT import * 
from Menu_Game import *
from EVENT import*
from PLAYER import*
from game_variables import *

pygame.init()



pygame.display.set_caption("My Game")

                            
                
# Initialize wall and player objects
wal1 = Wall(grass_image, map_matrix, tile_size, win, tile_size, tile_size)
introduction_Game = introduction_game(intro_game_picture,win)


player1=Player(player1_pos,False,intro_game_picture,wal1)
player2=Player(player2_pos,True ,intro_game_picture,wal1)


aff = affiche_resault()   # to affiche resaults 


 

run = True
mode = True 
while run:
    pygame.time.delay(60)
     # Clear the screen
    win.fill((0,0,0))


    
    # Handle events
    EVENT = Event_manipulation(pygame.event.get(), run, [pygame.K_a, pygame.K_z, pygame.K_e, pygame.K_r],[ pygame.K_q ,pygame.K_s ,pygame.K_d , pygame.K_f  ])
    EVENT.events_handler(player1,player2)
    run = EVENT.run
    
    introduction_Game.affiche_introduction_click_start_start(pygame.mouse.get_pressed()) # to affiche the first picture of the introduction game 
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
        
    if introduction_Game.i == introduction_Game.last_click : # to entre only one time !!
        game_music = pygame.mixer.music.load("music\game_music.wav")
        pygame.mixer.music.play(-1)
        introduction_Game.i += 1


   


    

    player2.play(player1,introduction_Game,(255,0,0))
    player1.play(player2,introduction_Game,(0,255,0)) 

    if  introduction_Game.i >= introduction_Game.last_click :
        
        print("someone win ")
        if player1.player_winner(player2) == 2 :
            win.fill((0,0,0))
            font = pygame.font.SysFont("robot", 60)
            text_surface = font.render("THE WINNER IS PLAYER 1 ", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screan_width // 2, screan_height // 2))
            win.blit(text_surface, text_rect)
        elif player2.player_winner(player2) == 2 :
            win.fill((0,0,0))
            font = pygame.font.SysFont("robot", 60)
            text_surface = font.render("THE WINNER IS PLAYER 2 ", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screan_width // 2, screan_height // 2))
            win.blit(text_surface, text_rect)
            


    pygame.display.update()

pygame.quit()
