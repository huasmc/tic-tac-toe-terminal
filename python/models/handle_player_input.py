class HandlePlayerInput:

    def get_input(self,text):
        return input(text)

    def get_player_spot(self):
        spot = self.get_input('Play')
        return int(spot)
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
