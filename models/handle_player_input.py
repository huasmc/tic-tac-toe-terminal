import copy
from .game_display import GameDisplay

class HandlePlayerInput:

    def get_player_spot(self, available_spots):
        GameDisplay.prompt_spot(available_spots)
        spot = input()
        if not spot in available_spots:
            return self.get_player_spot(available_spots)
        else:
            return int(spot)

    def get_player_token(self):
        GameDisplay.prompt_token()
        token = input()
        if (token == 'X'):
            return token
        elif (token == 'O'):
            return token
        else:
            return self.get_player_token()

    def get_first_player(self):
        GameDisplay.prompt_first_player()
        first_player = input()
        valid_input = ['O', 'X']
        if not first_player in valid_input:
            return self.get_first_player()
        else:
            return first_player

    def get_game_type(self):
        game_types = GameDisplay.game_types()
        game_type = input()
        game_type_index = self.handle_game_type_input(game_type)
        if game_type_index == None or not game_types[game_type_index] in game_types:
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
