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
        
        self.to_add = True
    def initialize_units(self,UNITS_INFORMATION):
        
        unit_class_mapping = {
            "unit_Clasian": matrice_Clasian,
            "unit_Rapidzio": matrice_Rapidzio,
            "unit_Berzerk": matrice_Berzerk,
            "unit_Spectre": matrice_Spectre
        }

        for idx, unit_name in enumerate(UNITS_INFORMATION.keys()):
            print("yes babyunit_name")
            if unit_name in self.units_choice:
                new_unit = unit(
                    pos=self.unit_positions[idx],
                    win=win,
                    wall=self.wall,
                    matrice_zone=UNITS_INFORMATION[unit_name]["matrice"],
                    walk_right=UNITS_INFORMATION[unit_name]["walk_right"],
                    walk_left=UNITS_INFORMATION[unit_name]["walk_left"],
                    walk_up=UNITS_INFORMATION[unit_name]["walk_up"],
                    walk_down=UNITS_INFORMATION[unit_name]["walk_down"],
                )
                if self.to_add :
                    self.units.append(new_unit)
                    

        
        


        


    def play(self,player2 , introduction_Game):

       

        
 # Draw and update all units
    
        for Unit in self.units:
            if Unit.affiche :
                Unit.draw(health_picture, introduction_Game)
                if Unit.is_selected :
                    Unit.draw_zone(introduction_Game)
                    Unit.move()
                    Unit.basic_attack(self,player2.units)
                    if Unit.remove:
                        self.units.remove(unit)
                
        
        
        
        
    
        
    












