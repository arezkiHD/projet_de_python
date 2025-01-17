from game_variables import *
from unit_add_work_imad import *





# wall_drawing




#def __init__(self,pos, win, wall_rect,matrice_zone , wlak_right, wlak_left, wlak_up , walk_down ):

class Player(): 
    
    def __init__(self,units_positions,play_or_not , image_player,wall):
    

        self.units_choice = []
        self.image_player = image_player
        self.wall=wall
        self.units=[]
        self.play_times = 0
        self.play_or_not=  play_or_not
        self.player_win_lose_not_yet  = 0 #     0 : it is playing not losing not winning , 1 : lose , 2:win


        random.shuffle(units_positions)

        self.unit_positions = units_positions   #lest's assume that we get 3 diff position 
    
    
    def initialize_units(self):
                            
                     
        for idx, unit_name in enumerate(self.units_choice):
            if unit_name == 'unit_Clasian' :
                new_unit = Classian(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  ) 
            elif  unit_name == 'unit_Spectre' :
                new_unit = Spectre(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )
            elif unit_name == 'unit_Berzerk' :
                new_unit = Berzerk(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )
            elif unit_name == 'unit_Rapidzio' :
                new_unit =Rapidzio(pos = self.unit_positions[idx] , pos_start=self.unit_positions[idx], wall=self.wall  , win=win  )

            
            self.units.append(new_unit)

    def use_specail_attack(self  ,enemy  ) :
        
        for unit in self.units :
            if isinstance(unit , Classian) :
                unit.special_attack( self, health_cost=80)
            if isinstance(unit , Rapidzio) :
                unit.special_attack(enemy)
            if isinstance(unit , Berzerk):
                unit.special_attack(enemy) 
            elif isinstance(unit , Spectre)  :
                unit.special_attack(enemy) 
                                            
    def play(self,player2 , introduction_Game,color ):

       
        for Unit in self.units:
            if Unit.affiche :
                Unit.draw( introduction_Game, color  )
                if Unit.is_selected :
                    Unit.draw_zone(introduction_Game)
                    Unit.move()
                    Unit.basic_attack(self,player2.units)
                    self.use_specail_attack(  player2)
                    if Unit.remove:
                        self.units.remove(Unit)


    def player_winner(self , player2 ):
        if len(self.units) == 0 :
            self.player_win_lose_not_yet = 1  # he lost 
            player2.player_win_lose_not_yet = 2 # player 2 wins 

        return self.player_win_lose_not_yet 

