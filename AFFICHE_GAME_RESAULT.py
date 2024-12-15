from game_variables import* 

x_of_black_screan = width_maps*tile_size




def affiche_text(self,texte,x_position, y_position,size,color=(255,255,255)):
    font = font = pygame.font.SysFont("robot", size)
    text_surface = font.render(texte, True, color)
    self.win.blit(text_surface, (x_position, y_position))

class affiche_resault:
    def __init__(self, win=win):
        
        self.win = win
        self.font = font = pygame.font.SysFont("Arial", 20)


    def draw_results(self,player1 , player2, potion_image = potion_power):
        
        
        x_offset = width_maps * tile_size + 60  # Start drawing past the game area
        y_offset = 120  # Initial Y offset for drawing
        spacing = 70  # Spacing between units
        
        # Draw Player 1 results
        player1_label = self.font.render("=========PLAYER1=========", True, (255, 255, 255))
        if player1.play_or_not : 
            width_player1_label , height_player1_label  = player1_label.get_size()
            pygame.draw.rect(self.win, (0,255, 0), (x_offset-10 , y_offset-10 , width_player1_label+20 , height_player1_label+20))



        self.win.blit(player1_label, (x_offset, y_offset))
        
        
        
        
                
        y_offset += 40  # Add space after the label

        for unit in player1.units:
            # Draw unit image
            unit_image = unit.inf["picture"] 
            image_width, image_height = [30 ,30 ]
            
            
            # Highlight selected unit
            if unit.is_selected:
                scaled_width = int(image_width * 1.5)
                scaled_height = int(image_height * 1.5)
                unit_image = pygame.transform.scale(unit_image, (scaled_width, scaled_height))
                pygame.draw.rect(self.win, (255, 255, 0), (x_offset - 5, y_offset - 5, scaled_width + 10, scaled_height + 10), 2)

            self.win.blit(unit_image, (x_offset, y_offset))
            
            # Draw unit name
             # Draw unit name
            name_text = self.font.render(f"{unit.name} :", True, (255, 255, 255))
            name_width, __ = name_text.get_size()
            health_level_value = self.font.render(f" health_level :{unit.health_level}", True, (255, 255, 255))
            helth_width, __ = health_level_value.get_size()
            self.win.blit(name_text, (x_offset + image_width + 10, y_offset + image_height // 4))
            self.win.blit(health_level_value, (x_offset + image_width + name_width + 10 , y_offset + image_height // 4))
            if unit.power_enable :
                self.win.blit(potion_image, (x_offset + image_width + name_width + helth_width + 10 , y_offset + image_height // 4 - 10))
            
            y_offset += spacing  # Adjust for next unit
        
        # Draw Player 2 results
        y_offset += 40  # Add space between players
        player2_label = self.font.render("=========PLAYER2=========", True, (255, 255, 255))
        if player2.play_or_not : 
            width_player2_label , height_player2_label  = player2_label.get_size()
            pygame.draw.rect(self.win, (255,0, 0), (x_offset-10 , y_offset-10 , width_player2_label+20 , height_player2_label+20))
        self.win.blit(player2_label, (x_offset, y_offset))



        y_offset += 40  # Add space after the label

        for unit in player2.units:

            # Draw unit image
            unit_image = unit.inf["picture"] # Default image
            image_width, image_height = [30 ,30 ]
            

            # Highlight selected unit
            if unit.is_selected:
                scaled_width = int(image_width * 1.2)
                scaled_height = int(image_height * 1.2)
                unit_image = pygame.transform.scale(unit_image, (scaled_width, scaled_height))
                pygame.draw.rect(self.win, (255, 255, 0), (x_offset - 5, y_offset - 5, scaled_width + 10, scaled_height + 10), 2)

            self.win.blit(unit_image, (x_offset, y_offset))
            
            # Draw unit name
            name_text = self.font.render(f"{unit.name} :", True, (255, 255, 255))
            name_width, __ = name_text.get_size()
            health_level_value = self.font.render(f" health_level :{unit.health_level}", True, (255, 255, 255))
            helth_width, __ = health_level_value.get_size()

            self.win.blit(name_text, (x_offset + image_width + 10, y_offset + image_height // 4))
            self.win.blit(health_level_value, (x_offset + image_width + name_width + 10 , y_offset + image_height // 4))
            if unit.power_enable :
                self.win.blit(potion_image, (x_offset + image_width + name_width + helth_width + 10 , y_offset + image_height // 4 - 10))

                
            
            



            
            y_offset += spacing  # Adjust for next unit





       

    