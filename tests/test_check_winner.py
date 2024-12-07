from models.board import Board

def test_check_winner():
    board = Board()
    board.grid = [
        ['X', 'X', 'X'],
        [' ', 'O', ' '],
        ['O', ' ', ' ']
    ]
    print("Test1: ", "Pass" if board.check_winner() == 'X' else "Fail")

    board.grid = [
        ['X', 'O', 'O'],
        ['X', 'O', ' '],
        ['X', ' ', 'O']
    ]
    print("Test2: ", "Pass" if board.check_winner() == 'X' else "Fail")

    board.grid = [
        ['O', ' ', ' '],
        ['X', 'O', ' '],
        [' ', ' ', 'O']
    ]
    print("Test3: ", "Pass" if board.check_winner() == 'O' else "Fail")

    board.grid = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O']
    ]
    print("Test4: ", "Pass" if board.check_winner() == '' else "Fail")

test_check_winner()