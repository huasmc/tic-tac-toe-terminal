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
            self.get_player_token()

    def get_first_player(self):
        first_player = input('Who would like to play first X or O?.')
        valid_input = ['O', 'X']
        if not first_player in valid_input:
            print('Please choose a valid player token as first player.')
            return self.get_first_player()
        else:
            return first_player

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
