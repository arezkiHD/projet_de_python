from game_variables import *
from UNIT_main import *




# wall_drawing




#def __init__(self,pos, win, wall_rect,matrice_zone , wlak_right, wlak_left, wlak_up , walk_down ):

class Player(unit): 
    
    def __init__(self,units_positions,units_choice ,play_or_not , image_player,wall):
    

        self.units_choice = units_choice
        self.image_player = image_player
        self.wall=wall
        self.units=[]
        self.play_times = 0
        self.play_or_not=  play_or_not

        random.shuffle(units_positions)

        self.unit_positions = units_positions   #lest's assume that we get 3 diff position 
        

        # Créer les unités avec leurs positions initiales et propriétés
    # Classian :    
        self.unit_Clasian = unit(
            self.unit_positions[0], win, self.wall, 
            matrice_Clasian , walk_right, walk_left, walk_up , walk_down     # here i will add pictures for each unit !
           
        )

    # Rapidzio :
        self.unit_Rapidzio = unit(
            self.unit_positions[1], win,self.wall, 
            matrice_Rapidzio , walk_right, walk_left, walk_up , walk_down
                )

    # Berzerk :

        self.unit_Berzerk = unit(
            self.unit_positions[2], win, self.wall, 
            matrice_Berzerk,  walk_right, walk_left, walk_up , walk_down
            )

    # Spectre :

        self.unit_Spectre = unit(
            self.unit_positions[3], win,self.wall, 
            matrice_Spectre,  walk_right, walk_left, walk_up , walk_down
            )
    
        self.units_of_palyer()


    def units_of_palyer(self ):
       
        for u in self.units_choice :
            if u == "unit_Clasian" :
                self.units.append(self.unit_Clasian)
            elif u == "unit_Spectre" :
                self.units.append(self.unit_Spectre)
            elif u == "unit_Rapidzio" :
                self.units.append(self.unit_Rapidzio)
            elif u == "unit_Berzerk" :
                self.units.append(self.unit_Berzerk)   

    def play(self , introduction_Game):
       

        
 # Draw and update all units

        for Unit in self.units:
            Unit.draw(health_picture, introduction_Game)
            if Unit.is_selected :
                Unit.draw_zone(introduction_Game)
                Unit.move()
                
                
                if Unit.remove:
                    self.units.remove(unit)
                
        
        
        
        
    
        
    












