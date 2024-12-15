from game_variables import *

class introduction_game():
    def __init__ (self,introduction_pictures, win ) :
        self.introduction_pictures=introduction_pictures
        self.win = win 
        self.i = 0  # this one i use it because i will use the mouse press for other reason so i add the condition when i == 0  
        self.player_2v2_or_3v3 = None   # to stock if 2v2 or 3v3
        self.mouse_down = False
        self.last_click = 10000
 

    def affiche_text(self,texte,x_position, y_position,size,color=(255,255,255)):


        font = font = pygame.font.SysFont("robot", size)
        text_surface = font.render(texte, True, color)
        self.win.blit(text_surface, (x_position, y_position))
    
    
    
    def affiche_introduction_click_start_start(self,press_mouse) :
        if self.i==0 : 
            pygame.mixer.music.load("music\game_music.wav")
            pygame.mixer.music.play() 
            self.win.blit(self.introduction_pictures, (0,0, screan_width  , screan_height ))
            if press_mouse[2]:                   
                if not self.mouse_down:
                    self.i +=1
                    self.mouse_down = True   

    def chosing_2v2_or_3v3(self,corsur_position,press_mouse , number_of_player= number_of_player   ) :
        cursor_x , cursor_y = corsur_position
        number_of_click_max= number_of_player["choice2"]["number_of_click_max"]
        number_of_click_min = number_of_player["choice1"]["number_of_click_min"]
       

        if self.i <   number_of_click_max and self.i  >=  number_of_click_min  :
            self.affiche_text("Prepare for battle! Choose your team size: 2v2 or 3v3!", screan_width //2-screan_width//4,150 , 30)
            for  __ ,choice_data in number_of_player.items():
                # Check if the cursor is within the bounds of the current choice
                if (choice_data["pos_x"] <= cursor_x <= choice_data["pos_x"] + choice_data["width_before"] and
                    choice_data["pos_y"] <= cursor_y <= choice_data["pos_y"] + choice_data["height_before"]):
                    # Enlarge the image when hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_after"], choice_data["height_after"])
                    )
                    hover_x = choice_data["pos_x"] - (choice_data["width_after"] - choice_data["width_before"]) // 2
                    hover_y = choice_data["pos_y"] - (choice_data["height_after"] - choice_data["height_before"]) // 2
                    self.win.blit(scaled_picture, (hover_x, hover_y))
                    self.affiche_text(f" {choice_data['name']} ", hover_x+choice_data["width_before"]//2,hover_y+choice_data["height_after"] , 60)
                                                                          
                    if press_mouse[2]:  
                        pygame.mixer.music.load("Menu Selection Click.wav")
                        pygame.mixer.music.play()                                              

                        if not self.mouse_down:
                            pygame.draw.rect(self.win, (0, 0, 255), (hover_x, hover_y,choice_data["width_after"], choice_data["height_after"]), 2)
                            self.player_2v2_or_3v3 = choice_data["name"]
                            
                            self.i +=1
                            self.mouse_down = True
                              
                else:
                     # Draw the image at default size if not hovered
                     scaled_picture = pygame.transform.scale(
                         choice_data["picture"], 
                         (choice_data["width_before"], choice_data["height_before"])
                     )
                     self.win.blit(scaled_picture, (choice_data["pos_x"], choice_data["pos_y"]))
                if not press_mouse[2]:
                     self.mouse_down = False                   
   
    def chosing_units_for_player1(self   ,corsur_position,press_mouse,player, unit_selection_player1=unit_selection_player1 ) :
        cursor_x , cursor_y = corsur_position
        
        if self.player_2v2_or_3v3 is None : 
            return 
        
        if self.player_2v2_or_3v3 == "3v3" :

            number_of_click_max= unit_selection_player1["number of click"]["number_of_click_max_for_3v3"]
            number_of_click_min = unit_selection_player1["number of click"]["number_of_click_min_for_3v3"]

        elif self.player_2v2_or_3v3 == "2v2" :

            number_of_click_max= unit_selection_player1["number of click"]["number_of_click_max_for_2v2"]
            number_of_click_min = unit_selection_player1["number of click"]["number_of_click_min_for_2v2"]
        
        if self.i <   number_of_click_max and self.i  >=  number_of_click_min  :
            self.affiche_text("Player 1, pick your units for battle!", screan_width //2-screan_width//6,30 , 30)

            for  __ ,choice_data in unit_selection_player1.items():
                if choice_data == unit_selection_player1["number of click"] :
                    continue

                # Check if the cursor is within the bounds of the current choice
                if (choice_data["pos_x"] <= cursor_x <= choice_data["pos_x"] + choice_data["width_before"] and
                    choice_data["pos_y"] <= cursor_y <= choice_data["pos_y"] + choice_data["height_before"]):
                    # Enlarge the image when hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_after"], choice_data["height_after"])
                    )
                    hover_x = choice_data["pos_x"] - (choice_data["width_after"] - choice_data["width_before"]) // 2
                    hover_y = choice_data["pos_y"] - (choice_data["height_after"] - choice_data["height_before"]) // 2
                    pygame.draw.rect(self.win, (108, 108, 108), (0,hover_y ,screan_width, choice_data["height_after"]))
                    self.win.blit(scaled_picture, (hover_x, hover_y))
                    self.affiche_text(f" {choice_data['range_helath']} ",  choice_data["pos_x"]+350, choice_data["pos_y"]+30, 30)
                    self.affiche_text(f" {choice_data['Special']} ",  choice_data["pos_x"]+350, choice_data["pos_y"]+60, 30)





                    # Check for a click to select the option
                    if press_mouse[2]:
                        pygame.mixer.music.load("Menu Selection Click.wav")
                        pygame.mixer.music.play()                                                
                         
                        if not self.mouse_down:
                            pygame.draw.rect(self.win, (0, 255, 0), (hover_x, hover_y,choice_data["width_after"], choice_data["height_after"]), 2)
                            player.units_choice.append(choice_data["name"])

                            self.i +=1
                            self.mouse_down = True
                            print(self.i) 
                        

                            

                else:
                    # Draw the image at default size if not hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_before"], choice_data["height_before"])
                    )
                    self.win.blit(scaled_picture, (choice_data["pos_x"], choice_data["pos_y"]))
            
            if not press_mouse[2]:
                self.mouse_down = False

            


    def chosing_units_for_player2(self   ,corsur_position,press_mouse,player, unit_selection_player2=unit_selection_player2 ) :
        cursor_x , cursor_y = corsur_position
        
        if self.player_2v2_or_3v3 is None : 
            return 
        
        if self.player_2v2_or_3v3 == "3v3" :
            number_of_click_max= unit_selection_player2["number of click"]["number_of_click_max_for_3v3"]
            number_of_click_min = unit_selection_player2["number of click"]["number_of_click_min_for_3v3"]
            self.last_click= number_of_click_max
        elif self.player_2v2_or_3v3 == "2v2" :
            number_of_click_max= unit_selection_player2["number of click"]["number_of_click_max_for_2v2"]
            number_of_click_min = unit_selection_player2["number of click"]["number_of_click_min_for_2v2"]
            self.last_click= number_of_click_max
        
        if self.i <   number_of_click_max and self.i  >=  number_of_click_min  :
            self.affiche_text("Now Player 2, pick your units for battle!", screan_width //2-screan_width//6,30 , 30)

            for  __ ,choice_data in unit_selection_player2.items():
                if choice_data == unit_selection_player2["number of click"] :
                    continue
                # Check if the cursor is within the bounds of the current choice
                if (choice_data["pos_x"] <= cursor_x <= choice_data["pos_x"] + choice_data["width_before"] and
                    choice_data["pos_y"] <= cursor_y <= choice_data["pos_y"] + choice_data["height_before"]):
                    # Enlarge the image when hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_after"], choice_data["height_after"])
                    )
                    hover_x = choice_data["pos_x"] - (choice_data["width_after"] - choice_data["width_before"]) // 2
                    hover_y = choice_data["pos_y"] - (choice_data["height_after"] - choice_data["height_before"]) // 2
                    pygame.draw.rect(self.win, (108, 108, 108), (0,hover_y ,screan_width, choice_data["height_after"]))

                    self.win.blit(scaled_picture, (hover_x, hover_y))
                    self.affiche_text(f" {choice_data['range_helath']} ",  choice_data["pos_x"]+350, choice_data["pos_y"]+30, 30)
                    self.affiche_text(f" {choice_data['Special']} ",  choice_data["pos_x"]+350, choice_data["pos_y"]+60, 30)

                    if press_mouse[2]:   
                        pygame.mixer.music.load("Menu Selection Click.wav")
                        pygame.mixer.music.play()                       
                         
                        if not self.mouse_down:
                            pygame.draw.rect(self.win, (255, 0, 0), (hover_x, hover_y,choice_data["width_after"], choice_data["height_after"]), 2)
                            player.units_choice.append(choice_data["name"])
                            self.i +=1
                            self.mouse_down = True
                            
                        
                            
                else:
                    # Draw the image at default size if not hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_before"], choice_data["height_before"])
                    )
                    self.win.blit(scaled_picture, (choice_data["pos_x"], choice_data["pos_y"]))
            
            if not press_mouse[2]:
                self.mouse_down = False
                                                                                                                                                                                                                

                                                                                                                                                        
                                                                                                                                                    