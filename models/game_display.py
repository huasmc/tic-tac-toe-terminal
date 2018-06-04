class GameDisplay:

    @staticmethod
    def show(board):
        result =  " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (board.grid[0], board.grid[1], board.grid[2],
                 board.grid[3], board.grid[4], board.grid[5],
                 board.grid[6], board.grid[7], board.grid[8])
        print(result)

    @staticmethod
    def log(text):
        print(text)

    @staticmethod
    def game_over():
        print('Game Over')

    @staticmethod
    def chosen_spot(token, spot):
        print(f"Player with token {token} has played in spot {spot}")

    @staticmethod
    def winner(token):
        print(f"Player with token {token} won!")

    @staticmethod
    def tie():
        print("It's a tie!")

    @staticmethod
    def game_types():
        game_types = ["1. Human Vs Bot", "2. Human Vs Human", "3. Bot Vs Bot"]
        print(*game_types, sep='\n')
        return game_types

    @staticmethod
    def prompt_spot(available_spots):
        print("Choose one of these spots [%s]:" % ", ".join(available_spots))

    @staticmethod
    def prompt_token():
        print('Choose your token! It can be either X or O:')

    @staticmethod
    def prompt_first_player():
        print('Who plays first, X or O?')

    @staticmethod
    def get_player_spot(self, available_spots):
        self.prompt_spot(available_spots)
        spot = input()
        if not spot in available_spots:
            return self.get_player_spot(self, available_spots)
        else:
            return int(spot)

    @staticmethod
    def get_player_token(self):
        self.prompt_token()
        token = input()
        if (token == 'X'):
            return token
        elif (token == 'O'):
            return token
        else:
            return self.get_player_token(self)

    @staticmethod
    def get_first_player(self):
        self.prompt_first_player()
        first_player = input()
        valid_input = ['O', 'X']
        if not first_player in valid_input:
            return self.get_first_player(self)
        else:
            return first_player

    @staticmethod
    def get_game_type(self):
        game_types = self.game_types()
        game_type = input()
        game_type_index = self.handle_game_type_input(self, game_type)
        if game_type_index == None or not game_types[game_type_index] in game_types:
            return self.get_game_type(self)
        else:
            return game_type_index

    @staticmethod
    def handle_game_type_input(self, game_type):
        if (game_type == '1'):
            return 0
        elif (game_type == '2'):
            return 1
        elif (game_type == '3'):
            return 2
        return None
