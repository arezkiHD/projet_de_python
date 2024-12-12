import pygame

from WALL import *
from game_variables import *


class Unit_V2:
    def __init__(self, pos, pos_start, wall_rect, matrice_zone, walk_right, walk_left, walk_up, walk_down, max_health, base_dammage, win = win, events = None):
        self.x = pos[0]
        self.y = pos[1]
        self.pos_start = pos_start
        self.wall_rect = wall_rect
        self.max_health = max_health
        self.health_level = max_health
        self.win = win
        self.matrice = matrice_zone
        self.base_dammage = base_dammage
        self.rect = pygame.Rect(self.x, self.y, tile_size, tile_size)
        self.vel = 30

        # Animations
        self.walk_right = walk_right
        self.walk_up = walk_up
        self.walk_left = walk_left
        self.walk_down = walk_down

        # States
        self.is_selected = False
        self.remove = False
        self.direction = None
        self.power_enable = False
        self.affiche = True 
        self.get_attacked = False

        self.event = events


        # Animation counters
        self.animation_count = {
            "left": 0,
            "right": 0,
            "up": 0,
            "down": 0
        }

        self.active_zone = []

    @property
    def health_level(self):
        return self._health_level

    @health_level.setter
    def health_level(self, value):
        self._health_level = max(0, min(value, self.max_health))
        if self._health_level == 0:
            self.remove = True

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
                en_unit.health_level -= self.base_dammage
                en_unit.get_attacked = True  # Make the enemy unit visible
                en_unit.to_remove()     # Check if the enemy should be removed  
                   

                # If you want to relocate the enemy only if it's still alive:
                if en_unit.health > 0:
                    en_unit.x, en_unit.y = en_unit.pos_start
                    en_unit.rect.topleft = (en_unit.x, en_unit.y)
    
                # Stop after attacking the first enemy in range
                break

    def calculate_zone(self):
        """Calculate movable zone based on current position and matrice."""
        zone_data = []
        if self.remove:
            return zone_data

        for i, cell in enumerate(self.matrice):
            if cell == 1:
                x_offset = (i % 11 - 5) * tile_size
                y_offset = (i // 11 - 5) * tile_size
                rect = pygame.Rect(self.x + x_offset, self.y + y_offset, tile_size, tile_size)
                if not any(rect.colliderect(wall) for wall in self.wall_rect.wall_positions["wall"]):
                    zone_data.append(rect)
        return zone_data

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
        self.check_obstacle("Health_raise", lambda: self.apply_healing(20))

    def passes_through_power_enable(self) :
        """Handle potion interaction."""
        self.check_obstacle("Power_enable", lambda: self.power_enabling())


    def update_animation(self, direction):
        """Update animation based on direction."""
        self.animation_count[direction] += 1
        if self.animation_count[direction] >= len(getattr(self, f"walk_{direction}")):
            self.animation_count[direction] = 0
        return getattr(self, f"walk_{direction}")[self.animation_count[direction]]

    def move(self):
        """Handle unit movement."""
        self.passes_through_trap()
        if self.is_selected and self.active_zone:
            keys = pygame.key.get_pressed()
            new_x, new_y = self.x, self.y
            self.direction = None

            if keys[pygame.K_LEFT] and self.x > 0:
                new_x -= self.vel
                self.direction = "left"

            elif keys[pygame.K_RIGHT] and self. x < len(facile_maps[:][0])* tile_size + tile_size:
                new_x += self.vel
                self.direction = "right"

            elif keys[pygame.K_UP] and self.y > 0:
                new_y -= self.vel
                self.direction = "up"

            elif keys[pygame.K_DOWN] and self.y < len(facile_maps[0][:])* tile_size - tile_size:
                new_y += self.vel
                self.direction = "down"

            if self.direction:
                new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)
                if any(new_rect.colliderect(zone) for zone in self.active_zone):
                    self.x, self.y = new_x, new_y

    # Dessin health bar
    def draw(self, health_picture, introduction_game, color):
        """Draw unit and health bar."""
        if not self.remove:
            # Draw the current animation frame
            if self.direction:
                sprite = self.update_animation(self.direction)
            else:
                sprite = self.walk_down[0]  # Default sprite
            self.win.blit(sprite, (self.x, self.y))

            # Draw health bar
            health_index = max(0, self.max_health // 20 - self.health_level // 20)
            self.win.blit(health_picture[health_index], (self.x, self.y - 10))

            # Highlight if selected
            if self.is_selected:
                pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, tile_size, tile_size), 1)

    # Dessin zone de mouvement
    def draw_zone(self,introduction_image ):
        if introduction_image.i >= unit_selection_player2["choice2"]["number_of_click_max"]: 
     # Draw grass tiles
            zone=[]
            if  self.is_selected and not self.remove:
                for rect in self.active_zone:
                    #pygame.draw.rect(self.win, (0, 255, 0), rect, 2)
                    zone.append(rect)
            return zone

## Classes des Joueurs :
""" 
-- UNITS :
- Clasian  : Zone de deplacement moyenne,                            degats moyens 25pnts/turn , santé moyenne 100 pnts, SP : Heal Team   (raises teams health 25% )
- Rapidzio : Zone de deplacement Large  ,                            degats Faible 15pnts/turn , santé Faible  75  pnts, SP : Long shot   (One case Hit, Big Dammage, no distance limit)
- Berzerk  : Zone de deplacement Faibe  ,                            degats Eleve  40pnts/turn , santé Elevée  150 pnts, SP : Mass attack (small zone 4x4, average dammage, no distance limit)
- Spectre  : Zone de deplacement Faibe mais tres Large sur les axes, degats Eleve 40 pnts/turn , santé Faible  75  pnts, SP : Reveal      (Reveals zone for one turn)
"""

class Classian(Unit_V2) :

    def __init__(self, pos, pos_start, wall_rect, win = win, walk_right = walk_right_Clasian, walk_left = walk_left_Clasian, walk_up = walk_up_Clasian, walk_down = walk_down_Clasian, max_health = 100, base_dammage = 25, matrice_zone = matrice_Clasian):
        if max_health is None or max_health <= 0:
            raise ValueError(f"Invalid max_health value: {max_health}")
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos, pos_start, wall_rect, matrice_zone, walk_right, walk_left, walk_up, walk_down, max_health, base_dammage, win = win, events = None)
        
    def heal_team(self, player, events, health_cost=10):
        """
        Soigne toutes les unités alliées d'un certain pourcentage de leur santé maximale,
        sauf le Clasian lui-même. """
        keys = pygame.key.get_pressed()

        # Activation du pouvoir avec la touche "P"
        if self.power_enable == True and keys[pygame.K_p]:

            if self.health_level <= health_cost:
                print("Not enough health to heal the team!")
                return

            # Réduction de la santé du Clasian pour effectuer l'action
            self.health_level -= health_cost
            print(f"Heal action used {health_cost} health. Remaining health: {self.health_level}")

            # Heal de la team (or Classian)
            for unit in player.units:
                if unit is not self and not unit.remove:  # Exclut le Clasian et vérifie si l'unité est encore en jeu
                    heal_amount = unit.max_health * 0.25
                    unit.health_level = min(unit.max_health, unit.health_level + heal_amount)
                    print(f"Unit {unit} healed for {heal_amount}. Current health: {unit.health_level}")

            self.power_enable = False



class Rapidzio(Unit_V2) :

    def __init__(self, pos, pos_start, wall_rect, win = win, walk_right = walk_right_Rapidzio, walk_left = walk_left_Rapidzio, walk_up = walk_up_Rapidzio, walk_down = walk_down_Rapidzio, max_health = 75, base_dammage = 15, matrice_zone = matrice_Rapidzio, enemy_units = None, events = None):
        if max_health is None or max_health <= 0:
            raise ValueError(f"Invalid max_health value: {max_health}")        
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos, pos_start, wall_rect, matrice_zone, walk_right, walk_left, walk_up, walk_down, max_health, base_dammage, win = win, events = None)
        self.x_attack = 0
        self.y_attack = 0
        self.events = events


    # Long shot   (One case Hit, Big Dammage, no distance limit)
    def long_shot (self, map_matrix, events) :
                
        # Initialisation des variables pour le ciblage
        if not hasattr(self, "target_cursor"):  # Ajouter un curseur si non défini
            self.target_cursor = [self.x, self.y] # [0, 0]  # Position initiale du curseur sur la carte

        # Activation du mode ciblage avec la touche "P"
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

            # Dessin du curseur sur la carte
            cursor_x, cursor_y = self.target_cursor
            pygame.draw.rect(win, (255, 0, 0), (cursor_x * tile_size, cursor_y * tile_size, tile_size, tile_size), 2)


            for enemy in self.enemy_units:  # Liste des unités enemis dans la game
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


class Berzerk(Unit_V2) :

    def __init__(self, pos, pos_start, wall_rect, win = win, walk_right = walk_right_Berzerk, walk_left = walk_left_Berzerk, walk_up = walk_up_Berzerk, walk_down = walk_down_Berzerk, max_health = 150, base_dammage = 40, matrice_zone = matrice_Berzerk, enemy_units = None, events = None):
        if max_health is None or max_health <= 0:
            raise ValueError(f"Invalid max_health value: {max_health}")
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos, pos_start, wall_rect, matrice_zone, walk_right, walk_left, walk_up, walk_down, max_health, base_dammage, win = win, events = None)
        self.x_attack = 0
        self.y_attack = 0
        self.events = events

    # Mass attack (small zone 4x4, average dammage, no distance limit)    
    def mass_attack(self, map_matrix, events) :
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
            for enemy in self.enemy_units:  # Liste des unités ennemis dans la game
                for dx in range(-2, 3):
                    for dy in range(-2 + abs(dx), 3 - abs(dx)):
                        target_x = cursor_x + dx
                        target_y = cursor_y + dy
                        if (enemy.x, enemy.y) == (target_x, target_y):
                            # Apply damage
                            enemy.health_level -= 20

            # Désactivation du pouvoir après l'attaque
            self.power_enable = False



class Spectre(Unit_V2) :

    def __init__(self, pos, pos_start, wall_rect, win = win, walk_right = walk_right_Spectre, walk_left = walk_left_Spectre, walk_up = walk_up_Spectre, walk_down = walk_down_Spectre, max_health = 100, base_dammage = 25, matrice_zone = matrice_Clasian):
        if max_health is None or max_health <= 0:
            raise ValueError(f"Invalid max_health value: {max_health}")        
        # Appelle le constructeur de la classe parente Unit
        super().__init__(pos, pos_start, wall_rect, matrice_zone, walk_right, walk_left, walk_up, walk_down, max_health, base_dammage, win = win, events = None)
    
    # Reveal      (Reveals zone (enemies) for one turn)
    def reveal(self, map_matrix, events) :
        
        # Initialisation des variables pour le ciblage
        if not hasattr(self, "target_cursor"):  # Ajouter un curseur si non défini
            self.target_cursor = [self.x, self.y]  # Position initiale du curseur sur la carte
            cursor_x, cursor_y = self.target_cursor

        # Activation du pouvoir avec la touche "p" ""POWER"""
        keys = pygame.key.get_pressed()

        if self.power_enable == True and keys[pygame.K_p] :
            pass