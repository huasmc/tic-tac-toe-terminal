import copy
from .game_display import GameDisplay

class HandlePlayerInput:

    def get_player_spot(self, available_spots):
        spot = GameDisplay.prompt('Choose your move: ')
        if not spot in available_spots:
            GameDisplay.log("Please choose an available spot on the board.")
            GameDisplay.log("Choose one of these spots [%s]:" % ", ".join(available_spots))
            return self.get_player_spot(available_spots)
        else:
            return int(spot)

    def get_player_token(self):
        token = GameDisplay.prompt('Choose your token! It can be either X or O: ')
        if (token == 'X'):
            return token
        elif (token == 'O'):
            return token
        else:
            GameDisplay.log('Please choose either X or O.')
            return self.get_player_token()

    def get_first_player(self):
        first_player = GameDisplay.prompt('Who would like to play first, X or O? ')
        valid_input = ['O', 'X']
        if not first_player in valid_input:
            GameDisplay.log('Please choose a valid player token as first player.')
            return self.get_first_player()
        else:
            return first_player

    def get_game_type(self):
        game_types = ["1. Human Vs Bot", "2. Human Vs Human", "3. Bot Vs Bot"]
        GameDisplay.log_as_list(game_types)
        game_type = GameDisplay.prompt('Given the options above please choose the number representing your preferred game type: ')
        game_type_index = self.handle_game_type_input(game_type)
        if game_type_index == None or not game_types[game_type_index] in game_types:
            GameDisplay.log('Please choose a valid option from the following list')
            return self.get_game_type()
        else:
            return game_type_index

    def handle_game_type_input(self, game_type):
        if (game_type == '1'):
            return 0
        elif (game_type == '2'):
            return 1
        elif (game_type == '3'):
            return 2
        return None
