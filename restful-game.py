from flask import Flask, request
from models.board import Board

from models.bot_player import BotPlayer

app = Flask(__name__)

@app.route("/play", methods=['POST'])
def Game():
    player_token = request.form["player_token"]
    player_board = request.form["board"]
    ai_player = BotPlayer()
    ai_player.auto_token(player_token)
    board = Board()
    board.set_board(eval(player_board))
    spot = ai_player.play(board)
    return str(spot)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if (port): 
        app.run(host="https://tic-tac-toe-flask-ai.herokuapp.com", port=port)
    else:
        app.run(host="http://127.0.0.1", port=5000)