import copy

class HandlePlayerInput:

    def get_player_spot(self, available_spots):
        spot = input('Choose your move: ')
        if not spot in available_spots:
            print("Please choose an available spot on the board.")
            print("Choose one of these spots [%s]:" % ", ".join(available_spots))
            return self.get_player_spot(available_spots)
        else:
            return int(spot)

    def get_player_token(self):
        token = input('Choose your token! It can be either X or O: ')
        if (token == 'X'):
            return token
        elif (token == 'O'):
            return token
        else:
            print('Please choose either X or O.')
            return self.get_player_token()

    def get_first_player(self):
        first_player = input('Who would like to play first, X or O? ')
        valid_input = ['O', 'X']
        if not first_player in valid_input:
            print('Please choose a valid player token as first player.')
            return self.get_first_player()
        else:
            return first_player

    def get_game_type(self):
        game_types = ["1. Human Vs Bot", "2. Human Vs Human", "3. Bot Vs Bot"]
        print(*game_types, sep='\n')
        game_type = input('Given the options above please choose the number representing your preferred game type: ')
        game_type_index = self.handle_game_type_input(game_type)
        if not game_types[game_type_index] in game_types:
            print('Please choose a valid option from the following list')
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
        return 'invalid'

#
# if __name__ == '__main__':
#     h=HandlePlayerInput()
#     h.get_player_spot()

    # def get_player_token(text):
    #     return input(text)

# def answer():
#     ans = get_input('enter yes or no')
#     if ans == 'yes':
#         return 'you entered yes'
#     if ans == 'no':
#         return 'you entered no'
