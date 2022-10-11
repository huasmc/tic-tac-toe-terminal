import os
from flask import Flask, request
from models.board import Board

from models.bot_player import BotPlayer

app = Flask(__name__)

@app.route("/")
def Home():
    return "Tic Tac Toe bot is active."

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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
