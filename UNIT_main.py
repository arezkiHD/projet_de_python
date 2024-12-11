from WALL import *
from game_variables import *




class unit:
    def __init__(self,pos,pos_start, win, wall,matrice_zone , walk_right, walk_left, walk_up , walk_down ):
        self.x = pos[0]
        self.y = pos[1]
        self.pos_start = pos_start
        
        self.wall_rect = wall  
        self.health = 100  
        
        self.win = win
        self.matrice = matrice_zone
        
        
        self.rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        self.vel = 30


        self.wlak_right = walk_right
        self.wlak_up = walk_up
        self.wlak_left = walk_left
        self.wlak_down = walk_down
        
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.is_selected = False
        self.remove = False
        self.affiche = True 
        self.get_attacked = False 

        self.walkcount_left = 0
        self.walkcount_right = 0
        self.walkcount_up = 0
        self.walkcount_down = 0

        self.active_zone = []

    def calculate_zone(self, origin_x, origin_y):
        """Calculate the movable zone based on a fixed origin."""
        zone_data = []
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
    
    def passes_through_trap(self) :
        rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        for water in self.wall_rect.wall_positions["water"] :
            if  rect.colliderect(water)   :
                self.health = self.health-20
                self.wall_rect.wall_positions["water"].remove(water)
                self.wall_rect.wall_positions["grass"].append(pygame.Rect(self.x,self.y,tile_size,tile_size))


    def to_remove(self) :
        if self.health <= 0 :
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
            if keys[pygame.K_LEFT] and self.x > 0 :
                new_x -= self.vel
                self.left = True
                self.right = False
                self.up = False
                self.down=False
                self.walkcount_left += 1
                if self.walkcount_left >= len(self.wlak_left):
                    self.walkcount_left = 0
            if keys[pygame.K_RIGHT] and self. x < len(facile_maps[:][0])* tile_size + tile_size:
                new_x += self.vel
                self.left = False
                self.right = True
                self.up = False
                self.down = False
                self.walkcount_right += 1
                if self.walkcount_right >= len(self.wlak_right):
                    self.walkcount_right = 0
            if keys[pygame.K_UP] and self.y > 0:
                new_y -= self.vel
                self.left = False
                self.right = False
                self.up = True
                self.down = False
                self.walkcount_up += 1
                if self.walkcount_up >= len(self.wlak_up):
                    self.walkcount_up = 0
            if keys[pygame.K_DOWN] and self.y < len(facile_maps[0][:])* tile_size - tile_size:
                new_y += self.vel
                
                self.down = True
                self.up = False
                self.left= False
                self.right = False
                self.walkcount_down += 1
                if self.walkcount_down >= len(self.wlak_down ):
                    self.walkcount_down = 0
            # Predict the player's next position
            new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

            # Allow movement only within the active zone
            if any(new_rect.colliderect(zone) for zone in self.active_zone) :
                self.x, self.y = new_x, new_y
  
    def basic_attack(self, player_me, enemy_units):
        # Only attack if it's the player's turn
        if not player_me.play_or_not:
            return
    
        # Check each enemy unit
        for en_unit in enemy_units:
            # Ensure rect is up-to-date with the current position
            en_unit.rect.topleft = (en_unit.x, en_unit.y)
    
            # Check if enemy unit is within any of the active zone tiles
            if any(en_unit.rect.colliderect(zone) for zone in self.active_zone):
                # Enemy is in range: Attack!
                en_unit.health -= 20
                en_unit.get_attacked = True  # Make the enemy unit visible
                en_unit.to_remove()     # Check if the enemy should be removed  
                   

                # If you want to relocate the enemy only if it's still alive:
                if en_unit.health > 0:
                    en_unit.x, en_unit.y = en_unit.pos_start
                    en_unit.rect.topleft = (en_unit.x, en_unit.y)
    
                # Stop after attacking the first enemy in range
                break



                                            
    def draw(self,health_picture,introduction_game, color  ):
        
        if  introduction_game.i>=introduction_game.last_click:   
            if self.health >0 :
                pygame.draw.rect(self.win ,color, (self.x,self.y ,  2,tile_size))
                # Draw a filled red circle with radius 50 at position (200, 150)
                #pygame.draw.circle(self.win, color , (self.x+tile_size/2, self.y+tile_size/2), tile_size/2 )
                if self.right:
                    self.win.blit(self.wlak_right[self.walkcount_right], (self.x, self.y))
                elif self.left:
                    self.win.blit(self.wlak_left[self.walkcount_left], (self.x, self.y))
                elif self.up:
                    self.win.blit(self.wlak_up[self.walkcount_up], (self.x, self.y))
                elif self.down:
                    self.win.blit(self.wlak_down[self.walkcount_down], (self.x, self.y))

                else:
                    self.win.blit(self.wlak_down[0], (self.x, self.y))
                if self.is_selected  :

                    pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, tile_size, tile_size), 1)
                    if self.health== 100 :
                        self.win.blit(health_picture[0], (self.x, self.y-10))
                    elif self.health== 80 :            
                        self.win.blit(health_picture[1], (self.x, self.y-10))
                    elif self.health== 60 :
                        self.win.blit(health_picture[2], (self.x, self.y-10))
                    elif self.health== 40:
                        self.win.blit(health_picture[3], (self.x, self.y-10))
                    elif self.health == 20 :
                        self.win.blit(health_picture[4], (self.x, self.y-10))