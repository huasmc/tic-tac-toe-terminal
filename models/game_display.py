class GameDisplay:
    def show(self, board):
        result =  " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (board.grid[0], board.grid[1], board.grid[2],
                 board.grid[3], board.grid[4], board.grid[5],
                 board.grid[6], board.grid[7], board.grid[8])
        print(result)

    def log(self, text):
        print(text)
