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
    def prompt(text):
        print(text)
        input_value = input()
        return input_value

    @staticmethod
    def log_as_list(array):
        print(*array, sep='\n')

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
        print('Choose your token! It can be either X or O: ')
