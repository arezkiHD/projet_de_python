from game_variables import *


class Event_manipulation():
    def __init__(self, event,run, units,unit_key_selection,show_zone_key, introduction_move ):
        self.event = event 
        self.run= run 
        self.units = units 
        self.unit_key_selection= unit_key_selection
        self.show_zone_key =show_zone_key
        self.introduction_move = introduction_move 
        

    def events_handler(self):
        for event in self.event :
            if event.type == pygame.QUIT:
                self.run = False
            for i,unit in enumerate(self.units) :
                # here to manipulate the key sected for each unit 
                if event.type == pygame.KEYDOWN and event.key == self.unit_key_selection[i]:
                    unit.is_selected = not unit.is_selected 
                    


                if event.type == pygame.KEYDOWN and event.key == self.show_zone_key and unit.is_selected:
                    unit.toggle_zone()
                    print(self.show_zone_key)
                
        