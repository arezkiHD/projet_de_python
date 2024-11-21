import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 500
screan_height = 500
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
tile_size = 30

# Create a wall list
world_data = []

# Create wall group
wall_group = pygame.sprite.Group()


# Define wall class
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size


# Open the world_list
with open("wall.txt", 'r') as world:
    for line in world:
        world_data.append(line.strip())  # Strip newline characters


# Create walls
for row, tiles in enumerate(world_data):
    for col, tile in enumerate(tiles):
        if tile == '1':
            wall = Wall(col, row, [0, 0, 255])  # col for x, row for y
            wall_group.add(wall)


# Game loop
run = True
while run:
    pygame.time.delay(10)  # The clock in our game

    # Draw the wall
    win.fill((0, 0, 0))  # Clear the screen
    wall_group.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()  # To show the things that we drew!!

pygame.quit()
