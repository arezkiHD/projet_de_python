import pygame
import numpy as np 

# Initialize pygame
pygame.init()

# Screen dimensions
screan_width = 1200
screan_height = 700
win = pygame.display.set_mode((screan_width, screan_height))
pygame.display.set_caption("My Game")
tile_size = 30

# Player settings
x = 50
y = 50
width = 50
height = 60
vel = 3

image_player = pygame.image.load("frame_0.png")
grass_image= pygame.image.load("grass.png")
water_image=pygame.image.load("water.png")
wall_image=pygame.image.load("wall.png")


# Wall class
class Wall:
    def __init__(self,grass_image, wall_txt_file, dim, win, width, height,water_image=water_image,wall_image=wall_image):
        self.dim = dim
        self.win = win
        self.width = width
        self.height = height
        self.wall_txt_file = wall_txt_file
        self.wall_positions = self.getting_XandY_of_wall()
        self.grass_image= grass_image
        self.water_image= water_image
        self.wall_image= wall_image

    def getting_XandY_of_wall(self):
        """Read wall positions from a file and return as a dictionary with wall types."""
        world_data = []
        wall_dict = {"water": [], "wall": [], "grass": []}
        with open(self.wall_txt_file, 'r') as world:
            for line in world:
                world_data.append(line.strip())

        for row, tiles in enumerate(world_data):
            for col, tile in enumerate(tiles):
                if tile == '1':  # Red walls
                    wall_dict["water"].append(
                        pygame.Rect(col * self.dim, row * self.dim, self.width, self.height)
                    )
                
                elif tile == '0':  # Red walls
                    wall_dict["grass"].append(
                        pygame.Rect(col * self.dim, row * self.dim, self.width, self.height)
    )

                elif tile == '2':  # Green walls
                    wall_dict["wall"].append(
                        pygame.Rect(col * self.dim, row * self.dim, self.width, self.height)
                    )
        return wall_dict

    def wall_drawing(self):
        """Draw all walls on the screen based on their type."""
        for rect in self.wall_positions["grass"]:
            win.blit(self.grass_image, rect)  # Red walls
        for rect in self.wall_positions["water"]:
        
            win.blit(self.water_image, rect)  # Green walls
        for rect in self.wall_positions["wall"]:
            win.blit(self.wall_image, rect)  # Green walls
        


# Player class
class Player:
    def __init__(self, pos_x, pos_y, image_player, win , vel=10):
        self.x = pos_x
        self.y = pos_y
        self.image_player= image_player
        self.win=win
        
        
        self.vel = vel       
        
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        
    

    def move(self, wall_positions):
        """Handle player movement and collision detection."""
        space_i=0 
        keys = pygame.key.get_pressed()
        new_x, new_y = self.x, self.y

        if keys[pygame.K_LEFT] :
            new_x -= self.vel
        if keys[pygame.K_RIGHT]:
            new_x += self.vel
        if keys[pygame.K_UP]:
            new_y -= self.vel
        if keys[pygame.K_DOWN]:
            new_y += self.vel
        


        # Predict the player's next position
        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

        # Check for collisions with both types of walls
        if not any(new_rect.colliderect(wall) for wall in wall_positions["water"] + wall_positions["wall"]):
            self.x, self.y = new_x, new_y
            self.rect.topleft = (self.x, self.y)

        

    def change_position(self ) :
        position_aviable = []
        for i in range(-4 , 5) :
            for j in range(-4 , 5) :
                if i == 0 and j == 0 :
                    continue
                else :               

                    position_aviable.append(pygame.Rect(self.x+i*32, self.y+j*32, 32, 32))
        
        return position_aviable   

    def draw(self,see):
        """Draw the player on the screen."""       
        
        win.blit(self.image_player, (self.x, self.y))
        if see == True :
            for rect in self.change_position():
                pygame.draw.rect(self.win, (255,255, 0), rect)


    
    

    

        
        
        
        


# Initialize wall and player objects
wal1 = Wall(grass_image,"map.txt", tile_size, win, tile_size, tile_size)
player1 = Player(x, y,image_player,win )

# Game loop
run = True
i_space = 0
see = False 
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            i_space = i_space +1
             
            if i_space % 2 == 0 :
                see = True 
            else : 
                see = False 

    # Update and draw everything
    player1.move(wal1.wall_positions)

    win.fill((255, 255, 255))
    wal1.wall_drawing()
    player1.draw(see)
    

    pygame.display.update()

pygame.quit()
