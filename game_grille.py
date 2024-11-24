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
x= 50 
y= 50
width = 50 
height = 60 
vel = 3
run = True

right = False 
left = False 

wlak_right = [ pygame.image.load("frame_0.png")  , pygame.image.load("frame_1.png") , pygame.image.load("frame_2.png"), pygame.image.load("frame_3.png"),pygame.image.load("frame_4.png"),pygame.image.load("frame_5.png") ,
pygame.image.load("frame_6.png")]

wlak_left = [ pygame.image.load("frame_8.png")  , pygame.image.load("frame_9.png") , pygame.image.load("frame_10.png"), pygame.image.load("frame_11.png"),pygame.image.load("frame_12.png"),pygame.image.load("frame_13.png") ,
pygame.image.load("frame_14.png")]

walkcount_right = 0
walkcount_left = 0

# Create a wall list
world_data = []




WAll = []




class wall:
    def __init__(self ,wall_txt_file , dim ,win, width,height):
        self.dim = dim 
        self.win = win 
        self.width= width
        self.height = height 
        self.wall_txt_file = wall_txt_file
        

    def getting_XandY_of_wall(self):
        world_data = []
        Wall_position= []
        with open(self.wall_txt_file, 'r') as world:
            for line in world:
                world_data.append(line.strip())
        
        for row, tiles in enumerate(world_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall_position.append([col , row ])
        return Wall_position
    
    def wall_drawing(self):
        Wall_position = self.getting_XandY_of_wall()
        for x,y in Wall_position:

            pygame.draw.rect(self.win,(255,0,0),(x*self.dim,y*self.dim,self.width,self.height))


wal1=wall("wall.txt",30,win,width, height)




# Game loop
run = True
while run:
    pygame.time.delay(20)  # The clock in our game


    


    for event in pygame.event.get():
        if event.type ==pygame.QUIT :
            run = False
        keys = pygame.key.get_pressed()

    if keys[ pygame.K_LEFT]and x > 0   :
        x-= vel
        left = True 
        right = False
        walkcount_left += 1
        if(walkcount_left ==  6) :
            walkcount_left =0
    if keys[pygame.K_RIGHT] and x<screan_width - width  :
        x+= vel
        left = False
        right = True
        walkcount_right+=1
        if(walkcount_right == 6 ) :
            walkcount_right=0

    if keys [pygame.K_UP]  and y > 0 :
        y-=vel
        left = False
        right = False
    if keys[pygame.K_DOWN ] and y < screan_height - height:
        y+= vel
        left = False
        right = False

   
   
    win.fill((0, 0, 0))
    wal1.wall_drawing()

    if ( right ==False and left ==True ) :
        win.blit(wlak_left[walkcount_left] ,(x,y))

    elif( right ==True and left == False ) :
        
        win.blit(wlak_right[walkcount_right] ,(x,y))
    
    
    else: 
        win.blit(pygame.image.load("frame_0.png") ,(x,y))
    
    
    #pygame.draw.rect(win,(255,0,0),(x,y,width,height))



    
    
    
    pygame.display.update() # to show the thing that we drew !!
        

pygame.quit()   