from game_variables import *




class introduction_game():
    def __init__ (self,introduction_pictures, win ) :
        self.introduction_pictures=introduction_pictures
        self.win = win 
        self.i = 0  # this one i use it because i will use the mouse press for other reason so i add the condition when i == 0  
        self.player = None   # to stock if 2v2 or 3v3
        self.unit = []    # to stock units for each player 
        self.mouse_down = False
    def affiche_introduction(self,press_mouse) :
        if self.i==0 :           
            self.win.blit(self.introduction_pictures, (0,0, screan_width  , screan_height ))
            if press_mouse[2]:                   
                if not self.mouse_down:
                    self.i +=1
                    self.mouse_down = True 



            
            
            

    def chosing(self , choices ,corsur_position,press_mouse ) :
        cursor_x , cursor_y = corsur_position
        number_of_click_max= choices["choice2"]["number_of_click_max"]
        number_of_click_min = choices["choice1"]["number_of_click_min"]
        
        if self.i <   number_of_click_max and self.i  >=  number_of_click_min  :
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
                         
                        if not self.mouse_down:
                            pygame.draw.rect(self.win, (0, 255, 0), (hover_x, hover_y,choice_data["width_after"], choice_data["height_after"]), 2)
                            if len(choices)==2 :
                                self.player = choice_data["name"]
                            elif len(choices) == 3 :
                                self.unit.append(choice_data["name"])

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

            


                                        



        

    
    
    
    
    
    
    
   
   
   
    
    

    
    
    

    
    
    
    


    
    
    


    

    