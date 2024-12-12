from game_variables import *
from Unit_V2 import *


class Player(): 
    
    def __init__(self, units_positions, play_or_not, image_player, wall):
    

        self.units_choice = []  # Doit contenir uniquement les noms valides des unités.
        self.image_player = image_player
        self.wall=wall
        self.units=[]
        self.play_times = 0
        self.play_or_not=  play_or_not


        random.shuffle(units_positions)

        self.unit_positions = units_positions   #lest's assume that we get 3 diff position 
        self.to_add = True

    def initialize_units(self, UNITS_INFORMATION):
        
        unit_class_mapping = {
            "Classian": Classian,
            "Rapidzio": Rapidzio,
            "Berzerk" : Berzerk,
            "Spectre" : Spectre
        }

        # Assurez-vous que les choix sont valides.
        self.units_choice = [choice for choice in self.units_choice if choice in unit_class_mapping]

        for idx, unit_name in enumerate(self.units_choice):
            if idx < len(self.unit_positions):  # Vérifie que nous avons une position disponible.
                unit_class = unit_class_mapping[unit_name]
                new_unit = unit_class(
                    pos=self.unit_positions[idx], 
                    pos_start=self.unit_positions[idx],
                    wall_rect=self.wall
                )
                self.units.append(new_unit)

    def play(self, player2, introduction_Game, color):
    # Draw and update all units
        for Unit in self.units:
            if Unit.affiche :
                Unit.draw(health_picture, introduction_Game, color)
                if Unit.is_selected :
                    Unit.draw_zone(introduction_Game)
                    Unit.move()
                    Unit.basic_attack(self,player2.units)
                    if Unit.remove:
                        self.units.remove(Unit)
                
