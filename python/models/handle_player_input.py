class HandlePlayerInput:
    def get_player_spot(self):
        spot = None
        while spot is None:
          spot = int(raw_input())
