import pygame
import os
from WALL import *

tile_size = 30  # Tile size for grid alignment

# Load animations





walk_right=[pygame.image.load(os.path.join("pictures\humain_male",f"right ({i}).png")) for i in range(1,6) ]
walk_left=[pygame.image.load(os.path.join("pictures\humain_male",f"left ({i}).png")) for i in range(1,6) ]
walk_up=[pygame.image.load(os.path.join("pictures\humain_male",f"up ({i}).png")) for i in range(1,6) ]
walk_down=[pygame.image.load(os.path.join("pictures\humain_male",f"down ({i}).png")) for i in range(1,5) ]
health_picture=[pygame.image.load(os.path.join("pictures\health_bar",f"health{i}.png")) for i in range(1,6) ]


matrice = [0,0,0,1,0,0,0,  0,0,1,1,1,0,0  ,0,1,1,1,1,1,0,  1,1,1,1,1,1,1,  0,1,1,1,1,1,0,    0,0,1,1,1,0,0 ,  0,0,0,1,0,0,0  ]  # matrice ppir la zone 



class Unit:
    def __init__(self, pos_x, pos_y, image_player, win, wall_rect, health_level, base_dammage, matrice_zone= matrice , walk_right=walk_right, walk_left=walk_left, walk_up = walk_up , walk_down = walk_down):
        self.x = pos_x
        self.y = pos_y
        self.wall_rect = wall_rect     
        self.image_player = image_player
        self.win = win
        self.matrice = matrice_zone
        self.health_level = health_level
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
        self.activate = False
        self.remove = False

        self.walkcount_left  = 0
        self.walkcount_right = 0
        self.walkcount_up    = 0
        self.walkcount_down  = 0

        self.active_zone = []
        self.zone_origin = (self.x, self.y)  # Origin of the zone when activated

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

    # Elimination d'une unité :
    def to_remove(self) :
        if self.health_level <= 0 :
            self.remove = True   

    # paermet d'Afficher (ou non) la zone de marche :
    def toggle_zone(self):
        """Toggle the activation and recalculate the active zone if needed."""
        self.activate = not self.activate
        if self.activate:
            self.zone_origin = (self.x, self.y)  # Lock the zone to the current position
            self.active_zone = self.calculate_zone(self.zone_origin[0], self.zone_origin[1])

    # Afficher la zone de marche :
    def draw_zone(self ):

        if self.activate and self.is_selected and not self.remove:
            for rect in self.active_zone:
                pygame.draw.rect(self.win, (0, 255, 0), rect, 2)

    def move(self):
        self.to_remove()
        if not self.remove : self.passes_through_trap()
        """Handle player movement and collision detection."""
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
            

    def draw(self,health_picture):
        """Draw the player on the screen."""
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
                self.win.blit(self.image_player, (self.x, self.y))
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