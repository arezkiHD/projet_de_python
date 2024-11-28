import pygame

class afiche_texte():   # it can be abstrect !!
    def __init__(self,texte, x_position, y_position, color,win ):
        self.texte = texte
        self.xpos = x_position
        self.ypos = y_position
        self.color = color 
        self.win = win 
    
    def draw_title(self, font):        
        text_surface = font.render(self.texte, True, self.color)
        self.win.blit(text_surface, (self.xpos, self.ypos))  # Blit the text to the screen