"""                
        if tile == 0 :  # Grass tiles
        if tile == 1 :  # Wall tiles
        if tile == 2 :  # Water tiles
        if tile == 3 :  # Bonus Potion (health potion)
        if tile == 4 :  # Power Potion
""" 

# Less traps(water), more Bonuses(10) and Power_enable points(8)


facile_maps = [
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0,2, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 2, 0, 0, 4, 1, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 1, 3, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,0, 0, 0, 0],
    [0, 0, 4, 0, 0, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,1, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 3, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 2, 2, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 1, 3, 0, 0, 2, 2, 1, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 1, 0, 0,0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 2, 2, 2, 0, 0, 1, 1, 0, 1, 1, 0, 0, 4, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0,0, 0, 0, 0],
    [0, 0, 2, 2, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0,1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
],
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 3, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0,0],
    [0, 0, 0, 0, 3, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,0],
    [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,0],
    [0, 0, 1, 0, 4, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 1, 3, 0, 0,0],
    [0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 1, 1, 0, 0, 0, 0, 4, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 0, 3, 1, 0, 0, 0, 1, 0, 0, 0,0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 1, 1, 0, 0, 1, 4, 0, 1, 0, 0, 1, 0, 0, 4, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
],
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0,2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 2, 0, 0, 1, 1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 4, 0, 0,0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0,1, 3, 0, 0, 1],
    [1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 3, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,1, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0,1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0],
]
]


matrice_Clasian  = [0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,1,0,0,0,0,0,
                    0,0,0,0,1,1,1,0,0,0,0,
                    0,0,0,1,1,1,1,1,0,0,0,  
                    0,0,1,1,1,1,1,1,1,0,0,  
                    0,0,0,1,1,1,1,1,0,0,0,  
                    0,0,0,0,1,1,1,0,0,0,0,  
                    0,0,0,0,0,1,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0]   

matrice_Rapidzio = [0,0,1,1,1,1,1,1,1,0,0,  
                    0,1,1,1,1,1,1,1,1,1,0,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    0,1,1,1,1,1,1,1,1,1,0,  
                    0,0,1,1,1,1,1,1,1,0,0]  

matrice_Berzerk  = [0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,1,1,1,0,0,0,0,  
                    0,0,0,1,1,1,1,1,0,0,0,  
                    0,0,0,1,1,1,1,1,0,0,0,  
                    0,0,0,1,1,1,1,1,0,0,0,  
                    0,0,0,0,1,1,1,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0,  
                    0,0,0,0,0,0,0,0,0,0,0]  

matrice_Spectre  = [1,0,0,0,0,1,0,0,0,0,1,  
                    1,1,0,0,0,1,0,0,0,1,1,  
                    0,1,1,0,0,1,0,0,1,1,0,  
                    0,0,1,1,0,1,0,1,1,0,0,  
                    0,0,0,1,1,1,1,1,0,0,0,  
                    1,1,1,1,1,1,1,1,1,1,1,  
                    0,0,0,0,1,1,1,1,0,0,0,  
                    0,0,0,1,1,1,0,1,1,0,0,  
                    0,0,1,1,0,1,0,0,1,1,0,  
                    0,1,1,0,0,1,0,0,0,1,1,  
                    1,1,0,0,0,1,0,0,0,0,1] 




matrice_attack = [  0,0,0,0,0,0,0,0,0,0,0, 
                     0,0,0,0,0,0,0,0,0,0,0, 
                     0,0,0,0,0,0,0,0,0,0,0, 
                     0,0,0,0,0,1,0,0,0,0,0, 
                     0,0,0,0,0,1,0,0,0,0,0, 
                     0,0,0,1,1,1,1,1,0,0,0, 
                     0,0,0,0,0,1,0,0,0,0,0, 
                     0,0,0,0,1,1,0,0,0,0,0, 
                     0,0,0,0,0,0,0,0,0,0,0, 
                     0,0,0,0,0,0,0,0,0,0,0, 
                     0,0,0,0,0,0,0,0,0,0,0  ] 



width_maps = len(facile_maps[0][0])
height_maps = len(facile_maps[0])












