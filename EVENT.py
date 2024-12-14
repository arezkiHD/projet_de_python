from game_variables import *

class Event_manipulation:
    def __init__(self, event, run, unit_key_selection1, unit_key_selection2):
        self.event = event
        self.run = run
        self.unit_key_selection1 = unit_key_selection1
        self.unit_key_selection2 = unit_key_selection2

    def events_handler(self, player1, player2):
        for event in self.event:
            if event.type == pygame.QUIT:
                self.run = False

            # Handle Player 1's turn
            if player1.play_or_not:
                # Ensure Player 2's units are hidden and Player 1's units are shown
                self.set_unit_affiche(player1, player2)
                self.handle_player_turn(player1, player2, self.unit_key_selection1, event)
                self.reset_get_attcked(player1)

            # Handle Player 2's turn
            if player2.play_or_not:
                # Ensure Player 1's units are hidden and Player 2's units are shown
                self.set_unit_affiche(player2, player1)
                self.handle_player_turn(player2, player1, self.unit_key_selection2, event)
                self.reset_get_attcked(player2)

    def handle_player_turn(self, current_player, other_player, unit_key_selection, event):
        # Process unit selection for the current player's turn
        print("the len is really big " , len(current_player.units))
        for i, unit in enumerate(current_player.units):
            if event.type == pygame.KEYDOWN and event.key == unit_key_selection[i]:
                # Deselect all current player's units except the chosen one
                for other_unit in current_player.units:
                    if other_unit != unit:
                        other_unit.is_selected = False
                        other_unit.use_attack = False 


                # Select or deselect the chosen unit
                unit.is_selected = not unit.is_selected


                # Calculate the active zone if the unit is selected
                if unit.is_selected:
                    unit.active_zone = unit.calculate_zone(unit.x, unit.y)
                    #pygame.draw.rect(win ,(255, 0, 0), (unit.x,unit.y , 30 , 2)) # when we seletc the the unit !!!

                # Increment the player's action count
                current_player.play_times += 1

        # Check if the player's turn is over
        if current_player.play_times >= 2 * len(current_player.units_choice):
            current_player.play_or_not = False
            other_player.play_or_not = True
            current_player.play_times = 0
            print(f"{current_player} finished their turn, switching turns.")

    def set_unit_affiche(self, active_player, inactive_player):
        # Show all active player's units
        for unit in active_player.units:
            unit.affiche = True

        # Hide all inactive player's units
        for unit in inactive_player.units:
            if not unit.get_attacked :
                unit.affiche = False
            else :
                unit.affiche = True
               
               
    def reset_get_attcked ( self, player  ) :
        for unit in player.units: 
            unit.get_attacked = False 


                       
