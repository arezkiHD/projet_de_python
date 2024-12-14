import pygame
from game_variables import *

tile_size = 30


class Wall:
    def __init__(self, grass_image, map, dim, win, width, height, water_image=water_image, wall_image=wall_image, bonus_image = potion_health, power_image = potion_power ):
    #def __init__(self, grass_image, map, dim, win, width, height, water_image=water_image, wall_image=wall_image):
        self.dim = dim
        self.win = win
        self.width = width
        self.height = height
        self.map = map
        

        self.wall_positions = self.getting_XandY_of_wall()
        self.grass_image = grass_image
        self.water_image = water_image
        self.wall_image = wall_image
        self.bonus_image = bonus_image
        self.power_image = power_image 
        
    def getting_XandY_of_wall(self):
        """Read wall positions from a file and return as a dictionary with wall types."""
        wall_dict = {"water": [], "wall": [], "grass": [],"health_raise" : [], "power_enable" : []}

        for row in range(0,len(self.map)):
            for col in range(0,len(self.map[row])):  # Correct way to access map[row][col]
                rect = pygame.Rect(col * self.dim, row * self.dim, self.dim, self.dim)
                tile = self.map[row][col]  # Access tile type

                if tile == 1 :  # Water tiles
                    wall_dict["wall"].append(rect)
                elif tile == 0:  # Grass tiles
                    wall_dict["grass"].append(rect)
                elif tile == 2:  # Wall tiles
                    wall_dict["water"].append(rect)  
                elif tile == 3:   
                    wall_dict["health_raise"].append(rect)   
                elif tile == 4 :
                    wall_dict["power_enable"].append(rect)

        return wall_dict

    def wall_drawing(self, introduction_image, units):
            """Draw walls based on the collective state of all units."""
            if introduction_image.i >=introduction_image.last_click:  
                # Draw grass tiles
                for rect in self.wall_positions["grass"]:
                    self.win.blit(self.grass_image, rect)
                    # Determine if any unit affects this tile
                    should_be_transparent = True
                    for unit in units:
                        if unit.is_selected and any(rect.colliderect(zone) for zone in unit.active_zone):
                            should_be_transparent = False
                            break
                    if should_be_transparent:
                        transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, 130))
                        self.win.blit(transparent_surface, (rect.x, rect.y))
        
                # Draw water tiles
                for rect in self.wall_positions["water"]:
                    self.win.blit(self.water_image, rect)
                    should_be_transparent = True
                    for unit in units:
                        if unit.is_selected and any(rect.colliderect(zone) for zone in unit.active_zone):
                            should_be_transparent = False
                            break
                    if should_be_transparent:
                        transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, 130))
                        self.win.blit(transparent_surface, (rect.x, rect.y))
        
                # Draw wall tiles
                for rect in self.wall_positions["wall"]:
                    self.win.blit(self.wall_image, rect)
                    should_be_transparent = True
                    for unit in units:
                        if unit.is_selected and any(rect.colliderect(zone) for zone in unit.active_zone):
                            should_be_transparent = False
                            break
                    if should_be_transparent:
                        transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, 130))
                        self.win.blit(transparent_surface, (rect.x, rect.y))

                # Draw health potion
                for rect in self.wall_positions["health_raise"]:
                    self.win.blit(self.bonus_image, rect)
                    should_be_transparent = True
                    for unit in units:
                        if unit.is_selected and any(rect.colliderect(zone) for zone in unit.active_zone):
                            should_be_transparent = False
                            break
                    if should_be_transparent:
                        transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, 130))
                        self.win.blit(transparent_surface, (rect.x, rect.y))            
                        
                # Draw power potion tiles
                for rect in self.wall_positions["power_enable"]:
                    self.win.blit(self.power_image, rect)
                    should_be_transparent = True
                    for unit in units:
                        if unit.is_selected and any(rect.colliderect(zone) for zone in unit.active_zone):
                            should_be_transparent = False
                            break
                    if should_be_transparent:
                        transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
                        transparent_surface.fill((0, 0, 0, 130))
                        self.win.blit(transparent_surface, (rect.x, rect.y))