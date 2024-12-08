from game_variables import *




class Event_manipulation():
    def __init__(self, event,run, units1,units2,unit_key_selection ):
        self.event = event 
        self.run= run 
        self.units1 = units1
        self.units2 = units2
        self.unit_key_selection= unit_key_selection
       
        
        

    def events_handler(self,player1,player2):
        for event in self.event :
            if event.type == pygame.QUIT:
                self.run = False

            if player1.play_or_not :
                player2.play_r_not =False 
                for i,unit in enumerate(self.units1) :
                    # here to manipulate the key sected for each unit 

                    if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                        player1.play_times += int(event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i])                  # here all other units are false 
                        for all_other_units in self.units1 :
                            if all_other_units == unit :
                                continue 
                            all_other_units.is_selected = False

                        unit.is_selected = not unit.is_selected                  # the unit that we selected is true 
                        # here to get only the zone in the previous x and y where we pressed the key 
                        unit.active_zone = unit.calculate_zone(unit.x, unit.y)
            if player1.play_times >= 8 :
                player1.play_or_not = False 
                player2.play_or_not = True
                print("la nrmnm it is o !!!!")
                player1.play_times =0


            if player2.play_or_not :
                player1.play_r_not =False 
                for i,unit in enumerate(self.units2) :
                    # here to manipulate the key sected for each unit 
                    if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                        player2.play_times += int(event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i])        
                        for all_other_units in self.units2 :
                            if all_other_units == unit :
                                continue 
                            all_other_units.is_selected = False
                        unit.is_selected = not unit.is_selected                  # the unit that we selected is true 
                        # here to get only the zone in the previous x and y where we pressed the key 
                        unit.active_zone = unit.calculate_zone(unit.x, unit.y)
            if player2.play_times >= 8 :
                player2.play_or_not = False 
                player1.play_or_not = True
                player2.play_times =0
            
            
            
                    
                


