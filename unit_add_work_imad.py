from wall_adding_imad_code import *
from game_variables import *




class unit:
    def __init__(self,pos,pos_start, win,max_health, base_dammage , wall,matrice_zone , walk_right, walk_left, walk_up , walk_down ):
        self.x = pos[0]
        self.y = pos[1]
        self.pos_start = pos_start
        self.damage =  base_dammage
        self.max_health = max_health
        self.health_level = max_health
        self.wall_rect = wall  
         
        
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
        self.power_enable = False  # Special power activation flag
        self.use_attack =False


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



    
    def apply_damage(self, damage):
        self.health_level -= damage
        print(f"{damage} dégâts subis. Santé actuelle : {self.health_level}")
    
    def apply_healing(self, healing):
        self.health_level += healing
        print(f"Soin de {healing} points. Santé actuelle : {self.health_level}")
    
    def power_enabling(self):
        if self.power_enable == False :
            self.power_enable = True
        print("Vous pouver utiliser votre pouvoir.")
       
    
    def check_obstacle(self, obstacle_type, effect_callback):
        """Handle interactions with specific obstacles."""
        rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        for obstacle in self.wall_rect.wall_positions[obstacle_type]:
            if rect.colliderect(obstacle):
                effect_callback()
                self.wall_rect.wall_positions[obstacle_type].remove(obstacle)
                self.wall_rect.wall_positions["grass"].append(
                    pygame.Rect(self.x, self.y, tile_size, tile_size)
                )

    def passes_through_trap(self):
        """Handle trap interaction."""
        self.check_obstacle("water", lambda: self.apply_damage(20))

    def passes_through_potion(self):
        """Handle potion interaction."""
        self.check_obstacle("health_raise", lambda: self.apply_healing(20))

    def passes_through_power_enable(self) :
        """Handle potion interaction."""
        self.check_obstacle("power_enable", lambda: self.power_enabling())
    


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
            self.passes_through_potion()
            self.passes_through_power_enable()

        
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
            if keys[pygame.K_RIGHT] and self. x < len(facile_maps[0][0])*tile_size - tile_size :
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
            if keys[pygame.K_DOWN] and self.y < len(facile_maps[0])* tile_size - tile_size:
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
                en_unit.health_level -= 20
                en_unit.get_attacked = True  # Make the enemy unit visible
                en_unit.to_remove()     # Check if the enemy should be removed  
                   

                # If you want to relocate the enemy only if it's still alive:
                if en_unit.health_level > 0:
                    en_unit.x, en_unit.y = en_unit.pos_start
                    en_unit.rect.topleft = (en_unit.x, en_unit.y)
    
                # Stop after attacking the first enemy in range
                break



                                            
    def draw(self,health_picture,introduction_game, color  ):
        
        if  introduction_game.i>=introduction_game.last_click:   
            if self.health_level >0 :
                #pygame.draw.rect(self.win ,color, (self.x,self.y ,  2,tile_size))
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

                    #pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, tile_size, tile_size), 1)
                    if self.health_level== 100 :
                        #self.win.blit(health_picture[0], (self.x, self.y-10))
                        pygame.draw.rect(self.win ,color, (self.x,self.y-5 ,  tile_size*1,5))
                    elif self.health_level== 80 :            
                        #self.win.blit(health_picture[1], (self.x, self.y-10))
                        pygame.draw.rect(self.win ,color, (self.x,self.y-5,  tile_size*0.8,5))
                    elif self.health_level== 60 :
                        #self.win.blit(health_picture[2], (self.x, self.y-10))
                        pygame.draw.rect(self.win ,color, (self.x,self.y-5,  tile_size*0.6,5))
                    elif self.health_level== 40:
                        #self.win.blit(health_picture[3], (self.x, self.y-10))
                        pygame.draw.rect(self.win ,color, (self.x,self.y-5 ,  tile_size*0.4,5))
                    elif self.health_level == 20 :
                        #self.win.blit(health_picture[4], (self.x, self.y-10))
                        pygame.draw.rect(self.win ,color, (self.x,self.y-5 ,  tile_size*0.2,5))





#- Clasian  : Zone de deplacement moyenne,                            degats moyens 25pnts/turn , santé moyenne 100 pnts, SP : Heal Team   (raises teams health 25% )

class Classian(unit):
    def __init__(self,pos,pos_start,wall , win  ,UNITS_INFORMATION=UNITS_INFORMATION  ) :
        self.inf= UNITS_INFORMATION["unit_Clasian"]

        super().__init__(pos=pos,pos_start=pos_start, win=win ,max_health= self.inf["max_health"], base_dammage= self.inf["base_damage"], wall=wall,matrice_zone =self.inf["matrice"], walk_right= self.inf["walk_right"], walk_left= self.inf["walk_left"], walk_up= self.inf["walk_up"] , walk_down= self.inf["walk_down"] )


    def special_attack(self, player, health_cost=10):
        """
        Heal all allied units except the Classian itself.
        """
        if  self.power_enable :
            for unit in player.units : 
                if unit is not self :
                    unit.self.health_level += health_cost   


        self.power_enable = False



class Rapidzio(unit) :

    def __init__(self,pos,pos_start,wall  ,win ,UNITS_INFORMATION= UNITS_INFORMATION   ) :
        self.inf= UNITS_INFORMATION["unit_Rapidzio"]     
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos=pos,pos_start=pos_start, win=win ,max_health= self.inf["max_health"], base_dammage= self.inf["base_damage"], wall=wall,matrice_zone =self.inf["matrice"], walk_right= self.inf["walk_right"], walk_left= self.inf["walk_left"], walk_up= self.inf["walk_up"] , walk_down= self.inf["walk_down"] )
        self.x_attack = 0
        self.y_attack = 0
        


    # Long shot   (One case Hit, Big Dammage, no distance limit)
    def special_attack(self, map_matrix, events,enemy_units) :
                
        # Initialisation des variables pour le ciblage
        if not hasattr(self, "target_cursor"):  # Ajouter un curseur si non défini
            self.target_cursor = [self.x, self.y] # [0, 0]  # Position initiale du curseur sur la carte

        # Activation du mode ciblage avec la touche "P"
        self.events= self.events
        if self.power_enable == True and self.events[pygame.K_p] :
            
            # Déplacement du curseur si le mode ciblage est activé
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.target_cursor[1] > 0:
                        self.target_cursor[1] -= 1
                    elif event.key == pygame.K_DOWN and self.target_cursor[1] < len(map_matrix) - 1:
                        self.target_cursor[1] += 1
                    elif event.key == pygame.K_LEFT and self.target_cursor[0] > 0:
                        self.target_cursor[0] -= 1
                    elif event.key == pygame.K_RIGHT and self.target_cursor[0] < len(map_matrix[0]) - 1:
                        self.target_cursor[0] += 1

                    # Afficher la position actuelle du curseur
                    print(f"Curseur à : {self.target_cursor}")

                    # Validation de la position avec la barre d'espace
                    if event.key == pygame.K_SPACE:
                        self.x_attack, self.y_attack = self.target_cursor
                        print(f"Attaque confirmée à : ({self.x_attack}, {self.y_attack})")

            # Dessin du curseur sur la carte
            cursor_x, cursor_y = self.target_cursor
            pygame.draw.rect(win, (255, 0, 0), (cursor_x * tile_size, cursor_y * tile_size, tile_size, tile_size), 2)


            for enemy in enemy_units:  # Liste des unités enemis dans la game
                # Verif des positions des enemis
                if (self.x_attack, self.y_attack) == (enemy.x, enemy.y):
                    # Apply damage
                    enemy.health_level -= 40
                    print(f"Attaque réussie ! Ennemi à ({enemy.x}, {enemy.y}) a perdu {40} points de vie.")
                    break

                else:
                    print("Aucun ennemi trouvé à cette position.")

            # Désactivation du pouvoir après l'attaque
            self.power_enable = False



class Berzerk(unit) :
    def __init__(self,pos,pos_start,wall  ,win ,UNITS_INFORMATION = UNITS_INFORMATION  ) :
        self.inf= UNITS_INFORMATION["unit_Berzerk"]     
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos=pos,pos_start=pos_start, win=win ,max_health= self.inf["max_health"], base_dammage= self.inf["base_damage"], wall=wall,matrice_zone =self.inf["matrice"], walk_right= self.inf["walk_right"], walk_left= self.inf["walk_left"], walk_up= self.inf["walk_up"] , walk_down= self.inf["walk_down"] )
        self.x_attack = 0
        self.y_attack = 0
        

    # Mass attack (small zone 4x4, average dammage, no distance limit)    
    def special_attack(self, map_matrix, events,enemy_units) :
        # Initialisation des variables pour le ciblage
        if not hasattr(self, "target_cursor"):  # Ajouter un curseur si non défini
            self.target_cursor = [self.x, self.y]  # Position initiale du curseur sur la carte
            cursor_x, cursor_y = self.target_cursor

        # Activation du mode ciblage avec la touche "p" ""POWER"""
        keys = pygame.key.get_pressed()

        if self.power_enable == True and keys[pygame.K_p] :
            
            # Déplacement du curseur si le mode ciblage est activé
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.target_cursor[1] > 0:
                        self.target_cursor[1] -= 1
                    elif event.key == pygame.K_DOWN and self.target_cursor[1] < len(map_matrix) - 1:
                        self.target_cursor[1] += 1
                    elif event.key == pygame.K_LEFT and self.target_cursor[0] > 0:
                        self.target_cursor[0] -= 1
                    elif event.key == pygame.K_RIGHT and self.target_cursor[0] < len(map_matrix[0]) - 1:
                        self.target_cursor[0] += 1

                    # Afficher la position actuelle du curseur
                    print(f"Curseur à : {self.target_cursor}")

                    # Validation de la position avec la barre d'espace
                    if event.key == pygame.K_SPACE:
                        self.x_attack, self.y_attack = self.target_cursor
                        print(f"Attaque confirmée à : ({self.x_attack}, {self.y_attack})")


            # Dessin de la zone d'attaque sur la carte

            for dx in range(-2, 3):  # Largeur du losange (4x4 cases)
                for dy in range(-2 + abs(dx), 3 - abs(dx)):  # Contrôle la forme du losange
                    target_x = cursor_x + dx
                    target_y = cursor_y + dy
                    if 0 <= target_x < len(map_matrix[0]) and 0 <= target_y < len(map_matrix):
                        # Couleur et transparence
                        if target_x == cursor_x and target_y == cursor_y:
                            color = (255, 0, 0)  # Rouge pour la case centrale
                            alpha = 255  # Pleine opacité
                        else:
                            color = (0, 255, 0)  # Vert pour les autres cases
                            alpha = 128  # Moitié d'opacité

                        # Dessin de la zone avec une surface pour gérer la transparence
                        zone_surface = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
                        zone_surface.fill((*color, alpha))  # Ajouter alpha à la couleur
                        win.blit(zone_surface, (target_x * tile_size, target_y * tile_size))
            
            # Application des dégâts aux ennemis dans la zone
            for enemy in enemy_units:  # Liste des unités ennemis dans la game
                for dx in range(-2, 3):
                    for dy in range(-2 + abs(dx), 3 - abs(dx)):
                        target_x = cursor_x + dx
                        target_y = cursor_y + dy
                        if (enemy.x, enemy.y) == (target_x, target_y):
                            # Apply damage
                            enemy.health_level -= 20

            # Désactivation du pouvoir après l'attaque
            self.power_enable = False



class Spectre(unit) :

    def __init__(self,pos,pos_start,wall , win  ,UNITS_INFORMATION = UNITS_INFORMATION ) :
        self.inf= UNITS_INFORMATION["unit_Spectre"]     
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos=pos,pos_start=pos_start, win=win ,max_health= self.inf["max_health"], base_dammage= self.inf["base_damage"], wall=wall,matrice_zone =self.inf["matrice"], walk_right= self.inf["walk_right"], walk_left= self.inf["walk_left"], walk_up= self.inf["walk_up"] , walk_down= self.inf["walk_down"] )
    
    
    # Reveal      (Reveals zone (enemies) for one turn)
    def special_attack(self, map_matrix, events) :
        
        # Initialisation des variables pour le ciblage
        if not hasattr(self, "target_cursor"):  # Ajouter un curseur si non défini
            self.target_cursor = [self.x, self.y]  # Position initiale du curseur sur la carte
            cursor_x, cursor_y = self.target_cursor

        # Activation du pouvoir avec la touche "p" ""POWER"""
        keys = pygame.key.get_pressed()

        if self.power_enable == True and keys[pygame.K_p] :
            pass