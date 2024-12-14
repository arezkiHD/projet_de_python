from game_variables import* 

x_of_black_screan = width_maps*tile_size

class afiche_texte():   # it can be abstrect !!
    def __init__(self, color,win ):
        
        
        
        self.color = color 
        self.win = win 
        self.space = 0 
        self.value = 30
        
    
    def draw_title(self, texte, x_position, y_position ):  
        
        font = pygame.font.SysFont("Arial", 15)
          
        text_surface = font.render(texte, True, self.color)
        self.win.blit(text_surface, (x_position, y_position + self.space ))  # Blit the text to the screen



texte1 = afiche_texte((255,255,255),win)

        