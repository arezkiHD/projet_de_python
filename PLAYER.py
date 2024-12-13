from game_variables import *
from unit_add_work_imad import *




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
    def initialize_units(self):
                            
                     
        for idx, unit_name in enumerate(self.units_choice):
            if unit_name == 'unit_Clasian' :
                new_unit = Rapidzio(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  ) 
            elif  unit_name == 'unit_Spectre' :
                new_unit = Spectre(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )
            elif unit_name == 'unit_Berzerk' :
                new_unit = Berzerk(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )
            elif unit_name == 'unit_Rapidzio' :
                new_unit = Rapidzio(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )

            if self.to_add :
                self.units.append(new_unit)

    def use_specail_attack(self ,enemy  ) :
        
        for unit in self.units :
            #if isinstance(unit , Classian) :
            #    unit.special_attack( self, health_cost=10)
            if isinstance(unit , Classian) :
                unit.special_attack(self)
            #if isinstance(unit , Berzerk): 
            #    unit.special_attack( UNITS_INFORMATION["unit_Brezerk"]["matrice"], events,enemy_player.units)
            #elif isinstance(unit , Classian) :
            #    unit.special_attack(UNITS_INFORMATION["unit_Classian"]["matrice"] , events,enemy_units) 



    
                    

        
        


        


    def play(self,player2 , introduction_Game,color ):
            
         # Draw and update all units
    
        for Unit in self.units:
            if Unit.affiche :
                Unit.draw(health_picture, introduction_Game, color  )
                if Unit.is_selected :
                    Unit.draw_zone(introduction_Game)
                    Unit.move()
                    Unit.basic_attack(self,player2.units)
                    if Unit.use_attack :  self.use_specail_attack( )

                    
                    if Unit.remove:
                        self.units.remove(Unit)
                
        
        
        
        
    
        
    












