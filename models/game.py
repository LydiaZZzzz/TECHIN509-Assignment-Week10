import csv
from models.board import Board
from models.player import Player

def play_game():
    board = Board()
    board.draw_board()
    turn = 0
    winner = ""

    player1 = Player('X', random=False)
    player2 = Player('O', random=True)

    first_player = player1.symbol if turn % 2 == 0 else player2.symbol

    while not board.is_full():
        current_player = player1 if turn % 2 == 0 else player2
        while True:
            row, col = current_player.get_move()
            if board.update_board(row, col, current_player.symbol):
                break
        board.draw_board()
        winner = board.check_winner()
        if winner:
            break
        turn += 1

    csv_file = "/Users/zhaoyunqing/Desktop/Tech509_10/TECHIN509-Assignment-Week10/data/game_data.csv"
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_player, winner])

csv_file = "/Users/zhaoyunqing/Desktop/Tech509_10/TECHIN509-Assignment-Week10/data/game_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["First Player", "Winner"])

for _ in range(3):
    play_game()