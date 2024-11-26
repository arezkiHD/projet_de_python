import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 1200
screan_height = 700
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
tile_size = 32

# Player settings
x = 50
y = 50
width = 50
height = 60
vel = 3

# Load animations
wlak_right = [pygame.image.load(f"frame_{i}.png") for i in range(7)]
wlak_left = [pygame.image.load(f"frame_{i + 8}.png") for i in range(7)]


# Wall class
class Wall:
    def __init__(self, wall_txt_file, dim, win, width, height):
        self.dim = dim
        self.win = win
        self.width = width
        self.height = height
        self.wall_txt_file = wall_txt_file
        self.wall_positions = self.getting_XandY_of_wall()

    def getting_XandY_of_wall(self):
        """Read wall positions from a file and return as a list of Rect objects."""
        world_data = []
        wall_rects = []
        with open(self.wall_txt_file, 'r') as world:
            for line in world:
                world_data.append(line.strip())

        for row, tiles in enumerate(world_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall_rects.append(
                        pygame.Rect(col * self.dim, row * self.dim, self.width, self.height)
                    )
        return wall_rects

    def wall_drawing(self):
        """Draw all walls on the screen."""
        for rect in self.wall_positions:
            pygame.draw.rect(self.win, (255, 0, 0), rect)


# Player class
class Player:
    def __init__(self, pos_x, pos_y, wlak_right, wlak_left, vel=10):
        self.x = pos_x
        self.y = pos_y
        self.wlak_right = wlak_right
        self.wlak_left = wlak_left
        self.vel = vel
        self.left = False
        self.right = False
        self.walkcount_left = 0
        self.walkcount_right = 0
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def move(self, wall_rects):
        """Handle player movement and collision detection."""
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.vel
            self.left = True
            self.right = False
            self.walkcount_left += 1
            if self.walkcount_left >= len(self.wlak_left):
                self.walkcount_left = 0
        if keys[pygame.K_RIGHT]:
            new_x += self.vel
            self.left = False
            self.right = True
            self.walkcount_right += 1
            if self.walkcount_right >= len(self.wlak_right):
                self.walkcount_right = 0
        if keys[pygame.K_UP]:
            new_y -= self.vel
        if keys[pygame.K_DOWN]:
            new_y += self.vel

        # Predict the player's next position
        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

        # Check for collisions
        if not any(new_rect.colliderect(wall) for wall in wall_rects):
            self.x, self.y = new_x, new_y
            self.rect.topleft = (self.x, self.y)

    def draw(self):
        """Draw the player on the screen."""
        if self.right:
            win.blit(self.wlak_right[self.walkcount_right], (self.x, self.y))
        elif self.left:
            win.blit(self.wlak_left[self.walkcount_left], (self.x, self.y))
        else:
            win.blit(self.wlak_right[0], (self.x, self.y))


# Initialize wall and player objects
wal1 = Wall("wall.txt", tile_size, win, tile_size, tile_size)
player1 = Player(x, y, wlak_right, wlak_left)

# Game loop
run = True
while run:
    pygame.time.delay(20)  # The clock in our game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update and draw everything
    player1.move(wal1.wall_positions)

    win.fill((255, 255, 255))
    wal1.wall_drawing()
    player1.draw()

    pygame.display.update()  # Show the drawn frame

pygame.quit()
