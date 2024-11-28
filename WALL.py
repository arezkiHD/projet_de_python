import pygame

image_player = pygame.image.load("up (2).png")
grass_image = pygame.image.load("grass.png")
water_image = pygame.image.load("water.png")
wall_image = pygame.image.load("wall.png")

tile_size = 30

class Wall:
    def __init__(self, grass_image, wall_txt_file, dim, win, width, height, water_image=water_image, wall_image=wall_image):
        self.dim = dim
        self.win = win
        self.width = width
        self.height = height
        self.wall_txt_file = wall_txt_file
        

        self.wall_positions = self.getting_XandY_of_wall()
        self.grass_image = grass_image
        self.water_image = water_image
        self.wall_image = wall_image
        
    def getting_XandY_of_wall(self):
        """Read wall positions from a file and return as a dictionary with wall types."""
        world_data = []
        wall_dict = {"water": [], "wall": [], "grass": []}
        with open(self.wall_txt_file, 'r') as world:
            for line in world:
                world_data.append(line.strip())

        for row, tiles in enumerate(world_data):
            for col, tile in enumerate(tiles):
                rect = pygame.Rect(col * self.dim, row * self.dim, self.dim, self.dim)
                if tile == '1':  # Water tiles
                    wall_dict["water"].append(rect)
                elif tile == '0':  # Grass tiles
                    wall_dict["grass"].append(rect)
                elif tile == '2':  # Wall tiles
                    wall_dict["wall"].append(rect)
        self.len_of_wall_matrice = col*tile_size
        return wall_dict

    def wall_drawing(self):
        """Draw all walls on the screen based on their type."""
        for rect in self.wall_positions["grass"]:
            self.win.blit(self.grass_image, rect)
        for rect in self.wall_positions["water"]:
            self.win.blit(self.water_image, rect)
        for rect in self.wall_positions["wall"]:
            self.win.blit(self.wall_image, rect)
