from game_variables import *




class introduction_game():
    def __init__ (self,introduction_pictures, win ) :
        self.introduction_pictures=introduction_pictures
        self.win = win 
        self.i = 0  # this one i use it because i will use the mouse press for other reason so i add the condition when i == 0  
        self.player = None   # to stock if 2v2 or 3v3
        self.unit = []    # to stock units for each player 
    def affiche_introduction(self) :
        if self.i==0 :           
            self.win.blit(self.introduction_pictures, (0,0, screan_width  , screan_height ))
            
            

    def chosing(self , choices ,corsur_position,press_mouse ) :
        cursor_x , cursor_y = corsur_position
        if self.i <=   choices["choice2"]["number_of_click_max"] and self.i  >=   choices["choice1"]["number_of_click_min"]  :
            for  __ ,choice_data in choices.items():
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
                    # Check for a click to select the option
                    if press_mouse[2]:  
                        self.i +=1 
                        if len(choices)==2 :
                            self.player = choice_data["name"]
                        elif len(choices) == 3 :
                            self.unit.append(choice_data["name"])

                            

                else:
                    # Draw the image at default size if not hovered
                    scaled_picture = pygame.transform.scale(
                        choice_data["picture"], 
                        (choice_data["width_before"], choice_data["height_before"])
                    )
                    self.win.blit(scaled_picture, (choice_data["pos_x"], choice_data["pos_y"]))

            


                                        



        
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

    
            
    
            