from game_variables import *
from UNIT_main import *




# wall_drawing




#def __init__(self,pos, win, wall_rect,matrice_zone , wlak_right, wlak_left, wlak_up , walk_down ):

class Player(unit): 
    
    def __init__(self,units_positions,play_or_not , image_player,wall):
    

        self.units_choice = []
        self.image_player = image_player
        self.wall=wall
        self.units=[]
        self.play_times = 0
        self.play_or_not=  play_or_not


        random.shuffle(units_positions)

        self.unit_positions = units_positions   #lest's assume that we get 3 diff position 
        

        # Créer les unités avec leurs positions initiales et propriétés
    # Classian :    
    #    self.unit_Clasian = unit(
    #        self.unit_positions[0], win, self.wall, 
    #        matrice_Clasian , walk_right, walk_left, walk_up , walk_down     # here i will add pictures for each unit !
    #       
    #    )
#
    ## Rapidzio :
    #    self.unit_Rapidzio = unit(
    #        self.unit_positions[1], win,self.wall, 
    #        matrice_Rapidzio , walk_right, walk_left, walk_up , walk_down
    #            )
#
    ## Berzerk :
#
    #    self.unit_Berzerk = unit(
    #        self.unit_positions[2], win, self.wall, 
    #        matrice_Berzerk,  walk_right, walk_left, walk_up , walk_down
    #        )
#
    ## Spectre :
#
    #    self.unit_Spectre = unit(
    #        self.unit_positions[3], win,self.wall, 
    #        matrice_Spectre,  walk_right, walk_left, walk_up , walk_down
    #        )
    #
    #    
    #    self.units_initialized = False

        self.to_add = True
    def initialize_units(self):
        
        unit_class_mapping = {
            "unit_Clasian": matrice_Clasian,
            "unit_Rapidzio": matrice_Rapidzio,
            "unit_Berzerk": matrice_Berzerk,
            "unit_Spectre": matrice_Spectre
        }

        for idx, unit_name in enumerate(self.units_choice):
            print("yes babyunit_name")
            if unit_name in unit_class_mapping:
                new_unit = unit(
                    pos=self.unit_positions[idx],
                    win=win,
                    wall=self.wall,
                   matrice_zone=unit_class_mapping[unit_name],
                    walk_right=walk_right,
                    walk_left=walk_left,
                    walk_up=walk_up,
                    walk_down=walk_down
                )
                if self.to_add :
                    self.units.append(new_unit)
                    print("okokok",idx)

        
        


        


    def play(self , introduction_Game):
       

        
 # Draw and update all units

        for Unit in self.units:
            Unit.draw(health_picture, introduction_Game)
            if Unit.is_selected :
                Unit.draw_zone(introduction_Game)
                Unit.move()
                
                
                if Unit.remove:
                    self.units.remove(unit)
                
        
        
        
        
    
        
    












