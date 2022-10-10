class Board:
    def __init__(self):
        self.grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.win_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def get_available_spots(self):
        available_spots = [s for s in self.grid if s != "X" and s != "O"]
        return available_spots

    def set_board(self, new_board): 
        self.grid = new_board

    def reset(self):
        self.grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
