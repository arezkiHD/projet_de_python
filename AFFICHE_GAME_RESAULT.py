from game_variables import* 

x_of_black_screan = width_maps*tile_size

#class afiche_texte():   # it can be abstrect !!
#    def __init__(self, color,win ):
#        
#        
#        
#        self.color = color 
#        self.win = win 
#        self.space = 0 
#        self.value = 30
#        
#    
#    def draw_title(self, texte, x_position, y_position ):  
#        
#        
#          
#        text_surface = font.render(texte, True, self.color)
#        self.win.blit(text_surface, (x_position, y_position + self.space ))  # Blit the text to the screen
#
#
#
#texte1 = afiche_texte((255,255,255),win)


class affiche_resault:
    def __init__(self, win=win):
        """
        Initialize the class with players and the window.
        
        Args:
            player1: The first player.
            player2: The second player.
            win: The Pygame window to draw on.
            font: The font for rendering text.
        """
        
        
        self.win = win
        self.font = font = pygame.font.SysFont("Arial", 15)


    def draw_results(self,player1 , player2):
        """
        Draw the player results on the right panel of the screen.
        """
        x_offset = width_maps * tile_size + 60  # Start drawing past the game area
        y_offset = 90  # Initial Y offset for drawing
        spacing = 70  # Spacing between units
        
        # Draw Player 1 results
        player1_label = self.font.render("============PLAYER1==============", True, (255, 255, 255))
        self.win.blit(player1_label, (x_offset, y_offset))
        y_offset += 40  # Add space after the label

        for unit in player1.units:
            # Draw unit image
            unit_image = unit.wlak_down[0]  # Default image
            image_width, image_height = unit_image.get_size()
            
            # Highlight selected unit
            if unit.is_selected:
                scaled_width = int(image_width * 1.5)
                scaled_height = int(image_height * 1.5)
                unit_image = pygame.transform.scale(unit_image, (scaled_width, scaled_height))
                pygame.draw.rect(self.win, (255, 255, 0), (x_offset - 5, y_offset - 5, scaled_width + 10, scaled_height + 10), 2)

            self.win.blit(unit_image, (x_offset, y_offset))
            
            # Draw unit name
            name_text = self.font.render(unit.name, True, (255, 255, 255))
            self.win.blit(name_text, (x_offset + image_width + 10, y_offset + image_height // 4))
            
            y_offset += spacing  # Adjust for next unit
        
        # Draw Player 2 results
        y_offset += 40  # Add space between players
        player2_label = self.font.render("Player 2", True, (255, 255, 255))
        self.win.blit(player2_label, (x_offset, y_offset))
        y_offset += 40  # Add space after the label

        for unit in player2.units:
            # Draw unit image
            unit_image = unit.wlak_down[0]  # Default image
            image_width, image_height = unit_image.get_size()

            # Highlight selected unit
            if unit.is_selected:
                scaled_width = int(image_width * 1.2)
                scaled_height = int(image_height * 1.2)
                unit_image = pygame.transform.scale(unit_image, (scaled_width, scaled_height))
                pygame.draw.rect(self.win, (255, 255, 0), (x_offset - 5, y_offset - 5, scaled_width + 10, scaled_height + 10), 2)

            self.win.blit(unit_image, (x_offset, y_offset))
            
            # Draw unit name
            name_text = self.font.render(unit.name, True, (255, 255, 255))
            self.win.blit(name_text, (x_offset + image_width + 10, y_offset + image_height // 4))
            
            y_offset += spacing  # Adjust for next unit
