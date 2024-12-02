import pygame
import os 

image_player =  pygame.image.load(os.path.join("pictures\humain_male", 'up (2).png')) 
grass_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'grass.png')) 
water_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'water.png')) 
wall_image =  pygame.image.load(os.path.join("pictures\maps_picture", 'wall.png')) 

tile_size = 30

class Wall:
    def __init__(self, grass_image, map, dim, win, width, height, water_image=water_image, wall_image=wall_image):
        self.dim = dim
        self.win = win
        self.width = width
        self.height = height
        self.map = map
        

        self.wall_positions = self.getting_XandY_of_wall()
        self.grass_image = grass_image
        self.water_image = water_image
        self.wall_image = wall_image
        
    def getting_XandY_of_wall(self):
        """Read wall positions from a file and return as a dictionary with wall types."""
        wall_dict = {"water": [], "wall": [], "grass": []}


        for row in range(0,len(self.map)):
            for col in range(0,len(self.map[row])):  # Correct way to access map[row][col]
                rect = pygame.Rect(col * self.dim, row * self.dim, self.dim, self.dim)
                tile = self.map[row][col]  # Access tile type

                if tile == 1 or tile == 3:  # Water tiles
                    wall_dict["water"].append(rect)
                elif tile == 0:  # Grass tiles
                    wall_dict["grass"].append(rect)
                elif tile == 2:  # Wall tiles
                    wall_dict["wall"].append(rect)        

        return wall_dict







    def wall_drawing(self):
        """Draw all walls on the screen based on their type."""
        for rect in self.wall_positions["grass"]:
            self.win.blit(self.grass_image, rect)
        for rect in self.wall_positions["water"]:
            self.win.blit(self.water_image, rect)
        for rect in self.wall_positions["wall"]:
            self.win.blit(self.wall_image, rect)