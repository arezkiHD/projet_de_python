import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 1200
screan_height = 720
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
tile_size = 30  # Tile size for grid alignment

# Player settings
x = 30
y = 30
width = 30
height = 30

image_player = pygame.image.load("frame_0.png")
grass_image = pygame.image.load("grass.png")
water_image = pygame.image.load("water.png")
wall_image = pygame.image.load("wall.png")


# Wall class
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
        return wall_dict

    def wall_drawing(self):
        """Draw all walls on the screen based on their type."""
        for rect in self.wall_positions["grass"]:
            win.blit(self.grass_image, rect)
        for rect in self.wall_positions["water"]:
            win.blit(self.water_image, rect)
        for rect in self.wall_positions["wall"]:
            win.blit(self.wall_image, rect)


# Cursor class
class Cursor:
    def __init__(self, pos_x, pos_y, win, height=tile_size, width=tile_size, vel=tile_size):
        self.x = pos_x
        self.y = pos_y
        self.height = height
        self.width = width
        self.vel = vel
        self.win = win

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < screan_width - self.width:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < screan_height - self.height:
            self.y += self.vel

    def draw(self):
        
        new_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.win, (255, 0, 0), new_rect)


# Player class
class Player:
    def __init__(self, pos_x, pos_y, image_player, win):
        self.x = pos_x
        self.y = pos_y
        self.image_player = image_player
        self.win = win
        self.is_selected = False

    def toggle_selection(self, cursor):
        """Toggle player selection based on cursor position."""
        player_rect = pygame.Rect(self.x, self.y, tile_size, tile_size)     
        cursor_rect = pygame.Rect(cursor.x, cursor.y, tile_size, tile_size)
        if player_rect.colliderect(cursor_rect):
            self.is_selected = not self.is_selected

    def move_to_cursor(self, cursor):
        """Move player to the cursor's position if selected."""
        if self.is_selected:
            self.x = cursor.x
            self.y = cursor.y
            self.is_selected = False  # Deselect after moving

    def draw(self):
        """Draw the player on the screen."""
        win.blit(self.image_player, (self.x, self.y))
        if self.is_selected:
            pygame.draw.rect(self.win, (0, 255, 0), (self.x, self.y, tile_size, tile_size), 3)


# Initialize wall and player objects
wal1 = Wall(grass_image, "map.txt", tile_size, win, tile_size, tile_size)
curs = Cursor(0, 0, win)
player1 = Player(x, y, image_player, win)
player2 = Player(x*4, y, image_player, win)

# Game loop
run = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if player1.is_selected:
                player1.move_to_cursor(curs)
            else:
                player1.toggle_selection(curs)
    curs.move()

    win.fill((255, 255, 255))
    wal1.wall_drawing()
    curs.draw()
    player1.draw()
    player2.draw()

    pygame.display.update()

pygame.quit()
