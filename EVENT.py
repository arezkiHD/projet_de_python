from game_variables import *




class Event_manipulation():
    def __init__(self, event,run, unit_key_selection ):
        self.event = event 
        self.run= run 
        self.unit_key_selection= unit_key_selection
       
        
        

    def events_handler(self,player1,player2):
        for event in self.event :
            if event.type == pygame.QUIT:
                self.run = False

            if player1.play_or_not :
                player2.play_r_not =False 
                for i,unit in enumerate(player1.units) :
                    # here to manipulate the key sected for each unit 

                    if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                        player1.play_times += int(event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i])                  # here all other units are false 
                        for all_other_units in player1.units :
                            if all_other_units == unit :
                                continue 
                            all_other_units.is_selected = False

                        unit.is_selected = not unit.is_selected                  # the unit that we selected is true 
                        # here to get only the zone in the previous x and y where we pressed the key 
                        unit.active_zone = unit.calculate_zone(unit.x, unit.y)
            if player1.play_times >= 2*len(player1.units_choice) :
                player1.play_or_not = False 
                player2.play_or_not = True
                print("la nrmnm it is o !!!!")
                player1.play_times =0


            if player2.play_or_not :
                player1.play_r_not =False 
                for i,unit in enumerate(player2.units) :
                    # here to manipulate the key sected for each unit 
                    if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                        player2.play_times += int(event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i])        
                        for all_other_units in player2.units :
                            if all_other_units == unit :
                                continue 
                            all_other_units.is_selected = False
                        unit.is_selected = not unit.is_selected                  # the unit that we selected is true 
                        # here to get only the zone in the previous x and y where we pressed the key 
                        unit.active_zone = unit.calculate_zone(unit.x, unit.y)
            if player2.play_times >= 2*len(player2.units_choice) :
                player2.play_or_not = False 
                player1.play_or_not = True
                player2.play_times =0
            
            
            
                    
                


