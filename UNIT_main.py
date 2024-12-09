from WALL import *
from game_variables import *




class Unit:
    def __init__(self,pos, win, wall_rect,matrice_zone , walk_right, walk_left, walk_up , walk_down, max_health, base_dammage):
        self.x = pos[0]
        self.y = pos[1]
        self.wall_rect = wall_rect  
        self.health_level = max_health 
        
        self.win = win
        self.matrice = matrice_zone
        self.base_dammage = base_dammage
        
        
        self.rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        self.vel = 30


        self.walk_right = walk_right
        self.walk_up   = walk_up
        self.walk_left = walk_left
        self.walk_down = walk_down
        
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.is_selected = False
        self.remove = False

        self.walkcount_left  = 0
        self.walkcount_right = 0
        self.walkcount_up    = 0
        self.walkcount_down  = 0

        self.active_zone = []

    def calculate_zone(self, origin_x, origin_y):
        """Calculate the movable zone based on a fixed origin."""
        zone_data = []
        # Zone theoriquement parcourable ==> carré de 11x11
        if not self.remove :
            i = 0
            for x in range(origin_x - 5 * tile_size, origin_x + 6 * tile_size, tile_size):
                for y in range(origin_y - 5 * tile_size, origin_y + 6 * tile_size, tile_size):
                    if self.matrice[i] == 1:
                        rect = pygame.Rect(x, y, tile_size, tile_size)
                        if not any(rect.colliderect(wall) for wall in self.wall_rect.wall_positions["wall"] ) :                        
                            zone_data.append(rect)

                    i += 1


        else :
            zone_data= []
        
            
        return zone_data
    
    # Zone de piege dans la map :
    def passes_through_trap(self) :
        rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        for water in self.wall_rect.wall_positions["water"] :
            if  rect.colliderect(water)   :                             # Passe dans l'eau degat = 20 pnts
                self.health = self.health_level-20
                self.wall_rect.wall_positions["water"].remove(water)
                self.wall_rect.wall_positions["grass"].append(pygame.Rect(self.x,self.y,tile_size,tile_size))

    # Passage par le Bonus de Vie (potion) dans la map :
    def passes_through_potion(self) :
        rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        for potion in self.wall_rect.wall_positions["Health_raise"] :
            if  rect.colliderect(potion)   :                             # Passe dans l'eau degat = 20 pnts
                self.health = self.health_level-20
                self.wall_rect.wall_positions["Health_raise"].remove(potion)
                self.wall_rect.wall_positions["grass"].append(pygame.Rect(self.x,self.y,tile_size,tile_size))

    # Elimination d'une unité :
    def to_remove(self) :
        if self.health_level <= 0 :
            self.remove = True   


    
    def draw_zone(self,introduction_image ):
        if introduction_image.i >= unit_selection_player2["choice2"]["number_of_click_max"]: 
     # Draw grass tiles
            zone=[]
            if  self.is_selected and not self.remove:
                for rect in self.active_zone:
                    #pygame.draw.rect(self.win, (0, 255, 0), rect, 2)
                    zone.append(rect)
            return zone

    def move(self):
        self.to_remove()
        if not self.remove :
            self.passes_through_trap()
        
        if self.is_selected and self.active_zone:
            keys = pygame.key.get_pressed()
            new_x, new_y = self.x, self.y
            if keys[pygame.K_LEFT]:
                new_x -= self.vel
                self.left = True
                self.right = False
                self.up = False
                self.down=False
                self.walkcount_left += 1
                if self.walkcount_left >= len(self.walk_left):
                    self.walkcount_left = 0
            if keys[pygame.K_RIGHT]:
                new_x += self.vel
                self.left = False
                self.right = True
                self.up = False
                self.down = False
                self.walkcount_right += 1
                if self.walkcount_right >= len(self.walk_right):
                    self.walkcount_right = 0
            if keys[pygame.K_UP]:
                new_y -= self.vel
                self.left = False
                self.right = False
                self.up = True
                self.down = False
                self.walkcount_up += 1
                if self.walkcount_up >= len(self.walk_up):
                    self.walkcount_up = 0
            if keys[pygame.K_DOWN]:
                new_y += self.vel
                
                self.down = True
                self.up = False
                self.left= False
                self.right = False
                self.walkcount_down += 1
                if self.walkcount_down >= len(self.walk_down ):
                    self.walkcount_down = 0
            # Predict the player's next position
            new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

            # Allow movement only within the active zone
            if any(new_rect.colliderect(zone) for zone in self.active_zone) :
                self.x, self.y = new_x, new_y
            

    def draw(self,health_picture,introduction_game):
        
        if  introduction_game.i>=unit_selection_player2["choice2"]["number_of_click_max"]:   
            if self.health_level >0 :
                if self.right:
                    self.win.blit(self.walk_right[self.walkcount_right], (self.x, self.y))
                elif self.left:
                    self.win.blit(self.walk_left[self.walkcount_left], (self.x, self.y))
                elif self.up:
                    self.win.blit(self.walk_up[self.walkcount_up], (self.x, self.y))
                elif self.down:
                    self.win.blit(self.walk_down[self.walkcount_down], (self.x, self.y))

                else:
                    self.win.blit(self.walk_down[0], (self.x, self.y))
                if self.is_selected  :

                    pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, tile_size, tile_size), 1)
                    if self.health_level== 100 :
                        self.win.blit(health_picture[0], (self.x, self.y-10))
                    elif self.health_level== 80 :            
                        self.win.blit(health_picture[1], (self.x, self.y-10))
                    elif self.health_level== 60 :
                        self.win.blit(health_picture[2], (self.x, self.y-10))
                    elif self.health_level== 40:
                        self.win.blit(health_picture[3], (self.x, self.y-10))
                    elif self.health_level == 20 :
                        self.win.blit(health_picture[4], (self.x, self.y-10))


# Je dois creeer des units dans ici qui herite de unit pour apres mettres les methodes des power puis les mettre dasn player




