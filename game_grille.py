import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 1200
screan_height = 700
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
tile_size = 30
x= 50 
y= 50
width = 50 
height = 60 
vel = 10
run = True

right = False 
left = False 
 


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


    


    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            run = False
        keys = pygame.key.get_pressed()

    if keys[ pygame.K_LEFT]and x > 0 :
        x-= vel
        left = True 
        right = False
    if keys[pygame.K_RIGHT] and x<screan_width - width :
        x+= vel
        left = False
        right = True
    else :
        left = False
        right = False
        walkcount = 0  
        walkcount=0 
    if keys [pygame.K_UP]  and y > 0 :
        y-=vel
    if keys[pygame.K_DOWN ] and y < screan_height - height:
        y+= vel

   
   
    win.fill((0, 0, 0))
    wall_group.draw(win)
    
    #pygame.draw.rect(win,(255,0,0),(x,y,width,height))

    win.blit(pygame.image.load("frame_0.png"),(x,y))
    
    
    pygame.display.update() # to show the thing that we drew !!
        

pygame.quit()
